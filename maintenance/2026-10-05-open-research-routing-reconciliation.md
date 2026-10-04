# Open-research routing reconciliation — 2026-10-05

Status: READY_FOR_MAINTAINER_REVIEW  
Repository: `lostlight530/epistemic-pipeline`  
Exact base revision: `fbd94950705e70ac1f0ef4001b921bd8c6dd3195`  
Branch: `maintenance/2026-10-05-open-research-routing`

## Confirmed current drift

Current `main` contains `OPEN_RESEARCH.md` as a durable repository-level open-research production guide and `RESEARCH_TEMPLATE.md` as prospective bounded-record scaffolding. README and CONTRIBUTING already route contributors to them.

At the observed base revision, the current document-governance router, agent recovery guide, and machine cadence path inventory did not enumerate either file. This left a durable current research-method surface outside the explicit authority router and deterministic maintenance scan inventory.

## Bounded repair

This repair only:
- adds `OPEN_RESEARCH.md` and `RESEARCH_TEMPLATE.md` to the current document router with explicit lower-than-implementation/validator/contract authority;
- routes agents to the open-research guide while preserving more specific native claim/evidence/runtime contracts;
- adds both files to maintenance canonical/scan paths.

It does not change implementation, `MANIFEST.yaml`, validators, runtime-policy semantics, claim/evidence acceptance, heuristic-score semantics, transfer acceptance, historical FOUR_DAY/FIVE_DAY/SIX_DAY records, frontier-research Stage/Part records, or `LONGITUDINAL_INDEX` semantics.

## Preserved boundaries

```text
Provenance != Truth
claim transfer != acceptance
linked evidence != sufficient evidence
heuristic score != probability
maintenance clean != scientific validation
frontier-research documentation != runtime authority
RESEARCH_TEMPLATE != historical rewrite instruction
```

## Evidence state

Executed in this producer pass:
- fresh exact-main recovery;
- open-PR overlap check;
- exact-file inspection of current authority and maintenance surfaces;
- static source/contract reconciliation.

NOT_EXECUTED in this producer pass:
- maintenance scanner execution;
- validator/test suite;
- runtime/provider execution;
- scientific validation;
- independent reproduction.

Source presence and static inspection are not reported as execution PASS.
