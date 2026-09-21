# Frontier Research Part C2 — Domain-Conditioned Evaluator Authority

## Identity

- Stage: `C / 2024-Q3`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Question

Can one evaluator/judge identity inherit evaluation authority across domains and task types

## Objects and sources

- O2 “Constructing Domain-Specific Evaluation Sets for LLM-as-a-judge”, submitted 2024-08-16: https://arxiv.org/abs/2408.08808
- O3 CodeJudge-Eval, submitted 2024-08-20 and revised 2024-09-16: https://arxiv.org/abs/2408.10718
- O4 Arena-Hard/BenchBuilder context, paper first posted 2024-06-17: https://arxiv.org/abs/2406.11939

O2/O3 are separate research teams; O4 is pre-Q3 context

## Observations

The domain-specific evaluation-set paper argues that general-purpose evaluator frameworks may not capture domain-specific behavior and studies construction of evaluation sets across specialized contexts

CodeJudge-Eval creates a distinct task: judging correctness of supplied code solutions rather than generating code

Its benchmark includes multiple error/compilation categories and reports that tested LLM judges struggle on this judging problem

Arena-Hard/BenchBuilder supplies adjacent context that automated judge-based benchmarking can achieve strong alignment with human preference under a specific curation/judge pipeline

## Analysis

The correct authority model is not:

```text
judge model X is good
→ judge X is authoritative everywhere
```

It is closer to:

```text
judge identity
+ judge version
+ task/domain
+ prompt/rubric
+ response-pair construction
+ scoring/aggregation method
+ validation reference
```

Different domains can alter error modes and what “agreement” means

Human-preference alignment is not the same target as factual/code correctness

## Counterevidence

These papers do not prove that domain-specific judges are always superior

No common judge was rerun across all selected Q3 objects in this Stage

## Conclusion

`SUPPORTED_OBSERVATION / STRONGER_EVALUATOR_BOUNDARY`

```text
evaluator identity
!= evaluator authority independent of domain/task
```
