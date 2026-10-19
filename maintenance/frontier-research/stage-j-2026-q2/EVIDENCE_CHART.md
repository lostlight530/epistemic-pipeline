# Frontier Research Stage J / 2026-Q2 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| J-O1 / v0.14.0 | Agents SDK introduces beta sandbox agents with manifest, mounts, snapshots, memory and resume interfaces. | A versioned workspace manifest and snapshot condition action possibilities; environment continuity cannot be inferred from terminal text. | Beta support does not establish independent safe execution or the target repo's use. |
| J-O2 / v0.17.3 | Agents SDK fixes leakage of mountpoint credentials into sandbox commands and tool-schema mutation problems. | Trace retention must not expose secrets; a tool's schema and arguments must be captured without unintended mutation. | Fix is not evidence the target repo leaked any secrets. |
| J-O3 / v0.17.6 | Agents SDK adds pre-approval tool input guardrails and SDK-only custom output data under a JSON contract. | A guardrail is a distinct decision gate before human authority; model-visible versus SDK-only metadata must be distinguished. | Interface support is not proof of universal policy enforcement. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
