# Historical Maintenance Recovery Index

This directory is the Class 03 recovery entry point for historical maintenance and audit material.

Current implementation, machine-readable contracts, and active subject contracts outrank every item indexed here. Historical records remain point-in-time evidence; indexing them does not modernize their claims.

## Root-retained historical snapshots

As of 2026-09-15, these historical snapshots remain at repository root for compatibility with existing machine/document references:

- [`FOUR_DAY_CONSOLIDATION.md`](../../../FOUR_DAY_CONSOLIDATION.md)
- [`FIVE_DAY_CONSOLIDATION.md`](../../../FIVE_DAY_CONSOLIDATION.md)
- [`SIX_DAY_CONSOLIDATION.md`](../../../SIX_DAY_CONSOLIDATION.md)
- [`STAGE_2026_08_MAINTENANCE.md`](../../../STAGE_2026_08_MAINTENANCE.md)
- [`POST_STAGE_REPAIR_2026_09_01.md`](../../../POST_STAGE_REPAIR_2026_09_01.md)
- [`FRONTIER_ALIGNMENT.md`](../../../FRONTIER_ALIGNMENT.md)

`JULES_CORRECTION_RECORD.md` remains an active correction/governance surface and is not classified as a historical snapshot here.

## Recovery rule

```text
current implementation / machine contracts / active subject contracts
> current maintenance and document-status routers
> dated maintenance / repair evidence
> historical snapshots
> historical PR or task narrative
```

Root retention is a path-compatibility fact, not a claim that these snapshots are current authority. Any later physical relocation must update current machine/document consumers atomically rather than leaving split paths.
