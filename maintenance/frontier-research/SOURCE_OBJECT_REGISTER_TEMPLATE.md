# Source and Research-Object Register — TEMPLATE

> Instantiate as `SOURCE_OBJECT_REGISTER.md` when a Stage has shared sources, multiple reports per object, mutable technical objects, or identity/version ambiguity. This is a research evidence registry, not a citation-count log.

## 0. Register identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `<Stage>`
- **Specification version:** `2026-09-19-first-batch`
- **Register date:** `<date>`
- **Source cutoff:** `<date>`

## 1. Identity rules

Define what counts as a research object/event and how versions are treated.

```text
object != report
source != object unless explicitly dual-role
multiple sources may describe one object
one source may describe multiple objects
same-origin restatement != independent source family
```

## 2. Research-object register

| Object ID | Canonical name | Object type | Version/revision | Event/start date | End/supersession date | Identity basis | Notes |
|---|---|---|---|---|---|---|---|
| `O1` | `<name>` | `<system / release / standard / method / paper-event / incident / practice / ...>` | `<version>` | `<date>` | `<date/none>` | `<basis>` | `<notes>` |

## 3. Evidence-source register

| Source ID | Title/name | Source type | Origin/source family | URL/DOI/revision | Publication/update date | Access/search date | Authority | Archive/status | Limitations |
|---|---|---|---|---|---|---|---|---|---|
| `S1` | `<title>` | `<paper/spec/repository/vendor/status/benchmark/secondary/...>` | `<family>` | `<identifier>` | `<date>` | `<date>` | `<bounded authority>` | `<live/archived/retracted/corrected/...>` | `<limits>` |

## 4. Source-to-object mapping

| Object ID | Source ID | Relation | Directness | Independence note |
|---|---|---|---|---|
| `O1` | `S1` | `<defines / announces / implements / evaluates / reproduces / critiques / reports / corrects>` | `<direct / indirect>` | `<independent / same-origin / unknown>` |

## 5. Source-family / independence map

Group sources that ultimately originate from the same evidence-producing actor or dataset when material.

| Family ID | Members | Common origin | Independence limitation |
|---|---|---|---|
| `SF1` | `S1,S3` | `<origin>` | `<why not independent>` |

## 6. Corrections, retractions, supersession

| Source/Object | Change type | Date | Replacement/correction | Research effect |
|---|---|---|---|---|
| `<ID>` | `<corrected/retracted/superseded/versioned>` | `<date>` | `<ID/ref>` | `<effect>` |

## 7. Identity conflicts

Record unresolved naming/version/date/provenance conflicts rather than forcing one canonical answer.

| Conflict | Competing evidence | Current treatment | What would resolve it |
|---|---|---|---|
| `<conflict>` | `<refs>` | `<UNKNOWN / bounded choice>` | `<needed evidence>` |

## 8. Register limitations

State what this register does not cover and whether candidate discovery was exhaustive, bounded, or opportunistic.
