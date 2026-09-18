# Frontier Research Stages

**Repository:** `lostlight530/epistemic-pipeline`  
**Status:** research guidance / non-normative support surface  
**Default horizon:** one three-month research stage  
**Effect on runtime or active contracts:** none unless a separate evidence-backed repository change is later justified

## Purpose

This directory supports longitudinal research into the external research-engineering landscape relevant to this repository.

Repository lens: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

A frontier stage is research, not scheduled report generation and not an automation target. A three-month window is one research stage. The stage may contain as many independent research parts as the evidence and research questions require, followed by an explicit stage-level synthesis.

**Do not split a stage into monthly sections merely because the window spans three months. Decomposition is by research subject, not by calendar month.**

## Stage model

```text
three-month stage
    ↓
stage brief / research design
    ↓
independent research parts chosen for this stage
    ↓
counterevidence, unresolved questions, source reconciliation
    ↓
repository-specific interpretation
    ↓
stage synthesis
```

A part is a research unit, not a template-filling task. Different stages may have different numbers of parts and different topics. Projects, papers, standards, runtimes, failures, provenance, reproducibility, scientific workflows, and other themes are examples only; the evidence determines the decomposition.

## Historical reconstruction vs live research

- **RETROSPECTIVE** — research reconstructed later for a historical three-month window.
- **LIVE_STAGE** — research conducted contemporaneously during or near the stage.
- **CORRECTION / RECONCILIATION** — later evidence that narrows or corrects an earlier stage without rewriting it.

```text
historical event date
!= reconstruction date
!= repository implementation date
!= evidence that this repository derived from that event
```

Historical reconstruction must never be written as though it was performed at the historical date.

## Stage identity

Prefer a human stage label plus an explicit canonical period and exact dates:

```text
Stage: A
Canonical period: 2024-Q1
Window: 2024-01-01 through 2024-03-31
Record type: RETROSPECTIVE
```

The stage letter is a human research label. The canonical period and exact dates remain the authoritative time identity.

## Recommended directory layout

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

## Research-part independence

Each part preserves its own research question, time boundary, source set, observations, counterevidence, unresolved facts, interpretation, repository relevance, and explicit non-claims. Parts may disagree or remain unresolved.

```text
part finding != whole-stage conclusion
whole-stage conclusion != rewrite of part evidence
synthesis != source evidence
```

## Source discipline

Prefer primary and authoritative sources when available. Record exact event/publication dates and versions where material. Separate vendor claims, papers, standards, repositories, status pages, benchmarks, independent reproductions, and secondary reporting by source type.

Do not infer provenance or intellectual lineage from similarity alone.

```text
historical similarity != lineage
earlier similar project != predecessor
parallel design != influence
later repository design != evidence of historical derivation
```

Unknown influence remains unknown.

## Repository authority boundary

Frontier-stage research is a calibration and research-memory surface. It does not outrank current repository truth. External research enters the repository-change path only when current repository evidence independently establishes a real defect, drift, or justified semantic transition.

A valid stage may end with:

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

## Repository-specific hard boundaries

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

These boundaries remain in force during historical comparison and frontier synthesis.

## Completion semantics

A stage is complete only when the stage brief fixes its time/evidence boundaries, the actually required research parts have explicit outcomes, material counterevidence and unresolved questions remain visible, repository relevance is assessed without converting similarity into provenance, and a stage synthesis is written from the completed parts.

Research outcomes may include `SUPPORTED_OBSERVATION`, `CONTESTED`, `INSUFFICIENT_EVIDENCE`, `UNKNOWN`, `NOT_APPLICABLE`, `NO_MATERIAL_FRONTIER_CHANGE`, `WATCH`, `CANDIDATE_REPOSITORY_RELEVANCE`, and `NO_CURRENT_REPOSITORY_DRIFT`. These are research outcomes, not runtime status codes.

## Templates

- [STAGE_BRIEF_TEMPLATE.md](STAGE_BRIEF_TEMPLATE.md)
- [RESEARCH_PART_TEMPLATE.md](RESEARCH_PART_TEMPLATE.md)
- [STAGE_SYNTHESIS_TEMPLATE.md](STAGE_SYNTHESIS_TEMPLATE.md)

Copy templates into a stage directory and replace the placeholders with actual research. The templates are scaffolding; they do not determine the number or subject of research parts.