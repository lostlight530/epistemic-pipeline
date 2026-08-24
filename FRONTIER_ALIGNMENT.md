# Frontier Alignment — 2026-08-25

**Repository:** `epistemic-pipeline`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** structured scientific-agent execution, evidence synthesis, provenance, uncertainty semantics and neighboring 2026 research systems

## 1. Why this calibration exists

Several 2026 publications now make the repository's problem statement easier to locate in the broader research landscape.

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that trust in autonomous science depends on a complete, re-openable record of what was reasoned, done and measured so that scientific activity can be audited and corrected.
- *The past, present and future of self-driving laboratories* (Nature Reviews Chemistry, 31 Jul 2026) identifies **scalability, generalizability and provenance-complete experimentation** as the next major requirements for self-driving laboratories.
- *El Agente Gráfico: Structured Execution Graphs for Scientific Agents* (arXiv, 19 Feb 2026) places LLM scientific decision-making inside a type-safe execution environment, uses typed scientific objects and external knowledge graphs, and explicitly targets provenance and auditability rather than prompt-only orchestration.
- *DeepEvidence* (Nature Machine Intelligence, 2 Jul 2026) demonstrates evidence exploration and synthesis with an incrementally constructed evidence graph for transparent tracking, attribution and validation in biomedical research.

These are neighboring research directions, not evidence that this repository is scientifically validated or equivalent to any of them.

## 2. Current repository role

`epistemic-pipeline` occupies the **evidence-aware research execution and synthesis plane**:

```text
validated execution graph
        -> provider / role contract
        -> runtime-policy evaluation
        -> claim / evidence / conflict structures
        -> bounded heuristic score propagation
        -> trace + checkpoint
        -> PROV-aligned lineage
        -> evidence envelope
```

Its core question is not "can an agent produce a research answer?"

Its core question is:

> Can a research run expose enough machine-readable structure that claims, evidence, conflicts, execution state, numerical score semantics and lineage remain inspectable after the run ends?

## 3. Strongest neighboring paradigm: typed scientific execution

`El Agente Gráfico` is currently the closest architectural neighbor identified in this calibration.

### Shared direction

Both systems reject prompt-only orchestration as a sufficient scientific execution model and instead emphasize:

- explicit execution structure;
- persistent state outside raw conversation text;
- inspectable scientific objects/records;
- provenance and auditability;
- bounded interfaces between LLM decisions and deterministic execution.

### Different center of gravity

`El Agente Gráfico` centers on:

- type-safe scientific objects;
- tool execution and computational workflows;
- object-graph mapping;
- external knowledge-graph persistence;
- scientific-domain computation.

`epistemic-pipeline` centers on:

- claim / evidence / conflict separation;
- machine-readable runtime predicates;
- bounded heuristic score semantics;
- graph/checkpoint identity;
- trace semantics;
- PROV-aligned lineage;
- a portable Evidence Envelope for cross-tool handoff.

The overlap is meaningful, but the abstraction boundaries are not identical.

## 4. Evidence graphs are becoming a first-class research object

DeepEvidence provides a second important signal: evidence exploration increasingly benefits from explicit graph structures that preserve attribution and research progress instead of collapsing the entire process into a final generated answer.

This repository should therefore continue to treat evidence relations as durable research state rather than incidental prompt context.

However:

```text
evidence graph != truth graph
more sources != stronger evidence by definition
retrieval depth != epistemic certainty
attribution != source reliability
```

A graph makes relationships inspectable. It does not adjudicate the scientific world automatically.

## 5. Provenance as corrective infrastructure

The 20 Aug Nature Computational Science comment makes a useful distinction: provenance can support correction even when model internals are not fully interpretable.

That aligns with the repository's current split between:

```text
trace          what happened during execution
checkpoint     what successful execution state may be reused
provenance     how recorded entities/activities/agents relate
evidence       what cross-tool references and semantics travel forward
```

The repository intentionally keeps these as different artifacts because one generic "log" cannot faithfully answer all four questions.

## 6. Why bounded epistemic semantics still matter

The expanding autonomous-science ecosystem creates pressure to turn convenient numbers into stronger claims than they support.

This repository therefore keeps the following invariants:

```text
heuristic score != probability
numerical convergence != certainty
runtime-policy pass != scientific validity
provider structure != provider truthfulness
provenance != truth
checkpoint resume != reproduction
```

A particularly relevant 2026 citation-faithfulness study shows that the measured unsupported-citation rate of agentic scientific synthesis can vary substantially depending on the verifier and protocol. The broader lesson is directly compatible with this repository's design: a validation instrument must carry its own semantics and assumptions rather than being treated as an oracle.

## 7. Relation to scientific RAG systems

Systems such as PaperQA2 and DeepEvidence are strong upstream/adjacent applications for literature retrieval, evidence gathering and cited synthesis.

`epistemic-pipeline` should not duplicate their retrieval stack by default.

Its reusable layer is lower and more general:

- execution identity;
- evidence/claim contracts;
- conflict representation;
- runtime predicate evaluation;
- provenance/evidence handoff;
- explicit score semantics.

A literature agent, laboratory agent or domain-specific scientific agent could use equivalent contracts without this repository becoming a domain RAG product.

## 8. Cross-repository interpretation

```text
auto-doc-engine
artifact / source identity
        |
        v
epistemic-pipeline
claims / evidence / conflicts / execution / lineage
        |
        v
sci-render-kit
figure / uncertainty / communication evidence
```

The distinguishing system-level idea is not any one library feature. It is preservation of research semantics across transitions between **artifact**, **epistemic process** and **scientific communication**.

## 9. Research-engineering thesis

The repository's current thesis is:

> Scientific-agent systems become more auditable when execution state, claims, evidence, conflicts, numerical semantics and provenance are represented as explicit artifacts rather than being recoverable only from free-form conversation.

That thesis is deliberately weaker than claiming autonomous scientific reasoning is solved.

## 10. What should not be added merely because neighboring systems are advancing

This calibration does **not** justify:

- turning the pipeline into a generic LangGraph clone;
- adding a vector database or knowledge graph only for architectural fashion;
- presenting heuristic scores as calibrated probabilities;
- treating an LLM verifier as a scientific oracle;
- inferring truth from provenance completeness;
- coupling the canonical runtime to one model provider;
- adding GitHub-native CI/merge governance as scientific architecture.

## 11. Primary external references

Checked 2026-08-25:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). DOI: https://doi.org/10.1038/s43588-026-01035-4
2. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). DOI: https://doi.org/10.1038/s41570-026-00847-2
3. Bai J, Aldossary A, Swanick T, et al. **El Agente Gráfico: Structured Execution Graphs for Scientific Agents.** arXiv:2602.17902. https://arxiv.org/abs/2602.17902
4. Wang Z, Chen Z, Yang Z, et al. **Empowering biomedical evidence exploration and synthesis with deep knowledge graph research.** Nature Machine Intelligence 8, 1142–1156 (2026). DOI: https://doi.org/10.1038/s42256-026-01266-0
5. **Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis.** arXiv:2607.20527. https://arxiv.org/abs/2607.20527
6. W3C PROV overview: https://www.w3.org/TR/prov-overview/

## 12. Bottom line

The 2026 frontier is moving toward typed scientific execution, explicit evidence graphs and provenance-complete autonomous workflows. `epistemic-pipeline` remains differentiated by treating **epistemic semantics themselves**—claim/evidence/conflict separation, bounded score meaning, runtime predicates and cross-tool evidence lineage—as first-class engineering contracts.
