# Architecture — Epistemic Pipeline

> Calibrated 2026-08-27. This document describes repository runtime/evidence semantics, not GitHub platform governance.

[README](README.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md)

## 1. Thesis: research execution is an evidence-bearing state-transition system

The repository separates concerns that generic “multi-agent workflow” language often collapses:

1. **epistemic state** — what research phase is being performed;
2. **dependency structure** — which prior state outputs are available;
3. **provider contract** — how structured outputs enter the runtime;
4. **runtime policy** — which explicit machine predicates are evaluated;
5. **claim/evidence/conflict structure** — what research relations are represented;
6. **score semantics** — what bounded numerical signals mean and do not mean;
7. **recovery identity** — which graph definition a checkpoint belongs to;
8. **execution trace** — what runtime events occurred;
9. **lineage** — how recorded entities/activities/agents relate;
10. **claim verification record** — which evidence/check/conflict/score observations exist for each claim;
11. **handoff envelope** — how downstream tools reference the run without copying payloads;
12. **upstream context** — which prior artifacts/evidence were declared as inputs.

The main design question is:

> Can a run explain its inputs, transitions, claim/evidence relations, constraints, score evolution, conflicts, recovery identity and evidence artifacts without pretending process correctness equals scientific truth?

## 2. Canonical Day-4 runtime/evidence flow

```text
[upstream artifact/evidence refs]
              ↓
[Graph YAML]
  duplicate/missing-dependency/cycle/reachability checks
  graph_id + canonical SHA-256
              ↓
[StateMachineEngine @2]
              ↓
[Role Binding + LLMProvider]
              ↓
[RuntimePolicyEvaluator @1]
              ↓
[claim / evidence / conflict structures]
              ↓
[initial heuristic scores @ verify]
              ↓
[final heuristic scores @ synthesize]
              ↓
[Trace @2] + [Checkpoint @2]
              ↓
[PROV-aligned lineage @2]
              ↓
[Claim Verification @1]
              ↓
[Evidence Envelope @2]
```

`run_bundle.py` composes these surfaces. It does not redefine scientific validity.

## 3. Graph and recovery identity

### 3.1 DAG semantics

`core/dependency_graph.py` checks:

- duplicate node IDs;
- unknown dependencies;
- cycles;
- reachability.

Executable repository graphs remain `linear`, `parallel`, and `diamond`. `adaptive.yaml` remains Experimental.

### 3.2 Graph digest

`StateMachineEngine` computes a canonical SHA-256 over parsed graph structure.

`checkpoint@2` stores:

```text
graph_id
graph_sha256
```

Resume requires both to match. Legacy checkpoints without digest identity are intentionally ambiguous and rejected.

Checkpoint success is not independent reproduction and does not prove external side-effect idempotency.

## 4. Provider and state contracts

`core/llm_harness.py` keeps provider concerns outside the state machine:

```text
LLMProvider.complete(system, user, schema) -> dict
LLMProvider.describe() -> bounded provider/process metadata
```

`MockProvider` remains deterministic synthetic fixture data. It is not evidence of real-model research quality.

Provider disclosure can expose fields such as provider/model/version/mode, but:

```text
provider string != verified provider identity
provider identity != output validity
model version != scientific competence proof
```

State YAML defines role bindings, outputs and machine-readable `runtime_policies`. Human-readable entry/exit/transition prose remains explanatory unless an executable mechanism exists.

## 5. Runtime-policy architecture

`core/gatekeeper.py` retains its historical filename/API aliases for compatibility, but the active semantic class is:

```text
RuntimePolicyEvaluator
epistemic-pipeline/runtime-policy@1
```

Example:

```yaml
runtime_policies:
  - id: claim_extraction
    check: non_empty
    field: claims_registry
```

The evaluator never parses prose to invent behavior. Unknown checks fail explicitly.

A policy success establishes only the declared predicate over the current structured output.

```text
runtime policy pass != source truth
runtime policy pass != scientific validity
runtime policy pass != peer review
```

## 6. Claim / evidence / conflict plane

The canonical provider/state contract keeps three research objects separate:

```text
claims_registry
evidence_chains
conflict_registry
```

This avoids collapsing all research state into one fluent synthesis string.

### Evidence relation boundary

An evidence chain can establish that a declared reference relation exists in the runtime data structure.

It cannot by itself establish:

- evidence sufficiency;
- source credibility;
- correct interpretation;
- causal validity;
- statistical validity;
- claim truth.

### Conflict boundary

A conflict record preserves disagreement/limitation context. Absence of a conflict record is not evidence that a claim is correct.

## 7. Bounded score semantics

Historical `confidence_*` vocabulary remains in compatibility surfaces, but active semantics are:

> **bounded heuristic scores in `[0,1]`, not calibrated probabilities**

### 7.1 Initial score

The verify state may emit `confidence_seed` / score seed values.

`claim-verification@1` records these as `heuristic_scores.initial`.

### 7.2 Final score

The synthesize stage can apply the bounded weighted score network.

`claim-verification@1` records resulting `confidence_network.final` values as `heuristic_scores.final` when available.

### 7.3 Interpretation

```text
initial score != prior probability
final score != posterior probability
score increase != truth probability increase
numerical convergence != certainty
```

`core/calibration.py` supplies a monotonic temperature transform. It becomes a probability-calibration claim only with labelled fitting and independent evaluation under a declared objective.

## 8. Reliability without overclaiming

### Retry

`core/resilience.py` distinguishes transient/permanent errors and can use exponential backoff + jitter.

Unknown exceptions are not automatically transient.

### Timeout

Caller-side thread timeout returns control but cannot forcefully kill an already running Python worker thread. External side effects need their own cancellation/idempotency design.

### Checkpoint

