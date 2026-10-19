# Frontier Research Stage Synthesis — I / 2026-Q1

## 0. Identity and status
- Repository: `lostlight530/epistemic-pipeline`
- Window: `2026-01-01 through 2026-03-31`; record type: `RETROSPECTIVE`
- Synthesis and research date: `2026-10-19`; specification: `2026-09-19-first-batch`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Evidence coverage actually achieved: `SOURCE_BOUNDED`, not field-comprehensive or independently replicated
- Status: `COMPLETE` as a bounded document research project; stage disposition: `FRONTIER_STAGE_COMPLETE`
- Review independence: `SAME_PRODUCER_REVIEW`; independent validation **not established**.

## 1. Research questions revisited
| Question | Outcome | Research evidence | Scope limit |
|---|---|---|---|
| What versioned upstream changes matter? | `ANSWERED_WITHIN_SELECTED_RELEASES` | I1, I2, I3 | Official project release descriptions |
| What evidence/provenance relations arise? | `BOUNDED_INTERPRETATION` | Part analyses + EVIDENCE_CHART | Not adoption or experimental performance |
| Is a current repository defect confirmed? | `UNRESOLVED / NOT_AUDITED` | No current-runtime audit | Upstream changes cannot prove current drift |

## 2. Inputs, selection and actual methods
- Stage Brief post-selection reconstruction protocol; [2026-01](MONTH_2026_01_RECONSTRUCTION.md), [2026-02](MONTH_2026_02_RECONSTRUCTION.md), [2026-03](MONTH_2026_03_RECONSTRUCTION.md).
- 3 selected versioned upstream release object(s), each independently inspectable in `I1`, `I2`, `I3`; the register and evidence chart preserve version/source mapping.
- Actual search/navigation: bounded GitHub release listings and selected tag descriptions, inspected 2026-10-19. No comprehensive literature search, independent evidence chaining, version-controlled installations, or experiments.
- All three months have at least one selected upstream release, but field completeness cannot be inferred.

## 3. Quarterly research narrative: change and persistence
Stage H / 2025-Q4 showed that agent evaluation needs toolset, mutable cost/blocking, replanning and trajectory identity, not final-score inheritance.
- **2026-01-23, openai-agents-python v0.7.0:** Handoff-history defaults and MCP manager. Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean.
- **2026-02-05, openai-agents-python v0.8.0:** Human approval and resumable run state. Approval decision, resume boundary, actor authority and failure-policy defaults become evidence in the executed trajectory.
- **2026-03-13, openai-agents-python v0.12.1:** Rejection evidence preservation. Negative decisions and their reasons are part of state-transition evidence; omission can make replay look like unexplained blocking.

Across these objects, the quarter's useful change is a sharper distinction between **released interface/standard state** and **observed execution state**. Where more than one object was selected, their relationship is an analytic comparison of provenance/identity surfaces, not a claimed causal dependency. Where the source density is low, the conclusion is correspondingly narrow.

## 4. Mechanism and cross-Part synthesis
1. **Handoff-history defaults and MCP manager:** Agents SDK v0.7.0 changes nested handoff history from default-on to opt-in and introduces MCPServerManager for multiple MCP server instances. The research interpretation is: Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean.

2. **Human approval and resumable run state:** Agents SDK v0.8.0 introduces human-in-the-loop tool approval, pending interruptions and RunState serialization/resume; it also changes synchronous tool threading and MCP failure handling defaults. The research interpretation is: Approval decision, resume boundary, actor authority and failure-policy defaults become evidence in the executed trajectory.

3. **Rejection evidence preservation:** Agents SDK v0.12.1 preserves explicit approval rejection messages across resume flows. The research interpretation is: Negative decisions and their reasons are part of state-transition evidence; omission can make replay look like unexplained blocking.

The stable technical mechanism is that changing software/specification versions can change which inputs, policies, parsers, environments, visual semantics, or evidence relations are possible. **Possibility ≠ realization**: any claim about realized behavior needs an identifiable repository revision, configuration and corresponding run/output evidence. The Stage Parts are conceptually connected through the repository's lens (claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer), not merged into a single experimental dataset.

## 5. Previous-stage delta, counterevidence and evidence maturity
- `NEW / STRENGTHENED`: selected release facts recorded in the Parts; new versioned source identities explicitly attached.
- `PERSISTENT`: claim indexed != claim true; evidence linked != evidence sufficient; heuristic score != probability; runtime-policy pass != truth; claim transfer != acceptance; provenance != truth.
- `NOT_COMPARABLE`: heterogeneous releases have no shared quantitative evaluator and are not a performance time series.
- Strong counter-reading: the apparent direction of progress partly reflects **source selection** and release-note authorship, not independent field-wide adoption.
- Source maturity: `PUBLISHED_UPSTREAM_RELEASE_RECORD`; independent downstream execution, conformance, scientific replication, user impact and `epistemic-pipeline` deployment are `UNKNOWN / NOT_TESTED`.
- No selected independent contrary source was examined; lack of reported contradiction is not a proof of universal agreement.

## 6. Temporal integrity and current repository assessment
Publisher release dates belong to 2026-Q1; the research and read date is 2026-10-19. No backdating as contemporary work. Earlier native Stages and old longitudinal files are preserved as their actual historical observations. This Stage identifies **no verified implementation drift** because it did **not** run a current-repository audit; it does not assert an all-clear. `NO_RUNTIME_CHANGE` and `NO_CONTRACT_CHANGE` are the changes enacted by this research-only artifact.

## 7. Review, limitations and handoff
See [RESEARCH_REVIEW.md](RESEARCH_REVIEW.md) for a same-producer review of temporal placement, source claims, negative space and boundary compliance. It is not independent review. See [STAGE_HANDOFF.md](STAGE_HANDOFF.md) for transferable research questions. Strongest limitations: single-origin release sources, source-bounded coverage, uneven monthly selection, absent independent reproduction, and no runtime/experiment verification.

## 8. Conclusion
`FRONTIER_STAGE_COMPLETE — SOURCE_BOUNDED_DOCUMENT_RESEARCH_ONLY`.

What was completed: a dated, independently navigable **research-documentation Stage**, with selected source facts, research Parts, month records, comparison and critical boundaries. What was not completed: a scientific validation of underlying software, runtime conformance check, exhaustive field synthesis or local experimental reproduction.
