# Versioned Evidence Chart — Stage I / 2026-Q1

- Repository: `lostlight530/epistemic-pipeline`
- Source window: `2026-01-01 through 2026-03-31`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/openai/openai-agents-python/releases/tag/v0.7.0) | Makes nested handoff history opt-in; introduces MCPServerManager | Handoff configuration changes retained trajectory context | Release behavior does not prove any historical replay | `NOT_RUN` |
| O2 / [S2](https://github.com/openai/openai-agents-python/releases/tag/v0.8.0) | Adds HITL interruptions, approval decisions and serialized RunState resume | Approval and execution are separate evidence/authority transitions | Approval does not prove an action safe or valid | `NOT_RUN` |
| O3 / [S3](https://github.com/openai/openai-agents-python/releases/tag/v0.10.3) | Exposes immutable tool invocation metadata on run results | Invocation identity belongs to evidence envelope | No independent tool trace replay performed | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.
