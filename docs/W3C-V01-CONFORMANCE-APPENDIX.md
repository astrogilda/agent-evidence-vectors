# Conformance appendix for v0.1 of the reporting format

This is the conformance set for v0.1 of the per-check reporting format of the W3C public-agent-conformance community group, written so that an editor can reference it by row and an implementer can run it without reading the thread. Every row of the rejection table is backed by two members of the corpus `vectors-w3c-report/` in the `agent-evidence-vectors` repository: one report that a conforming validator must reject under that row and no other, and one report, as close to it as one change allows, that the validator must accept. The corpus judges itself with two independent readers, one in Go and one in Python, and a test holds their output identical over the committed members and over deliberately broken copies.

The rows are the group's. The consolidated table Nicolas Rocchia published on 15 September is the text each row binds to; the two late additions Evgenii Arsentev took into sections 3 and 4 on 18 September, from Nicholas Templeman's proposal and the group's support for it, are rows 13 to 15; the rules the completed freeze list and the editor's restatement carry are rows 16 to 20; and the rules the thread settled beside the table, Kenne Ives's recomputed delta and coverage block and Arsentev's population rule and delta-related pair, are rows 21 to 24. A row's identifier is minted by the corpus and bound to a sentence of the vendored message by digest, because the messages carry no identifiers and a message number names a position rather than a sentence. A reword of the sentence stops the corpus from building, which is the property that makes the identifier citable.

A member of the corpus is a whole report rather than one record, because two of the rules are properties of the report and not of any record in it: whether the roll-up says its checks were capable of a negative verdict, and whether the digest over the check set binds the leaf count and names the tree shape. The corpus also carries the two gaps the editor recorded about the reference emitter on 18 September, that `void` had no slot and that `not-exercised` carried no cause, as members that show both closed, and it carries the 42 delta-related pairs Rocchia counted in his own corpus, each once as it was emitted before the freeze and once re-cut against v0.1. A mutation sweep, regenerated with the vectors and published beside them, relaxes each row in turn and records that only the members naming it flip.

## How to read a row

The reject member's `subject` is the report; its `expected.rejects` names the one row; the accept member differs from it by the smallest change that satisfies the row. Both cite the requirement in `requirements`, so a specification change that reworded the sentence would fail the pair by name. The sentence column quotes the vendored text with its line break where the sentence spans one; the digest column is the first sixteen hex digits of the SHA-256 over those bytes, and the full digest is in the manifest.

## The twelve rejection rows

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `W3C-R-001` (1) | `v58a46ac55b803155` | `v3949a35e22b64a4d`, `v92125f665ba987c8`, `vd443179d7d37fec0` | a non-verdict state with no cause | `87893835a3e13451` |
| `W3C-R-002` (2) | `v1d69f990f88ee513` | `v3949a35e22b64a4d`, `ve0d62017a7afcbb9` | void with not_applicable, out_of_scope or withheld | `05fb9274ff0859d9` |
| `W3C-R-003` (3) | `v0b7303efe873ba5e` | `ved9c03fc4eb64623` | not-exercised with integrity-failure | `587e9bc351daaed2` |
| `W3C-R-004` (4) | `v3cacf9884fdadcbd` | `v5ca57343666ee192` | a confinement control that failed while the check ran | `32dd6b74795b02bd` |
| `W3C-R-005` (5) | `v5821b8f0393e7bda` | `v84b862295e8bd427`, `v92125f665ba987c8` | a declared exclusion with any state but not-exercised | `ed9007c6e8a11eb2` |
| `W3C-R-006` (6) | `v61b7b88845756190` | `vdd0e8bbaa7a00714` | a non-verdict state carrying either qualifier | `4ef6f3c9383ae454` |
| `W3C-R-007` (7) | `v57c34a0d07c3f4b4` | `vac4901ced8434b96` | a verdict state carrying a cause | `831dc816ea23fa26` |
| `W3C-R-008` (8) | `va80130b2557877d0` | `v0de121457dabc092` | other-verdict foreclosed with discrimination demonstrated | `2c6f812fc2752889` |
| `W3C-R-009` (9) | `vaf075fdad27ad97c` | `vf085de0c74dfcad0` | discrimination demonstrated with other-verdict unknown | `111e3eb11cdcc313` |
| `W3C-R-010` (10) | `v36840e71fe0f6f69` | `v6d1bd6df443e2fc5` | foreclosed without a constraint set and a domain | `139eba59f4dc4345` |
| `W3C-R-011` (11) | `v67fa8be2bfc39fc3` | `vc33e992bbb6c0ddd` | an asserted value without its evidence reference | `f68cd56a997a5773` |
| `W3C-R-012` (12) | `v3ce86915f6ee7b7e` | `vf13537a247c05d3c` | whose changed slot is the checker | `d2268e7db1d50fe5` |

