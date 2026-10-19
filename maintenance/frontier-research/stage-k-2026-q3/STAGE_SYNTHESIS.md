# Frontier Research Stage K / 2026-Q3 — quarterly research synthesis
## Identity
- `lostlight530/epistemic-pipeline`; study window 2026-07-01–2026-09-30; reconstructed/synthesized 2026-10-19; `SOURCE_BOUNDED / COMPLETE`.
- `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; not contemporaneous execution, systematic review, or independently verified result.
## Question revisited
**Programmatic toolset, protocol and replay safety:** what evidentiary boundary changed in this selected three-month history?
## Month and Part inputs
- [2026-07](MONTH_2026_07_RECONSTRUCTION.md)
- [2026-08](MONTH_2026_08_RECONSTRUCTION.md)
- [2026-09](MONTH_2026_09_RECONSTRUCTION.md)
- [Part K1: Programmatic tool calling](K1_PROGRAMMATIC_TOOL_CALLING.md) — [openai/openai-agents-python v0.19.0](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0), 2026-07-27
- [Part K2: Stable MCP protocol revision](K2_STABLE_MCP_PROTOCOL_REVISION.md) — [modelcontextprotocol/modelcontextprotocol 2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28), 2026-07-28
- [Part K3: Replay redaction and checkpoints](K3_REPLAY_REDACTION_AND_CHECKPOINTS.md) — [openai/openai-agents-python v0.22.0](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0), 2026-08-19
- [Part K4: Approval tied to validated arguments](K4_APPROVAL_TIED_TO_VALIDATED_ARGUMENTS.md) — [openai/openai-agents-python v0.22.3](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3), 2026-09-17
## Source selection, method and appraisal
Executed 2026-10-19: publisher release-index enumeration and exact tag reads; chose 4 release objects in Programmatic toolset, protocol and replay safety. These are publisher-origin product/specification/version statements. `SOURCE_BOUNDED` is the only coverage claim. Comparison uses research-question, versioned mechanism, time and evidence authority, not benchmark scores or number of announcements. Same-origin releases are related but not independent corroboration.
## Substantive quarter narrative
### 1. Programmatic tool calling (2026-07-27)
**Evidence:** Agents SDK introduces generated JavaScript orchestration of eligible tools with allowed_callers and Runner integration. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0).
**Meaning:** Generated program, allowed-callers specification and actual effect form separate evidence objects.
**Counter-reading:** No program was executed or sandbox permission verified here.

### 2. Stable MCP protocol revision (2026-07-28)
**Evidence:** MCP repository marks the dated 2026-07-28 specification revision as stable and links the changelog. [Source](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28).
**Meaning:** A published protocol revision is an interoperable contract reference, not evidence of an SDK's deployed conformance.
**Counter-reading:** No normative conformance suite or client/server test was performed.

### 3. Replay redaction and checkpoints (2026-08-19)
**Evidence:** Agents SDK reports redaction of output-guardrail-blocked tool content from persisted/replayable state, error handling and usage isolation. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0).
**Meaning:** A faithful audit may intentionally redact forbidden bytes; checkpoint ownership and failure states should remain explicit.
**Counter-reading:** No replay/privacy or usage test was run for the target pipeline.

### 4. Approval tied to validated arguments (2026-09-17)
**Evidence:** Agents SDK aligns conditional approval decisions with validated tool arguments and repairs resume behavior. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3).
**Meaning:** Approval authority must bind normalized arguments and a versioned schema, not an unqualified true/false flag.
**Counter-reading:** A correction release is not a guarantee of race-free execution.

## Cross-Part interpretation
The common research movement is **programmatic toolset, protocol and replay safety**: selected release records reveal multiple distinct states—declared interface, effective runtime/configuration, action or rendering behavior, verification output and wider research interpretation. These states must not be collapsed. Different version families and software domains are not statistically comparable; there is no controlled common outcome metric.
## What persisted, failed to be shown and remains unknown
- Hard boundaries: `claim indexed != truth; approval != execution; tool schema != authorization; score != probability; transfer != acceptance`.
- Publisher release statement != current target repo capability; a fix is not evidence that this repo had the associated defect.
- No local native experiment, exact-version reproduction, formal citation chaining, implementation-conformance audit, independent counterevidence study or peer review.
- Historical event/publication dates were not backdated from 2026-10-19; source-family selection bias and missing independent validation persist.
## Review and current repository boundary
[Producer Research Review](RESEARCH_REVIEW.md); `SAME_PRODUCER_REVIEW`. Local implementation drift = `NOT_AUDITED`; active-contract drift = `NOT_AUDITED`; runtime change = `NO`; contract change = `NO`.
## Conclusion
`FRONTIER_STAGE_COMPLETE` only within the declared retrospective `SOURCE_BOUNDED` research scope. This is a knowledge artifact and [bounded handoff](STAGE_HANDOFF.md), not a certificate of scientific correctness, performance or project implementation.
