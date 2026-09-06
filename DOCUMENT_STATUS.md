# Document Status — epistemic-pipeline

**Status:** active document-governance map  
**Calibrated:** 2026-09-06  
**Stage:** August 2026 evidence-infrastructure phase closed on 2026-08-31

This file classifies repository documentation by current authority and historical role.

## Current authoritative documents

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
CLAIM_AUDIT_CONTRACT.md
CLAIM_TRANSFER_CONTRACT.md
ASSERTION_BASIS_AND_AUDIT_COVERAGE.md
MAINTENANCE_CADENCE.md
JULES_CORRECTION_RECORD.md
STAGE_2026_08_MAINTENANCE.md
POST_STAGE_REPAIR_2026_09_01.md
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
CUSTOMIZATION_GUIDE.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
```

Subject authority remains scoped:

- implementation defines actual runtime behavior;
- `MANIFEST.yaml` is the machine-readable capability map;
- `RESEARCH_CONTRACT.md` defines current scientific-integrity semantics;
- Claim Audit / Claim Transfer / Assertion Basis contracts define their named evidence surfaces;
- `MAINTENANCE_CADENCE.md` defines daily, weekly, and monthly maintenance responsibilities;
- `JULES_CORRECTION_RECORD.md` defines the evidence/authority boundary for historical Jules-created PR/task narratives;
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline;
- `POST_STAGE_REPAIR_2026_09_01.md` records post-close hardening without reopening the stage;
- `DOCUMENT_STATUS.md` defines documentation authority/history roles.

## Authority precedence for recovery

```text
current main implementation
> MANIFEST.yaml / current machine-readable configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active evidence/scientific-integrity contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> Architecture / README
> historical snapshots
> historical PR/task narratives
```

## Historical snapshots

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

These remain historical evidence of earlier repository states. They are not current runtime or scientific contracts and should not be rewritten merely because current terminology evolved.

## Dated maintenance / correction / research-calibration records

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
```

- the 2026-09-06 Daily/Weekly record documents a real authority/cadence reconciliation and does not assert a scanner run, test run, evidence-sufficiency verdict, or scientific validation;
- the 2026-09-01 through 2026-09-06 frontier refresh is **post-stage, non-normative, source-bounded research calibration** for provider/model provenance, execution status, long-running agents, telemetry, source-authority conflict and claim-transfer boundaries. It does not change the active Research Contract or turn external provider claims into scientific evidence.

`FRONTIER_ALIGNMENT.md` remains the August stage-close positioning snapshot. The dated frontier refresh is the newer external-research observation record through 2026-09-06 and must not be used as a truth oracle or capability contract.

Dated records are time-scoped maintenance/research evidence and do not override later implementation changes.

## Historical coding-agent / PR narratives

Early Jules-created PRs remain preserved in GitHub history.

Their task descriptions, PR bodies, automatic summaries, framework comparisons, test statements, confidence-related claims, and completion language are not current contracts or scientific evidence. Read `JULES_CORRECTION_RECORD.md` before reusing them.

```text
historical agent proposal != current authority
structured/test claim != current scientific verification
requires re-verification != false
correction != history deletion
```

## Examples, customization and reference material

```text
examples/README.md
CUSTOMIZATION_GUIDE.md
```

These describe supported patterns but do not override implementation, Manifest, or active contracts.

## External / citation metadata

```text
CITATION.cff
```

Real external standard/runtime versions remain legitimate provenance metadata. The no-decorative-version rule applies only to project-owned internal profile identifiers.

## Stage-close and post-stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The 2026-09-01 repair, 2026-09-06 maintenance reconciliation, and 2026-09-01 through 2026-09-06 frontier refresh do not extend or reopen that window.

## Maintenance rule

Daily maintenance corrects demonstrated local runtime/contract/governance drift.

Weekly maintenance reconciles the complete current evidence stack, current maintenance/correction records, coding-agent authority handling, and historical inventory.

If one pass serves as both Daily and Weekly maintenance, one branch/PR may carry the combined real work; cadence labels do not require duplicate PR churn.

Monthly or explicit phase-close maintenance records a closed baseline, inventories historical snapshots, and reviews current/experimental/not-integrated labels without deleting history.

## Hard boundaries

```text
document authority != claim truth
historical snapshot != invalid evidence
post-stage repair != stage rewrite
frontier calibration != claim verification
external provider event != evidence sufficiency
maintenance consistency != evidence sufficiency
reference demonstration != runtime proof
calendar close != scientific validation
monthly baseline != independent reproduction
agent PR narrative != current repository truth
cadence coalescing != skipped maintenance scope
```
