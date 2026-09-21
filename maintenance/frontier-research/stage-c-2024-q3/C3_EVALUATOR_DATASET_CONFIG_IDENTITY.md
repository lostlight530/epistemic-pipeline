# Frontier Research Part C3 — Evaluator and Dataset-Configuration Identity

## Identity

- Stage: `C / 2024-Q3`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Question

Which evaluator/configuration identities must remain visible when an evaluation result is preserved longitudinally

## Objects and sources

- O4 “LLM-as-a-Judge & Reward Model: What They Can and Cannot Do”, submitted 2024-09-17: https://arxiv.org/abs/2409.11239
- O5 MMLU-Redux repository issue #2, opened 2024-09-19: https://github.com/aryopg/mmlu-redux/issues/2
- Context: MMLU-Redux paper first posted 2024-06-06: https://arxiv.org/abs/2406.04127

## Observations

The September judge/reward-model paper explicitly treats judge effectiveness as context-dependent and investigates difficult contexts including non-English, factual verification and challenging questions

The MMLU-Redux issue asks about differing dataset/config references in project code/paper context

The issue is evidence that a user-visible configuration ambiguity was reported in the project on 2024-09-19

It is **not** evidence that a benchmark defect was confirmed or resolved

## Analysis

Stage B added benchmark revision/vintage to the evidence envelope

Stage C adds evaluator/configuration identity:

```text
EvaluationEnvelope
  model_revision
  benchmark_family
  benchmark_vintage
  dataset/config identity
  task/domain
  evaluator/judge identity
  evaluator version
  judge prompt/rubric
  scoring/aggregation method
  execution date
  source provenance
```

A repository issue can be part of uncertainty/provenance state without becoming an adjudicated fact

## Strong boundaries

```text
reported config ambiguity
!= confirmed benchmark defect

judge result
!= objective ground truth

agreement with humans on one surface
!= universal judging authority
```

## Conclusion

`SUPPORTED_OBSERVATION / PARTIAL`

Q3 supports treating evaluator and configuration state as first-class evidence identity while leaving unresolved project issues unresolved