## The two late additions of 18 September

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `W3C-R-013` ((a) roll-up) | `v02ca1b3fce47e3ca`, `v28ed5f74569195f7` | `v0beb3b74beb99bf1`, `vf913f33b40963260`, `vfb7eae4d1aede3eb` | a roll-up states whether the checks it aggregates were capable of a negative verdict | `f73fd10347201018` |
| `W3C-R-014` ((a) prior run) | `v8c712e7583459c72` | `v13a01b0473aa7595` | a prior discriminating run only counts where check identity survives across runs | `2da5682dbbb4be1f` |
| `W3C-R-015` ((b) set binding) | `v0b91eaac1cdcc248`, `v500e95527f03d635`, `v92ffeb0789292808` | `va67e7c700fd6e572`, `vbb34b5903d030863` | digest match establishes a set only when the count of leaves is bound too, and a report says which tree shape it uses | `c6fe2b8552666e81` |

## The rules the freeze list and the editor's restatement carry

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `W3C-R-016` (declared slots) | `v05639d5c3c8c0748`, `v0a35d1d5e36bf503`, `v1916a6ce919c9c5d`, `v1e8ac2d635dba457`, `v24d2ed3c70934115`, `v2a84fd527effc283`, `v2aec9aae50bd3992`, `v2d246349f0051a1c`, `v31b1b47ae148af1f`, `v321b67cda11cd67d`, `v36d216e75e2526d3`, `v468d3d041713bf7d`, `v4833c3b1ab7dceef`, `v57e0040ff0ad8028`, `v5f4b5733c5575b9f`, `v5fc98bb46ae0c270`, `v62ba14cf314c1762`, `v6ea8de1e96eaa2e7`, `v702752d4edc33185`, `v732ec2a879e6f405`, `v750f005fde7f2658`, `v756f896b8328c22f`, `v80a61d35636233e0`, `v85031f0b2100719d`, `v9008f04238a86871`, `v97f7609c206c765b`, `v9a4bca129398f9ad`, `va10f5159a7356122`, `va1d8a3aff7580097`, `vb0049d239061e73f`, `vb31d26cffc802d7f`, `vba4433cd2a45fdd4`, `vbb214dabb5d9514e`, `vc54053aab3059e9a`, `vc66d903f67842004`, `vccd7d6407f77183e`, `vd6dde6d30a8b5f66`, `vd70263ec9f011a2e`, `vd9d8d4550595657e`, `ve066f2cc9ab0f657`, `vedd446a69ad39c40`, `vf3bb8a41a6a2b3bb`, `vf4fa4d406b870a94` | `v02b5aa1c6f152cb8`, `v04c9ebbce835c688`, `v0802ba8c1adfd735`, `v0e100bb5f5f9b549`, `v1f766b6f6eab757b`, `v236138ba2b69c385`, `v244f25416a939dab`, `v28404c7cebd1aa87`, `v2a00957a7f256025`, `v34d068d7913a006d`, `v490f13fcc91800c2`, `v4acd588a3c0cc94e`, `v51667084eded3199`, `v59d7c0268acaec8c`, `v6775108beb739acf`, `v6c32781926fcdd5c`, `v74785d5a33f1eadb`, `v75a3e8e255520a6f`, `v75b42fab65afc397`, `v76eff81a9ab7e6dd`, `v8357c7ec77007bab`, `v86a6eabef30e4ba5`, `v89900ec30e1dfe82`, `v983f5e4b5f7cdc29`, `v9ae4fd335cc78dff`, `v9b5fd819ac7976bb`, `va3140cc886b694fe`, `va3cc235693ed9aa0`, `va5e6f618c7b58bf9`, `vaefd4325cf8ba171`, `vb0c5a3492d65d1eb`, `vb2f73291e8fe10d1`, `vb9efe6cec61c9489`, `vc0109df9efce7825`, `vcf73d5dd4703dd31`, `vd10e80041b1344d6`, `vda3eac1602712021`, `ve0d3587f68b26b73`, `ve955eb9e7db5531a`, `vf5a1a13446f43395`, `vf7fa99884a005fcb`, `vf94f59c1cd4d3670`, `vfe47c408d2abc7fb` | an object whose moved is not contained in its declared set is rejected | `303d488c14eed0d2` |
| `W3C-R-017` (roll-up denominator) | `ve7ec53356216c396` | `v6a468aead6a0997c` | never emitted without its complete denominator | `526d7694de57f6c5` |
| `W3C-R-018` (roll-up counter) | `v0e31d851b22cf706` | `v095044ecfd531f0e` | the counter over carried against referenced | `31c3dfd19fc59147` |
| `W3C-R-019` (closed vocabulary) | `vcfa49a358963e8a4` | `v3749565d86ca5c4a` | because free text does not aggregate | `1b376a60d7520ff7` |
| `W3C-R-020` (reference mismatch) | `vebd93abb8ee3a837` | `v2c385e784e0bac52` | resolves with a mismatch (an integrity failure) | `af507f1056e619da` |

