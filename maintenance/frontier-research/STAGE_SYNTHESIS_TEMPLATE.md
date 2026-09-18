# Frontier Research Stage Synthesis — TEMPLATE

> Write this only after the stage's substantive research parts are sufficiently complete. This file does not replace the part records, their search logs, or their source evidence.

## 0. Stage identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage ID:** `<A / B / ...>`
- **Canonical period:** `<YYYY-QN>`
- **Research window:** `<YYYY-MM-DD> through <YYYY-MM-DD>`
- **Record type:** `<RETROSPECTIVE | LIVE_STAGE>`
- **Coverage class:** `<SOURCE_BOUNDED | SEARCH_BOUNDED | METHODICALLY_SCOPED>`
- **Synthesis date:** `<YYYY-MM-DD>`
- **Source cutoff:** `<YYYY-MM-DD>`
- **Stage status:** `<READY_FOR_SYNTHESIS | COMPLETE | PARTIAL>`

## 1. Research inputs included

| Part | Title | Outcome | Search/source boundary | Material unresolved issue |
|---|---|---|---|---|
| `<A1>` | `<title>` | `<outcome>` | `<boundary>` | `<issue or none>` |

Identify intentionally excluded or incomplete parts. Do not imply completeness when a material part remains unresolved.

## 2. Method and coverage reconciliation

Summarize how the stage was actually researched, not merely how it was planned.

- **Planned vs executed searches:** `<summary>`
- **Material eligibility/selection changes:** `<summary>`
- **Unsearchable / inaccessible evidence classes:** `<summary>`
- **Known coverage gaps:** `<summary>`
- **Peer/independent review of search or selection, if any:** `<performed / NOT_PERFORMED / not applicable>`

Do not upgrade `SOURCE_BOUNDED` or `SEARCH_BOUNDED` into an exhaustive/systematic-completeness claim.

## 3. Amendment / deviation reconciliation

List material changes from the stage brief and explain their effect on comparability, coverage, or interpretation. Preserve the earlier plan rather than rewriting it away.

## 4. Cross-part evidence map

| Synthesis finding | Supporting parts | Independent source families | Counterevidence | Strength / limitation |
|---|---|---|---|---|
| `<finding>` | `<A1,A3>` | `<independent / same-origin / mixed / unknown>` | `<part/source>` | `<bounded assessment>` |

Repeated claims from one originating source are one source family, not independent convergence.

## 5. What changed during the stage

Describe the strongest time-bounded changes supported across the parts: newly introduced systems/methods/standards, maturation/adoption, failures/reversals, promotional or unverified claims, and changes in evidence quality.

## 6. What persisted

Identify durable problems, constraints, and engineering patterns that remained stable.

## 7. Conflicts and counterevidence

Preserve meaningful disagreements between parts or sources.

```text
synthesis != majority vote
repetition != independence
later success != earlier success
current knowledge != historical knowledge
```

Where evidence does not resolve a conflict, keep it unresolved.

## 8. Negative space

Summarize important things the stage did not establish, including missing capabilities, absent independent reproduction, standards without demonstrated adoption, unverified external claims, unknown provenance/influence, and missing archival evidence.

## 9. Repository-level interpretation

Interpret the stage through: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

### Independent convergence

What external developments resemble current repository choices without proving influence?

### Deliberate divergence

Where does the repository intentionally maintain a different boundary or architecture?

### Potential gaps

Which developments deserve watch or a separate current-state audit?

### Non-gaps

Which developments are interesting but do not expose a current repository defect?

## 10. Repository-specific hard boundaries preserved

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

## 11. Temporal reconciliation

For retrospective stages, distinguish what was knowable during the historical window, what later evidence revealed, what the repository did not yet contain, and what it contains now. Do not back-project current semantics into the historical period.

For a stage that crosses repository creation, explicitly distinguish the pre-creation external landscape from post-creation repository history.

## 12. Delta from the previous stage

Where a prior stage exists, state only evidence-backed transitions: `NEW`, `STRENGTHENED`, `WEAKENED`, `REVERSED`, `PERSISTENT`, `UNRESOLVED`, or `NOT_COMPARABLE`. Do not force a delta where methods or source coverage are not comparable.

## 13. Current repository assessment

- **Current implementation drift confirmed:** `<YES / NO / UNKNOWN>`
- **Current active-contract drift confirmed:** `<YES / NO / UNKNOWN>`
- **Current documentation drift confirmed:** `<YES / NO / UNKNOWN>`
- **Research-only watch items:** `<list>`
- **Separate repair/audit required:** `<YES / NO>`

If no current defect is independently established:

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

## 14. Synthesis provenance

| Activity | Responsible person/agent when known | Tool/surface when known | Date | Input set |
|---|---|---|---|---|
| `<synthesis>` | `<identity or UNKNOWN>` | `<tool or UNKNOWN>` | `<date>` | `<parts/refs>` |

## 15. Stage conclusion

Use `FRONTIER_STAGE_COMPLETE` or `FRONTIER_STAGE_PARTIAL`, followed by a prose conclusion that keeps external research separate from current repository truth.

```text
stage close != final truth
stage synthesis != deletion of part-level uncertainty
later correction != rewrite of historical research
```

## 16. Correction / update triggers

State what future evidence would justify reopening interpretation through a new correction/reconciliation record, for example a newly recovered primary source, corrected publication identity, later independent reproduction, or a discovered historical contradiction.

## 17. Carry-forward questions

- `<question for the next stage or later correction>`
