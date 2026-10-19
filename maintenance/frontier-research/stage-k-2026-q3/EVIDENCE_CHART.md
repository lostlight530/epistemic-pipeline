# Versioned Evidence Chart — Stage K / 2026-Q3

- Repository: `lostlight530/epistemic-pipeline`
- Source window: `2026-07-01 through 2026-09-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28) | Publishes stable 2026-07-28 MCP specification revision | Protocol version and actual server/client implementation differ | Spec release does not establish any local conformance | `NOT_RUN` |
| O2 / [S2](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0) | Redacts guardrail-rejected tool output from replay state and isolates RunState checkpoint usage | Replay trace can intentionally differ from raw observed effects | Does not establish complete sensitive-data coverage | `NOT_RUN` |
| O3 / [S3](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) | Aligns conditional approvals to validated arguments and fixes resume behavior | Approval policy and validated tool arguments need a time-bound binding | Valid arguments are not proof of permitted side effects | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.
