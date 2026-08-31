# Document Status — epistemic-pipeline

**Status:** active document-governance map  
**Calibrated:** 2026-09-01  
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
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline;
- `POST_STAGE_REPAIR_2026_09_01.md` records post-close hardening without reopening the stage;
- `DOCUMENT_STATUS.md` defines documentation authority/history roles.

## Historical snapshots

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

These remain historical evidence of earlier repository states. They are not current runtime or scientific contracts and should not be rewritten merely because current terminology evolved.

## Examples, customization and reference demonstrations

```text
examples/README.md
CUSTOMIZATION_GUIDE.md
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

These describe supported patterns and maintenance interpretation but do not override implementation, Manifest, or active contracts.

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

The 2026-09-01 repair does not extend that window. It corrects implementation/contract mismatches discovered after closure while preserving the stage-close record.

## Maintenance rule

Daily maintenance corrects demonstrated local runtime/contract drift.

Weekly maintenance reconciles the complete current evidence stack.

Monthly or explicit phase-close maintenance records a closed baseline, inventories historical snapshots, and reviews current/experimental/not-integrated labels without deleting history.

A post-stage repair may correct implementation defects or evidence-contract mismatches without being reclassified as part of the closed stage.

## Hard boundaries

```text
document authority != claim truth
historical snapshot != invalid evidence
post-stage repair != stage rewrite
maintenance consistency != evidence sufficiency
reference demonstration != runtime proof
calendar close != scientific validation
monthly baseline != independent reproduction
```
