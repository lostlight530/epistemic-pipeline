# Frontier Research Stage Brief — TEMPLATE

> Copy this file into a stage directory as `STAGE_BRIEF.md`. Replace placeholders with actual research design. The template itself is not execution evidence.

## 0. Stage identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage ID:** `<A / B / ...>`
- **Canonical period:** `<YYYY-QN>`
- **Research window:** `<YYYY-MM-DD> through <YYYY-MM-DD>`
- **Record type:** `<RETROSPECTIVE | LIVE_STAGE>`
- **Coverage class:** `<SOURCE_BOUNDED | SEARCH_BOUNDED | METHODICALLY_SCOPED>`
- **Research started / reconstructed on:** `<YYYY-MM-DD>`
- **Research cutoff:** `<YYYY-MM-DD>`
- **Status:** `<PLANNED | IN_PROGRESS | READY_FOR_SYNTHESIS | COMPLETE>`

Do not claim exhaustive or systematic coverage unless the executed method actually supports that claim.

## 1. Why this stage exists

State why this three-month window deserves research. For retrospective work, state why the historical window is being reconstructed now and do not imply contemporaneous observation.

## 2. Repository lens

This repository examines external developments through: **claims, evidence, state transitions, provenance, uncertainty, verification, conflicts, transfer, evidence envelopes, and research-execution traceability.**

State any narrower stage-specific emphasis.

## 3. Core research questions

List the real questions for this stage. Questions should drive search, source selection, extraction, and synthesis.

1. `<question>`
2. `<question>`
3. `<question>`

Add, merge, or remove questions as the design develops, but record material changes in the amendment log below.

## 4. Scope and eligibility logic

Define what evidence can answer the stage questions before broad searching begins.

### Inclusion logic

- `<source / event / system / paper / standard is in scope when ...>`

### Exclusion logic

- `<exclude when ...>`

### Time and version rules

- `<publication/event dates, versions, revisions, release windows>`

### Source-authority rules

- `<what a vendor page can establish>`
- `<what a paper can establish>`
- `<what repository/runtime evidence can establish>`
- `<what requires independent corroboration>`

## 5. Planned search and discovery method

| Search ID | Surface / database / website | Query concepts or exact planned query | Date/window limits | Other limits | Purpose |
|---|---|---|---|---|---|
| `Q1` | `<surface>` | `<query>` | `<limits>` | `<language/type/etc.>` | `<question served>` |

Record targeted browsing, citation chaining, repository searches, standards lookups, status-page checks, or expert/source leads when used. Different evidence classes may require different search methods.

Searches may evolve as terminology changes or new source classes are discovered. Record material changes as amendments instead of replacing the original plan silently.

## 6. Planned research parts

| Part | Working title | Research question | Expected evidence classes | Status |
|---|---|---|---|---|
| `<A1>` | `<topic>` | `<question>` | `<papers / projects / standards / repositories / official records / ...>` | `PLANNED` |

A stage may have two parts or twenty. Define parts by subject, not by month. Do not create empty parts to satisfy a predetermined taxonomy.

## 7. Planned synthesis approach

State how completed parts may be compared and what must remain separate.

- `<which findings can be grouped>`
- `<which evidence classes must not be collapsed>`
- `<how source independence will be judged>`
- `<how conflicting findings will be retained>`
- `<what would count as a repository-relevant signal>`

## 8. Research provenance and responsibility

Record only observed/declared identity. Do not infer provider, model, researcher, or tool identity.

| Activity | Responsible person/agent when known | Tool/surface when known | Date | Output |
|---|---|---|---|---|
| `<stage design>` | `<identity or UNKNOWN>` | `<tool or UNKNOWN>` | `<date>` | `STAGE_BRIEF.md` |

## 9. Amendment / deviation log

| Date | Item changed | Previous plan | New plan | Reason | Effect on comparability / coverage |
|---|---|---|---|---|---|
| `<date>` | `<question/search/eligibility/synthesis>` | `<old>` | `<new>` | `<reason>` | `<effect>` |

If there are no amendments, state `NONE`. Do not delete earlier entries.

## 10. Known historical boundaries

Record repository creation boundaries, whether the repository did not yet exist, evidenced predecessor/influence status, archival gaps, and current facts that must not be projected backward.

## 11. Repository-specific hard boundaries

- `claim indexed != claim true`
- `evidence linked != evidence sufficient`
- `heuristic score != probability`
- `runtime-policy pass != truth`
- `claim verification != scientific adjudication`
- `claim transfer != acceptance`
- `provider identity != output validity`
- `provenance != truth`

Add stage-specific non-claims when needed.

## 12. Research-change rule

```text
external finding
→ bounded research interpretation
→ compare against current repository truth
→ confirmed current defect/drift?
      NO → research record only
      YES → separate repository repair process
```

## 13. Completion gate

The stage can move to synthesis when planned research questions have explicit outcomes; executed searches are logged; material selection/exclusion decisions can be explained; relevant counterevidence is captured; unresolved questions remain visible; source dates and authority classes are traceable; material amendments are recorded; and no part has been silently replaced by the expected narrative.

The stage synthesis is a separate research act, not an automatic concatenation.
