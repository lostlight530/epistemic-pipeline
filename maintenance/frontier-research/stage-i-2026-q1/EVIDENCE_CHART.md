# Evidence and comparison chart — Stage I / 2026-Q1

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-I1 | O1 | Agents SDK v0.7.0 changes nested handoff history from default-on to opt-in and introduces MCPServerManager for multiple MCP server instances. | Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean. | S1: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-01-23 |
| F-I2 | O2 | Agents SDK v0.8.0 introduces human-in-the-loop tool approval, pending interruptions and RunState serialization/resume; it also changes synchronous tool threading and MCP failure handling defaults. | Approval decision, resume boundary, actor authority and failure-policy defaults become evidence in the executed trajectory. | S2: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-02-05 |
| F-I3 | O3 | Agents SDK v0.12.1 preserves explicit approval rejection messages across resume flows. | Negative decisions and their reasons are part of state-transition evidence; omission can make replay look like unexplained blocking. | S3: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-03-13 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `epistemic-pipeline` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
