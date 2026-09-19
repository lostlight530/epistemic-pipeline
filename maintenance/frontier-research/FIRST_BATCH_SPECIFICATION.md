# First-Batch Frontier Research Documentation Specification

**Repository:** `lostlight530/epistemic-pipeline`  
**Specification version:** `2026-09-19-first-batch`  
**Status:** active research-documentation specification / non-normative to repository runtime  
**Applies to:** `maintenance/frontier-research/` and instantiated frontier-research stages

## 1. Purpose

This specification defines the first complete document family for longitudinal frontier research in this repository. It governs how research is framed, decomposed, evidenced, synthesized, reviewed, corrected, and carried across time.

It does not define repository runtime behavior, scientific truth, scheduler behavior, or capability state.

## 2. Research principle

A three-month Stage is a research project unit. It is **not** three monthly reports joined together.

```text
Stage
= one bounded research window
+ one research design
+ multiple research parts as justified
+ explicit evidence discrimination
+ whole-stage synthesis
+ review
+ durable longitudinal placement
```

The number of research parts is not fixed. The subject matter determines the structure. A Stage with two deep parts may be valid; a Stage with fifteen parts may also be valid.

Do not reduce research structure for token efficiency, file-count minimization, or stylistic neatness.

## 3. Research ontology

### Stage

A time-bounded research project, normally three months, with a declared research design and closure boundary.

### Research Part

An independently inspectable research question or tightly bounded sub-study within a Stage. Parts may use different source classes or analytic methods.

### Research Object / Event

The thing being studied: for example a project, system, model release, standard version, method, paper as an intellectual event, benchmark, incident, policy change, or research practice.

### Evidence Source

A source that supports, contradicts, contextualizes, or reports a research object/event or finding: paper, specification, repository revision, official announcement, status record, benchmark, dataset, independent reproduction, or secondary report.

```text
research object != report about the object
multiple reports of one object != multiple objects
multiple same-origin reports != independent corroboration
```

### Finding

A bounded analytical statement derived from identified evidence, with temporal scope and source authority attached.

### Synthesis

An interpretive research product that integrates findings while preserving material disagreement, source dependence, and unknowns.

### Correction / Reconciliation

A later research artifact that changes interpretation forward without rewriting the historical record.

### Handoff

A bounded export of findings for cross-repository or project-level synthesis. A handoff transfers context, not authority.

### Review

An explicit assessment of method, evidence, temporal integrity, synthesis discipline, and repository-boundary compliance. Review independence must itself be stated rather than assumed.

## 4. Research design classes

A Stage or Part may use one or more declared design classes:

- `HISTORICAL_FRONTIER_RECONSTRUCTION` — reconstruct a past research-engineering landscape after the fact.
- `LIVE_FRONTIER_RESEARCH` — study a current window contemporaneously.
- `LANDSCAPE_MAPPING` — identify and structure a field, ecosystem, methods, systems, standards, and gaps.
- `SCOPING_STYLE_EVIDENCE_MAPPING` — borrow scoping-review discipline for breadth, eligibility, charting, and synthesis without claiming formal PRISMA-ScR/JBI compliance.
- `TARGETED_EVIDENCE_SYNTHESIS` — answer a narrower question using explicit evidence-selection and synthesis rules.
- `COMPARATIVE_TECHNICAL_STUDY` — compare systems, methods, standards, or evidence regimes on declared dimensions.
- `MIXED` — combine multiple declared designs where the research problem requires it.

Design labels describe the executed method; they are not prestige labels.

## 5. Coverage classes

Every Stage and Part must state what kind of coverage was actually achieved:

- `SOURCE_BOUNDED` — analysis is bounded to named sources or source families.
- `SEARCH_BOUNDED` — named searches/discovery procedures were executed, but exhaustiveness is not claimed.
- `METHODICALLY_SCOPED` — explicit eligibility, source coverage, selection, extraction/charting, and synthesis methods were executed over a declared scope.
- `EXHAUSTIVE_WITHIN_DECLARED_SOURCES` — exhaustive only within explicitly named sources/interfaces and only when that completeness was actually established.

