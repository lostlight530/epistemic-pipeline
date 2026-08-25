# Research Contract — 2026-08-26

Status: active contract for repository claims, evidence flow, runtime semantics, recovery identity, claim-aware audit, process disclosure and cross-repository handoff.

`epistemic-pipeline` is the **research orchestration and evidence-synthesis plane** of the three-repository research toolchain.

## 1. Bounded role

The current chain is:

```text
validated graph
  -> provider/role execution
  -> runtime-policy evaluation
  -> bounded score synthesis
  -> trace + digest-bound checkpoint
  -> PROV-aligned lineage
  -> claim index + process disclosure
  -> evidence envelope
```

The repository can structure, execute and record this process. It does not prove model truth, source reliability, calibrated probability, peer review, causal validity or scientific correctness.

## 2. Evidence-unit contract

A research claim SHOULD carry enough context to separate assertion, evidence and transformation history:

```text
claim_id
source_refs[]
evidence_refs[]
state_id
run_id
confidence_value
confidence_semantics
validation_status
trace_ref
```

Whenever a bounded numeric value might be mistaken for probability, `confidence_semantics` or equivalent score semantics MUST travel with it.

## 3. Runtime-policy contract

Current state YAML uses `runtime_policies`.

Executable behavior comes from explicit machine fields such as:

```text
check
field
min / max
required_fields
required_keys
```

Human `rule` prose is descriptive and is never parsed to decide behavior.

The active evaluator is `RuntimePolicyEvaluator`. The historical names `Gatekeeper`, `check_quality_gates`, `use_gatekeeper` and legacy state key `quality_gates` remain only for compatibility.

A policy result means only that a declared predicate evaluated over the current structured output. It does not establish semantic truth or scientific validity.

## 4. Score contract

`core/confidence_net.py` implements a synchronous bounded weighted heuristic update over claim nodes and typed relationships.

Its values:

- are constrained to `[0,1]`;
- may originate from provider/mock fixture scores;
- can be influenced by `supports`, `contradicts`, `related` and `derives` edges;
- are **not Bayesian posteriors**;
- are **not calibrated probabilities by default**.

`converged=True` means only that the numerical update reached the configured delta threshold within the configured iteration limit.

`core/calibration.py` provides a monotonic temperature-scaling transform. A probability-calibration claim requires a named labelled dataset, target definition, fitted temperature, evaluation metric and held-out evidence.

## 5. Graph and checkpoint identity

Graph human identity and executable identity are distinct:

```text
graph_id          human/project identifier
graph_sha256      canonical hash of parsed graph structure
```

`checkpoint@2` records both. Resume requires both to match the current graph.

A legacy checkpoint without graph digest is rejected as ambiguous. This prevents same-name changed graphs from silently reusing historical node results.

Checkpoint success is not independent reproduction and does not establish idempotency of external side effects.

## 6. Trace contract

`epistemic-pipeline/trace@2` is project JSONL.

The tracer may reuse selected OpenTelemetry GenAI field names where semantically appropriate, but it is not an OTel SDK/exporter implementation.

As rechecked 2026-08-24, the OpenTelemetry GenAI agent/framework span conventions remain **Development**.

Project-local identity remains distinct:

```text
epistemic.run.id
epistemic.node.id
epistemic.stage
```

A local `run_id` MUST NOT be treated as a provider-defined conversation/session identifier unless a real provider explicitly supplies and names such an identifier.

The internal SHA-256 chain can detect inconsistencies among records currently present. Without an external anchor it does not prove append-only storage or detect every possible tail-truncation history.

## 7. PROV contract

`epistemic-pipeline/prov@2` uses W3C PROV concepts and relation names in project JSON:

```text
Entity
Activity
SoftwareAgent
used
wasGeneratedBy
wasDerivedFrom
wasAssociatedWith
```

It is PROV-aligned, not a PROV-O RDF serializer.

By default it stores canonical/file hashes and structural metadata rather than full node research payloads.

Provenance records **how recorded artifacts relate**. Provenance does not make the underlying claim true.

## 8. Claim-aware audit contract

`epistemic-pipeline/claim-index@1` is a payload-minimizing audit surface built from structured `claims_registry` and `evidence_chains` outputs.

For each discoverable claim it can preserve:

```text
claim_id
state_id
claim_record_sha256
source_refs[]
evidence_refs[]
relations[]
```

The claim record hash identifies the canonical structured record observed in the run. The Evidence Envelope does not embed claim text.

Hard boundary:

```text
claim index != truth graph
claim hash != semantic truth
source reference != source credibility
evidence reference != evidence sufficiency
relation label != verified entailment
```

The index exists so downstream tools can discover claim/evidence relationships without copying every provider payload.

## 9. Provider and human-review disclosure

`LLMProvider.describe()` is an optional process-disclosure hook.

The base implementation knows only the Python provider class and leaves vendor/model/version unknown. External integrations may explicitly declare those values. Unknown fields MUST NOT be guessed.

