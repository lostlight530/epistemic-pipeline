# Evidence and comparison chart — Stage J / 2026-Q2

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-J1 | O4 | Agents SDK v0.14.0 introduces beta Sandbox Agents, workspace manifests, local/hosted sandbox clients, snapshots and serialized resume, plus memory capability. | Workspace manifest, mounts, sandbox provider, snapshot and memory state are execution-environment identity; trace text alone cannot recreate them. | S4: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-04-15 |
| F-J2 | O5 | Agents SDK v0.16.1 reports validation of MCP require_approval policies and session-history restoration after compaction replacement failures. | Approval-policy parsing and persistence failure form independent verification surfaces; a correct-looking final answer can hide a lost history segment. | S5: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-05-07 |
| F-J3 | O6 | Agents SDK v0.17.6 adds pre-approval tool input guardrails and SDK-only custom data for tool outputs with a strict JSON-compatible contract. | Input validation before human approval separates argument validity from permission grant; context-private metadata is not publicly validated evidence. | S6: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-06-19 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `epistemic-pipeline` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
