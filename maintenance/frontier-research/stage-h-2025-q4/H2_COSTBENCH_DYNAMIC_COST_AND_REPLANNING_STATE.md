# H2 — CostBench v1: Dynamic Cost, Blocking Events, and Replanning State

## Source identity
- arXiv:2511.02734v1
- v1 submitted: 2025-11-04
- Primary source: https://arxiv.org/abs/2511.02734
- Note: later v2/v3 revisions exist; Stage H is bound to the v1 historical identity.

## Frontier observation
CostBench evaluates cost-aware planning and replanning with alternative tool sequences, configurable costs, and dynamic blocking events such as tool failures or cost changes.

This introduces a state variable often absent from simple success evaluation:

```text
plan
+ available tools
+ current costs
+ blocking state
+ replanning decision
-> achieved outcome
+ realized evaluation cost
```

The relevant epistemic point is that “same task solved” does not imply “same plan quality” when environment costs and availability move during execution.

## Boundary
- benchmark cost != real invoice/economic utility
- simulated tool failure != provider incident
- cost-optimal under benchmark rules != globally optimal
- adaptation score != robustness proof

## Repository interpretation
No benchmark run was reproduced. Cost remains an evaluation dimension, not a probability or truth score.
