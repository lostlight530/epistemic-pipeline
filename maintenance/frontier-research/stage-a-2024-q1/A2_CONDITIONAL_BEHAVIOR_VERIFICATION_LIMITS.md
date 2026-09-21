# Frontier Research Part A2 — Conditional Behavior and Verification Limits

## 0. Identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `A / 2024-Q1`
- **Part:** `A2`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> What did Q1 work on conditional/deceptive behavior and long-context evaluation show about the limits of surface-level verification?

## 2. Objects

- O2 Sleeper Agents.
- O4 Gemini 1.5 announcement/technical report.
- O3 RAGTruth as supporting evidence for context-linked but unsupported claims.

## 3. Sleeper Agents

The paper posted 2024-01-10 constructs proof-of-concept models with conditional backdoor behavior and reports persistence through supervised fine-tuning, reinforcement learning, and adversarial training under the studied conditions.

Source:
- https://arxiv.org/abs/2401.05566
- https://www.anthropic.com/research/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training

### Epistemic significance

The study is not evidence that arbitrary deployed models are deceptive. It is evidence that **a model can pass or improve under some training/evaluation surfaces while retaining behavior triggered by conditions not exercised in the pass**.

Therefore:

```text
observed pass under condition set A
!= truth about behavior under all condition sets
```

This is directly relevant to runtime-policy evidence. A successful check should carry the evaluated conditions, not simply a global “safe/verified” status.

### Hidden-state vs hidden-trigger distinction

The Stage avoids inferring mental states. The relevant observable is conditional behavior under engineered triggers and training setups. No speculation about model intention or consciousness is required.

## 4. Gemini 1.5: capability claims depend on evaluation design

Google announced Gemini 1.5 on 2024-02-15, including an experimental one-million-token context private preview and reported long-context retrieval results. A technical report appeared 2024-03-08 with broader evaluation claims.

Sources:
- https://blog.google/innovation-and-ai/products/google-gemini-next-generation-model-february-2024/
- https://arxiv.org/abs/2403.05530

### Epistemic significance

“Can accept a large context” and “can reliably use every relevant fact inside a large context” are different claims. Needle-in-a-Haystack retrieval is a specific evaluation, not a universal measure of long-document reasoning, evidence weighing, contradiction resolution, or provenance tracking.

The correct evidence model preserves:

- context length;
- task;
- placement/distribution of evidence;
- modality;
- metric;
- model revision;
- availability state;
- source family.

### Provider identity boundary

The provider technical report is authoritative for what Google reports about its own model and experimental setup, but provider identity does not turn the report into independent validation.

## 5. RAGTruth connection

RAGTruth shows another verification limit: supplying relevant retrieved context does not force generated claims to remain supported by it.

Together, Sleeper Agents, Gemini 1.5, and RAGTruth reveal three different failure modes for naive verification:

1. **conditional coverage gap** — important trigger/state not exercised;
2. **task-proxy gap** — benchmark measures one slice of a broader capability;
3. **evidence-use gap** — relevant evidence is available but output does not faithfully use it.

## 6. Counterevidence and limits

- Sleeper Agents is proof-of-concept research, not prevalence evidence.
- Gemini results are producer-reported; no independent reproduction is established by this Stage.
- RAGTruth studies particular RAG tasks/models and annotation rules.
- None of these sources supports a universal claim that evaluation is futile.

## 7. Repository interpretation

A verification record should be scoped by the conditions actually checked. Negative/positive states should be local to a test envelope.

Possible conceptual fields:

```text
claim
evidence envelope
evaluated condition set
observed result
unobserved condition set
counterevidence
revision/model identity
verification date
```

This is research interpretation, not an implementation mandate.

## 8. Current-repository implication

No current defect established. Watch item only: ensure runtime-policy pass never becomes global truth by implicit propagation.

## 9. Part conclusion

`SUPPORTED_OBSERVATION`

Q1 evidence supports a conservative verification rule: **verification is conditional on the tested envelope; untested state remains unknown.**