## The rules the thread settled beside the table

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `W3C-R-021` (recomputed delta) | `v0164c803c34c3c4c` | `vc103c9ebc091176a` | they read moved as recomputed from the two observations the object names | `bc4afdb28cee9c30` |
| `W3C-R-022` (coverage block) | `v532f7ce5761b5119`, `vf53c0cf19e40b8b7` | `v44df6ea141d977e3`, `v9b20d711c1a0b368` | a sampled / full_coverage flag with the count of scannable files recorded before the per-repo cap | `50c6f490bcf092b2` |
| `W3C-R-023` (population denominator) | `v36fe3597c4a38c48`, `vae5bf9e259ca9fa2` | `v6886f2dea5b8d30c`, `vba28e0271213f6ef` | a claim over an empty population is reported as not claimable, not as satisfied | `04fa2499c017be72` |
| `W3C-R-024` (delta-related pair) | `vbcbbc065f5978092` | `vac73991b7eab80be` | Unrelated pass and fail records in one corpus must not qualify | `d75ca465cf824295` |

## The crosswalk from the harness's report

The reference emitter in `packaging/agent_evidence_vectors/w3creport.py` writes a v0.1 report from the report the AEE harness writes, one per-check record per replayed vector. The two altitudes are kept apart: the harness's `result` stays four-valued and recomputable, and the per-check record says what a consumer may conclude about the statement the vector carries. `pass` is a valid verdict with result `pass` or `pass_indirect`, the result carried as the qualifier; `fail` is a valid verdict with result `fail` or `degraded`, or an invalid verdict, with the codes carried; `inconclusive` is the indeterminate kind, with cause `reading-committed` and the condition the rail committed to, or `reading-uncommitted` with the declared readings; `not-exercised` is a manifest entry declaring `expected.unmeasurableBecause`, reported with cause `precondition-unsatisfiable` and that text, or a report member the manifest expects and the rail left absent, with cause `unavailable`; `void` is a harness that could not establish a verdict, with cause `harness-failure` and the rail's errors or exit as detail. The report the emitter writes from the AEE corpus conforms: no row fires on it.

## Two further subjects in the same corpus

The same manifest carries members of two other subject types, judged by their own sentences in their own modules: the Run object of `draft-arsentev-agent-run-metrics-00`, twenty-two rows over the members and invariants a validator can read off one Report, and the discovery snapshot of `draft-arsentev-llm-context-discovery-00`, eleven rows over what an origin advertises and what a consumer resolves. Their tables follow the same shape and are listed after the report rows.

