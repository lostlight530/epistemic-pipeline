# Documentation Taxonomy

**Calibrated:** 2026-09-15

This directory is the current routing layer for the repository's research, explanatory, contract, example, metadata, maintenance, audit, and historical materials. It classifies by **primary responsibility**, not by file extension or physical location.

1. [Source and explanation](01-source-and-explanation/README.md) — executable implementation, tests, build/runtime surfaces, and documents that explain current behavior.
2. [Examples and contracts](02-examples-and-contracts/README.md) — machine-readable capability contracts, active research/specialized contracts, examples, operator guidance, usage constraints, and repository metadata.
3. [Maintenance and audit](03-maintenance-and-audit/README.md) — maintenance rules/configuration, document-status routing, dated reconciliations, calibration/correction records, stage records, and historical snapshots.

## Placement policy

Classification does not require every file to be physically moved. Root-level canonical entrypoints and path-sensitive files remain where repository tooling, GitHub conventions, or existing contracts expect them. Physical relocation is appropriate only when it does not manufacture path drift.

Already-superseded Superpowers design/planning records are physically archived under `docs/03-maintenance-and-audit/history/superpowers/`; their content remains historical evidence.

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

`DOCUMENT_STATUS.md` is the repository's current document-governance router and classifier. It does not independently redefine implementation semantics. Dated maintenance records describe what a pass concluded at a point in time and do not outrank current implementation or active contracts.

`AGENTS.md` remains operational guidance. If an older embedded recovery-order list conflicts with this 2026-09-15 taxonomy or `DOCUMENT_STATUS.md`, the current taxonomy/router governs document recovery; the detailed hard rules in `AGENTS.md` remain active unless separately changed.

## Non-goals

This taxonomy does not change runtime capability, scientific meaning, evidence sufficiency, publisher/accessibility status, or historical claims. It does not authorize deletion or history rewrite.
