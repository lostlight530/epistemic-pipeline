# 2026-Q3 / 07 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/epistemic-pipeline`; research month: `2026-07-01 through 2026-07-31`
- Stage owner: `K / 2026-Q3`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-07-27 — Programmatic tool orchestration
- **Primary source:** https://github.com/openai/openai-agents-python/releases/tag/v0.19.0 (`openai/openai-agents-python@v0.19.0`, `S7`)
- **Publisher-described observation:** Agents SDK v0.19.0 adds ProgrammaticToolCallingTool for eligible tool coordination using generated JavaScript with allowed_callers, streaming, approvals and state integration.
- **Analytic implication:** The action unit becomes a programmatic coordinator operating under per-tool calling policy; evaluation must retain caller/approval and execution sequence.
- **Alternative / qualification:** A programmable orchestration API is not evidence that policy constraints were obeyed in a particular run.
- **Research owner:** `K1` in this Stage; one originating source family, no independent validation.

### 2026-07-28 — Stable protocol revision
- **Primary source:** https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28 (`modelcontextprotocol/modelcontextprotocol@2026-07-28`, `S8`)
- **Publisher-described observation:** MCP publishes stable revision 2026-07-28 and links its official revision and changelog.
- **Analytic implication:** Tool-protocol revision is a separate environment contract from agent SDK release and actual server conformance.
- **Alternative / qualification:** A stable spec tag does not establish that any server or client adopted it.
- **Research owner:** `K2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O7 / S7 (openai-agents-python v0.19.0), O8 / S8 (modelcontextprotocol 2026-07-28) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. claim indexed != claim true; evidence linked != evidence sufficient; heuristic score != probability; runtime-policy pass != truth; claim transfer != acceptance; provenance != truth.
No `epistemic-pipeline` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.