## Run object rows

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `ARM-R-001` (5.1) | `v35f9c4d0fac828df` | `v20aff5acca86c219` | Reporter MUST emit "1" while conforming to this specification | `f313511759b2f6ce` |
| `ARM-R-002` (3.1) | `vd568fb04bbfe75c7` | `v337f2e7acc229d39` | The "end" member MUST be present when "status" is "completed",    "failed" or "aborted", and MUST NOT be present when "status" is    "running" | `a82c8c4e90b439d6` |
| `ARM-R-003` (3.1) | `v9c3952c5f1467764` | `vc60f8ca141d363b3` | When present, "end" MUST NOT be earlier than "start" | `1651e4aa28aef3c5` |
| `ARM-R-004` (3.1) | `v143660ae522c83b7` | `v2fc9dabfe555dd2a` | a Reporter MUST NOT emit    a value other than the four listed | `532a0c7a01289d79` |
| `ARM-R-005` (3.1) | `v4c65aa9f3b8e431b` | `vc593cdd0df015927` | When the "steps" array is present, "step_count" MUST be    greater than or equal to the length of that array | `b0245f78d559c0cf` |
| `ARM-R-006` (3.2) | `va6299cdbedfb81f8` | `v3019a3f576b2feaa` | Within one Run, "index" values MUST be unique and MUST be assigned in    the order in which Steps began | `de2c45f5dcc4d136` |
| `ARM-R-007` (3.2) | `v2ec6bcd8fa774fbc` | `v3c96293f578f1b72` | When "kind" is "model_invocation", the "usage" and "model" members    MUST be present | `bb47f3459eea16f1` |
| `ARM-R-008` (3.2) | `v234281fbdc8cf63d` | `v20cc6cdd082e0e45` | When "kind" is "tool_call", the "tool" member MUST    be present and the "usage" member MUST NOT be present | `cbf735970617d21d` |
| `ARM-R-009` (3.4) | `ve25d40b143d66912` | `v8ab485d5b009b46c` | All members of a Usage object MUST be non-negative integers | `0748102d1586a9c5` |
| `ARM-R-010` (3.4) | `v5187613995b28f33` | `v78d66a8e657c2772` | "cache_read_tokens" is a subset of "input_tokens" and therefore        MUST be less than or equal to it | `912e608876053400` |
| `ARM-R-011` (3.4) | `vd182df4e94785dcb` | `v296d1a74025adc1c` | "cache_read_tokens" and "cache_write_tokens"        denote disjoint subsets of "input_tokens" and their sum MUST be        less than or equal to "input_tokens" | `ab264faa892721d2` |
| `ARM-R-012` (3.4) | `v0320e079760670a9` | `v1f6745a7841076d0` | "totals" object MUST be, member by member, the sum of the    corresponding members of every Step's Usage object | `e6b6a4c51dfe30f7` |
| `ARM-R-013` (3.5) | `v1c875fc4c36aa06d` | `v468366f762a8bdf4` | One    "lifetime" value MUST NOT appear in more than one element of the same    array | `89119163b621c774` |
| `ARM-R-014` (3.5) | `v096b392478fcf6fe` | `vc78c495fa2865996` | The sum of the "tokens" members of "cache_writes" MUST equal the    "cache_write_tokens" member of the same Usage object | `17816ade45921f0d` |
| `ARM-R-015` (3.3) | `v3bd7c51c7aa62b13` | `vaa9022b28508fbff` | A Reporter MUST NOT    emit two Steps of one Run with the same "invocation_id" | `0883bbd19a653019` |
| `ARM-R-016` (3.6) | `v93fe9e276462b6ea` | `vbecc90485b846e5a` | A Run that emits "root_run_id" and has no       parent MUST set it equal to its own "run_id" | `546781f078f7e248` |
| `ARM-R-017` (3.7) | `v9944d4e53d2325c1` | `v76384d66512cc6a4` | The "amount" member MUST be a JSON string matching the ABNF [RFC5234]    rule | `f15b1c8c7a0cfe45` |
| `ARM-R-018` (3.12) | `v466ace50ae1bbbc0` | `v745e2452410fd4fa` | Its value MUST be a JSON object whose members all    have string values | `4d1f574a3f6c8983` |
| `ARM-R-019` (5) | `v05d60efad92ebaf8` | `ve81bc854b081493b` | Timestamps MUST be strings conforming to the "date-time" production    of [RFC3339].  They MUST use the "Z" time offset | `af8a371a7c03ddaa` |
| `ARM-R-020` (5) | `vc4cc6abd16cb7848` | `v226c47602e7c328a` | MUST be non-empty strings of at most 128    characters | `f45b4290574244a8` |
| `ARM-R-021` (5.1) | `v5bd6bf20b3a439e7` | `v9357f80ad67b7286` | A Reporter MUST NOT use an unprefixed member    name for a purpose other than the one specified here | `a9283399f2f72c8c` |
| `ARM-R-022` (3.4) | `vbac3c7923a48045f` | `v066b4ec60aeb45ea` | "reasoning_tokens" is a subset of "output_tokens" and        therefore MUST be less than or equal to it | `77239d6671db6001` |

## Discovery snapshot rows

