# Frontier Research Part — TEMPLATE

> One file represents one independent research question or tightly bounded subject within a three-month stage. Duplicate this template only when another independent research part is actually justified.

## 0. Part identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `<Stage ID / canonical period>`
- **Part ID:** `<A1 / A2 / ...>`
- **Title:** `<research subject>`
- **Research window:** `<YYYY-MM-DD> through <YYYY-MM-DD>`
- **Research performed / reconstructed on:** `<YYYY-MM-DD>`
- **Source cutoff:** `<YYYY-MM-DD>`
- **Coverage statement:** `<SOURCE_BOUNDED / SEARCH_BOUNDED / other bounded description>`
- **Status:** `<IN_PROGRESS | COMPLETE | INSUFFICIENT_EVIDENCE | NOT_APPLICABLE>`

## 1. Research question

> `<one falsifiable or answerable question>`

Explain why this question matters within the stage.

## 2. Scope, inclusion, and exclusions

### In scope

- `<scope / eligible evidence>`

### Explicitly out of scope

- `<exclusion>`

### Selection rules

- `<why a candidate source/system/event is included or excluded>`

State temporal, geographic, technical, domain, version, language, and source limitations where material.

## 3. Research activity provenance

| Activity ID | Activity | Person/agent when known | Tool/surface when known | Executed at | Notes |
|---|---|---|---|---|---|
| `R1` | `<search / browse / inspect / compare / extract>` | `<identity or UNKNOWN>` | `<tool or UNKNOWN>` | `<date/time>` | `<notes>` |

Observed identity only; unknown stays unknown.

## 4. Search / discovery log

Preserve the actual search that was executed, not a cleaned-up query reconstructed after the fact.

| Search ID | Surface | Exact query / navigation method | Executed at | Filters / limits | Result count if observable | Reproducibility limitation |
|---|---|---|---|---|---|---|
| `Q1` | `<surface>` | `<exact query>` | `<date/time>` | `<limits>` | `<count / NOT_OBSERVED>` | `<ranking/index/history limitation>` |

If discovery used citation chaining, direct URL inspection, repository history, standards navigation, or another non-query method, record that method explicitly.

## 5. Candidate / selection ledger

Record materially relevant inclusion/exclusion decisions. This is not a claim that every search result was exhaustively screened unless that was actually done.

| Candidate ID | Candidate | Found via | Decision | Reason |
|---|---|---|---|---|
| `CAND-1` | `<source/system/event>` | `Q1` | `<INCLUDE / EXCLUDE / HOLD>` | `<reason>` |

## 6. Source register

| ID | Source | Source type | Event/publication date | Version/revision | Authority for this claim | Limitations / conflicts |
|---|---|---|---|---|---|---|
| `S1` | `<source>` | `<paper / official docs / repository / standard / status / secondary>` | `<date>` | `<version>` | `<bounded authority>` | `<limits>` |

Do not count multiple restatements of the same underlying claim as independent corroboration.

## 7. Evidence extraction matrix

| Finding ID | Claim / observation candidate | Supporting source IDs | Counter-source IDs | Evidence class | Time scope | Independence note |
|---|---|---|---|---|---|---|
| `F1` | `<bounded finding>` | `S1` | `<Sx / none found>` | `<vendor / paper / standard / runtime / independent / secondary>` | `<window>` | `<same-origin / independent / unknown>` |

## 8. Observations

Record what the sources actually establish. Keep observation separate from interpretation.

### O1 — `<observation>`

- Evidence: `S1, S2`
- Time scope: `<date/window>`
- Evidence boundary: `<bounded statement>`

Add observations as needed.

## 9. Counterevidence and competing interpretations

Actively record evidence that contradicts, narrows, shows source dependence, shows non-adoption/failure, or remains unresolved. Absence of a counterevidence search is not corroboration.

### C1 — `<counterevidence or alternative>`

`<analysis>`

## 10. Negative space / what was not established

Record meaningful non-findings: undemonstrated capabilities, unpublished/unadopted standards, missing independent reproduction, unavailable historical artifacts, unknown influence/provenance, or claims that could not be verified.

## 11. Interpretation

Distinguish `observed fact`, `attributed external claim`, `research interpretation`, `inference`, and `unknown / unresolved`.

## 12. Relation to this repository

Assess relevance through: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

Useful relationship labels: `DIRECTLY_RELEVANT`, `CONTEXTUAL`, `PARALLEL_CONVERGENCE`, `DELIBERATE_DIVERGENCE`, `WATCH`, `NO_MATERIAL_RELATION`, `UNKNOWN`.

Do not turn similarity into lineage or influence.

## 13. Current repository effect

- **Current implementation defect established?** `<YES / NO / UNKNOWN>`
- **Current active-contract drift established?** `<YES / NO / UNKNOWN>`
- **Runtime change justified by this part alone?** `NO`
- **Separate follow-up candidate?** `<none / bounded candidate>`

A research finding is not itself authorization to modify the repository.

## 14. Amendments / deviations within this part

| Date | Change | Reason | Effect on coverage or interpretation |
|---|---|---|---|
| `<date>` | `<change>` | `<reason>` | `<effect>` |

Use `NONE` if no material deviation occurred.

## 15. Part conclusion and limitations

Use a bounded outcome such as `SUPPORTED_OBSERVATION`, `CONTESTED`, `INSUFFICIENT_EVIDENCE`, `UNKNOWN`, `NO_MATERIAL_FRONTIER_CHANGE`, `WATCH`, `CANDIDATE_REPOSITORY_RELEVANCE`, or `NO_CURRENT_REPOSITORY_DRIFT`.

State the strongest conclusion the evidence supports, followed immediately by the important limitations on that conclusion.

## 16. Unresolved questions

- `<question the stage synthesis must preserve rather than hide>`
