# Independent A1 — epistemic-pipeline — 2026-11-09 Stage L source custody

## Identity and scope
- Repository: `lostlight530/epistemic-pipeline`; task: `independent-maintenance/A1`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 23:10:21 +08:00.
- A1 scope: November 01–08 inclusive; Nov09 is reserved for A2.
- Exact pre-write main: `384ae000ab681b54a5e593be599373c8c161f44f`.
- Prior A1 Nov01–07: `maintenance/frontier-research/annotations/2026-11-08_A1_STAGE_SOURCE_CONTENT.md` @ `2b0699e6987a23dc369c34f022ebbb522a0e8379`.
- Prior A2 Nov08: `maintenance/frontier-research/annotations/2026-11-08_A2_MONTH_RELATION.md` @ `c6f39aa35ea23d589c0a53d9af9132948fa97a5b`.
- D7 Nov08: `maintenance/2026-11-08-d7-operational-continuity.md` @ `ac34e145c0b6b3e7435a5bd57e772c559ea4769f`.
- Current index: `maintenance/frontier-research/LONGITUDINAL_INDEX.md` @ `6361bdf86a7b77dd036b4497c1ce809b1d3c5d7d`.
- The 2026-09-25 SOP requires complete Nov01→N−1 custody and merged A1 before A2; no universal 100-line/PR gate is specified.

## Exact Stage and D7 source custody
| Object | Blob SHA | Role |
|---|---|---|
| `stage-l-2026-q4/STAGE_BRIEF.md` | `a61af40d2f52e5d83293a4e4e323e0c9f1c57d2b` | Stage L scope and selection |
| `stage-l-2026-q4/L1_OPENAIAGENTSPYTHON_V0240.md` | `74528de0b79ca0ccffc634d4a894bc5fc7b1c224` | selected Agents Python v0.24.0 object |
| `LONGITUDINAL_INDEX.md` | `6361bdf86a7b77dd036b4497c1ce809b1d3c5d7d` | current month routing |
| `2026-11-08-d7-operational-continuity.md` | `ac34e145c0b6b3e7435a5bd57e772c559ea4769f` | D7 operational continuity |

## Nov08-specific findings and decisions
1. Stage L's selected OpenAI Agents Python v0.24.0 source cut remains October19; later prerelease candidates are not retroactive changes to the selected object.
2. The Stage L brief describes post-selection reconstruction, not a preregistered experiment; the quarter remains IN_PROGRESS.
3. A publisher SDK annotation that describes an MCP tool does not establish that a protected tool invocation was authorized.
4. Approval-required resume must bind the exact tool name, arguments, session identity and policy version to the grant.
5. A generic consent transcript cannot authorize a changed request or newer tool schema.
6. State compaction can erase approval history unless authority-bearing request receipts are preserved outside the summary.
7. A returned MCP tool message and an externally committed change are separate events with different failure outcomes.
8. Exactly-once external effect requires a sink-issued idempotency key or commit receipt; a trace ID alone is insufficient.
9. A denied execution path must show that the protected side effect did not occur, not merely that a refusal string was emitted.
10. Same-publisher release notes, code and documentation are one SDK lineage, not three independent validations.
11. The D7 report records six prior A1/A2 pairs Nov02–07; they are maintenance artifacts, not six additional Stage-L Native runs.
12. D7's current-pointer correction from Nov06 to Nov07 is a dated navigation repair and does not certify the Nov07 A1/A2 semantic gate.
13. The Nov08 A1 and A2 files are present on main, but the LONGITUDINAL_INDEX header still routes current relation through Nov07; the pointer is stale relative to merged Nov08 A2.
14. The D7 report explicitly preserves the original Stage selection, MANIFEST calendar clock and prior A1/A2; those boundaries remain intact.
15. No live MCP server, approval service, effect sink, publisher runtime or independent conformance suite was executed by this A1.

## Month-to-date coverage and decision matrix
| Window | Evidence owner | Decision |
|---|---|---|
| Nov01 | Prior A1 / month-start baseline | INHERIT_PRIOR_A1 |
| Nov02–07 | Prior A1 exact source review | INHERIT_PRIOR_A1 |
| Nov08 | D7 report, current index, Stage L brief and selected SDK object | REVIEWED; APPEND_RELATION / CURRENT_POINTER_DRIFT |
| Nov09 | Excluded from A1 | A2_INPUT_ONLY |
| Nov10–30 | Future dates | NOT_DUE |

- November remains OPEN; Stage L 2026-Q4 remains IN_PROGRESS.
- The current relation pointer needs a forward update after this A1 merges and the new A2 is created from fresh main.
- No Stage source selection, claim/evidence chart, MANIFEST calendar state, original research or runtime implementation is changed by A1.
- Result: `A1_COVERAGE_COMPLETE_WITH_NOV08_D7_AND_INDEX_RECONCILIATION_IDENTIFIED`.
