# Architecture — Epistemic Pipeline

> Calibrated 2026-08-24. This document describes repository runtime semantics, not GitHub platform governance.

## 1. Thesis: research execution is an evidence-bearing state-transition system

The repository separates concerns that generic “multi-agent workflow” language often collapses:

1. **epistemic state** — what research phase is being performed;
2. **dependency structure** — which prior state outputs are available;
3. **provider contract** — how structured outputs enter the runtime;
4. **runtime policy** — which explicit machine predicates are evaluated;
5. **score semantics** — what bounded numerical signals mean and do not mean;
6. **recovery identity** — which graph definition a checkpoint belongs to;
7. **lineage** — how graph, node outputs, trace and checkpoint relate;
8. **handoff** — how a downstream tool can reference the run without copying payloads.

The main design question is therefore:

> Can a run explain its inputs, transitions, constraints, numerical semantics, recovery identity and evidence artifacts without pretending that process correctness equals scientific truth?

## 2. Canonical runtime

```text
[Graph YAML]
    │
    ├─ duplicate/missing-dependency/cycle/reachability checks
    ├─ graph_id
    └─ canonical graph SHA-256
             ↓
[StateMachineEngine @2]
             ↓
[Role Binding + LLMProvider]
             ↓ structured mapping
[RuntimePolicyEvaluator @1]
             ↓
[Bounded heuristic score network @ synthesize]
             ↓
[Trace @2] + [Checkpoint @2]
             ↓
[Run Bundle]
     ├─ PROV-aligned lineage @2
     └─ Evidence Envelope @1
```

The modules remain separable. `run_bundle.py` composes them; it does not redefine scientific validity.

## 3. Graph and recovery identity

### 3.1 DAG semantics

`core/dependency_graph.py` checks:

- duplicate node identifiers;
- dependencies that reference unknown node IDs;
- cycles;
- reachability from root nodes.

Executable repository graphs remain `linear`, `parallel`, and `diamond`. `adaptive.yaml` remains an experimental specification and is not interpreted heuristically by the engine.

### 3.2 Graph digest

`StateMachineEngine` computes a canonical SHA-256 over parsed graph structure. `checkpoint@2` stores both:

```text
graph_id
graph_sha256
```

Resume requires both to match. This prevents a checkpoint from being reused merely because a changed graph retained the same human-readable ID.

Legacy checkpoints without `graph_sha256` are intentionally rejected as ambiguous.

## 4. Provider and state contracts

`core/llm_harness.py` keeps model-vendor concerns outside the state machine:

```text
LLMProvider.complete(system, user, schema) -> dict
```

`MockProvider` is a deterministic fixture. It is not evidence of real model performance.

State YAML defines role bindings, transition descriptions, outputs and active `runtime_policies`. Human-readable `entry_condition`, `exit_condition`, `transition.condition` and `rule` strings remain explanatory metadata unless a corresponding executable mechanism exists.

## 5. Runtime policy architecture

`core/gatekeeper.py` retains its filename and the historical `Gatekeeper` alias for compatibility, but the active class is:

```text
RuntimePolicyEvaluator
profile: epistemic-pipeline/runtime-policy@1
```

Current state files use:

```yaml
runtime_policies:
  - id: claim_extraction
    check: non_empty
    field: claims_registry
```

The evaluator never parses prose to infer behavior. Unknown `check` values fail explicitly instead of silently passing.

This is constraint evaluation, not a truth oracle. A policy success establishes only the declared predicate over the current structured output.

## 6. Bounded score semantics

### 6.1 Confidence compatibility vocabulary

Historical field names such as `confidence_seed` remain in parts of the provider/state contract for compatibility. Their active semantics are:

> bounded heuristic score in `[0,1]`, not calibrated probability

### 6.2 Propagation

`core/confidence_net.py` performs synchronous bounded weighted updates. Relationship types transform influence and weights; the initial score remains part of every update.

The algorithm reports:

```text
final scores
iteration count
last delta
numerical convergence flag
```

It is not a Bayesian network posterior calculator.

### 6.3 Temperature transform

