# F1 — PaperBench Replication Task and Judge Provenance

## Evidence
PaperBench was published 2025-04-02. It evaluates agents on replicating 20 ICML 2024 Spotlight/Oral papers from scratch, including understanding contributions, building code and executing experiments. The benchmark decomposes work into 8,316 gradable rubric tasks and uses an LLM-based judge whose own performance is separately benchmarked.

Sources:
- https://openai.com/index/paperbench/
- https://arxiv.org/abs/2504.01848

## Analysis
The evaluated object is no longer only an answer or local software task. It is a multi-stage research trajectory.

```text
paper understanding
-> implementation
-> experiment execution
-> artifact/result production
-> rubric assessment
```

A benchmark "replication score" is still rubric-scoped benchmark evidence. It does not establish that the scientific paper was independently reproduced in the stronger epistemic sense.

The judge itself becomes part of provenance:

```text
replication attempt
+ rubric
+ judge identity/protocol
-> benchmark score
```

## Outcome
`SUPPORTED_OBSERVATION`
