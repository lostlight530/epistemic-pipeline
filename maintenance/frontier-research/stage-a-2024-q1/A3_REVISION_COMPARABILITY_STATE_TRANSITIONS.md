# Frontier Research Part A3 — Revision, Comparability, and State Transitions

## 0. Identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `A / 2024-Q1`
- **Part:** `A3`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> How did benchmark, corpus, and toolkit revisions affect the meaning and comparability of evaluation claims?

## 2. Revision objects

### TrustLLM toolkit

Project history records multiple Q1 versions:

- 2024-01-12 initial dataset/leaderboard/toolkit release;
- 2024-01-20 v0.2.0;
- 2024-01-29 v0.2.1;
- 2024-03-20 v0.2.4 with bug fixes and Gemini Pro API support.

Source: https://github.com/HowieHwong/TrustLLM

### RAGTruth corpus

Project history says:

- January: corpus release;
- February: data update with more annotated hallucinations and `implicit_true`.

Source: https://github.com/ParticleMedia/RAGTruth

### WMDP

Project history records:

- paper/benchmark posted 2024-03-05;
- dataset modified 2024-03-08 for choice-randomization issues;
- later 2024-04-23 changes for formatting/unicode, overly long cyber questions, insufficient dual-use potential in some bio questions; RMU was also simplified.

Source: https://github.com/centerforaisafety/wmdp

The April update is outside Stage A, but it is relevant as a later correction that changes how Q1 evidence should be compared going forward.

## 3. State-transition model

A benchmark object should not be modeled as one timeless name.

A safer conceptual transition is:

```text
benchmark_v1
  --data correction--> benchmark_v1r1
  --annotation expansion--> benchmark_v1r2
  --method/tool update--> evaluation_pipeline_vN
```

Scores from different nodes may be comparable, partially comparable, or not comparable depending on what changed.

## 4. Correction != invalidation

A correction does not necessarily mean all earlier results are useless. It means the earlier result belongs to a different evidence state.

For WMDP:

```text
2024-03-05 benchmark state
!= 2024-03-08 corrected dataset state
!= 2024-04-23 later corrected state
```

A result must be linked to the state actually used.

## 5. Annotation ontology can change claim semantics

RAGTruth's February addition of `implicit_true` is more than metadata housekeeping. It distinguishes a response span that may be correct despite not being mentioned in context.

That changes the epistemic interpretation of labels. If earlier analyses treated all unsupported-in-context spans alike, a later ontology can refine rather than simply overwrite that earlier state.

## 6. Tool support changes execution evidence

TrustLLM's toolkit revisions changed evaluation pipeline support and provider/API coverage. A paper's conceptual benchmark and a toolkit's executable surface should therefore be versioned separately.

```text
benchmark specification
!= evaluation implementation
!= a particular executed run
```

## 7. Cross-object synthesis

Across TrustLLM, RAGTruth, and WMDP, Q1 shows three revision classes:

- implementation/tool revision;
- annotation/data revision;
- benchmark dataset correction.

Each affects different parts of an evidence envelope. A single generic “updated” relation loses useful semantics.

## 8. Counterevidence / limits

The Stage does not quantify how much each revision changed aggregate rankings or downstream conclusions. Such effects require reruns on multiple versions and are `NOT_EXECUTED`.

## 9. Repository relation

`DIRECTLY_RELEVANT`

This Part strongly supports forward-only state transitions, explicit dataset/benchmark/tool versions, and `NOT_COMPARABLE` as a legitimate result.

## 10. Current-repository implication

No defect established. Candidate future audit question: whether claim/evidence records preserve enough benchmark/data/tool revision identity for later reconciliation.

## 11. Part conclusion

`SUPPORTED_OBSERVATION`

Evaluation claims are **stateful**. A benchmark name without version/revision/execution provenance is often insufficient for longitudinal comparison.
