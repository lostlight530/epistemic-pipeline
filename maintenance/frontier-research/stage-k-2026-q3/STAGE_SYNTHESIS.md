# Frontier Research Stage Synthesis — K / 2026-Q3

## 0. Identity and status
- Repository: `lostlight530/epistemic-pipeline`
- Window: `2026-07-01 through 2026-09-30`; record type: `RETROSPECTIVE`
- Synthesis and research date: `2026-10-19`; specification: `2026-09-19-first-batch`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Evidence coverage actually achieved: `SOURCE_BOUNDED`, not field-comprehensive or independently replicated
- Status: `COMPLETE` as a bounded document research project; stage disposition: `FRONTIER_STAGE_COMPLETE`
- Review independence: `SAME_PRODUCER_REVIEW`; independent validation **not established**.

## 1. Research questions revisited
| Question | Outcome | Research evidence | Scope limit |
|---|---|---|---|
| What versioned upstream changes matter? | `ANSWERED_WITHIN_SELECTED_RELEASES` | K1, K2, K3, K4 | Official project release descriptions |
| What evidence/provenance relations arise? | `BOUNDED_INTERPRETATION` | Part analyses + EVIDENCE_CHART | Not adoption or experimental performance |
| Is a current repository defect confirmed? | `UNRESOLVED / NOT_AUDITED` | No current-runtime audit | Upstream changes cannot prove current drift |

## 2. Inputs, selection and actual methods
- Stage Brief post-selection reconstruction protocol; [2026-07](MONTH_2026_07_RECONSTRUCTION.md), [2026-08](MONTH_2026_08_RECONSTRUCTION.md), [2026-09](MONTH_2026_09_RECONSTRUCTION.md).
- 4 selected versioned upstream release object(s), each independently inspectable in `K1`, `K2`, `K3`, `K4`; the register and evidence chart preserve version/source mapping.
- Actual search/navigation: bounded GitHub release listings and selected tag descriptions, inspected 2026-10-19. No comprehensive literature search, independent evidence chaining, version-controlled installations, or experiments.
- All three months have at least one selected upstream release, but field completeness cannot be inferred.

## 3. Quarterly research narrative: change and persistence
The prior J Stage leaves open whether a richer evidence vocabulary corresponds to reproduced behavior. K tests the next bounded release set, rather than inheriting a verification result.
- **2026-07-27, openai-agents-python v0.19.0:** Programmatic tool orchestration. The action unit becomes a programmatic coordinator operating under per-tool calling policy; evaluation must retain caller/approval and execution sequence.
- **2026-07-28, modelcontextprotocol 2026-07-28:** Stable protocol revision. Tool-protocol revision is a separate environment contract from agent SDK release and actual server conformance.
- **2026-08-19, openai-agents-python v0.22.0:** Replay redaction and RunState usage. A trustworthy replay has privacy/redaction state, terminal status and checkpoint-accounting boundaries; retaining a trace must not leak rejected outputs.
- **2026-09-17, openai-agents-python v0.22.3:** Validated arguments before conditional approval. Approval decisions should bind to validated input, not merely a displayed tool name; resumed tool availability remains time-dependent.

Across these objects, the quarter's useful change is a sharper distinction between **released interface/standard state** and **observed execution state**. Where more than one object was selected, their relationship is an analytic comparison of provenance/identity surfaces, not a claimed causal dependency. Where the source density is low, the conclusion is correspondingly narrow.

## 4. Mechanism and cross-Part synthesis
1. **Programmatic tool orchestration:** Agents SDK v0.19.0 adds ProgrammaticToolCallingTool for eligible tool coordination using generated JavaScript with allowed_callers, streaming, approvals and state integration. The research interpretation is: The action unit becomes a programmatic coordinator operating under per-tool calling policy; evaluation must retain caller/approval and execution sequence.

2. **Stable protocol revision:** MCP publishes stable revision 2026-07-28 and links its official revision and changelog. The research interpretation is: Tool-protocol revision is a separate environment contract from agent SDK release and actual server conformance.

3. **Replay redaction and RunState usage:** Agents SDK v0.22.0 reports replay-state redaction of guardrail-blocked tool outputs, terminal response failure handling, provider option validation and RunState usage accounting isolation. The research interpretation is: A trustworthy replay has privacy/redaction state, terminal status and checkpoint-accounting boundaries; retaining a trace must not leak rejected outputs.

4. **Validated arguments before conditional approval:** Agents SDK v0.22.3 aligns conditional approvals with validated tool arguments and fixes server-managed resume tool-not-found output. The research interpretation is: Approval decisions should bind to validated input, not merely a displayed tool name; resumed tool availability remains time-dependent.

The stable technical mechanism is that changing software/specification versions can change which inputs, policies, parsers, environments, visual semantics, or evidence relations are possible. **Possibility ≠ realization**: any claim about realized behavior needs an identifiable repository revision, configuration and corresponding run/output evidence. The Stage Parts are conceptually connected through the repository's lens (claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer), not merged into a single experimental dataset.

## 5. Previous-stage delta, counterevidence and evidence maturity
- `NEW / STRENGTHENED`: selected release facts recorded in the Parts; new versioned source identities explicitly attached.
- `PERSISTENT`: claim indexed != claim true; evidence linked != evidence sufficient; heuristic score != probability; runtime-policy pass != truth; claim transfer != acceptance; provenance != truth.
- `NOT_COMPARABLE`: heterogeneous releases have no shared quantitative evaluator and are not a performance time series.
- Strong counter-reading: the apparent direction of progress partly reflects **source selection** and release-note authorship, not independent field-wide adoption.
- Source maturity: `PUBLISHED_UPSTREAM_RELEASE_RECORD`; independent downstream execution, conformance, scientific replication, user impact and `epistemic-pipeline` deployment are `UNKNOWN / NOT_TESTED`.
- No selected independent contrary source was examined; lack of reported contradiction is not a proof of universal agreement.

## 6. Temporal integrity and current repository assessment
Publisher release dates belong to 2026-Q3; the research and read date is 2026-10-19. No backdating as contemporary work. Earlier native Stages and old longitudinal files are preserved as their actual historical observations. This Stage identifies **no verified implementation drift** because it did **not** run a current-repository audit; it does not assert an all-clear. `NO_RUNTIME_CHANGE` and `NO_CONTRACT_CHANGE` are the changes enacted by this research-only artifact.

## 7. Review, limitations and handoff
See [RESEARCH_REVIEW.md](RESEARCH_REVIEW.md) for a same-producer review of temporal placement, source claims, negative space and boundary compliance. It is not independent review. See [STAGE_HANDOFF.md](STAGE_HANDOFF.md) for transferable research questions. Strongest limitations: single-origin release sources, source-bounded coverage, uneven monthly selection, absent independent reproduction, and no runtime/experiment verification.

## 8. Conclusion
`FRONTIER_STAGE_COMPLETE — SOURCE_BOUNDED_DOCUMENT_RESEARCH_ONLY`.

What was completed: a dated, independently navigable **research-documentation Stage**, with selected source facts, research Parts, month records, comparison and critical boundaries. What was not completed: a scientific validation of underlying software, runtime conformance check, exhaustive field synthesis or local experimental reproduction.
