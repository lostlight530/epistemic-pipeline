# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected at a given time, what was concluded, and what historical evidence must remain reviewable?**

It does **not** define the repository's scientific or runtime semantics merely because a record is newer than an active contract.

## Current maintenance / governance surfaces

- [`DOCUMENT_STATUS.md`](DOCUMENT_STATUS.md) — current document-governance router and subject-scoped authority classifier
- [`MAINTENANCE_CADENCE.md`](MAINTENANCE_CADENCE.md) — human-readable repository-maintenance contract
- root `maintenance/cadence.yaml` — machine-readable local maintenance/scanner configuration; classified here by function
- [`independent-gpt/README.md`](independent-gpt/README.md) — current public cold-start recovery kernel for a memoryless independent reviewer; it does not override subject-scoped authority

`core/maintenance_cadence.py` remains **Class 01 source** because it is executable implementation. Its presence or a successful local scan is not the same thing as an external governance patrol, GitHub-state audit, scientific validation, or a preserved historical run.

## Coordinated three-repository maintenance

This repository may be inspected in one coordinated pass with:

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination means shared timing, cross-repository name/profile checks, and a common report. It does **not** create cross-repository authority. Each repository must recover from its own latest merged `main`, implementation, machine contracts/configuration, active subject contracts, current document router, maintenance evidence, and history.

A legacy generic ordering such as `implementation > MANIFEST > latest repair > DOCUMENT_STATUS > AGENTS > contracts > cadence > Architecture/README > history` is not a universal authority law. When it conflicts with the current subject-scoped order in `DOCUMENT_STATUS.md`, the subject-scoped order wins.

The scheduled daily pass at 06:30 Asia/Shanghai is an inspection/maintenance opportunity, not a requirement to create churn. `NO_CHANGE_REQUIRED` is a valid result. Weekly or monthly artifacts are created only when the current contract, a natural calendar/phase boundary, accumulated evidence, demonstrated drift, or another explicit maintenance need justifies them.

For an authorized change, refresh remote `main`, inspect recent relevant merged/open PR state, branch from the latest merged revision, make one coherent scoped change, run only checks that actually exist and were actually executed, compare `main...branch`, require `behind_by = 0`, open a Draft PR, verify mergeability, and stop for maintainer review unless the maintainer explicitly authorizes another delivery mode. Do not write directly to `main`, rewrite history, or modify GitHub Actions/CI/CodeQL/branch-governance automation as routine repository maintenance.

When used by the coordinated research-maintenance GPT, the final user-facing report is written in Chinese while repository names, paths, SHAs, commands, state labels, profile names, and protocol terms remain canonical.

## Dated maintenance / calibration evidence

- root `maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md`
- root `maintenance/POST_STAGE_REPAIR_2026_09_01.md`
- root `maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md`
- root `maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md`
- root `maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md`

The 2026-08-24 through 2026-08-31 stage remains closed historical evidence. The 2026-09-01 post-stage repair is the dated starting checkpoint for steady-state maintenance, and current merged `main` may supersede that checkpoint only through explicit current evidence or reconciliation.

These records are point-in-time evidence. A later dated record may report a newer observation, correction, or maintenance result, but it does not silently override current implementation, machine contracts, or active scientific/specialized contracts.

## Stage / historical evidence

- [`history/STAGE_2026_08_MAINTENANCE.md`](history/STAGE_2026_08_MAINTENANCE.md)
- [`history/FRONTIER_ALIGNMENT.md`](history/FRONTIER_ALIGNMENT.md)
- [`history/FOUR_DAY_CONSOLIDATION.md`](history/FOUR_DAY_CONSOLIDATION.md)
- [`history/FIVE_DAY_CONSOLIDATION.md`](history/FIVE_DAY_CONSOLIDATION.md)
- [`history/SIX_DAY_CONSOLIDATION.md`](history/SIX_DAY_CONSOLIDATION.md)
- [`history/JULES_CORRECTION_RECORD.md`](history/JULES_CORRECTION_RECORD.md) — 2026-09-06 correction/authority record retained as historical calibration evidence, not a current top-level authority
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