`core/calibration.py` uses standard-library `math` for a monotonic logit-domain temperature transform. A transform becomes a real probability-calibration method only when the parameter is fitted and evaluated against labelled data under a declared calibration objective.

## 7. Reliability without overclaiming

### 7.1 Retry

`core/resilience.py` distinguishes transient and permanent failures and can retry transient failures with exponential backoff and jitter.

Unknown exceptions are not proof of transience. Retry policy is operational behavior, not epistemic evidence.

### 7.2 Timeout

Caller-side thread timeout returns control to the caller. Python cannot forcefully kill the underlying worker thread through this mechanism. External side effects may therefore continue after the caller observes timeout.

### 7.3 Checkpoint

Successful node results are atomically persisted. Resume reuses successful results only when checkpoint graph identity matches current graph identity.

Checkpoint success is **not** independent reproduction and does not guarantee external side-effect idempotency.

## 8. Trace semantics

`core/run_tracer.py` emits project-owned JSONL using profile:

```text
epistemic-pipeline/trace@2
```

It may reuse selected OpenTelemetry GenAI terminology where applicable. As of 2026-08-24, the GenAI agent/framework span semantic conventions remain **Development**.

Project-local identity uses:

```text
epistemic.run.id
epistemic.node.id
epistemic.stage
```

A local run ID is not substituted for provider conversation/session identity.

The SHA-256 `prev_hash` chain can establish internal sequence/hash consistency over records currently present. Without an external anchor, signature, transparency log or independently recorded head hash, it is not a universal tamper-proof log.

## 9. PROV-aligned lineage

`core/provenance.py` implements:

```text
epistemic-pipeline/prov@2
```

It adopts W3C PROV concepts:

- Entity;
- Activity;
- SoftwareAgent;
- `used`;
- `wasGeneratedBy`;
- `wasDerivedFrom`;
- `wasAssociatedWith`.

The serialization is project-owned JSON. It is **not PROV-O RDF**.

The profile records canonical/file graph hashes, node-output hashes, stage/status metadata and trace/checkpoint hashes without embedding complete research payloads by default.

## 10. Evidence Envelope

PROV answers lineage questions. A cross-tool handoff needs a smaller project-level index.

`core/evidence_envelope.py` implements:

```text
epistemic-pipeline/evidence-envelope@1
```

The envelope references available:

```text
graph
trace
checkpoint
provenance
```

with SHA-256 identity plus profile and semantic declarations. It explicitly records:

```text
confidence_semantics
reproducibility.level = R1
scientific_validity_claim = false
payloads_embedded = false
```

This is the preferred boundary for downstream research tooling such as `sci-render-kit`; it does not require direct runtime coupling between repositories.

## 11. Experimental modules

The following remain outside the canonical engine:

| File | Actual implementation semantics |
|---|---|
| `anti_entropy.py` | normalized Shannon-entropy metric window |
| `convergence.py` | momentum-style bounded heuristic updater |
| `infinite_regression.py` | bounded recursive transformation + termination reporting |
| `neuro_symbolic.py` | priority-ordered caller predicate dispatch |
| `perception.py` | signal-source prototypes; HTTP/WebSocket are descriptor simulations |
| `thread_collapse.py` | bounded heuristic hypothesis ranking/aggregation |

Names are compatibility surfaces, not capability proofs.

## 12. Cross-repository research architecture

The three research repositories form a conceptual chain:

```text
auto-doc-engine
  research material / artifact identity
        ↓
epistemic-pipeline
  claims / evidence / conflicts / bounded scores / lineage
        ↓
sci-render-kit
  scientific communication / uncertainty / accessibility / figure provenance
```

The repositories remain independently runnable. Interoperability is expressed through artifacts and contracts, not hidden imports.

## 13. Scientific-integrity invariants

```text
Structured output ≠ truthful output
Runtime policy pass ≠ scientific validity
Heuristic score ≠ calibrated probability
Numerical convergence ≠ epistemic certainty
Trace integrity ≠ immutable external audit log
Provenance ≠ truth
Checkpoint resume ≠ independent reproduction
```

These invariants take precedence over metaphorical module names or optimistic documentation.