Successful node outputs are atomically persisted for compatible graph identity.

Resume is recovery/reuse, not independent reproduction.

## 9. Trace plane

`core/run_tracer.py` emits:

```text
epistemic-pipeline/trace@2
```

Project-local identity:

```text
epistemic.run.id
epistemic.node.id
epistemic.stage
```

The trace may reuse selected OpenTelemetry GenAI naming where appropriate, but it is not an OTel SDK/exporter/span implementation.

A local run ID is not a provider conversation/session ID.

The `prev_hash` chain checks internal sequence/hash consistency of records currently present. Without an external anchor/signature/transparency log, it is not a universal tamper-proof ledger.

## 10. PROV-aligned lineage plane

`core/provenance.py` implements:

```text
epistemic-pipeline/prov@2
```

It uses W3C PROV concepts such as:

- Entity;
- Activity;
- SoftwareAgent;
- `used`;
- `wasGeneratedBy`;
- `wasDerivedFrom`;
- `wasAssociatedWith`.

Serialization is project-owned JSON, **not PROV-O RDF**.

The profile records hashes and structural metadata without duplicating complete research payloads by default.

## 11. Claim Verification plane

`core/claim_audit.py` implements:

```text
epistemic-pipeline/claim-verification@1
```

This is deliberately separate from both execution trace and PROV lineage.

For each claim it can record:

```text
claim_id
origin_state_id
claim_record_sha256
source_refs[]
evidence_refs[]
evidence_relations[]
internal_consistency observation
cross_source observation
conflict records
heuristic_scores.initial
heuristic_scores.final
audit_state
truth_claim=false
```

### 11.1 Audit states

Current descriptive states:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

These states report **what audit structure exists**, not scientific acceptance.

The repository intentionally does not expose `verified=true`.

### 11.2 Why no accepted/rejected labels

Systems such as Brain Researcher use scientific-review outcomes such as accepted, qualified, revised, blocked, rejected and deferred.

That is useful evidence that claim qualification should be first-class, but those labels assume a review authority/methodology this repository does not implement.

Therefore `claim-verification@1` stops at descriptive structural/process audit states.

### 11.3 Claim payload minimization

Full claim prose is not copied into the claim-audit sidecar. Claim identity uses IDs/hashes and references back to canonical run/checkpoint artifacts.

## 12. Evidence Envelope plane

`core/evidence_envelope.py` remains:

```text
epistemic-pipeline/evidence-envelope@2
```

The envelope is a small project-owned cross-tool index. It can reference:

```text
graph
trace
checkpoint
provenance
claim-audit
```

and include:

- claim index;
- provider/human-review disclosure;
- upstream artifact/evidence refs;
- reproducibility semantics;
- scientific-boundary flags.

The envelope does not copy the claim-audit contents. It references them.

This separation keeps:

```text
PROV = lineage
claim audit = claim-specific observations
Evidence Envelope = handoff/index
```

## 13. Upstream-reference plane

`run_bundle.py` accepts repeatable:

```text
--upstream-artifact-ref
--upstream-evidence-ref
```

The Evidence Envelope treats references conservatively:

- existing local files may be hashed;
- URI references remain opaque and are not dereferenced;
- unresolved strings remain explicit unresolved/opaque refs.

This enables loose coupling to `auto-doc-engine/artifact-record@1`.

No upstream reference transfers scientific validity automatically.

## 14. Cross-repository Day-4 architecture

```text
auto-doc-engine
  artifact-record@1
        ↓
epistemic-pipeline
  upstream refs
  claim-verification@1
  evidence-envelope@2
        ↓
sci-render-kit
  claim_audit_ref
  figure-claim-audit@1
  figure-evidence@2
```

The repositories remain independently runnable. Interoperability is expressed by artifacts/references, not hidden imports.

## 15. Experimental plane

The following remain outside the canonical engine:

| File | Actual implementation semantics |
|---|---|
| `anti_entropy.py` | normalized Shannon-entropy metric window |
| `convergence.py` | momentum-style bounded heuristic updater |
| `infinite_regression.py` | bounded recursive transformation + termination reporting |
| `neuro_symbolic.py` | priority-ordered caller predicate dispatch |
| `perception.py` | signal-source prototypes; HTTP/WebSocket are descriptor simulations |
| `thread_collapse.py` | bounded heuristic hypothesis ranking/aggregation |

Historical filenames are compatibility surfaces, not capability proofs.

## 16. Global frontier calibration

The Day-4 architecture is informed by:

- Nature's 2026 autonomous-science provenance argument;
- artifact-centered claim-aware observability;
- EarthVerse evidence-chain consistency failures;
- Brain Researcher claim-scope/review methodology;
- From Trajectories to Evidence's distinction between completed trajectories and admitted evidence;
- evolving OpenTelemetry GenAI naming;
- W3C PROV lineage concepts.

External research signals justify design questions, not scientific validation or conformance claims.

See `FOUR_DAY_CONSOLIDATION.md` and `FRONTIER_ALIGNMENT.md`.

## 17. Scientific-integrity invariants

```text
Structured output != truthful output
Runtime policy pass != scientific validity
Evidence binding != evidence sufficiency
Consistency observation != truth
Conflict absence != correctness
Heuristic score != calibrated probability
Numerical convergence != epistemic certainty
Audit state != scientific acceptance
Provider identity != output validity
Human review != peer review
Trace integrity != immutable external audit log
Provenance != truth
Checkpoint resume != independent reproduction
```

## 18. Maintenance architecture

Optional local checks may be used as maintenance aids.

The repository architecture explicitly does **not** require GitHub Actions, CI, CodeQL, dependency bots, branch-protection rules or merge gates.

The 2026-08-27 consolidation does not use test execution as completion evidence.
