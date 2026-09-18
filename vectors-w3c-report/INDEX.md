# Conformance vectors (v0.1 per-check report)

Every member of this suite in one table, rejected and accepted alike. Ground
truth: ten texts vendored in `spec-vendored/` and pinned by sha256 in
`MANIFEST.json`: eight messages of the W3C public-agent-conformance list that
together fix what v0.1 of the reporting format freezes, and the two
Internet-Drafts the format's editor holds.

This corpus is 210 vectors, of which 106 a conformant verifier must not fail closed
on and 104 it must reject.

**Three subject types, one manifest.** 144 members are whole
v0.1 reports, judged by the rows of the format; 44
are Run objects of the agent-run-metrics draft; 22
are discovery snapshots of the context-discovery draft. Each member names its
subject type and the reader selects the validator by it.

**A report member is a whole report**, not one record, because two of the rules
v0.1 carries are properties of the report: whether its roll-up says its checks
could have gone negative, and whether the digest over its check set binds the
leaf count and names the tree shape. A record-level corpus could not express
either.

**Every reject member names exactly one row.** The generator runs the validator
over each member before writing it and refuses a reject that fires two rows or
an accept that fires one, so a member here demonstrates which requirement is
live rather than the fact of rejection. `MUTATION-SWEEP.md`, regenerated with
the vectors, relaxes each row in turn and records that only the members naming
it flip.

**Identifiers are minted here and bound to a sentence.** The texts carry no
requirement identifiers, so each row below quotes its sentence, the generator
locates it in the vendored copy and hashes it, and a reword stops the build.

**The 84 members of family `w3c-f-disensor`** are re-cut from the
42 delta-related pairs Nicolas Rocchia counted in his own corpus at
`NicolasRocchia/disensor@1e36257`: each pair appears once as
emitted before the freeze, rejected under the declared-slot rule with its cause,
and once re-cut against v0.1, accepted. `origin/derive_pairs.py` derives the
pairs from that repository and `origin/disensor-1e36257-pairs.json` is what it
wrote.

Regenerate byte-identically: `python3 gen_vectors.py`.
Self-check: `aee-verify vectors-w3c-report/` from the repository root, or
`python3 packaging/run_vectors.py --corpus vectors-w3c-report`; the two print
the same lines.

## Vendored text

| key | author | path | sha256 | source |
|---|---|---|---|---|
| `0001` | Kenne Ives | `spec-vendored/0001-ives-2026-09-01-coverage-block.txt` | `62bafb6e88629bda` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0001.html |
| `0025` | Nicolas Rocchia | `spec-vendored/0025-rocchia-2026-09-13-state-cause-pair-table.txt` | `2ee9306408474a69` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0025.html |
| `0036` | Evgenii Arsentev | `spec-vendored/0036-arsentev-2026-09-14-discrimination-and-populations.txt` | `7a034174eb5f27f8` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0036.html |
| `0043` | Nicolas Rocchia | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `76f5af49f11108fc` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0043.html |
| `0050` | Kenne Ives | `spec-vendored/0050-ives-2026-09-15-recomputed-delta.txt` | `1399c56136e7aa76` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0050.html |
| `0060` | Nicolas Rocchia | `spec-vendored/0060-rocchia-2026-09-16-freeze-list.txt` | `47f96e10c2ac5dc0` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0060.html |
| `0062` | Evgenii Arsentev | `spec-vendored/0062-arsentev-2026-09-17-editor-freeze-list.txt` | `b92f4a6ca926eaa8` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0062.html |
| `0069` | Evgenii Arsentev | `spec-vendored/0069-arsentev-2026-09-18-late-additions.txt` | `40153b17403b0e65` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0069.html |
| `draft-arsentev-agent-run-metrics-00` | Evgenii Arsentev | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `0ef9e7fbc39d04bf` | https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/ |
| `draft-arsentev-llm-context-discovery-00` | Evgenii Arsentev | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `13081268c70a19e9` | https://datatracker.ietf.org/doc/draft-arsentev-llm-context-discovery/ |

## Requirements

