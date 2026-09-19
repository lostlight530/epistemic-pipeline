# Frontier Research Documentation

**Repository:** `lostlight530/epistemic-pipeline`  
**Research layer:** longitudinal frontier research / non-normative to runtime  
**First-batch specification:** 2026-09-19  
**Default stage horizon:** one three-month research stage  
**Primary specification:** [FIRST_BATCH_SPECIFICATION.md](FIRST_BATCH_SPECIFICATION.md)

## Research, not a maintenance log

This directory contains research artifacts. Its purpose is to formulate questions, collect and discriminate evidence, preserve counterevidence, analyse change, synthesize findings, and support longitudinal interpretation.

The directory lives under `maintenance/` because frontier research must remain governable, dated, reviewable, and recoverable alongside repository maintenance. That location does **not** turn the contents into activity logs.

```text
research artifact != activity log
search record != research conclusion
source register != source-count metric
stage index != stage synthesis
stage close != final truth
```

No template has a target word count. Do not simplify a research structure merely to reduce tokens, file size, or review effort. Omit a section only when it is genuinely not applicable and state why.

## Repository research lens

This repository studies external research-engineering developments through: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

## First-batch document family

- [STAGE_BRIEF_TEMPLATE.md](STAGE_BRIEF_TEMPLATE.md) — research protocol / study design for a three-month stage
- [RESEARCH_PART_TEMPLATE.md](RESEARCH_PART_TEMPLATE.md) — one independently inspectable research question or bounded sub-study
- [SOURCE_OBJECT_REGISTER_TEMPLATE.md](SOURCE_OBJECT_REGISTER_TEMPLATE.md) — distinguishes research objects/events from the sources that report them
- [EVIDENCE_CHART_TEMPLATE.md](EVIDENCE_CHART_TEMPLATE.md) — structured extraction/charting across selected evidence
- [STAGE_SYNTHESIS_TEMPLATE.md](STAGE_SYNTHESIS_TEMPLATE.md) — whole-stage interpretation built from completed research parts
- [LONGITUDINAL_INDEX_TEMPLATE.md](LONGITUDINAL_INDEX_TEMPLATE.md) — chronology and routing across stages; not a research conclusion
- [LONGITUDINAL_SYNTHESIS_TEMPLATE.md](LONGITUDINAL_SYNTHESIS_TEMPLATE.md) — research across multiple stages
- [CORRECTION_RECONCILIATION_TEMPLATE.md](CORRECTION_RECONCILIATION_TEMPLATE.md) — forward correction without silent history rewrite
- [STAGE_HANDOFF_TEMPLATE.md](STAGE_HANDOFF_TEMPLATE.md) — bounded export to cross-repository/L3 synthesis without authority transfer
- [CONTRIBUTOR_STATEMENT_TEMPLATE.md](CONTRIBUTOR_STATEMENT_TEMPLATE.md) — research responsibility and contribution attribution separated from tool provenance
- [RESEARCH_REVIEW_TEMPLATE.md](RESEARCH_REVIEW_TEMPLATE.md) — method/evidence/synthesis review, including reviewer-independence status

## External method calibration

The first-batch specification was calibrated on 2026-09-19 against current public research-method guidance. These are informative precedents, not compliance claims:

- OSF Projects / Components — modular research organization and separately configurable components: https://help.osf.io/article/353-welcome-to-projects
- OSF preregistration/update guidance — timestamped plans and transparent later updates: https://help.osf.io/article/626-simplifying-the-preregistration-process and https://help.osf.io/article/330-welcome-to-registrations
- Cochrane Handbook Chapter 4 — planned searching, documented searches, source selection, and distinction between a study and multiple reports: https://training.cochrane.org/handbook/current/chapter-04
- PRISMA-ScR — explicit objectives, eligibility, sources, charting methods, results, limitations, and conclusions for scoping reviews: https://www.prisma-statement.org/scoping
- JBI Manual for Evidence Synthesis, Scoping Reviews — protocol, aligned questions/eligibility, searching, selection, extraction/charting, analysis, presentation, and summary: https://jbi-global-wiki.refined.site/space/MANUAL/355862497/10.%2BScoping%2Breviews%C2%A0
- W3C PROV — provenance as relations among entities, activities, and responsible agents: https://www.w3.org/TR/prov-overview/ and https://www.w3.org/TR/prov-primer/
- RO-Crate 1.3 — research-object metadata and provenance for creation/update actions: https://www.researchobject.org/ro-crate/specification/1.3/
- CRediT — contributor-role transparency; roles are contribution descriptors, not authorship rules: https://credit.niso.org/
- The Turing Way Research Compendia — keeping digital research parts together while separating methods/data/output and preserving a clear research structure: https://book.the-turing-way.org/reproducible-research/compendia/
- Cochrane living-review guidance — update frequency, update triggers, and method-review decisions should be explicit when a research product is maintained over time: https://www.cochrane.org/learn/courses-and-resources/interactive-learning/module-14-conducting-living-systematic-reviews

### Explicit non-claims

```text
three-month stage != external standard
this research family != PRISMA compliance
this research family != JBI scoping-review compliance
this research family != Cochrane systematic review
web search != exhaustive literature search
structured documentation != scientific validity
source count != evidence quality
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

These remain in force in every retrospective, live, longitudinal, correction, handoff, and review artifact.

## Versioning rule

Every instantiated stage records the specification/template version it used. Later template improvements do not retroactively change the method used by an earlier stage. Substantive historical corrections are additive and use correction/reconciliation records.

See [FIRST_BATCH_SPECIFICATION.md](FIRST_BATCH_SPECIFICATION.md) for the complete artifact relationships, completion rules, and authority boundaries.
