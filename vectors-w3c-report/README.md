# v0.1 per-check report conformance corpus

The conformance set for v0.1 of the per-check reporting format of the W3C
public-agent-conformance community group, as whole reports: every rejection row
of the consolidated table backed by a member that must be rejected under that
row alone and a member that must pass, the two additions of 18 September, the
rules the freeze list and the editor's restatement carry, and the rules the
thread settled beside the table. The same manifest carries members of two
further subject types, the Run object of `draft-arsentev-agent-run-metrics-00`
and the discovery snapshot of `draft-arsentev-llm-context-discovery-00`, judged
by their own sentences.

## The text is vendored and every identifier is a sentence

The list messages and the two drafts carry no requirement identifiers. Each
row here quotes its normative sentence, `gen_vectors.py` locates that sentence
in the vendored copy under `spec-vendored/`, records the line it derived, and
hashes the bytes; `MANIFEST.json` pins every vendored file by sha256 and names
its author and source. A reword stops the build rather than re-pointing the
members that cite the sentence. `INDEX.md` lists every requirement with its
digest and every member with the row it is rejected under.

## Two readers, held identical

`aee-verify vectors-w3c-report/` judges the corpus through
`corpora/w3creport.go`, and `python3 packaging/run_vectors.py --corpus
vectors-w3c-report` judges it through
`packaging/agent_evidence_vectors/w3creport.py`; the run-metrics and
context-discovery members have their own modules on both rails.
`scripts/w3c-rails-parity-test.py` diffs every line the two print over the
committed corpus and over mutated copies.

## The mutation sweep

`MUTATION-SWEEP.md` is regenerated with the vectors: each row is relaxed in
turn and the corpus replayed, and the table records that only the members
naming the row flipped. The generator refuses to write a corpus in which any
row leaks.

## The 42 pairs

Family `w3c-f-disensor` re-cuts the 42 delta-related pairs a participant
counted in his own corpus at the commit the manifest names, each once as it
was emitted before the freeze, rejected under the declared-slot rule with its
cause, and once against v0.1, accepted. `origin/derive_pairs.py` derives the
pairs from that repository and the checker it pins; the JSON it wrote is
committed beside it and the generator reads only that.

## The appendix and the emitter

`docs/W3C-V01-CONFORMANCE-APPENDIX.md` is rendered from the manifest by
`scripts/gen-w3c-appendix.py`. The reference emitter is the same Python
module: `agent-evidence-vectors --emit-w3c-report PATH` writes a v0.1 report
from the harness's own conformance report, under the crosswalk the module
states, and the report it writes from the AEE corpus conforms.

Regenerate byte-identically: `python3 gen_vectors.py`. Refuse a drifted tree:
`python3 gen_vectors.py --check`.
