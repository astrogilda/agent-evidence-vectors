#!/usr/bin/env python3
"""Tests for scripts/_lockfile.py.

The lock's whole job is to refuse a second gate, so the cases that matter are
the ones where a refusal could be wrong in either direction.

Failing open is the first. A killed holder whose descriptor nobody inherited
must free the lock, and a lock that stayed held forever after a crash would stop
every later push for no reason.

Stating an unchecked fact is the second, and it is the defect these tests were
written for. `flock` binds the open file description rather than the process, so
a child that inherits the descriptor keeps the lock while the file still names
the dead parent. The refusal used to read that name and report it as a running
process, so an operator would stop a pid that did not exist and find the lock
still held. The case below kills the recorded holder, proves it is gone, and
requires the refusal both to keep refusing and to say the holder is gone rather
than claim it is running.

Every case runs in its own temporary directory with its own lock name and
spawns only short-lived children of this process, so the file touches nothing
outside itself and needs no network, no repository state and no ordering.

Usage: python3 scripts/_lockfile-test.py
Exit 0 when every case holds; 1 on a summary of the failures.
"""

from __future__ import annotations

import contextlib
import os
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUSY = 3

HOLD = """
import os, sys, time
sys.path.insert(0, {scripts!r})
from _lockfile import single_instance
fork = len(sys.argv) > 2 and sys.argv[2] == "fork"
with single_instance(sys.argv[1]):
    if fork and os.fork() == 0:
        time.sleep(60)          # inherits the descriptor, outlives the parent
        os._exit(0)
    print("HELD", flush=True)
    time.sleep(60)
"""

TAKE = """
import sys
sys.path.insert(0, {scripts!r})
from _lockfile import single_instance
with single_instance(sys.argv[1]):
    print("TOOK")
"""


def _env(tmp: Path) -> dict[str, str]:
    return {**os.environ, "TMPDIR": str(tmp)}


def _hold(tmp: Path, name: str, *, fork: bool = False) -> subprocess.Popen[str]:
    argv = [sys.executable, "-c", HOLD.format(scripts=str(HERE)), name]
    if fork:
        argv.append("fork")
    proc = subprocess.Popen(
        argv, env=_env(tmp), stdout=subprocess.PIPE, text=True, start_new_session=True
    )
    assert proc.stdout is not None
    deadline = time.monotonic() + 30
    while time.monotonic() < deadline:
        if (proc.stdout.readline() or "").strip() == "HELD":
            return proc
        if proc.poll() is not None:
            raise AssertionError("the holder exited before taking the lock")
    raise AssertionError("the holder never reported taking the lock")


def _take(tmp: Path, name: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", TAKE.format(scripts=str(HERE)), name],
        env=_env(tmp), capture_output=True, text=True, timeout=60,
    )


def _reap(proc: subprocess.Popen[str]) -> None:
    """Stop the holder and anything it forked, then wait for it to be reaped."""
    with contextlib.suppress(ProcessLookupError, OSError):
        os.killpg(proc.pid, signal.SIGKILL)
    proc.wait(timeout=30)


def _gone(pid: int) -> bool:
    """Whether pid is absent. A zombie is still a pid, so it is reaped first."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return True
    return False


def case_free_lock_is_taken(tmp: Path) -> None:
    done = _take(tmp, "case-free")
    assert done.returncode == 0, f"a free lock was refused: {done.stderr}"
    assert "TOOK" in done.stdout, done.stdout


def case_live_holder_refuses_and_is_confirmed(tmp: Path) -> None:
    holder = _hold(tmp, "case-live")
    try:
        done = _take(tmp, "case-live")
        assert done.returncode == BUSY, f"a held lock was granted (rc={done.returncode})"
        assert f"pid {holder.pid}" in done.stderr, done.stderr
        assert "confirmed still running" in done.stderr, done.stderr
        assert "GONE" not in done.stderr, done.stderr
    finally:
        _reap(holder)


def case_killed_holder_frees_the_lock(tmp: Path) -> None:
    """No inheritor, so the kernel drops the lock and we must not fail closed."""
    holder = _hold(tmp, "case-killed")
    _reap(holder)
    assert _gone(holder.pid), "the holder survived the kill, so the case proves nothing"
    done = _take(tmp, "case-killed")
    assert done.returncode == 0, f"a freed lock stayed refused: {done.stderr}"


def case_inherited_lock_refuses_without_claiming_a_live_holder(tmp: Path) -> None:
    """The regression. The recorded pid is dead; the lock is still held."""
    holder = _hold(tmp, "case-inherited", fork=True)
    pid = holder.pid
    try:
        os.kill(pid, signal.SIGKILL)   # the parent only; the fork keeps the lock
        holder.wait(timeout=30)
        assert _gone(pid), "the recorded holder survived, so the case proves nothing"

        done = _take(tmp, "case-inherited")
        # It must not fail open: the lock is genuinely still held.
        assert done.returncode == BUSY, (
            f"the lock was granted while an inheritor held it (rc={done.returncode})"
        )
        # And it must not assert that the dead pid is running.
        assert "confirmed still running" not in done.stderr, (
            f"the refusal called a dead pid running: {done.stderr}"
        )
        assert "GONE" in done.stderr, f"the refusal did not report the holder gone: {done.stderr}"
        assert "kill -TERM -" in done.stderr, (
            f"the refusal did not name the group to stop: {done.stderr}"
        )
    finally:
        with contextlib.suppress(ProcessLookupError, OSError):
            os.killpg(pid, signal.SIGKILL)


def case_unreadable_record_claims_nothing(tmp: Path) -> None:
    """A holder line with no pid must not be dressed up as a confirmed holder."""
    holder = _hold(tmp, "case-garbled")
    try:
        (tmp / "case-garbled.lock").write_text("who knows\n")
        done = _take(tmp, "case-garbled")
        assert done.returncode == BUSY, f"a held lock was granted (rc={done.returncode})"
        assert "confirmed still running" not in done.stderr, done.stderr
        assert "does not name a pid" in done.stderr, done.stderr
    finally:
        _reap(holder)


CASES = [
    case_free_lock_is_taken,
    case_live_holder_refuses_and_is_confirmed,
    case_killed_holder_frees_the_lock,
    case_inherited_lock_refuses_without_claiming_a_live_holder,
    case_unreadable_record_claims_nothing,
]


def main() -> int:
    failures: list[str] = []
    for case in CASES:
        with tempfile.TemporaryDirectory() as raw:
            try:
                case(Path(raw))
            except Exception as exc:  # noqa: BLE001 -- each case is reported, not the first
                failures.append(f"{case.__name__}: {exc}")
            else:
                print(f"ok {case.__name__}")
    for line in failures:
        print(f"FAIL {line}", file=sys.stderr)
    print(f"{len(CASES) - len(failures)}/{len(CASES)} cases held")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