| id | row | vendored in | sentence digest | normative sentence |
|---|---|---|---|---|
| `W3C-R-001` | 1 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `87893835a3e13451` | a non-verdict state with no cause |
| `W3C-R-002` | 2 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `05fb9274ff0859d9` | void with not_applicable, out_of_scope or withheld |
| `W3C-R-003` | 3 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `587e9bc351daaed2` | not-exercised with integrity-failure |
| `W3C-R-004` | 4 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `32dd6b74795b02bd` | a confinement control that failed while the check ran |
| `W3C-R-005` | 5 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `ed9007c6e8a11eb2` | a declared exclusion with any state but not-exercised |
| `W3C-R-006` | 6 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `4ef6f3c9383ae454` | a non-verdict state carrying either qualifier |
| `W3C-R-007` | 7 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `831dc816ea23fa26` | a verdict state carrying a cause |
| `W3C-R-008` | 8 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `2c6f812fc2752889` | other-verdict foreclosed with discrimination demonstrated |
| `W3C-R-009` | 9 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `111e3eb11cdcc313` | discrimination demonstrated with other-verdict unknown |
| `W3C-R-010` | 10 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `139eba59f4dc4345` | foreclosed without a constraint set and a domain |
| `W3C-R-011` | 11 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `f68cd56a997a5773` | an asserted value without its evidence reference |
| `W3C-R-012` | 12 | `spec-vendored/0043-rocchia-2026-09-15-consolidated-table.txt` | `d2268e7db1d50fe5` | whose changed slot is the checker |
| `W3C-R-013` | (a) roll-up | `spec-vendored/0069-arsentev-2026-09-18-late-additions.txt` | `f73fd10347201018` | a roll-up states whether the checks it aggregates were capable of a negative verdict |
| `W3C-R-014` | (a) prior run | `spec-vendored/0069-arsentev-2026-09-18-late-additions.txt` | `2da5682dbbb4be1f` | a prior discriminating run only counts where check identity survives across runs |
| `W3C-R-015` | (b) set binding | `spec-vendored/0069-arsentev-2026-09-18-late-additions.txt` | `c6fe2b8552666e81` | digest match establishes a set only when the count of leaves is bound too, and a report says which tree shape it uses |
| `W3C-R-016` | declared slots | `spec-vendored/0062-arsentev-2026-09-17-editor-freeze-list.txt` | `303d488c14eed0d2` | an object whose moved is not contained in its declared set is rejected |
| `W3C-R-017` | roll-up denominator | `spec-vendored/0060-rocchia-2026-09-16-freeze-list.txt` | `526d7694de57f6c5` | never emitted without its complete denominator |
| `W3C-R-018` | roll-up counter | `spec-vendored/0060-rocchia-2026-09-16-freeze-list.txt` | `31c3dfd19fc59147` | the counter over carried against referenced |
| `W3C-R-019` | closed vocabulary | `spec-vendored/0025-rocchia-2026-09-13-state-cause-pair-table.txt` | `1b376a60d7520ff7` | because free text does not aggregate |
| `W3C-R-020` | reference mismatch | `spec-vendored/0062-arsentev-2026-09-17-editor-freeze-list.txt` | `af507f1056e619da` | resolves with a mismatch (an integrity failure) |
| `W3C-R-021` | recomputed delta | `spec-vendored/0050-ives-2026-09-15-recomputed-delta.txt` | `bc4afdb28cee9c30` | they read moved as recomputed from the two observations the object names |
| `W3C-R-022` | coverage block | `spec-vendored/0001-ives-2026-09-01-coverage-block.txt` | `50c6f490bcf092b2` | a sampled / full_coverage flag with the count of scannable files recorded before the per-repo cap |
| `W3C-R-023` | population denominator | `spec-vendored/0036-arsentev-2026-09-14-discrimination-and-populations.txt` | `04fa2499c017be72` | a claim over an empty population is reported as not claimable, not as satisfied |
| `W3C-R-024` | delta-related pair | `spec-vendored/0036-arsentev-2026-09-14-discrimination-and-populations.txt` | `d75ca465cf824295` | Unrelated pass and fail records in one corpus must not qualify |
| `ARM-R-001` | 5.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `f313511759b2f6ce` | Reporter MUST emit "1" while conforming to this specification |
| `ARM-R-002` | 3.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `a82c8c4e90b439d6` | The "end" member MUST be present when "status" is "completed",    "failed" or "aborted", and MUST NOT be present when "status" is    "running" |
| `ARM-R-003` | 3.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `1651e4aa28aef3c5` | When present, "end" MUST NOT be earlier than "start" |
| `ARM-R-004` | 3.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `532a0c7a01289d79` | a Reporter MUST NOT emit    a value other than the four listed |
| `ARM-R-005` | 3.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `b0245f78d559c0cf` | When the "steps" array is present, "step_count" MUST be    greater than or equal to the length of that array |
| `ARM-R-006` | 3.2 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `de2c45f5dcc4d136` | Within one Run, "index" values MUST be unique and MUST be assigned in    the order in which Steps began |
| `ARM-R-007` | 3.2 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `bb47f3459eea16f1` | When "kind" is "model_invocation", the "usage" and "model" members    MUST be present |
| `ARM-R-008` | 3.2 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `cbf735970617d21d` | When "kind" is "tool_call", the "tool" member MUST    be present and the "usage" member MUST NOT be present |
| `ARM-R-009` | 3.4 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `0748102d1586a9c5` | All members of a Usage object MUST be non-negative integers |
| `ARM-R-010` | 3.4 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `912e608876053400` | "cache_read_tokens" is a subset of "input_tokens" and therefore        MUST be less than or equal to it |
| `ARM-R-011` | 3.4 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `ab264faa892721d2` | "cache_read_tokens" and "cache_write_tokens"        denote disjoint subsets of "input_tokens" and their sum MUST be        less than or equal to "input_tokens" |
| `ARM-R-012` | 3.4 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `e6b6a4c51dfe30f7` | "totals" object MUST be, member by member, the sum of the    corresponding members of every Step's Usage object |
| `ARM-R-013` | 3.5 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `89119163b621c774` | One    "lifetime" value MUST NOT appear in more than one element of the same    array |
| `ARM-R-014` | 3.5 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `17816ade45921f0d` | The sum of the "tokens" members of "cache_writes" MUST equal the    "cache_write_tokens" member of the same Usage object |
| `ARM-R-015` | 3.3 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `0883bbd19a653019` | A Reporter MUST NOT    emit two Steps of one Run with the same "invocation_id" |
| `ARM-R-016` | 3.6 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `546781f078f7e248` | A Run that emits "root_run_id" and has no       parent MUST set it equal to its own "run_id" |
| `ARM-R-017` | 3.7 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `f15b1c8c7a0cfe45` | The "amount" member MUST be a JSON string matching the ABNF [RFC5234]    rule |
| `ARM-R-018` | 3.12 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `4d1f574a3f6c8983` | Its value MUST be a JSON object whose members all    have string values |
| `ARM-R-019` | 5 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `af8a371a7c03ddaa` | Timestamps MUST be strings conforming to the "date-time" production    of [RFC3339].  They MUST use the "Z" time offset |
| `ARM-R-020` | 5 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `f45b4290574244a8` | MUST be non-empty strings of at most 128    characters |
| `ARM-R-021` | 5.1 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `a9283399f2f72c8c` | A Reporter MUST NOT use an unprefixed member    name for a purpose other than the one specified here |
| `ARM-R-022` | 3.4 | `spec-vendored/draft-arsentev-agent-run-metrics-00.txt` | `77239d6671db6001` | "reasoning_tokens" is a subset of "output_tokens" and        therefore MUST be less than or equal to it |
| `LCD-R-001` | 3.1 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `dea0684290a3e21a` | A context file MUST NOT be served with a "Content-Type" of "text/    html" |
| `LCD-R-002` | 3.2 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `993eae7ed8a98e13` | A discovery mechanism defined in Section 4 MUST point at an index       resource, never directly at a detail resource |
| `LCD-R-003` | 4.1 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `b75a01b97d999548` | A publisher advertising a context file through this mechanism MUST    arrange that a GET request for "/.well-known/llm-context" on the    origin returns either |
| `LCD-R-004` | 4.3 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `cbf9300432d96463` | Its value MUST be an absolute    URI |
| `LCD-R-005` | 4.3 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `6c62b556add0487c` | A publisher MUST NOT use this record to advertise a context file    whose retrieval the same robots.txt disallows |
| `LCD-R-006` | 4.4 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `bc76905fa3c30441` | a consumer MUST    apply the following precedence, highest first |
| `LCD-R-007` | 4.4 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `9303b76c717a46a4` | A consumer MUST NOT retrieve more than one index resource per origin    per retrieval cycle |
| `LCD-R-008` | 7.2 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `de7f08a1b2a8a663` | A consumer MUST NOT attribute the content of a cross-origin index    resource to the advertising origin |
| `LCD-R-009` | 7.4 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `6bf3ffe5624cb4d3` | A consumer MUST impose its own ceiling on the size of any retrieved    context file |
| `LCD-R-010` | 3.3 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `1f8ceb1482c75131` | the response MUST carry an appropriate "Content-Language" |
| `LCD-R-011` | 4.4 | `spec-vendored/draft-arsentev-llm-context-discovery-00.txt` | `1cb26bd4e4ca5526` | a consumer MUST evaluate the exclusion    rules of [RFC9309] against the index resource's URI before retrieving    it |

