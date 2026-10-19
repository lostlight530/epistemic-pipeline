# 2026-Q1 / 01 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/epistemic-pipeline`; research month: `2026-01-01 through 2026-01-31`
- Stage owner: `I / 2026-Q1`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-01-23 — Handoff-history defaults and MCP manager
- **Primary source:** https://github.com/openai/openai-agents-python/releases/tag/v0.7.0 (`openai/openai-agents-python@v0.7.0`, `S1`)
- **Publisher-described observation:** Agents SDK v0.7.0 changes nested handoff history from default-on to opt-in and introduces MCPServerManager for multiple MCP server instances.
- **Analytic implication:** Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean.
- **Alternative / qualification:** Release-described API behavior does not establish production deployments or any benchmark pass.
- **Research owner:** `I1` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O1 / S1 (openai-agents-python v0.7.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. claim indexed != claim true; evidence linked != evidence sufficient; heuristic score != probability; runtime-policy pass != truth; claim transfer != acceptance; provenance != truth.
No `epistemic-pipeline` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
