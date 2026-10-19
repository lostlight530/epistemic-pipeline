# Frontier Research Stage K / 2026-Q3 — bounded research handoff
- Date 2026-10-19; source `lostlight530/epistemic-pipeline`; review [RESEARCH_REVIEW.md](RESEARCH_REVIEW.md); synthesis [STAGE_SYNTHESIS.md](STAGE_SYNTHESIS.md).
- Eligible transfer: contextual knowledge about **Programmatic toolset, protocol and replay safety**, supported by 4 first-party releases and their exact dates.
- K-O1 — Programmatic tool calling: Generated program, allowed-callers specification and actual effect form separate evidence objects. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0).
- K-O2 — Stable MCP protocol revision: A published protocol revision is an interoperable contract reference, not evidence of an SDK's deployed conformance. [Source](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28).
- K-O3 — Replay redaction and checkpoints: A faithful audit may intentionally redact forbidden bytes; checkpoint ownership and failure states should remain explicit. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0).
- K-O4 — Approval tied to validated arguments: Approval authority must bind normalized arguments and a versioned schema, not an unqualified true/false flag. [Source](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3).
- Unsafe to transfer: benchmark score, runtime capability, local defect, independent validation, security compliance or other repositories' truth states.
- Unknowns: `claim indexed != truth; approval != execution; tool schema != authorization; score != probability; transfer != acceptance`. Cross-repository analogy is a research question only: `handoff != authority transfer`; `claim transfer != acceptance`.
