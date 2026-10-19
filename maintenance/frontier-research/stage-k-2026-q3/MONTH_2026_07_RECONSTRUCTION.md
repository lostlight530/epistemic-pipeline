# Frontier Research Month Reconstruction — 2026-07

## Identity and temporal integrity
- Repository: `lostlight530/epistemic-pipeline`; Stage: K / 2026-Q3
- Historical event window: 2026-07-01 to 2026-07-31
- Reconstruction performed: 2026-10-19; source-access date: 2026-10-19
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION`; achieved coverage: `SOURCE_BOUNDED`
- Result: `SELECTED_SOURCE_OBJECTS`

## Source discovery actually executed
GitHub repository Releases REST listing and, for each included release, exact `/repos/{owner}/{repo}/releases/tags/{tag}` retrieval. Initial surface restricted to the selected official release families relevant to this repository lens; release `published_at` used to attribute the event to its month, except original release-note calendar references retained as notes. No systematic literature-wide search, independent scientific replication or guarantee of exhausting even adjacent projects.

## Selected events and evidence
- **2026-07-27 · openai/openai-agents-python v0.19.0** — Programmatic Tool Calling with caller restrictions and Runner/approval integration. [Primary release](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0)
  - *Evidence-bound interpretation:* The model can coordinate eligible tools programmatically, enlarging the causal chain between policy, generated code, tool calls and results; allowed_callers scope is not a substitute for inspecting actions.
  - *Negative space:* Vendor release is not an independent security review or local runtime trace.
- **2026-07-28 · modelcontextprotocol/modelcontextprotocol 2026-07-28** — stable 2026-07-28 MCP specification revision. [Primary release](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28)
  - *Evidence-bound interpretation:* Protocol revision identity is a separate clock from SDK release identity and any tool-server implementation; compatibility claims require all three versions.
  - *Negative space:* The release notice alone does not establish adoption/conformance by a specific SDK or server.

## Month analysis
These selected release objects matter to claim/evidence discrimination, uncertainty, policy authority, tool trajectories, execution state, evaluator versions and transfer boundaries. The distinction is **upstream published behavior versus reproducible downstream execution**: the official release record can document the upstream change, but this research has not run the release in this repository, replayed its outputs or independently validated its results. The records above may belong to the same upstream-origin family; repeated vendor claims are not independent corroboration.

## Forward boundary
- No modification to earlier monthly history or Stage H.
- Native runtime drift: `UNKNOWN / NOT_AUDITED`; no code or contract change.
- Parent [Stage brief](STAGE_BRIEF.md); subsequent [quarter synthesis](STAGE_SYNTHESIS.md).
