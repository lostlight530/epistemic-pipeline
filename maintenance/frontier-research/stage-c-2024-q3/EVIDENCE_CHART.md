# Evidence Chart — Stage C / 2024-Q3

## Variables

| Variable | Meaning |
|---|---|
| benchmark_family | benchmark lineage/name |
| benchmark_vintage | dated task/question state |
| task_domain | evaluation target/domain |
| evaluator_identity | judge/evaluator model/system |
| evaluator_contract | rubric/prompt/scoring/aggregation |
| config_identity | dataset/configuration state |
| execution_time | when scoring occurred |
| provenance | source family and record state |

## Chart

| Object | Q3 evidence | Main boundary | Reproduction |
|---|---|---|---|
| LiveBench | July/August task refresh + Sep snapshot | same family != same measurement instance | NOT_EXECUTED |
| Domain-specific evaluator sets | domain-specific construction/evaluation | evaluator usefulness is context-conditioned | NOT_EXECUTED |
| CodeJudge-Eval | judging code correctness as separate task | judge authority depends on target task | NOT_EXECUTED |
| Judge/reward-model limits | context-dependent strengths/limits | judge output != ground truth | NOT_EXECUTED |
| MMLU-Redux issue #2 | reported config ambiguity | issue != confirmed defect | NOT_EXECUTED |

## Comparability states

```text
COMPARABLE
PARTIALLY_COMPARABLE
NOT_COMPARABLE
UNKNOWN
```

These are reasoning states for future evidence envelopes

This Stage does not retroactively assign them to every historical leaderboard row because row-level benchmark/config replay was not performed

## Counterexamples

| Overclaim | Counterevidence | Resolution |
|---|---|---|
| same benchmark name means same measurement | LiveBench changes questions/tasks | reject |
| one good judge is authoritative everywhere | domain/code judge studies show task dependence | reject |
| human agreement means factual ground truth | target/contract differs by study | reject |
| issue proves benchmark defect | MMLU-Redux report remains unresolved | reject |
| later refresh invalidates earlier score | earlier score remains evidence for earlier vintage | reject |

## Amendments

`NONE`