| row | reject | accept | sentence | digest |
|---|---|---|---|---|
| `LCD-R-001` (3.1) | `vf749dad865952b0e` | `vf5442792fb3883dc` | A context file MUST NOT be served with a "Content-Type" of "text/    html" | `dea0684290a3e21a` |
| `LCD-R-002` (3.2) | `v802e4cd278a0fbd2` | `v58f8859669e43d97` | A discovery mechanism defined in Section 4 MUST point at an index       resource, never directly at a detail resource | `993eae7ed8a98e13` |
| `LCD-R-003` (4.1) | `v6027f56ef7676a5d` | `v7b61413822815cfb` | A publisher advertising a context file through this mechanism MUST    arrange that a GET request for "/.well-known/llm-context" on the    origin returns either | `b75a01b97d999548` |
| `LCD-R-004` (4.3) | `v59d76289515e9386` | `v50ef3e4bd9f138bc` | Its value MUST be an absolute    URI | `cbf9300432d96463` |
| `LCD-R-005` (4.3) | `v134763ca9f01867c` | `v2ec19f234a21c62f` | A publisher MUST NOT use this record to advertise a context file    whose retrieval the same robots.txt disallows | `6c62b556add0487c` |
| `LCD-R-006` (4.4) | `v1f14e5858f61534b` | `v6d6b62187cfc99ef` | a consumer MUST    apply the following precedence, highest first | `bc76905fa3c30441` |
| `LCD-R-007` (4.4) | `vadc27fccee1d1084` | `v3c97c572e8c9f739` | A consumer MUST NOT retrieve more than one index resource per origin    per retrieval cycle | `9303b76c717a46a4` |
| `LCD-R-008` (7.2) | `v5fa1792bbc9887c1` | `v6ad97761064d2e7f` | A consumer MUST NOT attribute the content of a cross-origin index    resource to the advertising origin | `de7f08a1b2a8a663` |
| `LCD-R-009` (7.4) | `v80e52166b6a54bab` | `veea533d0c7f0b4f6` | A consumer MUST impose its own ceiling on the size of any retrieved    context file | `6bf3ffe5624cb4d3` |
| `LCD-R-010` (3.3) | `v6ec17de3ba07cb6b` | `v748108bc07240595` | the response MUST carry an appropriate "Content-Language" | `1f8ceb1482c75131` |
| `LCD-R-011` (4.4) | `v93bd3bcb57b6e753` | `v1b2f5cbd6e1c2bd6` | a consumer MUST evaluate the exclusion    rules of [RFC9309] against the index resource's URI before retrieving    it | `1cb26bd4e4ca5526` |

## The vendored text

| key | author | sha256 | source |
|---|---|---|---|
| `0001` | Kenne Ives | `62bafb6e88629bda0dc09c1d19982aaf831be7b8845bf80a2fb31deda676b143` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0001.html |
| `0025` | Nicolas Rocchia | `2ee9306408474a6966d8294d4e641c39aa253a2ab2bb377d01abcee5c3b94e95` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0025.html |
| `0036` | Evgenii Arsentev | `7a034174eb5f27f8f8865f49ab6999de20157dd3906b9d158366b62cc83b7738` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0036.html |
| `0043` | Nicolas Rocchia | `76f5af49f11108fccf5d01c3710771acdb4539c8761b655b8e06bda993bb03f1` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0043.html |
| `0050` | Kenne Ives | `1399c56136e7aa7630000f723a92169c12313ef6012eab130b3511ed2c7a5e35` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0050.html |
| `0060` | Nicolas Rocchia | `47f96e10c2ac5dc023a0dde77582331f58431cf4e8fabbb53a068a6d6a8f12bd` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0060.html |
| `0062` | Evgenii Arsentev | `b92f4a6ca926eaa8514c313054cf1736524d187ce36c9b6ef6c1f5d2b19ed977` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0062.html |
| `0069` | Evgenii Arsentev | `40153b17403b0e6594dfe00a9e9a5c01e5b978b6ce47b12a4ef0bbe31817514b` | https://lists.w3.org/Archives/Public/public-agent-conformance/2026Sep/0069.html |
| `draft-arsentev-agent-run-metrics-00` | Evgenii Arsentev | `0ef9e7fbc39d04bf2e245ed12b6a15eb4988d56abf3b07a65aab7861ad14d7f0` | https://datatracker.ietf.org/doc/draft-arsentev-agent-run-metrics/ |
| `draft-arsentev-llm-context-discovery-00` | Evgenii Arsentev | `13081268c70a19e9b3f74a6f772b657c56403ce6c45623da39a188394eefd411` | https://datatracker.ietf.org/doc/draft-arsentev-llm-context-discovery/ |
