"""An exclusive single-instance lock for the expensive local gates.

Both gates in this directory build and run one binary per worker. Two of either
running at once do not halve the wall clock -- they oversubscribe the scheduler,
both slow down, and neither can use the other's results. Queueing is the wrong
answer too: the second caller almost always wants the answer the first is
already computing, so the right behaviour is to refuse and say who holds it.

The refusal is loud, and an unopenable or unlockable lock file is also a refusal.
A lock that fails open leaves exactly the behaviour it exists to prevent, which
is worse than no lock at all, because the caller believes they are protected.

The refusal also says only what it checked. `flock` binds the open file
description, not the process, so a child that inherits the descriptor keeps the
lock after its parent is killed -- while the file still names the parent. The
earlier refusal read that name and reported it as a running process without ever
asking whether it was, so an operator stopping the named pid would find the lock
still held and no remaining pid to blame. The holder line is therefore verified
before it is quoted, and the two cases are worded differently: a live holder is
named as still running, and a dead one is named as gone with the process group
to stop, because stopping a group is what frees an inherited lock. Neither case
grants the lock; failing open here would restore the defect above.
"""

from __future__ import annotations

import contextlib
import errno
import fcntl
import os
import sys
import tempfile
import time
from collections.abc import Iterator
from pathlib import Path
from typing import NoReturn

BUSY = 3
"""Exit status for "another instance holds the lock". Distinct from a gate
failure, so a caller can tell "the check said no" from "the check did not run"."""


def _start_ticks(pid: int) -> str | None:
    """The pid's start time, which distinguishes it from a later pid reuse.

    Returns None where it cannot be read, so the caller can say the identity was
    not re-checked rather than imply that it was.
    """
    try:
        stat = Path(f"/proc/{pid}/stat").read_bytes()
    except OSError:
        return None
    # The comm field is parenthesised and may itself contain spaces, so the
    # fields are counted from the last ')' rather than from the left.
    tail = stat.rpartition(b")")[2].split()
    if len(tail) < 20:
        return None
    return tail[19].decode()


def _record(pid: int) -> str:
    line = f"pid {pid}, pgid {os.getpgid(pid)}, started {time.strftime('%Y-%m-%d %H:%M:%S')}"
    ticks = _start_ticks(pid)
    return line if ticks is None else f"{line}, starttime {ticks}"


def _field(record: str, key: str) -> str | None:
    for part in record.split(","):
        head, _, value = part.strip().partition(" ")
        if head == key:
            return value
    return None


def _alive(pid: int, ticks: str | None) -> bool:
    """Whether that exact process still exists -- not merely that pid is in use."""
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        pass  # it exists; it is simply not ours to signal
    if ticks is None:
        return True
    current = _start_ticks(pid)
    # An unreadable start time cannot refute the pid, so it is not treated as
    # having done so; a readable one that differs means the pid was reused.
    return current is None or current == ticks


def _holder(record: str) -> str:
    """Describe the recorded holder, asserting only what was checked."""
    if not record:
        return "an unrecorded process holds it"
    raw = _field(record, "pid")
    pid = int(raw) if raw is not None and raw.isdigit() else None
    if pid is None:
        return f"its holder line ({record}) does not name a pid, so nothing was confirmed"
    if _alive(pid, _field(record, "starttime")):
        return f"{record}, confirmed still running"
    group = _field(record, "pgid")
    stop = "stop its process group"
    if group:
        stop = f"{stop} with: kill -TERM -{group}"
    return (
        f"{record}, but that process is GONE -- the lock is held by a process that "
        f"inherited it, which is why the pid above cannot be found; {stop}"
    )


@contextlib.contextmanager
def single_instance(name: str) -> Iterator[None]:
    """Hold an exclusive lock named `name`, or exit BUSY naming the holder."""
    path = Path(tempfile.gettempdir()) / f"{name}.lock"
    try:
        handle = path.open("a+")
    except OSError as exc:
        _refuse(f"cannot open the lock at {path}: {exc}")
    try:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            if exc.errno not in (errno.EACCES, errno.EAGAIN):
                _refuse(f"cannot take the lock at {path}: {exc}")
            handle.seek(0)
            _refuse(
                f"another {name} is already running -- {_holder(handle.read().strip())}; "
                f"refusing to start a second one. Wait for it, or stop it and retry."
            )
        handle.seek(0)
        handle.truncate()
        handle.write(f"{_record(os.getpid())}\n")
        handle.flush()
        yield
    finally:
        handle.close()


def _refuse(message: str) -> NoReturn:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(BUSY)
