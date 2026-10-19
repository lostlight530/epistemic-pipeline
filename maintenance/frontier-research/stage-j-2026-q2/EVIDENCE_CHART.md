# Versioned Evidence Chart — Stage J / 2026-Q2

- Repository: `lostlight530/epistemic-pipeline`
- Source window: `2026-04-01 through 2026-06-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0) | Adds beta persistent sandbox agents, manifests, snapshots and multiple backends | Workspace snapshots and backend are separate from task score | Beta announcement is not sandbox isolation certification | `NOT_RUN` |
| O2 / [S2](https://github.com/openai/openai-agents-python/releases/tag/v0.15.0) | Surfaces model refusal as ModelRefusalError instead of empty output | Refusal is explicit terminal/control state | API classification does not adjudicate refusal correctness | `NOT_RUN` |
| O3 / [S3](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) | Exposes sandbox error retryability | Retryable, retried and recovered are distinct claims | No live failure recovery independently executed | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.
