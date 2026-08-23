# Agent Guide — epistemic-pipeline

This file is the operational contract for agents modifying the repository. Capability authority is shared by `README.md`, `ARCHITECTURE.md`, `RESEARCH_CONTRACT.md`, and `MANIFEST.yaml`.

## 1. System identity

Canonical architecture:

```text
graphs/*.yaml
  -> core/engine.py
     -> role templates
     -> core/llm_harness.py
     -> core/gatekeeper.py::RuntimePolicyEvaluator
     -> core/confidence_net.py @ synthesize
     -> core/resilience.py
     -> core/run_tracer.py
     -> checkpoint@2

core/run_bundle.py
  -> core/provenance.py       epistemic-pipeline/prov@2
  -> core/evidence_envelope.py epistemic-pipeline/evidence-envelope@1
```

Executable graphs: `linear`, `parallel`, `diamond`. `adaptive` remains Experimental.

## 2. Repository-governance boundary

Do not introduce GitHub Actions, CI/CodeQL workflows, dependency-update bots, branch-protection assumptions, or merge-gate architecture as part of ordinary repository maintenance.

Local commands may exist as optional maintenance tools. They are not the epistemic architecture and do not establish scientific validity.

Historical 2026-08-05 design material is superseded where it conflicts with the current 2026-08-24 contract.

## 3. Runtime vocabulary

Use these active terms:

```text
runtime policy / constraint evaluation
bounded heuristic score
numerical convergence
project trace
checkpoint identity
PROV-aligned lineage
Evidence Envelope
```

Historical compatibility terms such as `Gatekeeper`, `quality_gates`, `check_quality_gates` and `use_gatekeeper` may remain in code only where compatibility requires them. Do not use them to describe the current architecture.

## 4. Hard rules

1. **State machine first.** New integrated execution behavior must map to a state or explicitly version the state model.
2. **Graph identity is content-sensitive.** Checkpoint resume requires both `graph_id` and canonical `graph_sha256`.
3. **Runtime policy is explicit.** Current state files use `runtime_policies`; behavior comes from machine-readable `check` parameters, never parsed prose.
4. **Provider neutrality.** Vendor-specific SDK calls do not belong inside `StateMachineEngine`.
5. **Mock honesty.** MockProvider output is a deterministic fixture, not model-performance evidence.
6. **Score honesty.** Historical confidence fields are bounded heuristic scores unless separate calibration evidence exists.
7. **Convergence honesty.** Numerical stability is not truth or consensus.
8. **Retry taxonomy.** Preserve transient/permanent distinction and explicit timeout limitations.
9. **Trace scope.** Project JSONL may align with selected OTel GenAI Development names but is not an OTel exporter.
10. **Local run identity.** Never substitute local run ID for provider conversation/session ID.
11. **PROV scope.** `prov@2` is project JSON aligned with W3C PROV concepts, not PROV-O RDF.
12. **Payload minimization.** Evidence artifacts default to hashes and structural metadata.
13. **R3 discipline.** Metadata/checkpoint/provenance existence never counts as independent reproduction.
14. **Experimental stays Experimental.** Correctness fixes do not promote unwired modules.

## 5. Where to change what

| Goal | Primary files | Synchronize |
|---|---|---|
| graph semantics | `graphs/`, `core/dependency_graph.py`, `core/engine.py` | graph identity docs |
| state output | `states/`, `core/llm_harness.py` | runtime policies |
| runtime predicate | `states/`, `core/gatekeeper.py` | README/Architecture when public |
| provider | `core/llm_harness.py` or external adapter | preserve engine neutrality |
| score propagation | `core/confidence_net.py`, `core/knowledge_extractor.py` | confidence schema + semantics |
| retry/timeout | `core/resilience.py` | limitation docs |
| checkpoint | `core/engine.py` | profile/version + resume semantics |
| trace | `core/run_tracer.py` | OTel scope + integrity semantics |
| lineage | `core/provenance.py` | PROV profile version |
| handoff | `core/evidence_envelope.py`, `core/run_bundle.py` | cross-repo contract |
| public boundary | README/Architecture/Research Contract/MANIFEST | update together |

## 6. Current profiles

```text
epistemic-pipeline/engine@2
epistemic-pipeline/runtime-policy@1
epistemic-pipeline/confidence-heuristic@1
epistemic-pipeline/checkpoint@2
epistemic-pipeline/trace@2
epistemic-pipeline/prov@2
epistemic-pipeline/evidence-envelope@1
```

Breaking semantics require a profile version change rather than silent reinterpretation.

## 7. Experimental modules

Current concrete meanings:

- `anti_entropy.py`: normalized Shannon-entropy metric window;
- `convergence.py`: momentum-style heuristic updater;
- `infinite_regression.py`: bounded recursive termination controller;
- `neuro_symbolic.py`: priority-ordered local predicate dispatcher;
- `perception.py`: signal intake prototypes; HTTP/WebSocket do not perform network I/O;
- `thread_collapse.py`: bounded hypothesis score aggregator.

Do not infer capability from metaphorical filenames.

## 8. Local maintenance

Core runtime dependency:

```bash
python -m pip install pyyaml
```

Optional local check:

```bash
make test
```

Do not describe local check success as evidence for real-provider behavior, network behavior, probability calibration, external standards certification, peer review, or independent reproduction.
