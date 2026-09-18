#!/usr/bin/env python3
"""Tests for the owner-path permit in pre-push-identity-scan.py.

WHY THIS FILE EXISTS. The scanner refuses first-party names in this public,
product-neutral repository. The organisation that owns the repository is named
in its own clone URL, its badge targets and its citation file, and a URL cannot
avoid naming its owner, so one narrow permit was added: the handle passes where
a slash and one of the three repository names follow it, and nowhere else.

A permit on a refusal is the one change that can only ever loosen, and a
loosening that goes unnoticed is indistinguishable from the control working. So
every case below asserts a direction. The permitted shapes are here to prove the
push is possible at all; the refused ones are the point, and they outnumber them.

The tokens are built from hex at run time, exactly as the scanner holds its own,
so this file can be read by anyone without carrying the strings it is about.

Usage: python3 scripts/pre-push-identity-scan-test.py
Exit 0 when every case holds; 1 on a summary of the failures.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("scan", HERE / "pre-push-identity-scan.py")
assert _spec is not None and _spec.loader is not None
scan = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(scan)


def _hex(value: str) -> str:
    return bytes.fromhex(value).decode("ascii")


OWNER = _hex("70726f626974796169")
COMPANY = _hex("70726f62697479")
SITE = _hex("67657470726f62697479") + ".dev"
OTHER = _hex("6d617463686c6f636b")

_sidecar = scan.Sidecar()


def refused(line: str) -> bool:
    """Whether the scanner would report this as an added line."""
    scanned = scan.permit("+" + line)
    if any(rule.search(scanned) for _, rule in scan.RULES):
        return True
    return bool(_sidecar.labels(scanned[1:]))


PERMITTED = (
    ("an owner-qualified path", f"{OWNER}/agent-evidence-vectors"),
    ("a web URL", f"https://github.com/{OWNER}/agent-evidence-vocabulary/blob/main/README.md"),
    ("an ssh URL", f"git@github.com:{OWNER}/agent-evidence-admission.git"),
    ("a package source URL", f"git+https://github.com/{OWNER}/agent-evidence-vectors@v0.11.1"),
    ("an action reference", f"uses: {OWNER}/agent-evidence-vectors@v0.11.1"),
)

REFUSED = (
    ("the handle with no repository after it", f"maintainer of the {OWNER} organisation"),
    ("the handle before a repository not ours", f"{OWNER}/something-else"),
    ("the handle ending a sentence", f"the owner is {OWNER}."),
    ("an organisation page, which is not a repository URL", f"https://github.com/{OWNER}"),
    ("the company word alone", f"built by {COMPANY} in 2026"),
    ("the company word beside a permitted path", f"{OWNER}/agent-evidence-vectors run by {COMPANY}"),
    ("the website in a sentence", f"see {SITE} for more"),
    ("the website inside a link", f"[docs](https://{SITE}/predicate/v1/)"),
    ("the website bare", SITE),
    ("another first-party product", f"the {OTHER} runtime"),
)


def main() -> int:
    failures: list[str] = []
    for what, line in PERMITTED:
        if refused(line):
            failures.append(f"{what}: refused, but the permit exists for exactly this shape")
        else:
            print(f"ok   permitted  {what}")
    for what, line in REFUSED:
        if refused(line):
            print(f"ok   refused    {what}")
        else:
            failures.append(f"{what}: PASSED the scanner, which widens the permit to the bare name")
    for line in failures:
        print(f"FAIL {line}", file=sys.stderr)
    total = len(PERMITTED) + len(REFUSED)
    print(f"{total - len(failures)}/{total} cases held")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
