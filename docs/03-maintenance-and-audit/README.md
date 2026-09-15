# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected at a given time, what was concluded, and what historical evidence must remain reviewable?**

It does **not** define the repository's scientific or runtime semantics merely because a record is newer than an active contract.

## Current maintenance / governance surfaces

- [`DOCUMENT_STATUS.md`](DOCUMENT_STATUS.md) — current document-governance router and subject-scoped authority classifier
- [`MAINTENANCE_CADENCE.md`](MAINTENANCE_CADENCE.md) — human-readable repository-maintenance contract
- root `maintenance/cadence.yaml` — machine-readable local maintenance/scanner configuration; classified here by function
- [`independent-gpt/README.md`](independent-gpt/README.md) — current public cold-start recovery kernel for a memoryless independent reviewer; it does not override subject-scoped authority

`core/maintenance_cadence.py` remains **Class 01 source** because it is executable implementation. Its presence or a successful local scan is not the same thing as an external governance patrol, GitHub-state audit, scientific validation, or a preserved historical run.

## Coordinated research-infrastructure context

This repository participates in a coordinated research-infrastructure set with:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination allows shared inspection windows and cross-repository checks for profile names, contract names, and handoff vocabulary. It does **not** create cross-repository authority. Each repository recovers from and is governed by its own current `main`, implementation, machine-readable contracts/configuration, active subject contracts, current document router, maintenance evidence, and preserved history.

A generic historical authority ordering is not a permanent repository law. When older maintenance or correction prose conflicts with the current subject-scoped recovery order in `DOCUMENT_STATUS.md`, the current subject-scoped order governs present interpretation.

Periodic maintenance is an opportunity to inspect current truth, not a requirement to manufacture changes. `NO_CHANGE_REQUIRED` is a valid outcome. Weekly or monthly synthesis is justified by the current contract, a natural calendar/phase boundary, accumulated evidence, demonstrated drift, or another explicit maintenance need rather than by schedule alone.

## Dated maintenance / calibration evidence

- root `maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md`
- root `maintenance/POST_STAGE_REPAIR_2026_09_01.md`
- root `maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md`
- root `maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md`
- root `maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md`

The 2026-08-24 through 2026-08-31 research stage remains closed historical evidence. The 2026-09-01 post-stage repair is the dated starting checkpoint for steady-state maintenance, while current merged `main` may supersede that checkpoint through explicit current evidence or reconciliation.

These records are point-in-time evidence. A later dated record may report a newer observation, correction, or maintenance result, but it does not silently override current implementation, machine contracts, or active scientific/specialized contracts.

## Stage / historical evidence

- [`history/STAGE_2026_08_MAINTENANCE.md`](history/STAGE_2026_08_MAINTENANCE.md)
- [`history/FRONTIER_ALIGNMENT.md`](history/FRONTIER_ALIGNMENT.md)
- [`history/FOUR_DAY_CONSOLIDATION.md`](history/FOUR_DAY_CONSOLIDATION.md)
- [`history/FIVE_DAY_CONSOLIDATION.md`](history/FIVE_DAY_CONSOLIDATION.md)
- [`history/SIX_DAY_CONSOLIDATION.md`](history/SIX_DAY_CONSOLIDATION.md)
- [`history/JULES_CORRECTION_RECORD.md`](history/JULES_CORRECTION_RECORD.md) — dated correction/authority evidence retained at its original calibration boundary, not a current top-level authority
- `history/superpowers/` — superseded/historical implementation design and planning evidence

Historical records remain reviewable at their original time boundary. Physical reclassification does not rewrite their claims.

## Interpretation rules

```text
maintenance record != current implementation semantics
latest date != highest semantic authority
scanner source != scanner execution
file presence != runtime evidence
local scan != scientific validation
later success != earlier success
correction != history rewrite
historical snapshot != invalid evidence
NO_CHANGE_REQUIRED != missing inspection
```

When current state conflicts with a dated record, preserve the dated record and correct forward in current governance or a later correction/reconciliation record.
