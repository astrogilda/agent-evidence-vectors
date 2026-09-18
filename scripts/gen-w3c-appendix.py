#!/usr/bin/env python3
"""Render docs/W3C-V01-CONFORMANCE-APPENDIX.md from vectors-w3c-report/MANIFEST.json.

    python3 scripts/gen-w3c-appendix.py            # write the appendix
    python3 scripts/gen-w3c-appendix.py --check    # refuse when the file on disk differs

The appendix is the conformance set for v0.1 of the W3C public-agent-conformance
reporting format, in the form the editor can reference: every rejection row
with the vector that must be rejected under it and the vector that must pass,
the sentence the row binds to and that sentence's digest. Every identifier in it
is a function of the vectors' own bytes, so the file is rendered from the
manifest rather than typed, and the regenerability gate refuses a copy that
drifted from the corpus.
"""

# ruff: noqa: E501 -- the appendix paragraphs are written unwrapped on purpose:
# GitHub renders a hard line break literally, and this file is the one place the
# prose is authored, so the source lines are as long as the paragraphs.
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parent.parent
MANIFEST = REPO / "vectors-w3c-report" / "MANIFEST.json"
TARGET = REPO / "docs" / "W3C-V01-CONFORMANCE-APPENDIX.md"

ROW_ORDER = [f"W3C-R-{n:03d}" for n in range(1, 25)]

SECTIONS = (
    ("The twelve rejection rows", ROW_ORDER[:12]),
    ("The two late additions of 18 September", ROW_ORDER[12:15]),
    ("The rules the freeze list and the editor's restatement carry", ROW_ORDER[15:20]),
    ("The rules the thread settled beside the table", ROW_ORDER[20:24]),
)

INTRO = """# Conformance appendix for v0.1 of the reporting format

This is the conformance set for v0.1 of the per-check reporting format of the W3C public-agent-conformance community group, written so that an editor can reference it by row and an implementer can run it without reading the thread. Every row of the rejection table is backed by two members of the corpus `vectors-w3c-report/` in the `agent-evidence-vectors` repository: one report that a conforming validator must reject under that row and no other, and one report, as close to it as one change allows, that the validator must accept. The corpus judges itself with two independent readers, one in Go and one in Python, and a test holds their output identical over the committed members and over deliberately broken copies.

The rows are the group's. The consolidated table Nicolas Rocchia published on 15 September is the text each row binds to; the two late additions Evgenii Arsentev took into sections 3 and 4 on 18 September, from Nicholas Templeman's proposal and the group's support for it, are rows 13 to 15; the rules the completed freeze list and the editor's restatement carry are rows 16 to 20; and the rules the thread settled beside the table, Kenne Ives's recomputed delta and coverage block and Arsentev's population rule and delta-related pair, are rows 21 to 24. A row's identifier is minted by the corpus and bound to a sentence of the vendored message by digest, because the messages carry no identifiers and a message number names a position rather than a sentence. A reword of the sentence stops the corpus from building, which is the property that makes the identifier citable.

A member of the corpus is a whole report rather than one record, because two of the rules are properties of the report and not of any record in it: whether the roll-up says its checks were capable of a negative verdict, and whether the digest over the check set binds the leaf count and names the tree shape. The corpus also carries the two gaps the editor recorded about the reference emitter on 18 September, that `void` had no slot and that `not-exercised` carried no cause, as members that show both closed, and it carries the 42 delta-related pairs Rocchia counted in his own corpus, each once as it was emitted before the freeze and once re-cut against v0.1. A mutation sweep, regenerated with the vectors and published beside them, relaxes each row in turn and records that only the members naming it flip.

## How to read a row

The reject member's `subject` is the report; its `expected.rejects` names the one row; the accept member differs from it by the smallest change that satisfies the row. Both cite the requirement in `requirements`, so a specification change that reworded the sentence would fail the pair by name. The sentence column quotes the vendored text with its line break where the sentence spans one; the digest column is the first sixteen hex digits of the SHA-256 over those bytes, and the full digest is in the manifest.
"""

