#!/usr/bin/env python3
"""The two rails that judge vectors-w3c-report/ print the same bytes.

``aee-verify <dir>`` judges the corpus through corpora/w3creport.go and
``packaging/run_vectors.py --corpus vectors-w3c-report`` judges it through
packaging/agent_evidence_vectors/w3creport.py. Each is a full statement of the
v0.1 rows, and two statements of one set of rules drift unless something holds
them together. This holds them together: the committed corpus and a set of
mutated copies are judged by both, and every line of output is compared.

The mutations are chosen so that different parts of the reader answer: a
flipped byte (identifier and corpus digest), a manifest row expecting the wrong
requirement (the validator's answer against the manifest's), a member whose
report loses its roll-up field (a row firing where none was expected), and a
member whose check-set count is edited (the set-binding row).

Usage: python3 scripts/w3c-rails-parity-test.py
Exit 0 when every case prints identically on both rails; 1 otherwise.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
CORPUS = "vectors-w3c-report"


def run(cmd: list[str], cwd: Path) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout + proc.stderr


def manifest_of(corpus: Path) -> dict[str, Any]:
    with open(corpus / "MANIFEST.json", encoding="utf-8") as handle:
        data: dict[str, Any] = json.load(handle)
        return data


def write_manifest(corpus: Path, manifest: dict[str, Any]) -> None:
    (corpus / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def flip_first_member(corpus: Path) -> None:
    entry = manifest_of(corpus)["vectors"][0]
    path = corpus / entry["file"]
    body = bytearray(path.read_bytes())
    body[len(body) // 2] ^= 0x01
    path.write_bytes(bytes(body))


def wrong_row(corpus: Path) -> None:
    manifest = manifest_of(corpus)
    for entry in manifest["vectors"]:
        if entry["kind"] == "reject":
            entry["expected"]["rejects"] = ["W3C-R-012"]
            entry["requirements"] = ["W3C-R-012"]
            break
    write_manifest(corpus, manifest)


def edit_member(corpus: Path, edit: Callable[[dict[str, Any]], None]) -> None:
    entry = next(
        e for e in manifest_of(corpus)["vectors"]
        if e["kind"] == "accept" and e["subjectType"] == "report"
    )
    path = corpus / entry["file"]
    document = json.loads(path.read_text(encoding="utf-8"))
    edit(document["subject"])
    path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def drop_negative_capable(corpus: Path) -> None:
    edit_member(corpus, lambda report: report["roll-up"].pop("negative-capable"))


def miscount_check_set(corpus: Path) -> None:
    def edit(report: dict[str, Any]) -> None:
        report["check-set"]["leaf-count"] = report["check-set"]["leaf-count"] + 1

    edit_member(corpus, edit)


def float_count(corpus: Path) -> None:
    def edit(report: dict[str, Any]) -> None:
        report["roll-up"]["declared"] = float(report["roll-up"]["declared"])

    edit_member(corpus, edit)


CASES: list[tuple[str, Callable[[Path], None] | None]] = [
    ("committed", None),
    ("flipped-byte", flip_first_member),
    ("wrong-row", wrong_row),
    ("silent-roll-up", drop_negative_capable),
    ("miscounted-set", miscount_check_set),
    ("float-count", float_count),
]


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="w3c-parity-") as tmp:
        work = Path(tmp)
        binary = work / "aee-verify"
        status, output = run(["go", "build", "-o", str(binary), "./cmd/aee-verify"], REPO)
        if status != 0:
            print(f"FAIL: aee-verify did not build:\n{output}")
            return 1
        failures = 0
        for name, mutate in CASES:
            corpus = work / name / CORPUS
            shutil.copytree(REPO / CORPUS, corpus)
            if mutate is not None:
                mutate(corpus)
            go_status, go_out = run([str(binary), str(corpus)], REPO)
            py_status, py_out = run(
                [sys.executable, "packaging/run_vectors.py", "--vectors", str(corpus)], REPO
            )
            same = go_out == py_out and go_status == py_status
            findings = sum(1 for line in go_out.splitlines() if line.startswith("FAIL"))
            mark = "ok  " if same else "FAIL"
            print(f"{mark} {name}: exit go={go_status} py={py_status}, {findings} finding line(s)")
            if mutate is not None and go_status == 0:
                print(f"FAIL {name}: the mutation was not noticed, so the case asserted nothing")
                failures += 1
            if not same:
                failures += 1
                for label, text in (("go", go_out), ("py", py_out)):
                    print(f"--- {label}\n{text}")
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
