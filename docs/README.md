# Documentation Taxonomy

**Calibrated:** 2026-09-15

This directory is the current routing layer for the repository's research, explanatory, contract, example, metadata, maintenance, audit, and historical materials. It classifies by **primary responsibility** and now also owns the physical placement of repository documentation that does not need to remain a root/platform entry point.

1. [Source and explanation](01-source-and-explanation/README.md) — executable implementation, tests, build/runtime surfaces, and documents that explain current behavior.
2. [Examples and contracts](02-examples-and-contracts/README.md) — machine-readable capability contracts, active research/specialized contracts, examples, operator guidance, usage constraints, and repository metadata.
3. [Maintenance and audit](03-maintenance-and-audit/README.md) — maintenance rules/configuration, document-status routing, dated reconciliations, calibration/correction records, stage records, and historical snapshots.

## Placement policy

Root is reserved for repository/platform entry points and machine entry points that materially benefit from root placement: `README.md`, `MANIFEST.yaml`, `AGENTS.md`, contributor/citation/license metadata, `Makefile`, and implementation directories.

Current explanatory documents live under class 01. Active project contracts and customization guidance live under class 02. Current maintenance/governance documents and historical evidence live under class 03, while dated operational maintenance records may live under `maintenance/`.

Physical relocation is not a semantic upgrade. Historical bodies retain their point-in-time meaning, and a path change does not rewrite what was or was not executed.

Already-superseded Superpowers design/planning records remain archived under `docs/03-maintenance-and-audit/history/superpowers/`; their content remains historical evidence.

## Recovery authority

For current-state recovery, use subject-scoped authority in this order:

```text
current merged main implementation
> current machine-readable capability contract / schema / configuration for that subject
> active Research Contract and active specialized contract for that subject
> operational examples / configuration / test evidence for supported use
> README / Architecture / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

Execution evidence exists only when the execution was actually performed and preserved; file presence or a historical claim is not execution evidence.

[`03-maintenance-and-audit/DOCUMENT_STATUS.md`](03-maintenance-and-audit/DOCUMENT_STATUS.md) is the repository's current document-governance router and classifier. It does not independently redefine implementation semantics. Dated maintenance records describe what a pass concluded at a point in time and do not outrank current implementation or active contracts.

`AGENTS.md` remains operational guidance. If an older embedded recovery-order list conflicts with this 2026-09-15 taxonomy or the current Document Status router, the current taxonomy/router governs document recovery; the detailed hard rules in `AGENTS.md` remain active unless separately changed.

## Non-goals

This taxonomy does not change runtime capability, scientific meaning, evidence sufficiency, publisher/accessibility status, or historical claims. It does not authorize deletion or history rewrite.
