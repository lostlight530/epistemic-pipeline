# Agent Guide — epistemic-pipeline

This file is the operational contract for agents modifying the repository. Capability authority is shared by `README.md`, `ARCHITECTURE.md`, `RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, and `MANIFEST.yaml`.

## 1. System identity

Canonical architecture:

```text
graphs/*.yaml
  -> core/engine.py
     -> role templates
     -> core/llm_harness.py
        -> LLMProvider.complete(...)
        -> LLMProvider.describe()
     -> core/gatekeeper.py::RuntimePolicyEvaluator
     -> core/confidence_net.py @ synthesize
     -> core/resilience.py
     -> core/run_tracer.py
     -> checkpoint@2

core/run_bundle.py
  -> core/provenance.py        epistemic-pipeline/prov@2
  -> claim-index@1             derived from claims_registry/evidence_chains
  -> process-disclosure@1      provider + declared human review
  -> core/evidence_envelope.py epistemic-pipeline/evidence-envelope@2
```

Executable graphs: `linear`, `parallel`, `diamond`. `adaptive` remains Experimental.

## 2. Repository-governance boundary

Do not introduce GitHub Actions, CI/CodeQL workflows, dependency-update bots, branch-protection assumptions, or merge-gate architecture as part of ordinary repository maintenance.

Local commands may exist as optional maintenance tools. They are not the epistemic architecture and do not establish scientific validity.

Historical 2026-08-05 design material is superseded where it conflicts with the current 2026-08-26 contract.

## 3. Runtime vocabulary

Use these active terms:

```text
runtime policy / constraint evaluation
bounded heuristic score
numerical convergence
project trace
checkpoint identity
PROV-aligned lineage
claim-aware observability
process disclosure
Evidence Envelope
```

Historical compatibility terms such as `Gatekeeper`, `quality_gates`, `check_quality_gates` and `use_gatekeeper` may remain in code only where compatibility requires them. Do not use them to describe the current architecture.

## 4. Hard rules

1. **State machine first.** New integrated execution behavior must map to a state or explicitly version the state model.
2. **Graph identity is content-sensitive.** Checkpoint resume requires both `graph_id` and canonical `graph_sha256`.
3. **Runtime policy is explicit.** Current state files use `runtime_policies`; behavior comes from machine-readable `check` parameters, never parsed prose.
4. **Provider neutrality.** Vendor-specific SDK calls do not belong inside `StateMachineEngine`.
5. **Provider disclosure is declared, not guessed.** External providers may override `LLMProvider.describe()`; unknown vendor/model/version fields remain unknown.
6. **Mock honesty.** MockProvider output is a deterministic fixture and declares `external_model_call: false`; it is not model-performance evidence.
7. **Score honesty.** Historical confidence fields are bounded heuristic scores unless separate calibration evidence exists.
8. **Convergence honesty.** Numerical stability is not truth or consensus.
9. **Retry taxonomy.** Preserve transient/permanent distinction and explicit timeout limitations.
10. **Trace scope.** Project JSONL may align with selected OTel GenAI Development names but is not an OTel exporter.
11. **Local run identity.** Never substitute local run ID for provider conversation/session ID.
12. **PROV scope.** `prov@2` is project JSON aligned with W3C PROV concepts, not PROV-O RDF.
13. **Claim index scope.** `claim-index@1` carries identity + source/evidence refs, not claim truth or evidence sufficiency.
14. **No inferred human review.** Default `human_review` is `not_declared`; never turn missing metadata into `reviewed`.
15. **Payload minimization.** Evidence artifacts default to hashes and structural metadata; claim text is not embedded in the Evidence Envelope.
16. **R3 discipline.** Metadata/checkpoint/provenance/provider disclosure existence never counts as independent reproduction.
17. **Experimental stays Experimental.** Correctness fixes do not promote unwired modules.

## 5. Where to change what

| Goal | Primary files | Synchronize |
|---|---|---|
| graph semantics | `graphs/`, `core/dependency_graph.py`, `core/engine.py` | graph identity docs |
| state output | `states/`, `core/llm_harness.py` | runtime policies |
| runtime predicate | `states/`, `core/gatekeeper.py` | README/Architecture when public |
| provider execution | `core/llm_harness.py` or external adapter | preserve engine neutrality |
| provider disclosure | `LLMProvider.describe()` | Claim Audit / README / Manifest |
| score propagation | `core/confidence_net.py`, `core/knowledge_extractor.py` | confidence schema + semantics |
| retry/timeout | `core/resilience.py` | limitation docs |
| checkpoint | `core/engine.py` | profile/version + resume semantics |
| trace | `core/run_tracer.py` | OTel scope + integrity semantics |
| lineage | `core/provenance.py` | PROV profile version |
| claim audit | `core/run_bundle.py`, `core/evidence_envelope.py` | claim-index profile + no-payload rule |
| process disclosure | `core/llm_harness.py`, `core/run_bundle.py` | human-review/provider semantics |
| handoff | `core/evidence_envelope.py`, `core/run_bundle.py` | cross-repo contract |
| public boundary | README/Architecture/Research Contract/Claim Audit/MANIFEST | update together |

## 6. Current profiles

```text
epistemic-pipeline/engine@2
epistemic-pipeline/runtime-policy@1
epistemic-pipeline/confidence-heuristic@1
epistemic-pipeline/checkpoint@2
epistemic-pipeline/trace@2
epistemic-pipeline/prov@2
epistemic-pipeline/claim-index@1
epistemic-pipeline/process-disclosure@1
epistemic-pipeline/evidence-envelope@2
```

Breaking semantics require a profile version change rather than silent reinterpretation.

## 7. Claim audit and disclosure boundaries

The run bundle may expose:

```text
claim_id
claim_record_sha256
source_refs[]
evidence_refs[]
relations[]
provider/model declaration
human_review
```

Do not promote these fields into stronger claims:

```text
claim index ≠ truth graph
source ref ≠ source credibility
relation label ≠ verified entailment
provider/model identity ≠ output validity
human review ≠ peer review
```

Detailed semantics live in `CLAIM_AUDIT_CONTRACT.md`.

## 8. Experimental modules

Current concrete meanings:

- `anti_entropy.py`: normalized Shannon-entropy metric window;
- `convergence.py`: momentum-style heuristic updater;
- `infinite_regression.py`: bounded recursive termination controller;
- `neuro_symbolic.py`: priority-ordered local predicate dispatcher;
- `perception.py`: signal intake prototypes; HTTP/WebSocket do not perform network I/O;
- `thread_collapse.py`: bounded hypothesis score aggregator.

Do not infer capability from metaphorical filenames.

## 9. Local maintenance

Core runtime dependency:

```bash
python -m pip install pyyaml
```

Optional local check:

```bash
make test
```

Do not describe local check success as evidence for real-provider behavior, claim truth, network behavior, probability calibration, external standards certification, peer review, or independent reproduction.