`SYSTEMATIC` or `COMPREHENSIVE` must not be used as generic adjectives when the method does not justify them.

## 6. Required first-batch artifact relationships

### For every Stage

Required:

1. `STAGE_BRIEF.md` — research design before or at the start of the Stage/reconstruction.
2. One or more substantive Part files instantiated from `RESEARCH_PART_TEMPLATE.md`.
3. `STAGE_SYNTHESIS.md` — written only after the substantive Parts are sufficiently complete.
4. `RESEARCH_REVIEW.md` — review of the Stage research before declaring `FRONTIER_STAGE_COMPLETE`. Independent review is preferred; when independence is not established, say so.
5. Research responsibility/provenance information. It may be embedded in the Stage/Parts or instantiated as `CONTRIBUTOR_STATEMENT.md`; when multiple material contributors/agents are involved, the separate contributor statement is preferred.

Conditional but first-class:

- `SOURCE_OBJECT_REGISTER.md` when objects have multiple reports/sources, multiple Parts share evidence, or identity/version disambiguation matters.
- `EVIDENCE_CHART.md` when structured cross-source extraction or comparison materially supports the synthesis.
- `STAGE_HANDOFF.md` when Stage findings are exported to L3/cross-repository synthesis.
- correction/reconciliation records when later evidence materially changes an earlier interpretation.

### Across multiple Stages

- `LONGITUDINAL_INDEX.md` routes across Stage records and corrections. It does not contain the research conclusion.
- `LONGITUDINAL_SYNTHESIS_<range>.md` performs actual cross-Stage research when at least two sufficiently comparable Stages exist.

## 7. Suggested instantiated directory

```text
maintenance/frontier-research/
├── LONGITUDINAL_INDEX.md
├── longitudinal/
│   └── LONGITUDINAL_SYNTHESIS_<range>.md
├── corrections/
│   └── CORRECTION_<date>_<subject>.md
└── stage-a-2024-q1/
    ├── STAGE_BRIEF.md
    ├── A1_<topic>.md
    ├── A2_<topic>.md
    ├── ...
    ├── SOURCE_OBJECT_REGISTER.md        # when needed
    ├── EVIDENCE_CHART.md                # when needed
    ├── CONTRIBUTOR_STATEMENT.md         # preferred for multi-contributor research
    ├── RESEARCH_REVIEW.md
    ├── STAGE_SYNTHESIS.md
    └── STAGE_HANDOFF.md                 # when exported cross-repository
```

Do not create empty artifacts merely to mimic this tree.

## 8. Research workflow

```text
question / rationale
        ↓
Stage Brief / protocol
        ↓
source discovery + object identification + eligibility/selection
        ↓
independent Research Parts
        ↓
evidence charting / appraisal when justified
        ↓
counterevidence + negative space + unresolved questions
        ↓
Stage Synthesis
        ↓
Research Review
        ↓
Stage close
        ↓
Longitudinal placement / bounded handoff
        ↓
later correction or next Stage when new evidence warrants it
```

Research may iterate. Material changes to questions, eligibility, source coverage, extraction, or synthesis method are recorded as amendments/deviations; they are not silently normalized after the result is known.

## 9. Source and object discipline

Each source receives a stable local ID within the Stage or Part. Each research object/event receives a separate ID when identity matters.

Record exact version/revision/date for mutable technical objects when available. Distinguish event date, publication date, search/access date, and reconstruction date.

Primary sources establish only what they are authoritative for. Vendor statements establish vendor-described state; repositories establish revision-bounded implementation/source state; standards establish their own normative text; independent reproductions establish only what they actually reproduced.

Do not count duplicated reports, mirrors, syndicated reporting, or same-provider restatements as independent corroboration.

## 10. Evidence charting and appraisal

Before structured charting, declare the variables/dimensions that matter to the research question. Add new dimensions only with an amendment when the change is material.

Critical appraisal is method-dependent. Do not invent a universal numeric quality score. When appraisal is performed, state the criteria and how appraisal affects inclusion or synthesis.

