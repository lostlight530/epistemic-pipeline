# Evidence and comparison chart — Stage K / 2026-Q3

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-K1 | O7 | Agents SDK v0.19.0 adds ProgrammaticToolCallingTool for eligible tool coordination using generated JavaScript with allowed_callers, streaming, approvals and state integration. | The action unit becomes a programmatic coordinator operating under per-tool calling policy; evaluation must retain caller/approval and execution sequence. | S7: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-07-27 |
| F-K2 | O8 | MCP publishes stable revision 2026-07-28 and links its official revision and changelog. | Tool-protocol revision is a separate environment contract from agent SDK release and actual server conformance. | S8: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-07-28 |
| F-K3 | O9 | Agents SDK v0.22.0 reports replay-state redaction of guardrail-blocked tool outputs, terminal response failure handling, provider option validation and RunState usage accounting isolation. | A trustworthy replay has privacy/redaction state, terminal status and checkpoint-accounting boundaries; retaining a trace must not leak rejected outputs. | S9: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-08-19 |
| F-K4 | O10 | Agents SDK v0.22.3 aligns conditional approvals with validated tool arguments and fixes server-managed resume tool-not-found output. | Approval decisions should bind to validated input, not merely a displayed tool name; resumed tool availability remains time-dependent. | S10: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-09-17 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `epistemic-pipeline` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
