# D1 — Scope, Reference Construction, and Dataset Error

## Question
What does a narrowly scoped factuality benchmark establish, and what does its own quality process leave uncertain?

## Object and source
- O1: SimpleQA, 2024-10-30.
- S1: https://openai.com/index/introducing-simpleqa/

## Observations
SimpleQA intentionally restricts factuality evaluation to short, fact-seeking questions with single verifiable answers. The release describes two independent trainer answers for inclusion and a third-trainer random sample used to estimate remaining dataset error.

Its grading uses a prompted model classifier over predicted and reference answers. The publisher explicitly states that the benchmark's narrow short-answer scope leaves the relation to long-form factuality open.

## Analysis
The benchmark makes two evidence boundaries visible:

```text
reference construction quality
!= zero dataset error

short-answer factuality
!= general factuality
```

A score inherits the benchmark's scope and grading contract. It cannot be transferred to long-form, retrieval-grounded, scientific or domain-specific factuality without new evidence.

## Counterevidence / limits
- This Stage does not independently audit the 4,326 items.
- The publisher's estimated error is not independently reproduced.
- Prompted-grader behavior is an evaluator layer, not reference truth itself.

## Conclusion
`SUPPORTED_SCOPE_BOUNDARY`.
