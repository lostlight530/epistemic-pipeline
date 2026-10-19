# 2026-10-19 additional-source reconciliation — Stage J MCP authority and input schema

## Research status and original source boundary
- Repository: `lostlight530/epistemic-pipeline`; historical 2026-Q2, written/researched **2026-10-19**.
- Record class: `ADDITIVE_SOURCE_SELECTION_EXPANSION / SOURCE_BOUNDED`.
- The native Stage J uses OpenAI Agents SDK 0.14.0 (April), 0.16.1 (May) and 0.17.6 (June), with dated monthly owners, two-or-more original Research Parts and an internal review. Their prior source selection is intact; this annex is **not** a rewrite of the Stage register, research Part or conclusion.
- Method actually used here: official GitHub SDK release collections and exact tag descriptions, accessed 2026-10-19. No runtime execution, security proof, evaluator replay, systematic search or independent reviewer.

## Additional versioned research objects
| Candidate | Historical owner | Release / published UTC | Release-publisher observation | Interpretation boundary |
|---|---|---|---|---|
| EX-J1 | [April / Stage J](../../stage-j-2026-q2/MONTH_2026_04_RECONSTRUCTION.md) | [Agents SDK v0.13.5](https://github.com/openai/openai-agents-python/releases/tag/v0.13.5), 2026-04-06 | Callable approval policies for local MCP servers; public trace-flush API; serializes SQLite writes with shared file locks | An approval policy may be executable/callable and source-defined; existence of API is not evidence of correct local policy enforcement |
| EX-J2 | [May / Stage J](../../stage-j-2026-q2/MONTH_2026_05_RECONSTRUCTION.md) | [Agents SDK v0.15.3](https://github.com/openai/openai-agents-python/releases/tag/v0.15.3), 2026-05-06 | Avoid mutation of MCP input schemas, reject non-object tool input JSON, deterministic duplicate-tool errors | Tool discovery/schema snapshot and input-validation failure should be separate trace/evaluator evidence |
| Existing native comparator | [May / Stage J](../../stage-j-2026-q2/STAGE_SYNTHESIS.md) | [Agents SDK v0.16.1](https://github.com/openai/openai-agents-python/releases/tag/v0.16.1), 2026-05-07 | Validates MCP `require_approval` policies, handles corrupt session state and also non-object function-tool JSON | Adjacent versions describe different change sets and cannot be silently merged into one release object |
| Existing native comparator | [June / Stage J](../../stage-j-2026-q2/STAGE_SYNTHESIS.md) | [Agents SDK v0.17.6](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6), 2026-06-19 | Adds pre-approval tool input guardrails | Input checks, conditional approval and tool execution are distinct state transitions |

## Mechanism and competing accounts
The selected versions suggest a **conditional action-evidence contract**:

```text
tool schema snapshot / source revision
 -> candidate input
 -> typed JSON/schema validation
 -> approval-policy evaluation / human authorization
 -> authorized tool execution or explicit rejection
 -> durable trace / resume record
 -> bounded claim under an evaluator
```

That is a **research model**, not proof the SDK or this repository realized each transition correctly. All EX-J1/EX-J2 and the native comparator releases originate from the **same SDK source family**; version multiplicity does not establish independence. The May 0.15.3 and 0.16.1 notes overlap on non-object JSON handling but document distinct scopes and changes; a valid alternative reading is ordinary patch maintenance rather than a categorical shift in all agent systems.

The native quarter's broader sandbox story remains unchanged. EX-J1/EX-J2 are **additional candidates** under an expanded selection, not retroactively authored April/May research and not a claim that the original J source selection was erroneous. No extra object IDs are silently inserted into the existing register.

## Disposition / evidence gate
- `SOURCE_BOUNDED_ADDITIONAL_EVIDENCE`, same-session producer analysis only; `INDEPENDENCE_NOT_ESTABLISHED`.
- Native Stage J `FRONTIER_STAGE_COMPLETE` continues to mean its originally declared source-bounded project. Current repository defects, benchmark pass, tool-policy enforcement correctness and cross-run state replay remain **UNKNOWN / NOT_TESTED**.
- Future integration into the Stage owner would require explicit selection amendment, object IDs, source/evidence chart change and forward review; history stays append-only.
- `NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE / NO_AUTOMATIC_AUTHORITY_TRANSFER`.

