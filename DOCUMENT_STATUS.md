# Document Status — epistemic-pipeline

**Status:** active document-governance map  
**Calibrated:** 2026-08-31  
**Stage:** August 2026 evidence-infrastructure phase closed on 2026-08-31

This file classifies repository documentation by current authority and historical role

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
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
CUSTOMIZATION_GUIDE.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
```

Subject authority remains scoped

- implementation defines actual runtime behavior
- `MANIFEST.yaml` is the machine-readable capability map
- `RESEARCH_CONTRACT.md` defines current scientific-integrity semantics
- Claim Audit / Claim Transfer / Assertion Basis contracts define their named evidence surfaces
- `MAINTENANCE_CADENCE.md` defines daily, weekly, and monthly maintenance responsibilities
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline
- `DOCUMENT_STATUS.md` defines documentation authority/history roles

## Historical snapshots

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

These remain historical evidence of earlier repository states

They are not current runtime or scientific contracts

Do not rewrite them merely because current terminology, profiles, or capabilities evolved later

```text
historical snapshot != current contract
later claim qualification != permission to rewrite earlier context
```

## Examples, customization and reference demonstrations

```text
examples/README.md
CUSTOMIZATION_GUIDE.md
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

These describe supported patterns, extension boundaries and maintenance interpretation but do not override implementation, Manifest, or active contracts

The dated maintenance demonstration is the first complete Daily / Weekly / Monthly worked example for the evidence stack
It does not pre-assert a clean scanner result and does not become a scientific-review record

```text
reference demonstration != evidence sufficiency
worked maintenance example != scientific validation
```

## External / citation metadata

```text
CITATION.cff
```

Real external standard/runtime versions remain legitimate provenance metadata

The project no-decorative-version rule applies only to project-owned internal profile identifiers

## Stage-close status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The earlier 2026-08-30 `month-to-date` statement was correct for that date and remains historical context only

## Maintenance rule

Daily maintenance corrects demonstrated local runtime/contract drift

Weekly maintenance reconciles the complete current evidence stack

Monthly or explicit phase-close maintenance records a closed baseline, inventories historical snapshots, and reviews current/experimental/not-integrated labels without deleting history

The first complete cadence demonstration under `maintenance/` is reference material for future maintainers and agents after they read the active cadence contract

## Hard boundaries

```text
document authority != claim truth
historical snapshot != invalid evidence
maintenance consistency != evidence sufficiency
reference demonstration != runtime proof
calendar close != scientific validation
monthly baseline != independent reproduction
```
