# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-08-31  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the research-execution and evidence layer

It is not a scheduler, scientific-review authority, or GitHub merge gate

## Cadence model

```text
daily
  local runtime / claim / evidence drift
        ↓
weekly
  cross-day evidence-stack and document-authority reconciliation
        ↓
monthly or explicit phase-close
  calendar baseline / complete evidence-document inventory / deprecation review
```

## Daily

Daily maintenance remains bounded to demonstrated drift

Required checks

- start from current `main`
- use `DOCUMENT_STATUS.md` to identify current authoritative documentation
- verify claim-verification, claim-transfer, Evidence Envelope, provider disclosure, trace/checkpoint/provenance names remain consistent
- preserve unknown provider/model/version values as unknown
- preserve heuristic score semantics as non-probability
- preserve conflicts during claim transfer
- keep unsupported composite quality scores absent or null
- incorporate new research only when it changes a real evidence-contract decision
- create at most one final maintenance PR for the repository

Daily maintenance must not

- rewrite historical consolidation snapshots
- promote audit states into scientific verdicts
- convert coverage into provenance soundness
- add accepted/rejected labels without scientific-review authority
- add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates

## Weekly

Weekly maintenance includes daily checks plus complete current-evidence reconciliation

Required review

- implementation ↔ Manifest ↔ Research Contract ↔ Claim Audit Contract ↔ Claim Transfer Contract
- README / Architecture / Contributor / Customization / Examples consistency
- `DOCUMENT_STATUS.md` against files actually present
- trace / checkpoint / provenance / claim audit / claim transfer / Evidence Envelope separation
- cross-repository profile names
- provider assertion basis and unknown-value handling
- score/interval semantics
- previous seven days of historical snapshots without rewriting them
- frontier calibration freshness
- canonical SHA-256 baseline when the local scanner is used

Weekly questions

```text
Did a daily change collapse two evidence objects into one
Did a provider field become inferred rather than reported
Did a conflict disappear during transfer
Did a heuristic score get described as probability
Did a historical snapshot get treated as current authority
Did a cross-repository handoff profile drift
Did an external paper become an unsupported capability claim
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest evidence-stack review

Required behavior

- determine actual calendar status from the date
- use `month-to-date` before the final day and `calendar-month-close` on the final day
- inventory all historical snapshots
- hash configured canonical evidence-contract and documentation files
- reconcile every current authoritative document in `DOCUMENT_STATUS.md`
- review integrated / experimental / proposed / not-integrated labels
- review stale-document candidates manually
- reconcile all merged changes from the calendar month against the current evidence stack
- confirm no structural state has been renamed into a scientific verdict
- record whether an explicit research phase is active or closed

For the current stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Hard boundaries

```text
monthly review != scientific review
phase close != history rewrite
coverage inventory != provenance soundness
clean evidence stack != claim truth
calendar close != reproduction
```

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional close report

```bash
python core/maintenance_cadence.py monthly --as-of 2026-08-31 --output maintenance/august-close.json
```

The scanner reports configured canonical paths, forbidden governance paths, decorative internal profile versions, Manifest calibration freshness, optional canonical hashes, historical snapshots, calendar-month status, and configured stage status

It does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, or modify repository files

## First complete Daily / Weekly / Monthly demonstration

The first complete three-horizon worked example is

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

Recommended read order

```text
MAINTENANCE_CADENCE.md
        ↓ normative horizon semantics
DOCUMENT_STATUS.md
        ↓ current vs historical authority
STAGE_2026_08_MAINTENANCE.md
        ↓ closed evidence-infrastructure stage
FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
        ↓ worked commands and evidence-layer interpretation
```

The dated demonstration does not invent a clean run, findings, or SHA-256 values that require execution

```text
reference demonstration != provenance soundness
worked example != evidence sufficiency
```

## Document authority and history

`DOCUMENT_STATUS.md` is the current map of authoritative, historical, example/customization, and external-metadata documents

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` remain time-scoped snapshots rather than current contracts

```text
historical snapshot != current contract
current contract != permission to erase earlier state
```

## External calibration

The cadence design is informed by long-horizon research studies reporting phase structure, persistent state, recoverable research segments, regime-aware re-validation, and process-level evaluation beyond final scores, together with provenance work emphasizing re-openable records

These sources calibrate maintenance design only

They do not establish that daily, weekly, or monthly intervals are scientifically optimal

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
calendar-month close != reproduction
coverage != provenance soundness
heuristic score != probability
provenance != truth
```
