# E2 — SWE-Lancer Economic Task and Grading Identity

## Research question
What changes when benchmark tasks are real freelance software-engineering work with monetary value and task-specific grading?

## Evidence
OpenAI introduced SWE-Lancer on 2025-02-18. The benchmark contains more than 1,400 Upwork freelance software-engineering tasks with $1M total real-world payouts. It separates independent engineering tasks from managerial proposal-selection tasks. Engineering tasks use end-to-end tests triple-verified by experienced engineers; managerial tasks are assessed against original manager choices. A unified Docker image and public Diamond split were released.

Sources:
- https://openai.com/index/swe-lancer/
- https://arxiv.org/abs/2502.12115

## Analysis
SWE-Lancer makes the evaluation object more operationally situated:

```text
task artifact
+ repository/environment
+ grading mechanism
+ task class
+ payout metadata
+ split identity
-> bounded benchmark result
```

Dollar value is task metadata and a way to aggregate benchmark outcomes. It is not by itself a causal estimate of economy-wide labor substitution or realized production value.

End-to-end tests and manager choices are different evaluator authorities and should not be collapsed into one generic "correct" label.

## Outcome
`SUPPORTED_OBSERVATION`
