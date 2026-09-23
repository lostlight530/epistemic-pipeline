# Frontier Research Stage Handoff — Stage D / 2024-Q4

## Eligible findings
| Finding | Boundary | Cross-repo use |
|---|---|---|
| benchmark scope bounds claim scope | SimpleQA | compare artifact/communication scope |
| freshness != difficulty | LiveBench / FrontierMath | compare lifecycle/version semantics |
| benchmark vintage + answer format affect comparability | LiveBench | compare derivative/version identity |
| judge ensemble belongs to evidence provenance | FACTS Grounding | compare verifier independence |
| private split improves leakage control but constrains replay | FACTS Grounding | compare evidence availability |

## Unsafe generalization
- universal model ranking
- universal factuality
- cross-benchmark score equivalence
- judge output as truth
- private split as independent reproduction
- automatic target-repository change

```text
handoff != acceptance
evaluation evidence != scientific truth
shared provenance concept != shared implementation
```


## A2 handoff calibration — 2026-09-23

This Stage D handoff carries scoped research context only. It does not transfer truth, acceptance, scientific adjudication, or runtime-policy success.

```text
HANDOFF_CONTEXT
!= CLAIM_ACCEPTANCE
!= TRUTH
!= SCIENTIFIC_VALIDATION
```

Any downstream claim transfer must preserve origin identity, evidence references, ambiguity/conflict state, and its own acceptance decision.