The built-in `MockProvider` declares itself as a deterministic synthetic fixture and records `external_model_call: false`.

`core/run_bundle.py` also accepts a declared human-review state:

```text
reviewed
partial
not_reviewed
not_declared
```

Default: `not_declared`.

These values are process metadata only:

```text
provider identity != output authenticity proof
model name != model capability proof
human review != peer review
human review != truth
process disclosure != scientific validity
```

## 10. Evidence Envelope contract

`epistemic-pipeline/evidence-envelope@2` is the preferred cross-tool handoff object.

It can reference:

```text
graph
trace
checkpoint
provenance
```

with SHA-256 identity and active profile declarations.

Version 2 additionally carries:

```text
claim_observability
process_disclosure
```

and explicitly records:

```text
confidence_semantics
reproducibility.level
scientific_validity_claim
payloads_embedded
```

The envelope remains payload-minimizing:

```text
payloads_embedded: false
claim_observability.payload_text_embedded: false
```

The default reproducibility label is **R1 — replay-addressable**, not R3.

## 11. Reproducibility levels

Local project terminology:

- **R0 — Traceable**: run/evidence references exist.
- **R1 — Replay-addressable**: graph/config/input identities and intended replay context are addressable.
- **R2 — Environment-bounded**: runtime/provider/dependency versions and stochastic settings are also recorded.
- **R3 — Reproduced**: an actual separate rerun was performed and compared under a declared criterion.

Checkpoint availability, deterministic mock output, provider metadata, or provenance metadata alone does not justify R3.

## 12. Cross-repository contract

Preferred input from `auto-doc-engine` or another source layer:

```text
artifact_id
content_sha256
source_refs[]
provenance_ref
validation_status
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

Preferred output toward `sci-render-kit` or another communication layer:

```text
run_id
graph_id
graph_sha256
evidence_envelope_ref
provenance_ref
claim_index_profile
claim_refs[]
evidence_refs[]
confidence_semantics
provider_disclosure
human_review
terminal_status
```

These fields define interoperability. They do not imply the repositories import or invoke one another directly.

## 13. RO-Crate target

RO-Crate 1.3 remains the current interoperability target for packaged research objects. `epistemic-pipeline` does **not** currently emit an RO-Crate.

A downstream packager may map the Evidence Envelope, PROV sidecar and run artifacts into an RO-Crate. Such a package must not be called an RO-Crate merely because this repository produced JSON metadata.

## 14. Experimental contract

Experimental modules remain outside the canonical engine. Their names are historical compatibility surfaces; documentation must describe concrete implementation semantics.

In particular:

- repeated recursive state = cycle termination, not convergence;
- local predicate dispatch = rule evaluation, not formal neuro-symbolic theorem proving;
- HTTP/WebSocket prototype anchors currently perform no network I/O;
- hypothesis score aggregation = heuristic ranking, not truth selection;
- entropy/convergence prototypes expose descriptive numeric mechanisms only.

## 15. 2026-08-26 research alignment

Three recent signals reinforce the engineering direction without serving as external certification:

- **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents** (arXiv:2608.18312) argues that model-call logs are insufficient and that scientific agents need portable artifact/claim lineage as an audit layer.
- **EarthVerse** (arXiv:2608.23525) evaluates scientific agents through package-scoped investigations and reports a large gap between completing individual answer units and maintaining an end-to-end consistent chain across evidence, units, calculations and interpretation.
- Nature Computational Science's **Responsible and transparent use of AI in scientific publishing** (20 Aug 2026) emphasizes transparency, accountability and human oversight as AI becomes integrated through the research lifecycle.

This repository responds narrowly: make claim/evidence relations and provider/review context inspectable without treating those records as truth.

## 16. Scientific-integrity invariants

1. Structured output is not truthful output by definition.
2. Runtime-policy success is not scientific validity.
3. Numerical convergence is not epistemic certainty.
4. Bounded heuristic score is not probability unless independently calibrated and validated.
5. Claim indexing is not truth adjudication.
6. Provider/model identity is not output validity.
7. Human review is not peer review or scientific correctness.
8. Recovery success is not independent reproduction.
9. Trace hash consistency is not an externally anchored immutable log.
10. Provenance is not truth.
11. Experimental code is not an integrated capability merely because it exists or runs.

## 17. Primary references

Rechecked through 2026-08-26:

- RO-Crate 1.3: https://www.researchobject.org/ro-crate/1.3/
- FAIR Principle R1.2: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- OpenTelemetry GenAI semantic conventions: https://github.com/open-telemetry/semantic-conventions-genai
- W3C PROV overview: https://www.w3.org/TR/prov-overview/
- Nature Computational Science, *Provenance grounds trust in autonomous science*: https://www.nature.com/articles/s43588-026-01035-4
- Nature Computational Science, *Responsible and transparent use of AI in scientific publishing*: https://www.nature.com/articles/s43588-026-01043-4
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*: https://arxiv.org/abs/2608.18312
- *EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards*: https://arxiv.org/abs/2608.23525
