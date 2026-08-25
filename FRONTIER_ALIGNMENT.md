# Frontier Alignment — 2026-08-25 / 2026-08-26 delta

**Repository:** `epistemic-pipeline`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** structured scientific-agent execution, claim-aware observability, evidence synthesis, provenance, process disclosure, uncertainty semantics and neighboring 2026 research systems

## 1. Why this calibration exists

Several 2026 publications now make the repository's problem statement easier to locate in the broader research landscape.

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that trust in autonomous science depends on a complete, re-openable record of what was reasoned, done and measured so that scientific activity can be audited and corrected.
- *The past, present and future of self-driving laboratories* (Nature Reviews Chemistry, 31 Jul 2026) identifies **scalability, generalizability and provenance-complete experimentation** as the next major requirements for self-driving laboratories.
- *El Agente Gráfico: Structured Execution Graphs for Scientific Agents* (arXiv, 19 Feb 2026) places LLM scientific decision-making inside a type-safe execution environment, uses typed scientific objects and external knowledge graphs, and explicitly targets provenance and auditability rather than prompt-only orchestration.
- *DeepEvidence* (Nature Machine Intelligence, 2 Jul 2026) demonstrates evidence exploration and synthesis with an incrementally constructed evidence graph for transparent tracking, attribution and validation in biomedical research.
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (arXiv:2608.18312, 18 Aug 2026) argues that model-call logs are not enough and proposes portable claim/artifact lineage as an audit layer complementary to telemetry, PROV-O and RO-Crate.
- *EarthVerse* (arXiv:2608.23525, 24 Aug 2026) evaluates scientific agents on package-scoped investigations requiring heterogeneous evidence selection, transparent calculations, source reconciliation and provenance preservation; its reported results show a substantial gap between completing local answer units and maintaining an end-to-end consistent scientific chain.

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
        -> claim index + provider/review disclosure
        -> evidence envelope
```

Its core question is not "can an agent produce a research answer?"

Its core question is:

> Can a research run expose enough machine-readable structure that claims, evidence, conflicts, execution state, provider context, numerical score semantics and lineage remain inspectable after the run ends?

## 3. Strongest neighboring paradigm: typed scientific execution

`El Agente Gráfico` remains one of the closest architectural neighbors identified in this calibration.

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
- claim-aware audit references;
- provider/process disclosure;
- a portable Evidence Envelope for cross-tool handoff.

The overlap is meaningful, but the abstraction boundaries are not identical.

## 4. Claim-aware observability becomes a first-class layer

The 18 Aug claim-aware observability preprint sharpens a gap between ordinary telemetry and scientific auditability.

A generic trace can answer:

```text
operation X started
operation X ended
operation X failed
```

A scientific audit may also need:

```text
claim c17 existed
claim c17 referenced source s3
claim c17 referenced evidence segment e9
this run/provider path produced the surrounding structured outputs
```

That distinction motivates today's `claim-index@1` and `evidence-envelope@2` update.

The claim index is intentionally payload-minimizing. It carries identity and references, not prose, and therefore does not become a duplicate transcript store.

```text
claim index != truth graph
attached evidence != sufficient evidence
source reference != source reliability
claim record hash != semantic truth
```

## 5. EarthVerse and the end-to-end consistency problem

EarthVerse is especially useful because it evaluates scientific agents under package-scoped investigations rather than judging only final fluency.

Its benchmark structure requires agents to work across heterogeneous evidence, calculations, source differences and provenance. The reported gap between answer-unit accuracy and strict end-to-end success supports a key engineering distinction:

> Local step success does not imply a globally coherent research chain.

That is exactly why this repository keeps graph identity, runtime-policy results, claim/evidence structure, trace, checkpoint and provenance as separable evidence instead of collapsing them into a single `success=true` flag.

## 6. Process disclosure without oracle claims

Nature Computational Science's August 2026 editorial position emphasizes transparency, accountability and human oversight in AI-assisted research and publishing.

The repository now exposes two narrow mechanisms:

1. `LLMProvider.describe()` — a provider may declare provider/model/version metadata; the base class leaves unknown vendor/model fields unset instead of guessing.
2. `--human-review` in `core/run_bundle.py` — a caller may explicitly declare `reviewed`, `partial`, `not_reviewed`, or `not_declared`.

These are process records, not stronger scientific claims:

```text
provider identity != output authenticity proof
model name != capability proof
human review != peer review
human review != truth
```

## 7. Provenance as corrective infrastructure

The 20 Aug Nature Computational Science comment makes a useful distinction: provenance can support correction even when model internals are not fully interpretable.

That aligns with the repository's current split between:

```text
trace              what happened during execution
checkpoint         what successful execution state may be reused
provenance         how recorded entities/activities/agents relate
claim index        which claim identities point to which source/evidence refs
process disclosure which provider/review context was declared
evidence envelope  what cross-tool references and semantics travel forward
```

The repository intentionally keeps these as different artifacts because one generic "log" cannot faithfully answer all six questions.

## 8. Why bounded epistemic semantics still matter

The expanding autonomous-science ecosystem creates pressure to turn convenient numbers and validators into stronger claims than they support.

This repository therefore keeps the following invariants:

```text
heuristic score != probability
numerical convergence != certainty
runtime-policy pass != scientific validity
provider structure != provider truthfulness
claim index != truth graph
provenance != truth
checkpoint resume != reproduction
```

A particularly relevant 2026 citation-faithfulness study shows that the measured unsupported-citation rate of agentic scientific synthesis can vary substantially depending on the verifier and protocol. The broader lesson is directly compatible with this repository's design: a validation instrument must carry its own semantics and assumptions rather than being treated as an oracle.

## 9. Relation to scientific RAG systems

Systems such as PaperQA2 and DeepEvidence are strong upstream/adjacent applications for literature retrieval, evidence gathering and cited synthesis.

`epistemic-pipeline` should not duplicate their retrieval stack by default.

Its reusable layer is lower and more general:

- execution identity;
- evidence/claim contracts;
- conflict representation;
- runtime predicate evaluation;
- claim-aware observability;
- provider/process disclosure;
- provenance/evidence handoff;
- explicit score semantics.

A literature agent, laboratory agent or domain-specific scientific agent could use equivalent contracts without this repository becoming a domain RAG product.

## 10. 2026-08-26 engineering delta

Today the repository converts the new research signal into runtime-facing evidence contracts:

```text
LLMProvider.describe()
    -> bounded provider/model disclosure

