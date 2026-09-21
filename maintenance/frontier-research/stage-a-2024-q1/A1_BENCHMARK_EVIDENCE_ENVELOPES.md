# Frontier Research Part A1 — Benchmarks and Evidence Envelopes

## 0. Identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `A / 2024-Q1`
- **Part:** `A1`
- **Design:** `TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> How did Q1 2024 benchmarks and corpora define bounded evidence envelopes for trustworthiness, hallucination, and human preference?

## 2. Units of analysis

- O1 TrustLLM benchmark/toolkit.
- O3 RAGTruth corpus.
- O5 Chatbot Arena evaluation platform/paper.
- O6 WMDP benchmark, where relevant to evidence-envelope structure.

## 3. Discovery

Primary sources: arXiv/project repositories/platform papers. Same-origin sources are grouped.

## 4. Evidence

### TrustLLM

TrustLLM was posted 2024-01-10 and described a trustworthiness taxonomy across eight dimensions, with benchmark evaluation across six dimensions, 16 mainstream LLMs, and more than 30 datasets.

Project evidence records concrete Q1 toolkit state changes:

- 2024-01-12 dataset/leaderboard/toolkit release;
- 2024-01-20 v0.2.0;
- 2024-01-29 v0.2.1;
- 2024-03-20 v0.2.4 with bug fixes and Gemini Pro API support.

Sources:
- https://arxiv.org/abs/2401.05561
- https://github.com/HowieHwong/TrustLLM

### RAGTruth

RAGTruth constructs an annotated hallucination corpus for retrieval-augmented generation. The project repository states that the corpus was released in January 2024 and updated in February with more annotations and a new `implicit_true` metadata field.

Sources:
- https://arxiv.org/abs/2401.00396
- https://github.com/ParticleMedia/RAGTruth

### Chatbot Arena

The 2024-03-07 paper describes pairwise human preference evaluation using crowdsourced votes and analyzes more than 240K votes. It explicitly studies agreement with expert raters and statistical ranking methodology.

Source:
- https://arxiv.org/abs/2403.04132

### WMDP

WMDP, posted 2024-03-05, defines 3,668 multiple-choice questions as a **proxy** for hazardous knowledge and as a benchmark for unlearning methods.

Sources:
- https://arxiv.org/abs/2403.03218
- https://www.wmdp.ai/
- https://github.com/centerforaisafety/wmdp

## 5. Core observation: every benchmark has an evidence envelope

A benchmark result is meaningful only inside an envelope that includes:

```text
benchmark/dataset version
+ task/dimension definition
+ sample selection
+ model/version/configuration
+ prompting/evaluation protocol
+ annotation/judge procedure
+ metric/statistical method
+ execution date/state
```

TrustLLM makes this visible through multiple dimensions and datasets. RAGTruth makes it visible through source-linked, span-level annotation. Chatbot Arena makes it visible through pairwise votes and statistical aggregation. WMDP makes it visible by explicitly calling itself a proxy benchmark.

## 6. Evidence linkage is not sufficiency

RAGTruth is particularly instructive. A response can be connected to retrieved source information and still contain unsupported or contradictory claims. Therefore:

```text
retrieval performed != answer supported
evidence linked != evidence sufficient
source present in context != entailment
```

The February `implicit_true` metadata update further shows that “not explicitly mentioned in retrieved context” and “false” are not equivalent states. A claim may be true but unsupported by the supplied context. Epistemic state therefore needs more than a binary hallucination flag.

## 7. Benchmark dimensions are not interchangeable

TrustLLM separates truthfulness, safety, fairness, robustness, privacy, and machine ethics rather than collapsing them into one universal trust score. This reinforces a repository design principle: heterogeneous evidence dimensions should remain typed and should not be silently averaged into a false universal probability.

## 8. Human preference is a distinct evidence class

Chatbot Arena provides evidence about **human preference under a particular pairwise evaluation process**. It does not directly establish factual correctness, safety, scientific validity, or universal utility.

The correct relation is closer to:

```text
model response
--evaluated-by--> pairwise human preference process
--aggregated-into--> ranking estimate
```

not:

```text
ranked higher -> objectively truer
```

## 9. WMDP's proxy language matters

WMDP explicitly frames its questions as proxy measurement for hazardous knowledge. That wording should remain attached to downstream claims. A lower score after unlearning does not by itself prove removal of all hazardous capability or safe deployment.

## 10. Counterevidence / competing interpretations

- More benchmark dimensions can improve coverage but can also create false comprehensiveness if unmeasured dimensions disappear from view.
- More annotations can improve corpus quality but change comparability with earlier versions.
- Human-preference agreement can support ranking credibility without turning preference into factual correctness.
- Proxy benchmarks can be useful without being complete models of real-world risk.

## 11. Relation to repository

`DIRECTLY_RELEVANT / PARALLEL_CONVERGENCE`

The Stage strongly supports typed evidence envelopes, explicit benchmark versions, and preservation of proxy/metric semantics.

## 12. Current-repository implication

No current implementation or active-contract defect is established by this Part.

## 13. Part conclusion

`SUPPORTED_OBSERVATION`

Q1 2024 benchmark work repeatedly demonstrates that evaluation evidence is scoped, typed, and revision-sensitive. **A score is an observation under a protocol, not a portable truth value.**
