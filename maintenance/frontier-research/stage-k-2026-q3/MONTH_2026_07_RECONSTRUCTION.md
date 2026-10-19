# Frontier Research Stage K / 2026-Q3 — 2026-07 monthly research reconstruction
- Source period: 2026-07; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Programmatic toolset, protocol and replay safety. Evidence-object count: 2; **not** a measure of field-wide activity.
## 2026-07-27 — Programmatic tool calling (`K-O1`)
**Publisher source:** [openai/openai-agents-python v0.19.0](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) (`K-S1`).
**Observed release note:** Agents SDK introduces generated JavaScript orchestration of eligible tools with allowed_callers and Runner integration.
**Analysis:** Generated program, allowed-callers specification and actual effect form separate evidence objects.
**Alternative / caution:** No program was executed or sandbox permission verified here.

## 2026-07-28 — Stable MCP protocol revision (`K-O2`)
**Publisher source:** [modelcontextprotocol/modelcontextprotocol 2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28) (`K-S2`).
**Observed release note:** MCP repository marks the dated 2026-07-28 specification revision as stable and links the changelog.
**Analysis:** A published protocol revision is an interoperable contract reference, not evidence of an SDK's deployed conformance.
**Alternative / caution:** No normative conformance suite or client/server test was performed.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
