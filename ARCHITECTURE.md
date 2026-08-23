# Architecture — Epistemic Pipeline

## 1. Thesis: research execution is a governed state transition system

The repository separates four concerns that are often collapsed into a generic "multi-agent workflow":

1. **epistemic state** — what phase of research is being performed,
2. **dependency structure** — which evidence must exist before a state can run,
3. **execution contract** — what a provider must return and what gates must accept,
4. **evidence lineage** — how outputs, traces, and checkpoints can be tied back to the run that produced them.

The result is a research runtime whose main design question is not "how many agents exist?" but "can every transition be explained, gated, resumed, and traced?"

## 2. Runtime layers

```text
[Graph YAML]
    ↓ validate DAG / reachable nodes
[State Machine]
    ↓ role binding
[Provider Contract]
    ↓ structured output
[Gatekeeper]
    ↓ accepted state result
[Confidence Network @ synthesize]
    ↓ convergence signal
[Checkpoint + JSONL Trace]
    ↓
[Audited Run Bundle]
    ↓
[PROV-aligned hash lineage]
```

### 2.1 Graph and state model

`core/engine.py` loads executable graphs whose nodes point to the five canonical states. `linear`, `parallel`, and `diamond` are executable DAGs. `adaptive.yaml` remains an experimental routing specification and is explicitly rejected by the engine rather than interpreted heuristically.

### 2.2 Provider and role contract

`core/llm_harness.py` separates the engine from any specific model vendor through `LLMProvider.complete(system, user, schema) -> dict`. `MockProvider` is the repository default and carries deterministic five-stage output contracts. Real providers are integrations, not implicit repository capabilities.

Role templates are loaded by state. They shape prompts but do not bypass state schemas or gates.

### 2.3 Gatekeeper and confidence semantics

Gatekeeper is part of the execution chain, not a reporting-only module. A missing required gate input or failed quality condition causes the node/run to fail.

At `synthesize`, the confidence network consumes upstream claim/conflict/confidence evidence and iterates to a convergence signal. In mock mode these values are **heuristic confidence signals**, not calibrated probabilities. `core/calibration.py` provides an optional monotonic temperature-scaling transform but does not fit a real calibration parameter from labelled data.

## 3. Reliability layer

### 3.1 Retry and timeout

`core/resilience.py` classifies transient vs permanent failures. Transient failures may retry with exponential backoff and jitter; permanent failures fail fast. Caller-side thread timeouts do not terminate the underlying Python worker thread, and the documentation must keep that limitation visible.

### 3.2 Checkpoints

Successful layer results are atomically persisted under `checkpoints/<run_id>/checkpoint.json`. Resume is same-graph and reuses successful states only. Cross-graph resume is fail-closed because state identity without graph identity is not sufficient evidence of equivalence.

### 3.3 Structured trace

`core/run_tracer.py` writes a project JSONL audit stream with a SHA-256 `prev_hash` chain. Applicable names reference the Development-grade OpenTelemetry GenAI agent conventions, including `gen_ai.operation.name`, but the file is not an OpenTelemetry exporter and its `start`/`end` records are not Span Event API objects.

This separation matters: **semantic naming alignment is not implementation conformance**.

## 4. Research provenance layer

### 4.1 Why provenance is separate from logging

A trace answers "what happened over time?" A checkpoint answers "what state can be resumed?" Provenance answers a different question: **what entities and activities produced this research artifact, and what did it depend on?**

The 2026-08-23 architecture therefore adds `core/provenance.py` and `core/run_bundle.py` rather than overloading the trace file.

### 4.2 `epistemic-pipeline/prov@1`

The profile adopts the W3C PROV starting-point model:

- **Entity** — dependency graph, node output, trace, checkpoint
- **Activity** — whole run and node execution
- **Agent** — epistemic-pipeline as a software agent

and the core relations:

- `used`
- `wasGeneratedBy`
- `wasDerivedFrom`
- `wasAssociatedWith`

The JSON sidecar is explicitly **PROV-aligned**, not PROV-O RDF. This avoids a false standards claim while preserving a clean path to future JSON-LD/RDF serialization if needed.

### 4.3 Privacy-minimising evidence

Provenance records canonical SHA-256 values and structural keys for node outputs by default. It does not duplicate the full research payload. This gives stable evidence identity without turning every provenance record into a second copy of sensitive or high-volume content.

Trace and checkpoint files are represented by file hashes when they exist. The run bundle also records whether the trace hash chain verifies.

## 5. Canonical entry points

Low-level engine:

```bash
python3 core/engine.py run graphs/linear.yaml
```

Audited research run:

```bash
python3 core/run_bundle.py graphs/linear.yaml
```

The wrapper does not replace `StateMachineEngine`; it composes engine output with trace/checkpoint evidence and provenance. This keeps execution and audit concerns separable while still offering a canonical audited workflow.

## 6. Verification architecture

`make test` is the repository contract. It runs the existing execution-chain suite plus provenance/run-bundle tests. `.github/workflows/ci.yml` executes the same contract under Python 3.12 for pull requests and main-branch pushes.

A green contract proves the tested deterministic boundaries. It does not prove a real external LLM provider, network availability, or calibrated real-world confidence.

## 7. Hard boundaries

- `adaptive` remains Experimental until it becomes an executable graph with tests.
- real LLM calls are not built into the default repository path.
- mock confidence values are not probabilities.
- OTel field reuse is naming alignment only.
- `epistemic-pipeline/prov@1` is not an RDF serializer.
- provenance hashes prove content identity relative to the recorded bytes/structure; they do not prove factual truth of a claim.
- experimental modules do not become integrated merely because they import or have demos.

## 8. Design direction

The architecture is moving from "multi-agent orchestration" toward a **governed research runtime**:

```text
state -> contract -> gate -> evidence -> recovery -> lineage
```

Future extensions should strengthen those six nouns before adding more agent personas or speculative modules.