run_bundle --human-review ...
    -> explicit review-state declaration

claims_registry + evidence_chains
    -> claim-index@1

prov@2 + trace@2 + checkpoint@2 + claim-index@1 + process-disclosure@1
    -> evidence-envelope@2
```

`evidence-envelope@2` keeps `payloads_embedded: false` and `claim_observability.payload_text_embedded: false`.

Detailed semantics are in `CLAIM_AUDIT_CONTRACT.md`.

## 11. Cross-repository interpretation

```text
auto-doc-engine
artifact / source identity + declared process context
        |
        v
epistemic-pipeline
claims / evidence / conflicts / execution / lineage / provider disclosure
        |
        v
sci-render-kit
figure / uncertainty / claim binding / communication evidence
```

The distinguishing system-level idea is not any one library feature. It is preservation of research semantics across transitions between **artifact**, **epistemic process** and **scientific communication**.

## 12. Research-engineering thesis

The repository's current thesis is:

> Scientific-agent systems become more auditable when execution state, claims, evidence, conflicts, provider context, numerical semantics and provenance are represented as explicit artifacts rather than being recoverable only from free-form conversation.

That thesis is deliberately weaker than claiming autonomous scientific reasoning is solved.

## 13. What should not be added merely because neighboring systems are advancing

This calibration does **not** justify:

- turning the pipeline into a generic LangGraph clone;
- adding a vector database or knowledge graph only for architectural fashion;
- presenting heuristic scores as calibrated probabilities;
- treating an LLM verifier as a scientific oracle;
- inferring truth from provenance completeness;
- treating provider/model disclosure as scientific validation;
- coupling the canonical runtime to one model provider;
- adding GitHub-native CI/merge governance as scientific architecture.

## 14. Primary external references

Checked through 2026-08-26:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. Nature Computational Science. **Responsible and transparent use of AI in scientific publishing.** 20 Aug 2026. https://doi.org/10.1038/s43588-026-01043-4
3. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). https://doi.org/10.1038/s41570-026-00847-2
4. Bai J, Aldossary A, Swanick T, et al. **El Agente Gráfico: Structured Execution Graphs for Scientific Agents.** arXiv:2602.17902. https://arxiv.org/abs/2602.17902
5. Wang Z, Chen Z, Yang Z, et al. **Empowering biomedical evidence exploration and synthesis with deep knowledge graph research.** Nature Machine Intelligence 8, 1142–1156 (2026). https://doi.org/10.1038/s42256-026-01266-0
6. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
7. Cui Z, et al. **EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
8. **Evaluating and Guarding Citation Faithfulness in Agentic Scientific Synthesis.** arXiv:2607.20527. https://arxiv.org/abs/2607.20527
9. W3C PROV overview: https://www.w3.org/TR/prov-overview/

## 15. Bottom line

The 2026 frontier is moving beyond generic tracing toward typed scientific execution, explicit evidence graphs, claim-aware audit relations and provenance-complete autonomous workflows. `epistemic-pipeline` remains differentiated by treating **epistemic semantics themselves**—claim/evidence/conflict separation, bounded score meaning, runtime predicates, provider disclosure and cross-tool evidence lineage—as first-class engineering contracts.
