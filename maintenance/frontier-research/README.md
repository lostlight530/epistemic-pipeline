# Frontier Research Stages

**Repository:** `lostlight530/epistemic-pipeline`  
**Status:** research guidance / non-normative support surface  
**Default horizon:** one three-month research stage  
**Method calibration checked:** 2026-09-19  
**Effect on runtime or active contracts:** none unless a separate evidence-backed repository change is later justified

## 1. Purpose

This directory supports longitudinal research into the external research-engineering landscape relevant to this repository.

Repository lens: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

A frontier stage is research, not scheduled report generation and not an automation target. A three-month window is one project-defined research stage. The stage may contain as many independent research parts as the evidence and research questions require, followed by an explicit stage-level synthesis.

**Do not split a stage into monthly sections merely because the window spans three months. Decomposition is by research subject, not by calendar month.**

## 2. External-method calibration

The method borrows bounded practices from established open-science and evidence-synthesis approaches without claiming conformance to any of them.

- OSF projects/components support modular research work where sub-projects can remain independently documented.
- Cochrane review guidance emphasizes defining the review question and eligibility logic before searching, documenting searches in enough detail for later reporting/reproduction, and retaining selection decisions.
- PRISMA-S emphasizes recording information sources, exact search strategies, limits, search dates, updating methods, peer review where applicable, and record-management details.
- OSF preregistration guidance supports timestamped research plans and transparent later updates rather than silently making the initial plan appear correct in hindsight.
- W3C PROV distinguishes entities, activities, and responsible agents; this stage model likewise separates sources/results from research actions and responsibility.
- RO-Crate provenance guidance models creation/update activities and supports retaining prior versions when curation creates a new version; this aligns with forward correction rather than silent history rewrite.
- The Turing Way describes a research compendium as a collection of the digital parts of a research project, supporting the decision to keep research parts and synthesis together but separately inspectable.

These precedents support the **method discipline**, not the three-month duration. The three-month stage horizon is this project's own research convention.

### Explicit non-claims

```text
three-month stage != external standard
this template != PRISMA compliance
this template != Cochrane systematic review
web search != exhaustive literature search
source count != evidence quality
structured record != scientific validity
```

Each stage must state its own search/coverage class. Default to `SOURCE_BOUNDED` unless a stronger method was actually executed and documented.

## 3. Stage model

```text
three-month stage
    ↓
stage brief / research protocol
    ↓
independent research parts chosen for this stage
    ↓
search + selection + extraction + counterevidence records
    ↓
repository-specific interpretation
    ↓
stage synthesis
    ↓
forward correction / next-stage questions when needed
```

A part is a research unit, not a template-filling task. Different stages may have different numbers of parts and different topics. Projects, papers, standards, runtimes, failures, provenance, reproducibility, scientific workflows, and other themes are examples only; the research question determines the decomposition.

## 4. Historical reconstruction vs live research

- **RETROSPECTIVE** — research reconstructed later for a historical three-month window.
- **LIVE_STAGE** — research conducted contemporaneously during or near the stage.
- **CORRECTION / RECONCILIATION** — later evidence that narrows or corrects an earlier stage without rewriting it.

```text
historical event date
!= reconstruction date
!= search execution date
!= repository implementation date
!= evidence that this repository derived from that event
```

Historical reconstruction must never be written as though it was performed at the historical date.

## 5. Stage identity and layout

Prefer a human stage label plus an explicit canonical period and exact dates:

```text
Stage: A
Canonical period: 2024-Q1
Window: 2024-01-01 through 2024-03-31
Record type: RETROSPECTIVE
Coverage class: SOURCE_BOUNDED
```

The stage letter is a human research label. The canonical period and exact dates remain the authoritative time identity.

```text
maintenance/frontier-research/
└── stage-a-2024-q1/
    ├── STAGE_BRIEF.md
    ├── A1_<research-topic>.md
    ├── A2_<research-topic>.md
    ├── ...
    └── STAGE_SYNTHESIS.md
```

