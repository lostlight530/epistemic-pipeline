# Frontier Research Part — TEMPLATE

> Instantiate one file per independently meaningful research question or bounded sub-study. A Part is research, not a progress note.

## 0. Part identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Specification version:** `2026-09-19-first-batch`
- **Stage:** `<Stage ID / canonical period>`
- **Part ID:** `<A1 / A2 / ...>`
- **Title:** `<research subject>`
- **Research design:** `<design class>`
- **Research window:** `<date range>`
- **Research performed/reconstructed on:** `<date>`
- **Source cutoff:** `<date>`
- **Coverage achieved:** `<coverage class>`
- **Status:** `<IN_PROGRESS | COMPLETE | INSUFFICIENT_EVIDENCE | NOT_APPLICABLE>`

## 1. Research question and rationale

> `<question>`

Explain why this question is analytically distinct and how it contributes to the Stage.

## 2. Scope and unit of analysis

Define the unit(s) being studied: project, system, release, standard version, paper/method, benchmark, incident, workflow, community practice, or another explicit object.

State when versions/releases count as the same object and when they are distinct.

## 3. Eligibility and selection criteria

### Include

- `<criterion>`

### Exclude

- `<criterion>`

### Hold / unresolved

- `<criterion>`

## 4. Discovery/search method actually executed

Record the method that actually ran, not a cleaned-up reconstruction.

| ID | Surface | Exact query or navigation method | Executed at | Filters/limits | Coverage/reproducibility limitation |
|---|---|---|---|---|---|
| `Q1` | `<surface>` | `<exact query/navigation>` | `<date/time>` | `<limits>` | `<limitation>` |

For direct known-source retrieval, citation chaining, repository history, or standards navigation, describe the exact route used.

## 5. Research-object and source selection

Use stable local object/source IDs or reference `SOURCE_OBJECT_REGISTER.md`.

| Candidate/Object | Source(s) | Decision | Reason | Object identity/version note |
|---|---|---|---|---|
| `<O1>` | `<S1,S2>` | `<INCLUDE / EXCLUDE / HOLD>` | `<reason>` | `<identity>` |

Do not count repeated reports of the same object as independent objects.

## 6. Source authority and provenance

| Source ID | Type | Origin/source family | Event date | Publication/update date | Version/revision | Authority | Limitations |
|---|---|---|---|---|---|---|---|
| `S1` | `<type>` | `<family>` | `<date>` | `<date>` | `<version>` | `<bounded authority>` | `<limits>` |

## 7. Evidence extraction / charting

Use `EVIDENCE_CHART.md` for large structured studies; otherwise record the necessary extraction here.

| Finding candidate | Object | Supporting source(s) | Contradicting source(s) | Evidence class | Temporal scope | Independence |
|---|---|---|---|---|---|---|
| `F1` | `O1` | `S1` | `<Sx / none found>` | `<class>` | `<scope>` | `<independent / same-origin / unknown>` |

## 8. Observations

Observations are bounded statements directly supported by sources. Separate them from interpretation.

### O1 — `<observation>`

- **Evidence:** `<source IDs>`
- **Object/event:** `<object ID>`
- **Time scope:** `<scope>`
- **Authority boundary:** `<what is actually established>`

## 9. Counterevidence and competing interpretations

Actively search for and preserve material evidence that weakens, narrows, contradicts, or contextualizes the initial interpretation.

### C1 — `<counterevidence / alternative>`

- Evidence: `<source IDs>`
- Effect: `<contradicts / narrows / source-dependent / unresolved / other>`

Absence of a counterevidence search is not corroboration.

## 10. Negative space

Record meaningful non-findings and absences: no public implementation, no independent reproduction, inaccessible historical revision, no adoption evidence, missing benchmark detail, no provenance link, or another research-relevant absence.

Distinguish `NOT_FOUND_IN_DECLARED_SEARCH` from `DOES_NOT_EXIST`.

## 11. Critical appraisal, when used

State appraisal method and result without converting qualitative judgment into an invented universal score.

- **Appraisal method:** `<none / declared method>`
- **Key strengths:** `<...>`
- **Key limitations:** `<...>`
- **Effect on synthesis:** `<...>`

## 12. Analysis

Explain patterns, mechanisms, relationships, transitions, or differences supported by the evidence. This is the analytic core of the Part and should not be reduced to a bullet inventory of sources.

## 13. Interpretation and competing explanations

Separate:

- observed fact;
- attributed external claim;
- research interpretation;
- inference;
- unresolved/unknown.

Where multiple explanations remain plausible, keep them visible.

## 14. Relation to this repository

Interpret through: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

Possible relationship labels: `DIRECTLY_RELEVANT`, `CONTEXTUAL`, `PARALLEL_CONVERGENCE`, `DELIBERATE_DIVERGENCE`, `WATCH`, `NO_MATERIAL_RELATION`, `UNKNOWN`.

Do not infer lineage, influence, or predecessor status from similarity.

## 15. Current-repository implication boundary

- **Current implementation defect established?** `<YES / NO / UNKNOWN>`
- **Current active-contract drift established?** `<YES / NO / UNKNOWN>`
- **Current documentation drift established?** `<YES / NO / UNKNOWN>`
- **Candidate follow-up:** `<none / bounded question>`
- **Runtime change justified by this Part alone?** `NO`

## 16. Method amendments / deviations

| Date | Change | Reason | Effect on coverage/interpretation/comparability |
|---|---|---|---|
| `<date>` | `<change>` | `<reason>` | `<effect>` |

Use `NONE` when no material deviation occurred.

## 17. Contribution and instrument provenance

Identify who/what performed conceptualization, methodology, investigation, evidence curation, analysis, validation/review, and writing/synthesis when known. Keep responsible contributor attribution separate from tools/models used as instruments.

## 18. Part conclusion

Use bounded outcome labels such as `SUPPORTED_OBSERVATION`, `CONTESTED`, `INSUFFICIENT_EVIDENCE`, `UNKNOWN`, `NOT_COMPARABLE`, `NO_MATERIAL_FRONTIER_CHANGE`, `WATCH`, `CANDIDATE_REPOSITORY_RELEVANCE`, or `NO_CURRENT_REPOSITORY_DRIFT`.

Write the strongest defensible conclusion in prose, followed by its limitations.

## 19. Unresolved questions

- `<question>`

## 20. Inputs to Stage synthesis

State what the Stage synthesis may safely carry forward and what must remain unresolved or source-qualified.
