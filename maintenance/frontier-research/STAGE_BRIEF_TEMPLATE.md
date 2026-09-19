# Frontier Research Stage Brief — TEMPLATE

> Instantiate as `STAGE_BRIEF.md`. This is a research protocol/study-design artifact, not an activity log.

## 0. Identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Specification version:** `2026-09-19-first-batch`
- **Stage ID:** `<A / B / ...>`
- **Canonical period:** `<YYYY-QN>`
- **Research window:** `<YYYY-MM-DD> through <YYYY-MM-DD>`
- **Record type:** `<RETROSPECTIVE | LIVE_STAGE>`
- **Research design class(es):** `<HISTORICAL_FRONTIER_RECONSTRUCTION | LIVE_FRONTIER_RESEARCH | LANDSCAPE_MAPPING | SCOPING_STYLE_EVIDENCE_MAPPING | TARGETED_EVIDENCE_SYNTHESIS | COMPARATIVE_TECHNICAL_STUDY | MIXED>`
- **Coverage class intended:** `<SOURCE_BOUNDED | SEARCH_BOUNDED | METHODICALLY_SCOPED | EXHAUSTIVE_WITHIN_DECLARED_SOURCES>`
- **Protocol/reconstruction date:** `<date>`
- **Research cutoff:** `<date>`
- **Status:** `<PLANNED | IN_PROGRESS | READY_FOR_SYNTHESIS | COMPLETE>`

## 1. Rationale

Explain why this three-month window deserves research and what is not adequately answered by existing Stage or repository records. For retrospective work, explain why reconstruction is being undertaken now.

## 2. Repository lens and non-claims

Repository lens: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

State any narrower Stage-specific lens and explicit non-claims.

Repository hard boundaries:

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

## 3. Objectives and research questions

State the overall objective, then the actual research questions. Questions drive discovery, selection, extraction/charting, analysis, and synthesis.

### Objective

`<objective>`

### Research questions

1. `<question>`
2. `<question>`
3. `<question>`

## 4. Conceptual scope

Define the concepts, technologies, practices, evidence forms, institutions, communities, and technical boundaries relevant to this Stage.

State important adjacent topics that are intentionally excluded so that absence from the research is not mistaken for a negative finding.

## 5. Temporal scope

Distinguish:

- event/implementation dates that fall inside the Stage;
- publication dates for sources;
- later sources used retrospectively to reconstruct earlier events;
- repository creation date when relevant;
- research/reconstruction date;
- source-access/search date.

## 6. Eligibility and selection logic

### Inclusion criteria

- `<criterion>`

### Exclusion criteria

- `<criterion>`

### Hold / unresolved criteria

- `<conditions that prevent immediate inclusion/exclusion>`

State how multiple reports of one research object/event will be grouped.

## 7. Source classes and authority plan

| Source class | Intended use | What it can establish | What it cannot establish |
|---|---|---|---|
| `<official specification>` | `<use>` | `<authority>` | `<limit>` |
| `<paper>` | `<use>` | `<authority>` | `<limit>` |
| `<repository revision>` | `<use>` | `<authority>` | `<limit>` |
| `<secondary report>` | `<use>` | `<authority>` | `<limit>` |

## 8. Discovery and search design

Document planned searches/discovery methods. Use different strategies for different evidence classes where necessary.

| Search/Discovery ID | Surface | Planned query/navigation method | Date/version limits | Language/type limits | Research question served |
|---|---|---|---|---|---|
| `Q1` | `<surface>` | `<query/navigation>` | `<limits>` | `<limits>` | `<RQ>` |

Include citation chaining, repository history inspection, standards-version navigation, direct known-source retrieval, status/archive checks, or expert/source leads when part of the design.

## 9. Research-object model

State what counts as a distinct object/event for this Stage and how versions/releases/updates are separated or grouped.

```text
source != research object
multiple reports != multiple independent objects
version change may or may not constitute a new object; define the rule
```

## 10. Planned research Parts

| Part ID | Working title | Research question | Method/design | Expected evidence | Dependencies |
|---|---|---|---|---|---|
| `<A1>` | `<title>` | `<question>` | `<design>` | `<sources>` | `<none / other Part>` |

Part count is evidence-driven. Do not create placeholder Parts to satisfy a fixed taxonomy.

## 11. Planned extraction / evidence charting

List the variables/dimensions that will be extracted when structured charting is useful.

- `<object identity/version>`
- `<event/publication date>`
- `<capability/method claim>`
- `<implementation or execution evidence>`
- `<source authority>`
- `<independence/source family>`
- `<counterevidence>`
- `<uncertainty/unknowns>`
- `<repository relevance>`

Remove or add variables based on the actual research question. Material additions after research begins belong in the amendment record.

## 12. Critical appraisal plan

State whether formal or structured appraisal will be performed. If yes, define criteria before applying them and state how appraisal affects interpretation or inclusion.

`<NONE / descriptive source-authority appraisal / domain-specific appraisal / other>`

Do not invent a universal numeric quality score.

## 13. Analysis and synthesis plan

Describe how findings will be analysed: chronological analysis, thematic analysis, technical comparison, standards mapping, evidence-maturity analysis, source-family triangulation, negative-space analysis, or other declared method.

State how contradictions and non-comparability will be handled.

## 14. Longitudinal comparability plan

If previous/future Stages are expected to be compared, identify the dimensions that should remain stable enough for comparison and the dimensions allowed to evolve.

## 15. Review plan

- **Research review required before Stage close:** `YES`
- **Desired reviewer independence:** `<INDEPENDENT_REVIEW preferred / other>`
- **Search-method review needed:** `<YES / NO / CONDITIONAL>`
- **Domain specialist review needed:** `<YES / NO / CONDITIONAL>`
- **What must be reviewed:** `<method / source identity / extraction / synthesis / boundary>`

## 16. Contributor responsibility and instrument provenance plan

Identify known responsible contributors/roles separately from software, models, search engines, scripts, and agents used as instruments.

Do not infer hidden model/provider identity.

## 17. Amendment / deviation record

| Date | Affected design element | Original plan | Revised plan | Reason | Effect on coverage/comparability |
|---|---|---|---|---|---|
| `<date>` | `<element>` | `<old>` | `<new>` | `<reason>` | `<effect>` |

Use `NONE` until a material amendment occurs. Preserve prior entries.

## 18. Completion and stopping criteria

Define what must be true before the Stage can be synthesized and closed. Include treatment of unresolved questions and inaccessible evidence.

Stage completion does not require certainty; it requires completion of the declared research process and honest reporting of remaining uncertainty.

## 19. Update / correction triggers

State what later evidence would justify a new correction/reconciliation record, longitudinal reinterpretation, or targeted follow-up.

## 20. Expected outputs

- `STAGE_BRIEF.md`
- substantive Part files
- `SOURCE_OBJECT_REGISTER.md` when identity/source sharing justifies it
- `EVIDENCE_CHART.md` when structured charting supports synthesis
- `CONTRIBUTOR_STATEMENT.md` for multi-contributor research when appropriate
- `STAGE_SYNTHESIS.md`
- `RESEARCH_REVIEW.md`
- `STAGE_HANDOFF.md` if exported to cross-repository synthesis

## 21. Protocol limitations

State expected blind spots: inaccessible databases, language limits, mutable search ranking, archival gaps, vendor-only evidence, missing historical revisions, or other constraints.