Add source registers, appendices, comparison tables, or mapping studies when the research needs them. Do not create empty files to satisfy a shape.

## 6. Research-part independence

Each part preserves its own research question, time boundary, search and source record, observations, counterevidence, unresolved facts, interpretation, repository relevance, and explicit non-claims. Parts may disagree or remain unresolved.

```text
part finding != whole-stage conclusion
whole-stage conclusion != rewrite of part evidence
synthesis != source evidence
repetition != independent corroboration
```

## 7. Search and source discipline

Whenever search is part of the method, preserve the actual search surface, exact query or query family, execution date, filters/limits, relevant coverage boundary, and selection rationale. If exact reproduction is impossible because a search engine, ranking system, or database changes over time, record that limitation.

Do not infer provenance or intellectual lineage from similarity alone.

```text
historical similarity != lineage
earlier similar project != predecessor
parallel design != influence
later repository design != evidence of historical derivation
```

Unknown influence remains unknown.

## 8. Amendments and deviations

Research plans are allowed to improve. Changes to questions, search strategy, eligibility, or synthesis method should be recorded as dated amendments/deviations rather than silently editing the record so that the final method appears to have been the original method.

## 9. Repository authority boundary

Frontier-stage research is a calibration and research-memory surface. It does not outrank current repository truth. External research enters the repository-change path only when current repository evidence independently establishes a real defect, drift, or justified semantic transition.

A valid stage may end with:

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

## 10. Repository-specific hard boundaries

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

These boundaries remain in force during historical comparison and frontier synthesis.

## 11. Completion semantics

A stage is complete only when the stage brief fixes its time/evidence boundaries; the actually required research parts have explicit outcomes; search/selection limitations are inspectable; material counterevidence and unresolved questions remain visible; amendments are recorded; repository relevance is assessed without converting similarity into provenance; and a stage synthesis is written from the completed parts.

Research outcomes may include `SUPPORTED_OBSERVATION`, `CONTESTED`, `INSUFFICIENT_EVIDENCE`, `UNKNOWN`, `NOT_APPLICABLE`, `NO_MATERIAL_FRONTIER_CHANGE`, `WATCH`, `CANDIDATE_REPOSITORY_RELEVANCE`, and `NO_CURRENT_REPOSITORY_DRIFT`. These are research outcomes, not runtime status codes.

Stage close means that the declared research process reached its closure boundary. It does not mean final truth; later evidence is handled through correction/reconciliation or a later stage.

## 12. Method references

- Open Science Framework Projects / Components: https://help.osf.io/article/353-welcome-to-projects
- OSF preregistration guidance on timestamped plans and transparent updates: https://help.osf.io/article/626-simplifying-the-preregistration-process
- Cochrane Handbook, defining scope / eligibility / synthesis: https://training.cochrane.org/handbook/current/chapter-03
- Cochrane Handbook, searching / selection / documenting searches: https://training.cochrane.org/handbook/current/chapter-04
- PRISMA-S, reporting literature searches: https://www.prisma-statement.org/prisma-search
- W3C PROV overview / primer: https://www.w3.org/TR/prov-overview/ and https://www.w3.org/TR/prov-primer/
- RO-Crate 1.3 specification / provenance: https://www.researchobject.org/ro-crate/specification/1.3/introduction.html
- The Turing Way, Research Compendia: https://book.the-turing-way.org/reproducible-research/compendia/

## 13. Templates

- [STAGE_BRIEF_TEMPLATE.md](STAGE_BRIEF_TEMPLATE.md)
- [RESEARCH_PART_TEMPLATE.md](RESEARCH_PART_TEMPLATE.md)
- [STAGE_SYNTHESIS_TEMPLATE.md](STAGE_SYNTHESIS_TEMPLATE.md)

Copy templates into a stage directory and replace placeholders with actual research. The templates are scaffolding; they do not determine the number or subject of research parts.