## Families

| id | what the family is |
|---|---|
| `w3c-f-1` | row 1: a non-verdict state with no cause |
| `w3c-f-2` | row 2: void with a cause that describes a unit never examined |
| `w3c-f-3` | row 3: not-exercised with integrity-failure |
| `w3c-f-4` | row 4: a confinement control failed while the check ran, and the state is not void |
| `w3c-f-5` | row 5: a declared exclusion whose state is not not-exercised |
| `w3c-f-6` | row 6: a non-verdict state carrying a qualifier |
| `w3c-f-7` | row 7: a verdict state carrying a cause |
| `w3c-f-8` | row 8: other-verdict foreclosed beside discrimination demonstrated |
| `w3c-f-9` | row 9: discrimination demonstrated beside an other-verdict that is not demonstrated |
| `w3c-f-10` | row 10: foreclosed without its constraint set and domain |
| `w3c-f-11` | row 11: an asserted qualifier value without its evidence reference |
| `w3c-f-12` | row 12: discrimination demonstrated citing evidence whose changed slot is the checker |
| `w3c-f-13` | late addition (a): a roll-up says whether its checks could have gone negative |
| `w3c-f-14` | late addition (a): a prior discriminating run binds the check identity that survived |
| `w3c-f-15` | late addition (b): a digest over a set binds its leaf count and names its tree shape |
| `w3c-f-16` | declared slots: moved is contained in the declared compared set |
| `w3c-f-17` | roll-up: the aggregate carries its complete denominator |
| `w3c-f-18` | roll-up: the counter over carried against referenced recomputes |
| `w3c-f-19` | closed vocabulary: a value outside a registry is not read |
| `w3c-f-20` | carry-or-reference: a set digest that does not recompute is an integrity failure |
| `w3c-f-21` | recomputed delta: moved is read as recomputed over the observations, not as declared |
| `w3c-f-22` | coverage block: scope disclosure in controlled fields, with the pre-cap file count |
| `w3c-f-23` | population denominator: a completeness claim carries the size of its population |
| `w3c-f-24` | delta-related pair: unrelated pass and fail records do not witness discrimination |
| `w3c-f-gaps` | the two known gaps of the reference emitter, closed: void has a slot and not-exercised carries a cause |
| `w3c-f-disensor` | the 42 delta-related pairs of the disensor corpus at 1e36257, re-cut against v0.1 |
| `arm-f-run` | agent run metrics: the Run object's own members |
| `arm-f-steps` | agent run metrics: the Step objects and their order |
| `arm-f-usage` | agent run metrics: the Usage invariants and the cache-write ledger |
| `arm-f-totals` | agent run metrics: the totals as the sum of the steps |
| `arm-f-serialization` | agent run metrics: timestamps, identifiers, labels, cost and extensions |
| `lcd-f-publisher` | context discovery: what the origin advertises and serves |
| `lcd-f-consumer` | context discovery: what a consumer resolves, retrieves and attributes |

