# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected at a given time, what was concluded, and what historical evidence must remain reviewable?**

It does **not** define the repository's scientific or runtime semantics merely because a record is newer than an active contract.

## Current maintenance / governance surfaces

- `DOCUMENT_STATUS.md` — current document-governance router and authority classifier
- `MAINTENANCE_CADENCE.md` — human-readable repository-maintenance contract
- `maintenance/cadence.yaml` — machine-readable local maintenance/scanner configuration; classified here by function
- `JULES_CORRECTION_RECORD.md` — boundary for reusing historical coding-agent / PR narratives as evidence

`core/maintenance_cadence.py` remains **Class 01 source** because it is executable implementation. Its presence or a successful local scan is not the same thing as an external governance patrol, GitHub-state audit, scientific validation, or a preserved historical run.

## Dated maintenance / calibration evidence

- `maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md`
- `POST_STAGE_REPAIR_2026_09_01.md`
- `maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md`
- `maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md`
- `maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md`

These are point-in-time evidence. A later dated record may report a newer observation, correction, or maintenance result, but it does not silently override current implementation, machine contracts, or active scientific/specialized contracts.

## Stage / historical evidence

- `STAGE_2026_08_MAINTENANCE.md`
- `FRONTIER_ALIGNMENT.md`
- `FOUR_DAY_CONSOLIDATION.md`
- `FIVE_DAY_CONSOLIDATION.md`
- `SIX_DAY_CONSOLIDATION.md`
- `docs/03-maintenance-and-audit/history/superpowers/` — superseded/historical implementation design and planning evidence

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
