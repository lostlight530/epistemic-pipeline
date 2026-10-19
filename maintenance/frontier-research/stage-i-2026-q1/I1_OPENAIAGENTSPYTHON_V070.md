# I1 — Handoff-history defaults and MCP manager

## 0. Research Part identity
- Repository: `lostlight530/epistemic-pipeline`; Stage `I / 2026-Q1`; Part `I1`
- Unit: upstream versioned release `openai/openai-agents-python@v0.7.0`
- Event/release publication: `2026-01-23`; research/access: `2026-10-19`
- Design: `TARGETED_EVIDENCE_SYNTHESIS`; coverage: `SOURCE_BOUNDED`; status: `COMPLETE (documentary)`

## 1. Research question and rationale
What identity, authority and replay problem is exposed by **Handoff-history defaults and MCP manager**, and which stronger conclusions are blocked by the evidence? This Part is independently meaningful because its upstream revision has a separate version clock and source authority. Its relation to 2026-Q1 is analytic, not causal proof.

## 2. Selection / object definition
The researched object `O1` is the named release openai/openai-agents-python v0.7.0, not all revisions in that software family and not all products mentioning this release. Inclusion: published official upstream release within the Stage window, explicit evidence-bearing change relevant to claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer. Excluded: downstream performance/adoption reports not investigated, inference from unrelated revisions, unobserved local executions. Holds: third-party independent replication, compatibility matrix and local-contract implications.

## 3. Discovery actually performed / evidence authority
- `S1`: [upstream GitHub release v0.7.0](https://github.com/openai/openai-agents-python/releases/tag/v0.7.0); release publication date: 2026-01-23; accessed in a 2026-10-19 connected-GitHub evidence check.
- Discovery/navigation: official repository GitHub Releases listing, then selected release-tag metadata/body where retrieved. No exhaustive search, independent audit, or second-origin corroboration.
- Release publisher controls the project release description and tag; it can establish **what the project says it shipped**, not a runtime observation in `epistemic-pipeline`.

## 4. Source/Object and finding chart
| Object | Source | Release-described observation | Analytic inference | Independent validation |
|---|---|---|---|---|
| `O1` | `S1`, same-origin release note | Agents SDK v0.7.0 changes nested handoff history from default-on to opt-in and introduces MCPServerManager for multiple MCP server instances. | Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean. | `NOT_EXECUTED / UNKNOWN` |

## 5. Observation with scope
**Publisher record (source-asserted):** Agents SDK v0.7.0 changes nested handoff history from default-on to opt-in and introduces MCPServerManager for multiple MCP server instances.
The date is a *release publication date*, not an observation of deployment, field adoption, user activation or repository use. The documented upstream change is evidence about this versioned **research object**, not an automatically inherited implementation state.

## 6. Alternative interpretation and counterevidence boundary
Release-described API behavior does not establish production deployments or any benchmark pass.
No independent contradictory source family was selected or audited within this Part. That limitation means `COUNTEREVIDENCE_NOT_INDEPENDENTLY_TESTED`, not `NO_COUNTEREVIDENCE_EXISTS`. An apparent trend across upstream releases could reflect the researcher's selection of salient changes rather than ecosystem prevalence.

## 7. Negative space / authority matrix
| Question | Result in this Part | Correct interpretation |
|---|---|---|
| Official release record available? | Yes: `S1` | Release metadata and description available |
| Exact local environment or model/tool state captured? | `NO` | Cannot infer deployment or local conformance |
| Cross-version replay performed? | `NO` | Cannot assert semantic/output equivalence |
| Independent source-family replication? | `NOT_FOUND_IN_SELECTED_SOURCE_SET` | Not a global absence assertion |
| A current defect in `epistemic-pipeline` identified? | `UNKNOWN / NOT_AUDITED` | External release alone cannot authorize repair |

## 8. Analysis: mechanism and repository lens
Run provenance must include handoff-history configuration and connected tool-server membership; a changed default alters what the trace can mean.
This matters to claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer: the release changes the vocabulary of what a *versioned evidence receipt* might need to identify. An evidence receipt would require the source identity, release revision, applicable configuration, artifact or run state, and independently observed local result before making repository-specific claims. Those conditions were not met by reading this release record.

## 9. Temporal, methodological and uncertainty reconciliation
This is a 2026-10-19 reconstruction of a 2026-01-23 published upstream release. The original Stage H and earlier research files remain unchanged; later knowledge is not projected backward as contemporary evidence. Search method is selection from named public upstream release surfaces; it is `SOURCE_BOUNDED`, not a systematic/scoping review. No measured release adoption, exhaustive negative search or statistical performance estimate is asserted.

## 10. Part conclusion / follow-up
`SUPPORTED_UPSTREAM_RELEASE_OBSERVATION / BOUNDED_RESEARCH_INTERPRETATION`.
The source supports the documented release statement; it does **not** establish tested repository behavior. Follow-up: reproduce the relevant conversion/approval/rendering surface with pinned revision and environment *only if separately approved and within a dedicated audit*.

## 11. Responsibility and instrument provenance
Research synthesis prepared in this ChatGPT project session, 2026-10-19, using the connected GitHub read tools as evidence instruments; independent human/subject-specialist verification not observed. Responsible repository governance remains separate from the instrument.