## Vectors

| id | kind | subject | family | requirements | rejected under |
|---|---|---|---|---|---|
| `v0164c803c34c3c4c` | reject | report | w3c-f-21 | W3C-R-021 | W3C-R-021 |
| `v02b5aa1c6f152cb8` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v02ca1b3fce47e3ca` | reject | report | w3c-f-13 | W3C-R-013 | W3C-R-013 |
| `v0320e079760670a9` | reject | agent-run-metrics | arm-f-totals | ARM-R-012 | ARM-R-012 |
| `v04c9ebbce835c688` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v05639d5c3c8c0748` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v05d60efad92ebaf8` | reject | agent-run-metrics | arm-f-serialization | ARM-R-019 | ARM-R-019 |
| `v066b4ec60aeb45ea` | accept | agent-run-metrics | arm-f-usage | ARM-R-022 | none |
| `v0802ba8c1adfd735` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v095044ecfd531f0e` | accept | report | w3c-f-18 | W3C-R-018 | none |
| `v096b392478fcf6fe` | reject | agent-run-metrics | arm-f-usage | ARM-R-014 | ARM-R-014 |
| `v0a35d1d5e36bf503` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v0b7303efe873ba5e` | reject | report | w3c-f-3 | W3C-R-003 | W3C-R-003 |
| `v0b91eaac1cdcc248` | reject | report | w3c-f-15 | W3C-R-015 | W3C-R-015 |
| `v0beb3b74beb99bf1` | accept | report | w3c-f-13 | W3C-R-013 | none |
| `v0de121457dabc092` | accept | report | w3c-f-8 | W3C-R-008 | none |
| `v0e100bb5f5f9b549` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v0e31d851b22cf706` | reject | report | w3c-f-18 | W3C-R-018 | W3C-R-018 |
| `v134763ca9f01867c` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-005 | LCD-R-005 |
| `v13a01b0473aa7595` | accept | report | w3c-f-14 | W3C-R-014 | none |
| `v143660ae522c83b7` | reject | agent-run-metrics | arm-f-run | ARM-R-004 | ARM-R-004 |
| `v1916a6ce919c9c5d` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v1b2f5cbd6e1c2bd6` | accept | llm-context-discovery | lcd-f-consumer | LCD-R-011 | none |
| `v1c875fc4c36aa06d` | reject | agent-run-metrics | arm-f-usage | ARM-R-013 | ARM-R-013 |
| `v1d69f990f88ee513` | reject | report | w3c-f-2 | W3C-R-002 | W3C-R-002 |
| `v1e8ac2d635dba457` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v1f14e5858f61534b` | reject | llm-context-discovery | lcd-f-consumer | LCD-R-006 | LCD-R-006 |
| `v1f6745a7841076d0` | accept | agent-run-metrics | arm-f-totals | ARM-R-012 | none |
| `v1f766b6f6eab757b` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v20aff5acca86c219` | accept | agent-run-metrics | arm-f-run | ARM-R-001 | none |
| `v20cc6cdd082e0e45` | accept | agent-run-metrics | arm-f-steps | ARM-R-008 | none |
| `v226c47602e7c328a` | accept | agent-run-metrics | arm-f-serialization | ARM-R-020 | none |
| `v234281fbdc8cf63d` | reject | agent-run-metrics | arm-f-steps | ARM-R-008 | ARM-R-008 |
| `v236138ba2b69c385` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v244f25416a939dab` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v24d2ed3c70934115` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v28404c7cebd1aa87` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v28ed5f74569195f7` | reject | report | w3c-f-13 | W3C-R-013 | W3C-R-013 |
| `v296d1a74025adc1c` | accept | agent-run-metrics | arm-f-usage | ARM-R-011 | none |
| `v2a00957a7f256025` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v2a84fd527effc283` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v2aec9aae50bd3992` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v2c385e784e0bac52` | accept | report | w3c-f-20 | W3C-R-020 | none |
| `v2d246349f0051a1c` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v2ec19f234a21c62f` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-005 | none |
| `v2ec6bcd8fa774fbc` | reject | agent-run-metrics | arm-f-steps | ARM-R-007 | ARM-R-007 |
| `v2fc9dabfe555dd2a` | accept | agent-run-metrics | arm-f-run | ARM-R-004 | none |
| `v3019a3f576b2feaa` | accept | agent-run-metrics | arm-f-steps | ARM-R-006 | none |
| `v31b1b47ae148af1f` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v321b67cda11cd67d` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v337f2e7acc229d39` | accept | agent-run-metrics | arm-f-run | ARM-R-002 | none |
| `v34d068d7913a006d` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v35f9c4d0fac828df` | reject | agent-run-metrics | arm-f-run | ARM-R-001 | ARM-R-001 |
| `v36840e71fe0f6f69` | reject | report | w3c-f-10 | W3C-R-010 | W3C-R-010 |
| `v36d216e75e2526d3` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v36fe3597c4a38c48` | reject | report | w3c-f-23 | W3C-R-023 | W3C-R-023 |
| `v3749565d86ca5c4a` | accept | report | w3c-f-19 | W3C-R-019 | none |
| `v3949a35e22b64a4d` | accept | report | w3c-f-gaps | W3C-R-001, W3C-R-002 | none |
| `v3bd7c51c7aa62b13` | reject | agent-run-metrics | arm-f-steps | ARM-R-015 | ARM-R-015 |
| `v3c96293f578f1b72` | accept | agent-run-metrics | arm-f-steps | ARM-R-007 | none |
| `v3c97c572e8c9f739` | accept | llm-context-discovery | lcd-f-consumer | LCD-R-007 | none |
| `v3cacf9884fdadcbd` | reject | report | w3c-f-4 | W3C-R-004 | W3C-R-004 |
| `v3ce86915f6ee7b7e` | reject | report | w3c-f-12 | W3C-R-012 | W3C-R-012 |
| `v44df6ea141d977e3` | accept | report | w3c-f-22 | W3C-R-022 | none |
| `v466ace50ae1bbbc0` | reject | agent-run-metrics | arm-f-serialization | ARM-R-018 | ARM-R-018 |
| `v468366f762a8bdf4` | accept | agent-run-metrics | arm-f-usage | ARM-R-013 | none |
| `v468d3d041713bf7d` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v4833c3b1ab7dceef` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v490f13fcc91800c2` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v4acd588a3c0cc94e` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v4c65aa9f3b8e431b` | reject | agent-run-metrics | arm-f-run | ARM-R-005 | ARM-R-005 |
| `v500e95527f03d635` | reject | report | w3c-f-15 | W3C-R-015 | W3C-R-015 |
| `v50ef3e4bd9f138bc` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-004 | none |
| `v51667084eded3199` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v5187613995b28f33` | reject | agent-run-metrics | arm-f-usage | ARM-R-010 | ARM-R-010 |
| `v532f7ce5761b5119` | reject | report | w3c-f-22 | W3C-R-022 | W3C-R-022 |
| `v57c34a0d07c3f4b4` | reject | report | w3c-f-7 | W3C-R-007 | W3C-R-007 |
| `v57e0040ff0ad8028` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v5821b8f0393e7bda` | reject | report | w3c-f-5 | W3C-R-005 | W3C-R-005 |
| `v58a46ac55b803155` | reject | report | w3c-f-1 | W3C-R-001 | W3C-R-001 |
| `v58f8859669e43d97` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-002 | none |
| `v59d76289515e9386` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-004 | LCD-R-004 |
| `v59d7c0268acaec8c` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v5bd6bf20b3a439e7` | reject | agent-run-metrics | arm-f-serialization | ARM-R-021 | ARM-R-021 |
| `v5ca57343666ee192` | accept | report | w3c-f-4 | W3C-R-004 | none |
| `v5f4b5733c5575b9f` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v5fa1792bbc9887c1` | reject | llm-context-discovery | lcd-f-consumer | LCD-R-008 | LCD-R-008 |
| `v5fc98bb46ae0c270` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v6027f56ef7676a5d` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-003 | LCD-R-003 |
| `v61b7b88845756190` | reject | report | w3c-f-6 | W3C-R-006 | W3C-R-006 |
| `v62ba14cf314c1762` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v6775108beb739acf` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v67fa8be2bfc39fc3` | reject | report | w3c-f-11 | W3C-R-011 | W3C-R-011 |
| `v6886f2dea5b8d30c` | accept | report | w3c-f-23 | W3C-R-023 | none |
| `v6a468aead6a0997c` | accept | report | w3c-f-17 | W3C-R-017 | none |
| `v6ad97761064d2e7f` | accept | llm-context-discovery | lcd-f-consumer | LCD-R-008 | none |
| `v6c32781926fcdd5c` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v6d1bd6df443e2fc5` | accept | report | w3c-f-10 | W3C-R-010 | none |
| `v6d6b62187cfc99ef` | accept | llm-context-discovery | lcd-f-consumer | LCD-R-006 | none |
| `v6ea8de1e96eaa2e7` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v6ec17de3ba07cb6b` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-010 | LCD-R-010 |
| `v702752d4edc33185` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v732ec2a879e6f405` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v745e2452410fd4fa` | accept | agent-run-metrics | arm-f-serialization | ARM-R-018 | none |
| `v74785d5a33f1eadb` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v748108bc07240595` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-010 | none |
| `v750f005fde7f2658` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v756f896b8328c22f` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v75a3e8e255520a6f` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v75b42fab65afc397` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v76384d66512cc6a4` | accept | agent-run-metrics | arm-f-serialization | ARM-R-017 | none |
| `v76eff81a9ab7e6dd` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v78d66a8e657c2772` | accept | agent-run-metrics | arm-f-usage | ARM-R-010 | none |
| `v7b61413822815cfb` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-003 | none |
| `v802e4cd278a0fbd2` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-002 | LCD-R-002 |
| `v80a61d35636233e0` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v80e52166b6a54bab` | reject | llm-context-discovery | lcd-f-consumer | LCD-R-009 | LCD-R-009 |
| `v8357c7ec77007bab` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v84b862295e8bd427` | accept | report | w3c-f-5 | W3C-R-005 | none |
| `v85031f0b2100719d` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v86a6eabef30e4ba5` | accept | report | w3c-f-16 | W3C-R-016 | none |
| `v89900ec30e1dfe82` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v8ab485d5b009b46c` | accept | agent-run-metrics | arm-f-usage | ARM-R-009 | none |
| `v8c712e7583459c72` | reject | report | w3c-f-14 | W3C-R-014 | W3C-R-014 |
| `v9008f04238a86871` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v92125f665ba987c8` | accept | report | w3c-f-gaps | W3C-R-001, W3C-R-005 | none |
| `v92ffeb0789292808` | reject | report | w3c-f-15 | W3C-R-015 | W3C-R-015 |
| `v9357f80ad67b7286` | accept | agent-run-metrics | arm-f-serialization | ARM-R-021 | none |
| `v93bd3bcb57b6e753` | reject | llm-context-discovery | lcd-f-consumer | LCD-R-011 | LCD-R-011 |
| `v93fe9e276462b6ea` | reject | agent-run-metrics | arm-f-run | ARM-R-016 | ARM-R-016 |
| `v97f7609c206c765b` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v983f5e4b5f7cdc29` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v9944d4e53d2325c1` | reject | agent-run-metrics | arm-f-serialization | ARM-R-017 | ARM-R-017 |
| `v9a4bca129398f9ad` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `v9ae4fd335cc78dff` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v9b20d711c1a0b368` | accept | report | w3c-f-22 | W3C-R-022 | none |
| `v9b5fd819ac7976bb` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `v9c3952c5f1467764` | reject | agent-run-metrics | arm-f-run | ARM-R-003 | ARM-R-003 |
| `va10f5159a7356122` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `va1d8a3aff7580097` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `va3140cc886b694fe` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `va3cc235693ed9aa0` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `va5e6f618c7b58bf9` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `va6299cdbedfb81f8` | reject | agent-run-metrics | arm-f-steps | ARM-R-006 | ARM-R-006 |
| `va67e7c700fd6e572` | accept | report | w3c-f-15 | W3C-R-015 | none |
| `va80130b2557877d0` | reject | report | w3c-f-8 | W3C-R-008 | W3C-R-008 |
| `vaa9022b28508fbff` | accept | agent-run-metrics | arm-f-steps | ARM-R-015 | none |
| `vac4901ced8434b96` | accept | report | w3c-f-7 | W3C-R-007 | none |
| `vac73991b7eab80be` | accept | report | w3c-f-24 | W3C-R-024 | none |
| `vadc27fccee1d1084` | reject | llm-context-discovery | lcd-f-consumer | LCD-R-007 | LCD-R-007 |
| `vae5bf9e259ca9fa2` | reject | report | w3c-f-23 | W3C-R-023 | W3C-R-023 |
| `vaefd4325cf8ba171` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vaf075fdad27ad97c` | reject | report | w3c-f-9 | W3C-R-009 | W3C-R-009 |
| `vb0049d239061e73f` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vb0c5a3492d65d1eb` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vb2f73291e8fe10d1` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vb31d26cffc802d7f` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vb9efe6cec61c9489` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vba28e0271213f6ef` | accept | report | w3c-f-23 | W3C-R-023 | none |
| `vba4433cd2a45fdd4` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vbac3c7923a48045f` | reject | agent-run-metrics | arm-f-usage | ARM-R-022 | ARM-R-022 |
| `vbb214dabb5d9514e` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vbb34b5903d030863` | accept | report | w3c-f-15 | W3C-R-015 | none |
| `vbcbbc065f5978092` | reject | report | w3c-f-24 | W3C-R-024 | W3C-R-024 |
| `vbecc90485b846e5a` | accept | agent-run-metrics | arm-f-run | ARM-R-016 | none |
| `vc0109df9efce7825` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vc103c9ebc091176a` | accept | report | w3c-f-21 | W3C-R-021 | none |
| `vc33e992bbb6c0ddd` | accept | report | w3c-f-11 | W3C-R-011 | none |
| `vc4cc6abd16cb7848` | reject | agent-run-metrics | arm-f-serialization | ARM-R-020 | ARM-R-020 |
| `vc54053aab3059e9a` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vc593cdd0df015927` | accept | agent-run-metrics | arm-f-run | ARM-R-005 | none |
| `vc60f8ca141d363b3` | accept | agent-run-metrics | arm-f-run | ARM-R-003 | none |
| `vc66d903f67842004` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vc78c495fa2865996` | accept | agent-run-metrics | arm-f-usage | ARM-R-014 | none |
| `vccd7d6407f77183e` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vcf73d5dd4703dd31` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vcfa49a358963e8a4` | reject | report | w3c-f-19 | W3C-R-019 | W3C-R-019 |
| `vd10e80041b1344d6` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vd182df4e94785dcb` | reject | agent-run-metrics | arm-f-usage | ARM-R-011 | ARM-R-011 |
| `vd443179d7d37fec0` | accept | report | w3c-f-1 | W3C-R-001 | none |
| `vd568fb04bbfe75c7` | reject | agent-run-metrics | arm-f-run | ARM-R-002 | ARM-R-002 |
| `vd6dde6d30a8b5f66` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vd70263ec9f011a2e` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vd9d8d4550595657e` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vda3eac1602712021` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vdd0e8bbaa7a00714` | accept | report | w3c-f-6 | W3C-R-006 | none |
| `ve066f2cc9ab0f657` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `ve0d3587f68b26b73` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `ve0d62017a7afcbb9` | accept | report | w3c-f-2 | W3C-R-002 | none |
| `ve25d40b143d66912` | reject | agent-run-metrics | arm-f-usage | ARM-R-009 | ARM-R-009 |
| `ve7ec53356216c396` | reject | report | w3c-f-17 | W3C-R-017 | W3C-R-017 |
| `ve81bc854b081493b` | accept | agent-run-metrics | arm-f-serialization | ARM-R-019 | none |
| `ve955eb9e7db5531a` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vebd93abb8ee3a837` | reject | report | w3c-f-20 | W3C-R-020 | W3C-R-020 |
| `ved9c03fc4eb64623` | accept | report | w3c-f-3 | W3C-R-003 | none |
| `vedd446a69ad39c40` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `veea533d0c7f0b4f6` | accept | llm-context-discovery | lcd-f-consumer | LCD-R-009 | none |
| `vf085de0c74dfcad0` | accept | report | w3c-f-9 | W3C-R-009 | none |
| `vf13537a247c05d3c` | accept | report | w3c-f-12 | W3C-R-012 | none |
| `vf3bb8a41a6a2b3bb` | reject | report | w3c-f-disensor | W3C-R-016 | W3C-R-016 |
| `vf4fa4d406b870a94` | reject | report | w3c-f-16 | W3C-R-016 | W3C-R-016 |
| `vf53c0cf19e40b8b7` | reject | report | w3c-f-22 | W3C-R-022 | W3C-R-022 |
| `vf5442792fb3883dc` | accept | llm-context-discovery | lcd-f-publisher | LCD-R-001 | none |
| `vf5a1a13446f43395` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vf749dad865952b0e` | reject | llm-context-discovery | lcd-f-publisher | LCD-R-001 | LCD-R-001 |
| `vf7fa99884a005fcb` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vf913f33b40963260` | accept | report | w3c-f-13 | W3C-R-013 | none |
| `vf94f59c1cd4d3670` | accept | report | w3c-f-disensor | W3C-R-016 | none |
| `vfb7eae4d1aede3eb` | accept | report | w3c-f-13 | W3C-R-013 | none |
| `vfe47c408d2abc7fb` | accept | report | w3c-f-disensor | W3C-R-016 | none |
