# Frontier Research Stage J / 2026-Q2 — 2026-05 monthly research reconstruction
- Source period: 2026-05; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Sandbox execution and policy-before-approval. Evidence-object count: 1; **not** a measure of field-wide activity.
## 2026-05-19 — Credential and tool schema safeguards (`J-O2`)
**Publisher source:** [openai/openai-agents-python v0.17.3](https://github.com/openai/openai-agents-python/releases/tag/v0.17.3) (`J-S2`).
**Observed release note:** Agents SDK fixes leakage of mountpoint credentials into sandbox commands and tool-schema mutation problems.
**Analysis:** Trace retention must not expose secrets; a tool's schema and arguments must be captured without unintended mutation.
**Alternative / caution:** Fix is not evidence the target repo leaked any secrets.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
