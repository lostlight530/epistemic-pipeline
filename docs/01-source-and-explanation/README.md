# 01 — Source and Explanation

This class answers three durable questions:

1. **What does epistemic-pipeline actually execute or validate?**
2. **Where are claim, state, graph, role, and provider boundaries explained?**
3. **Which observed results are structural/runtime evidence rather than scientific truth?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| `core/` | pipeline orchestration and repository-owned execution semantics | source defines implemented behavior; contract prose cannot add a missing runtime feature |
| `graphs/` | graph representations and graph-related evidence/state structures | graph presence or reachability does not establish claim truth |
| `states/` | explicit execution/claim lifecycle state | a state transition is repository control state, not external factual validation |
| `roles/` | repository role/actor abstractions | role labels do not establish external identity or authority |
| `validators/` | machine-readable structural/policy validation | validator success supports only the implemented rule being checked |
| `tests/` | revision-scoped regression/contract evidence | passing tests do not prove evidence sufficiency or scientific correctness |
| `Makefile` | supported engineering command entry points | command presence != command execution |

The maintenance scanner remains implementation source even when it supports class 03 materials. Its source presence is not scanner execution.

## Architecture and explanation

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — current architecture, execution layers, evidence/claim separation, provider boundaries, and cross-repository interfaces.

Implementation and revision-matched execution evidence own actual behavior. README and Architecture explain that behavior; they do not override it.

## Core epistemic boundaries

Use the repository with these separations intact:

```text
claim indexed != claim true
evidence linked != evidence sufficient
validator PASS != scientific verification
runtime-policy PASS != truth
heuristic score != calibrated probability
provider-reported identity != vendor authentication
```

When a result is cited, identify the exact revision, input/evidence envelope, configuration/profile, command or execution surface, result, and untested boundary when material.

## Cross-layer reading

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) define how claims, evidence, assertion basis, audit coverage, and cross-repository transfer are represented and interpreted.

A contract may constrain meaning; it does not prove that an external claim is correct or that a run occurred.

Current document taxonomy is routed from [`../README.md`](../README.md). Maintenance/audit material belongs to class 03 and remains separate from the repository's primary claim/evidence architecture.
