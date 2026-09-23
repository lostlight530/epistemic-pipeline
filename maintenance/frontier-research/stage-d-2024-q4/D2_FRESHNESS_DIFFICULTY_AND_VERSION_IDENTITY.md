# D2 — Freshness, Difficulty, and Version Identity

## Question
Do benchmark freshness and benchmark difficulty prove the same thing?

## Objects and sources
- O2: FrontierMath announcement, 2024-11-08.
- O3: LiveBench refresh, 2024-11-25.
- S2: https://epoch.ai/frontiermath/tiers-1-4/the-benchmark
- S3: https://github.com/LiveBench/LiveBench/blob/main/changelog.md

## Observations
FrontierMath introduced hundreds of original expert-crafted mathematics problems, with exact/automatic verification where possible and an explicit benchmark version for the reported analysis.

LiveBench's 2024-11-25 update refreshed instruction-following articles and reasoning tasks, increased difficulty, and changed answer-format requirements for some tasks. Its changelog frames refresh as a response to contamination/saturation risk.

## Analysis
These mechanisms attack different measurement problems:

```text
freshness
= reduce exposure/saturation risk by changing content

expert difficulty
= raise capability ceiling and task depth
```

Neither implies the other. A fresh task may be easy; a hard task may later become exposed. Both require version identity for longitudinal comparison.

## Counterevidence / limits
- "Fresh" is a design intent and temporal property, not proof that no model saw the questions.
- FrontierMath difficulty is domain-specific and does not generalize to other capabilities.
- Later clarifications about benchmark governance are later evidence and are not rewritten into the original November observation.

## Conclusion
`SUPPORTED_COMPARABILITY_BOUNDARY`.