OUTRO = """
## The crosswalk from the harness's report

The reference emitter in `packaging/agent_evidence_vectors/w3creport.py` writes a v0.1 report from the report the AEE harness writes, one per-check record per replayed vector. The two altitudes are kept apart: the harness's `result` stays four-valued and recomputable, and the per-check record says what a consumer may conclude about the statement the vector carries. `pass` is a valid verdict with result `pass` or `pass_indirect`, the result carried as the qualifier; `fail` is a valid verdict with result `fail` or `degraded`, or an invalid verdict, with the codes carried; `inconclusive` is the indeterminate kind, with cause `reading-committed` and the condition the rail committed to, or `reading-uncommitted` with the declared readings; `not-exercised` is a manifest entry declaring `expected.unmeasurableBecause`, reported with cause `precondition-unsatisfiable` and that text, or a report member the manifest expects and the rail left absent, with cause `unavailable`; `void` is a harness that could not establish a verdict, with cause `harness-failure` and the rail's errors or exit as detail. The report the emitter writes from the AEE corpus conforms: no row fires on it.

## Two further subjects in the same corpus

The same manifest carries members of two other subject types, judged by their own sentences in their own modules: the Run object of `draft-arsentev-agent-run-metrics-00`, twenty-two rows over the members and invariants a validator can read off one Report, and the discovery snapshot of `draft-arsentev-llm-context-discovery-00`, eleven rows over what an origin advertises and what a consumer resolves. Their tables follow the same shape and are listed after the report rows.
"""


def load() -> dict[str, Any]:
    with open(MANIFEST, encoding="utf-8") as handle:
        data: dict[str, Any] = json.load(handle)
        return data


def members_for(manifest: dict[str, Any], row: str) -> tuple[list[str], list[str]]:
    rejects = [e["id"] for e in manifest["vectors"] if e["expected"]["rejects"] == [row]]
    accepts = [
        e["id"] for e in manifest["vectors"]
        if e["kind"] == "accept" and row in e["requirements"]
    ]
    return rejects, accepts


def table(manifest: dict[str, Any], rows: list[str]) -> str:
    requirements = {r["id"]: r for r in manifest["requirements"]}
    lines = [
        "| row | reject | accept | sentence | digest |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        req = requirements[row]
        rejects, accepts = members_for(manifest, row)
        sentence = req["sentence"].replace("\n", " ").replace("|", "\\|")
        lines.append(
            f"| `{row}` ({req['row']}) | {', '.join(f'`{r}`' for r in rejects) or 'none'} | "
            f"{', '.join(f'`{a}`' for a in accepts) or 'none'} | {sentence} | "
            f"`{req['sentenceDigest'][:16]}` |"
        )
    return "\n".join(lines)


def render(manifest: dict[str, Any]) -> str:
    parts = [INTRO]
    for heading, rows in SECTIONS:
        parts.append(f"\n## {heading}\n\n{table(manifest, rows)}\n")
    parts.append(OUTRO)
    for prefix, heading in (("ARM-R-", "Run object rows"), ("LCD-R-", "Discovery snapshot rows")):
        rows = [r["id"] for r in manifest["requirements"] if r["id"].startswith(prefix)]
        parts.append(f"\n## {heading}\n\n{table(manifest, rows)}\n")
    vendored = "\n".join(
        f"| `{key}` | {pin['author']} | `{pin['sha256']}` | {pin['source']} |"
        for key, pin in manifest["specVendored"].items()
    )
    parts.append(
        "\n## The vendored text\n\n| key | author | sha256 | source |\n|---|---|---|---|\n"
        + vendored + "\n"
    )
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="refuse a file this does not emit")
    args = parser.parse_args()
    text = render(load())
    if args.check:
        current = TARGET.read_text(encoding="utf-8") if TARGET.exists() else None
        if current != text:
            print(f"FAIL: {TARGET.relative_to(REPO)} differs from what the manifest renders",
                  file=sys.stderr)
            return 1
        print(f"OK {TARGET.relative_to(REPO)} is what the manifest renders")
        return 0
    TARGET.write_text(text, encoding="utf-8")
    print(f"wrote {TARGET.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
