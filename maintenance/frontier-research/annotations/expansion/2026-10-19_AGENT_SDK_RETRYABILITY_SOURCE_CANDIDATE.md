# Additional 2026 source-selection evidence — reconciliation of superseded PR #147

## Identity, trigger, history
- Repository: `lostlight530/epistemic-pipeline`; evidence-check date: **2026-10-19**; record type: `ADDITIVE_CANDIDATE_EVIDENCE / SOURCE_BOUNDED`.
- Parallel proposal [#147](https://github.com/lostlight530/epistemic-pipeline/pull/147) was based on an older `main`. While it was being researched, native Stages I–K, open L, the index correction and other source-selection reconciliations were merged independently.
- **Main's earlier Stage files, Part IDs, month selections, syntheses and A2 index retain authority.** This record selects only source objects not carried as native findings by those prior sampled Stage owners; it does not reclassify the older selections or rewrite their negative space.
- `CURRENT_BRANCH_SOURCE_SHA` at this note's preparation: `bb4557a1fb326a2bd91a8c44541ca2bb94f5be2f`. Later states must be checked separately.

## Distinct upstream versioned candidate objects
| Intended quarter / month | GitHub release published | Exact source | Release-described observation | Interpretation and limitation |
|---|---|---|---|---|
| 2026-Q2 / June | 2026-06-11 | [openai/openai-agents-python v0.17.5](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) | SDK release reports exposure of sandbox error retryability, distinct from v0.17.6 pre-approval tool input guardrails. | `RETRYABLE` is a tool/SDK classification, not evidence the same operation was retried, a side effect rolled back, or a task recovered. |

## Executed method and source authority
On **2026-10-19**, the connected GitHub API was used to inspect upstream tagged-release listings and the exact `/repos/{owner}/{repo}/releases/tags/{tag}` release-note bodies for every listed candidate. Dates are the publisher's GitHub published-at timestamps, not repository execution dates. A release notice reports what its issuer says it changed; it is not independent corroboration, downstream adoption, runtime execution, a security test, or proof of semantic equivalence. Retrieval is `SOURCE_BOUNDED`, not an exhaustive field search.

## Analytic delta and counter-reading
Stage J currently selects v0.17.6 June and has separate approval/schema extension candidates; the now-conflicted parallel PR #147 also independently selected a neighboring v0.17.5 release that is not a native J object.

The comparison asks whether an evidence envelope must record **failure reason → retryable classification → actual retry attempt → observed post-retry state** as separate facts, instead of letting a final success or exception label erase intervening state. The v0.17.5 and v0.17.6 notes share one issuer origin; no independent runtime reproduction or evaluator audit was executed.

**Strong alternative:** ordinary maintenance and purposive selection may explain these release differences better than any field-wide turning point. The number of upstream versions does not measure progress or independent confirmation. No external contradictory-source search, local experiment, artifact replay, formal methods review or current repository audit was performed for this addendum.

## Disposition / temporal and governance boundary
- `HOLD_FOR_EXPLICIT_STAGE_SELECTION_AMENDMENT`: these are **supplemental candidates**, not silently admitted objects in Stage I–K's original `SOURCE_OBJECT_REGISTER` or `EVIDENCE_CHART`.
- Proposed elevation requires dated Stage study-design amendment or new correction/reconciliation, source IDs, charting and bounded review; preserve the original publication/source-selection snapshot.
- Stage L remains `OPEN / 2026-Q4`; 2026 year remains `YEAR_OPEN`. No local drift established and no runtime or contract change.
- This addendum preserves the provenance of why overlapping PR #147 should **not** be merged; it does not assert independent review.
