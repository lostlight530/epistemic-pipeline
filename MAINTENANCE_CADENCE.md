# Maintenance Cadence — epistemic-pipeline

**Status:** active maintenance contract  
**Calibrated:** 2026-08-30

This contract separates daily, weekly, and monthly maintenance for the research-execution and evidence layer

It is not a scheduler, not a scientific-review authority, and not a GitHub merge gate

## Cadence model

```text
daily
  local runtime / claim / evidence drift
        ↓
weekly
  cross-day evidence-stack reconciliation
        ↓
monthly or explicit phase-close
  canonical baseline / history inventory / deprecation review
```

## Daily

Daily maintenance should remain bounded to demonstrable drift

Required checks

- start from current `main`
- verify claim-verification, claim-transfer, Evidence Envelope, provider disclosure, trace/checkpoint/provenance names remain consistent
- preserve unknown provider/model/version values as unknown
- preserve heuristic score semantics as non-probability
- preserve conflicts during claim transfer
- keep `aggregate_score: null` on unsupported composite-quality surfaces
- incorporate new research only when it changes an actual evidence-contract decision
- create at most one final maintenance PR for the repository

Daily maintenance must not

- rewrite historical consolidation snapshots
- promote audit states into scientific verdicts
- convert coverage into provenance soundness
- add accepted/rejected labels without a real scientific-review authority
- add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates

## Weekly

Weekly maintenance includes daily checks plus cross-contract reconciliation

Required review

- code ↔ Manifest ↔ Research Contract ↔ Claim Audit Contract ↔ Claim Transfer Contract
- trace / checkpoint / provenance / claim audit / claim transfer / Evidence Envelope separation
- cross-repository profile names
- provider assertion basis and unknown-value handling
- score/interval semantics
- previous seven days of stage snapshots without rewriting history
- global-calibration freshness
- canonical SHA-256 baseline when the local scanner is used

Weekly questions

```text
Did a daily change collapse two evidence objects into one
Did a provider field become inferred rather than reported
Did a conflict disappear during transfer
Did a heuristic score get described as probability
Did a cross-repository handoff profile drift
Did an external paper become an unsupported capability claim
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest evidence-stack review

Required behavior

- build a month-to-date or explicit phase-close baseline
- inventory historical consolidation snapshots
- hash canonical contract/runtime files
- review integrated / experimental / proposed / not-integrated labels
- review stale-document candidates manually
- reconcile all merged changes from the month against the current evidence stack
- confirm no temporary runtime label became a scientific verdict
- state explicitly whether the month is closed or only month-to-date

On 2026-08-30 the August record is **month-to-date**, not final calendar-month close

Hard boundaries

```text
monthly review != scientific review
phase close != history rewrite
coverage inventory != provenance soundness
clean evidence stack != claim truth
```

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-30
```

Optional report file

```bash
python core/maintenance_cadence.py weekly --output maintenance/weekly-report.json
```

The scanner checks configured canonical paths, forbidden governance paths, decorative internal profile versions, Manifest calibration freshness, optional canonical hashes, and optional historical snapshots

It does not execute the research workflow, call an LLM, run tests, verify citations, judge evidence sufficiency, evaluate provenance soundness, or modify repository files

## History rule

Historical stage notes are evidence of earlier repository state

They are not automatically rewritten when later semantics improve

```text
historical snapshot != current contract
current contract != permission to erase earlier state
```

## External calibration

The cadence design is informed by long-horizon autonomous-research studies that report phase structure, persistent state, recoverable research segments, and regime-aware re-validation, together with current provenance work emphasizing re-openable records

These sources calibrate maintenance design only

They do not establish that daily, weekly, or monthly intervals are scientifically optimal

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != evidence sufficiency
monthly baseline != reproduction
coverage != provenance soundness
heuristic score != probability
provenance != truth
```
