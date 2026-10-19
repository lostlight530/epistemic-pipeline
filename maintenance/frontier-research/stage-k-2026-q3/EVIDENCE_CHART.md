# Frontier Research Stage K / 2026-Q3 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| K-O1 / v0.19.0 | Agents SDK introduces generated JavaScript orchestration of eligible tools with allowed_callers and Runner integration. | Generated program, allowed-callers specification and actual effect form separate evidence objects. | No program was executed or sandbox permission verified here. |
| K-O2 / 2026-07-28 | MCP repository marks the dated 2026-07-28 specification revision as stable and links the changelog. | A published protocol revision is an interoperable contract reference, not evidence of an SDK's deployed conformance. | No normative conformance suite or client/server test was performed. |
| K-O3 / v0.22.0 | Agents SDK reports redaction of output-guardrail-blocked tool content from persisted/replayable state, error handling and usage isolation. | A faithful audit may intentionally redact forbidden bytes; checkpoint ownership and failure states should remain explicit. | No replay/privacy or usage test was run for the target pipeline. |
| K-O4 / v0.22.3 | Agents SDK aligns conditional approval decisions with validated tool arguments and repairs resume behavior. | Approval authority must bind normalized arguments and a versioned schema, not an unqualified true/false flag. | A correction release is not a guarantee of race-free execution. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