```text
metadata completeness != evidence quality
source prestige != correctness
provider identity != output validity
structured extraction != adjudication
```

## 11. Synthesis discipline

Synthesis must preserve:

- source-family dependence;
- contradictions and unresolved interpretations;
- negative evidence and meaningful absences;
- temporal boundaries;
- differences between capability claims, observed implementation, execution evidence, and independent validation;
- method comparability across Parts or Stages.

Do not force consensus. `CONTESTED`, `INSUFFICIENT_EVIDENCE`, `NOT_COMPARABLE`, and `UNKNOWN` are valid research outcomes.

## 12. Contributor and tool provenance

Responsibility, contribution, and instrumentation are distinct.

- Contributor roles describe who was responsible for conceptualization, methodology, investigation, curation, analysis, validation, synthesis/writing, review, or supervision.
- CRediT terminology may be used descriptively where appropriate, especially for human scholarly contribution, but this specification does not use CRediT roles to determine authorship.
- Software, models, search engines, browsers, agents, and scripts used as instruments are recorded as tool/instrument provenance.
- If an AI agent materially performs a research activity, record the observed agent/tool identity and the responsible human/governance context where known. Do not infer hidden provider/model identity.

```text
responsibility != tool invocation
tool invocation != authorship
agent execution != research validity
```

## 13. Review discipline

Stage review should assess at minimum: research-question alignment, method execution, search/source coverage claims, selection logic, object/source identity, source-family independence, temporal integrity, evidence-to-finding traceability, counterevidence handling, synthesis overreach, and repository-boundary compliance.

Reviewer independence is evidence, not an assumption. Use `INDEPENDENT_REVIEW`, `PARTIALLY_INDEPENDENT`, `SAME_PRODUCER_REVIEW`, or `INDEPENDENCE_NOT_ESTABLISHED`.

## 14. Longitudinal discipline

An index is routing. A longitudinal synthesis is research.

```text
index != synthesis
later synthesis != rewrite of earlier Stage
method drift != comparable evidence
later knowledge != historical knowledge
```

Cross-Stage comparison must state when methods/source coverage are not comparable. Later evidence may change interpretation through a new correction/reconciliation or longitudinal synthesis, while the original Stage record remains recoverable.

## 15. Correction and reconciliation

Substantive historical corrections are additive. A correction record identifies the original statement, trigger, new evidence, correction class, revised interpretation, affected syntheses, and current-repository implication.

Correction classes may include `FACTUAL_CORRECTION`, `SOURCE_IDENTITY_CORRECTION`, `TEMPORAL_CORRECTION`, `NARROWING`, `EXPANSION`, `METHOD_RECONCILIATION`, `CONTRADICTION_DISCOVERED`, or `LATER_VALIDATION`.

## 16. Cross-repository handoff

A handoff may export a bounded finding from this repository's research lens to L3/project synthesis. It must state what is being transferred, the evidence boundary, unresolved issues, and prohibited inferences.

```text
handoff != authority transfer
semantic relevance != shared truth state
cross-repository synthesis != source-repository override
```

## 17. Repository authority boundary

Frontier research does not outrank current repository truth. A Stage may identify a candidate gap, but implementation or contract change requires a separate current-state audit and the repository's normal repair/governance process.

If no current defect is independently established, a valid conclusion is:

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

## 18. Repository-specific hard boundaries

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

## 19. First-batch external basis

This specification is method-calibrated against OSF modular projects and transparent updates; Cochrane search/selection/update guidance; PRISMA-Search reporting discipline; PRISMA-ScR/JBI scoping-review structure and charting; W3C PROV; RO-Crate 1.3 provenance; CRediT contributor roles; and The Turing Way research-compendium practice. These sources inform the research architecture but do not certify this repository as conformant to those frameworks.

## 20. Specification evolution

Future revisions may add or refine templates. Historical Stages retain the method version actually used. New template versions must not silently project new fields, terminology, or methodological claims backward into prior research.
