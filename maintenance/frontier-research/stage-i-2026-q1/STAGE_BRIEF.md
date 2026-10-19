# Frontier Research Stage I — 2026-Q1 | Study brief

## Identity and reconstruction protocol
- Repository: `lostlight530/epistemic-pipeline`; first-batch research-documentation specification: `2026-09-19-first-batch`
- Stage: `I / 2026-Q1`; canonical window: `2026-01-01 through 2026-03-31`
- Record type: `RETROSPECTIVE`; research written: `2026-10-19`
- Research design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Intended/achieved evidence coverage: `SOURCE_BOUNDED`; source cutoff `2026-10-19`; status: `COMPLETE`
- **Protocol timing:** This brief documents an explicit **post-selection reconstruction protocol**, not a preregistration or a search plan recorded before the upstream events.

## Rationale and relation to previous research
Stage H / 2025-Q4 showed that agent evaluation needs toolset, mutable cost/blocking, replanning and trajectory identity, not final-score inheritance.
The full source period is closed, but this is a bounded reconstruction from selected official release surfaces, not an exhaustive field census.

## Research questions
1. Which exact claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer state changed in the selected upstream records for 2026-Q1?
2. What provenance and temporal distinctions connect the source objects without making their release claims independent proof of runtime behavior?
3. What cannot be inferred about this repository from those external records?

## Scope, eligibility and research-object identity
- Include official versioned upstream software/specification release records dated within `2026-01-01` and `2026-03-31` relevant to the repository lens: claims, uncertainty, action authority, trace/state transitions, guardrails, tool exposure, evaluation contract and transfer.
- Exclude future releases, prereleases when classed as stable research objects, undated marketing claims, same-origin mirrors, and unsupported downstream deployment conclusions.
- Objects are **versioned releases**; a patch, minor or major revision is a different object when it changes the stated evidence/behavior relevant to the question.
- Source and object IDs do not denote independent studies: one release may serve as one research object and one originating project source family.
- Hold cross-version equivalence, user adoption, downstream implementation and security certification for separate investigation.

## Discovery route actually used
On 2026-10-19, the investigator read the repository's existing Stage H / prior native syntheses, then inspected public GitHub Release metadata and selected release descriptions via the connected GitHub API, notably `GET /repos/{owner}/{repo}/releases?per_page=100` and selected `/releases/tags/{tag}` routes. The explicit release paths included in the Source/Object Register define the actual selection set. This does not claim historical web search on each source event date, full archive search, literature database search, or exhaustive pagination. Some release descriptions were inspected as returned snippets rather than audited in full.

## Selected Research Parts
- `I1_OPENAIAGENTSPYTHON_V070.md` — Handoff-history defaults and MCP manager, 2026-01-23
- `I2_OPENAIAGENTSPYTHON_V080.md` — Human approval and resumable run state, 2026-02-05
- `I3_OPENAIAGENTSPYTHON_V0121.md` — Rejection evidence preservation, 2026-03-13

## Extraction dimensions and synthesis
Extract date/version, source family, release-described change, inferred evidence/provenance consequence, competing explanation, missing validation, and permitted repository-level relation. Compare *identity/evidence dimensions*, never heterogeneous release-note metrics as a controlled quantitative improvement series.

## Review and guardrails
claim indexed != claim true; evidence linked != evidence sufficient; heuristic score != probability; runtime-policy pass != truth; claim transfer != acceptance; provenance != truth. A same-producer methodological review is required before closed-stage conclusion; independent review and local execution are not implied.
