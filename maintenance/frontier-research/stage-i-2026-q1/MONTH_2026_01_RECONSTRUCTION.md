# Frontier Research Stage I / 2026-Q1 — 2026-01 monthly research reconstruction
- Source period: 2026-01; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Handoff history and approval state. Evidence-object count: 1; **not** a measure of field-wide activity.
## 2026-01-23 — Handoff history configuration (`I-O1`)
**Publisher source:** [openai/openai-agents-python v0.7.0](https://github.com/openai/openai-agents-python/releases/tag/v0.7.0) (`I-S1`).
**Observed release note:** Agents SDK changes nested handoff history to opt-in and introduces a multi-MCP-server manager.
**Analysis:** Run history and connected tool surfaces are part of what an evaluator can observe; SDK defaults should be versioned.
**Alternative / caution:** No local SDK run, MCP connection or historical trace was observed.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
