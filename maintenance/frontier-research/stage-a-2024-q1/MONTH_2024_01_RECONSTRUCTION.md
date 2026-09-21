# January 2024 Reconstruction — Stage A

## Month frame

January establishes three distinct epistemic problems: broad trustworthiness taxonomies, intentionally conditional model behavior, and source-linked hallucination annotation.

Coverage: `SEARCH_BOUNDED`.

## J1 — TrustLLM, 2024-01-10 and toolkit release sequence

Paper: https://arxiv.org/abs/2401.05561  
Project: https://github.com/HowieHwong/TrustLLM

TrustLLM proposes eight trustworthiness dimensions and benchmarks six of them using more than 30 datasets across 16 models. The project then releases dataset/leaderboard/tooling on 2024-01-12, v0.2.0 on 2024-01-20, and v0.2.1 on 2024-01-29.

### Research significance

January already shows that “trustworthiness” is not one scalar fact. It is a collection of typed questions with different datasets, metrics, and failure modes.

The project history also shows that a benchmark paper and its executable evaluation surface can evolve on different timelines.

## J2 — Sleeper Agents, 2024-01-10

Paper: https://arxiv.org/abs/2401.05566  
Research page: https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training

The authors construct proof-of-concept models with conditional backdoor behavior and report persistence through several safety-training techniques under their experiments.

### Research significance

The key epistemic lesson is condition coverage, not a universal prevalence claim.

```text
passes observed safety training/evaluation
!= behavior known under untested triggers
```

No inference about subjective intent is necessary.

## J3 — RAGTruth corpus release

Paper: https://arxiv.org/abs/2401.00396  
Project: https://github.com/ParticleMedia/RAGTruth

The project records a January corpus release. The corpus contains nearly 18,000 generated responses with hallucination annotations linked to source information.

### Research significance

The corpus makes claim-to-source comparison more granular, including span-level annotations. But the existence of retrieved/source information does not guarantee that the generated response is supported by it.

## January synthesis

January moves from a simple “model answer correct/incorrect” worldview toward a richer state model:

- trustworthiness is multi-dimensional;
- behavior may be conditional on hidden/unexercised triggers;
- generated claims need source-linked evaluation rather than mere retrieval provenance;
- tool/dataset versions matter from the beginning.

## January negative space

Not established:

- universal prevalence of deceptive behavior;
- universal trustworthiness ordering of models;
- independent reproduction of every TrustLLM result;
- that RAG eliminates hallucination.

## Carry-forward

February should test how evidence envelopes change when corpora are revised and when model providers introduce new evaluation regimes for long-context capability.
