# D3 — Grounded Long-Form Evaluation and Judge Ensemble

## Question
What new evidence fields appear when factuality becomes long-form and grounded in supplied documents?

## Object and source
- O4: FACTS Grounding, 2024-12-17.
- S4: https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/
- S5: https://storage.googleapis.com/deepmind-media/FACTS/FACTS_grounding_paper.pdf

## Observations
FACTS Grounding evaluates long-form responses against provided source documents. The associated paper describes a two-stage automated judging process and aggregation across multiple judge models to mitigate evaluator bias. The leaderboard design includes public and private splits.

## Analysis
Compared with SimpleQA, the evidence envelope expands:

```text
question/task scope
+ source document
+ response
+ fulfillment gate
+ grounding/factuality judge
+ judge prompt/config
+ judge ensemble/aggregation
+ public/private split identity
+ benchmark vintage
```

Multiple judges may reduce some evaluator variance while remaining one designed evaluation protocol. An ensemble is not automatically independent scientific adjudication.

## Counterevidence / limits
- No FACTS run is reproduced locally.
- Held-out/private evaluation strengthens leakage control but limits full external replay.
- Grounded factuality does not imply factuality with respect to external world knowledge.

## Conclusion
`SUPPORTED_EVIDENCE_ENVELOPE_EXPANSION`.
