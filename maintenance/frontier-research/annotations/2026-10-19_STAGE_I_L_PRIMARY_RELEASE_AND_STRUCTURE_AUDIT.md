# 2026 Stage I–L primary-release and structure audit — 2026-10-19

## Observation identity, cutoff and method
- Repository: `lostlight530/epistemic-pipeline`; inspected main SHA: `62b80e2cdb5d0aa9af55e4a7224577b468c0641d`; older baseline for previous-year preservation: `d52cd2cccee778073f60339a2368f1903bba915e`.
- Review class: `DOCUMENTARY_SOURCE_IDENTITY_AND_ROUTE_CHECK`; authored by ChatGPT project-session researcher; `SAME_PRODUCER / NOT_INDEPENDENT`.
- Executed on 2026-10-19: compare all eleven source objects selected in native I/J/K/L source registers against the exact GitHub `GET /repos/{owner}/{repo}/releases/tags/{tag}` publisher response, checking tag identity, UTC release publication date, draft flag, pre-release flag. Query native Stage source registers, recursive main tree, and comparison from the prior year's annual synthesis merge.
- Scope: every **selected release-tag record in these four registers**, not all SDK/MCP ecosystem developments, all versions, actual server/client protocol conformance, execution traces or scientific evidence.

## Publisher release identity findings
GitHub API reported `published_at` dates agreeing with the native Stage registers for all eleven selected objects; all had `draft=false` and `prerelease=false` at inspection. This validates publisher *release record identity and timing only*. Nine or more entries from one SDK remain **one originating publisher family**, not multiple independent reproductions.

| Stage | Publisher-owned release record | Native recorded UTC date | Checked identity |
|---|---|---|---|
| I | [openai/openai-agents-python@v0.7.0](https://github.com/openai/openai-agents-python/releases/tag/v0.7.0) | 2026-01-23 | MATCH / published / not pre-release / not draft |
| I | [openai/openai-agents-python@v0.8.0](https://github.com/openai/openai-agents-python/releases/tag/v0.8.0) | 2026-02-05 | MATCH / published / not pre-release / not draft |
| I | [openai/openai-agents-python@v0.12.1](https://github.com/openai/openai-agents-python/releases/tag/v0.12.1) | 2026-03-13 | MATCH / published / not pre-release / not draft |
| J | [openai/openai-agents-python@v0.14.0](https://github.com/openai/openai-agents-python/releases/tag/v0.14.0) | 2026-04-15 | MATCH / published / not pre-release / not draft |
| J | [openai/openai-agents-python@v0.16.1](https://github.com/openai/openai-agents-python/releases/tag/v0.16.1) | 2026-05-07 | MATCH / published / not pre-release / not draft |
| J | [openai/openai-agents-python@v0.17.6](https://github.com/openai/openai-agents-python/releases/tag/v0.17.6) | 2026-06-19 | MATCH / published / not pre-release / not draft |
| K | [openai/openai-agents-python@v0.19.0](https://github.com/openai/openai-agents-python/releases/tag/v0.19.0) | 2026-07-27 | MATCH / published / not pre-release / not draft |
| K | [modelcontextprotocol/modelcontextprotocol@2026-07-28](https://github.com/modelcontextprotocol/modelcontextprotocol/releases/tag/2026-07-28) | 2026-07-28 | MATCH / published / not pre-release / not draft |
| K | [openai/openai-agents-python@v0.22.0](https://github.com/openai/openai-agents-python/releases/tag/v0.22.0) | 2026-08-19 | MATCH / published / not pre-release / not draft |
| K | [openai/openai-agents-python@v0.22.3](https://github.com/openai/openai-agents-python/releases/tag/v0.22.3) | 2026-09-17 | MATCH / published / not pre-release / not draft |
| L-OPEN | [openai/openai-agents-python@v0.24.0](https://github.com/openai/openai-agents-python/releases/tag/v0.24.0) | 2026-10-15 | MATCH / published / not pre-release / not draft |

**Outcome:** `11_OF_11_RELEASE_TAG_DATES_MATCH / ZERO_MISMATCHES_IN_DECLARED_SET`. Vendor-described HITL, guardrail, sandbox, run-state, protocol-integration and trace features remain external claims until independently executed against pinned code/configuration. The MCP specification publisher's stable release is a different source family; it does not certify an SDK or server as conformant.

## 2026 hierarchy and temporal integrity
- Recursive repository tree contained all `39/39` essential native routes: seven Stage contract files + three month reconstructions in each completed I, J, K; six bounded open-month/source/review files in L; 2026 YTD and 2024→2026 YTD synthesis; dated forward index reconciliation.
- Current native Stage I/J/K/L path counts: `13 / 13 / 14 / 7` (total `47` files). This is a file count, not 47 independently executed studies.
- L / 2026-Q4 had **no Stage synthesis** and **no November or December monthly reconstruction**, preserving the open-quarter state. YTD remains `YEAR_OPEN`, not a final 2026 annual.
- Git compare from the 2025 annual-main commit `d52cd2cccee778073f60339a2368f1903bba915e` detected **no edits to native 2024/2025 Stage A–H files**. The large longitudinal index retains old A2 `STAGE_I_NOT_EVIDENCED` assertions as dated historical observations and uses an additive Stage I–L status block; correction path is `corrections/RECONCILIATION_2026-10-19_STAGE_I_TO_L.md`.

## Source-selection conflict and governance
Existing `annotations/PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md` and `annotations/expansion/` contain possible same-origin SDK release objects outside original Stage selection. They are **not Stage-admitted** by this audit, and their existence does not invalidate a prior `NO_SELECTED_OBJECT_IN_DECLARED_SOURCE_SET` finding. If such evidence is admitted, preserve the original source register and issue a dated protocol amendment/correction with explicit review.

## Audit disposition and limitations
| Finding | Observed check | Bounded result |
|---|---|---|
| E1 release identity | GitHub official tag objects vs registered dates | `11/11_MATCH` |
| E2 Stage/longitudinal routing | Git recursive tree | `39/39_REQUIRED_PATHS_EXIST` |
| E3 temporal opening | L directory and YTD status | `Q4_OPEN / YEAR_OPEN` |
| E4 historical integrity | Diff to 2025 annual merge | `A–H_STAGE_FILES_UNCHANGED` |
| E5 independent execution/benchmark replication | **Not performed** | `UNKNOWN / NOT_TESTED` |
| E6 current active-contract or runtime drift | **Not audited** | `UNKNOWN` |
| E7 research peer review | Same producer/document-oriented | `NOT_INDEPENDENT` |

`DOCUMENTARY_IDENTITY_AND_STRUCTURE_CHECK_COMPLETE / NO_CORRECTION_TRIGGER_IN_CHECKED_SCOPE`.

Identity proof is not an evaluator result, `MCP protocol release != endpoint conformance`, `trace existence != verified trajectory`, `runtime-policy pass != truth`, `source count != epistemic independence`. This document is additive; no Stage, old primary evidence or earlier year snapshot is rewritten.
