# Research Contract — 2026-08-23

Status: active architecture contract for repository claims, evidence flow, and research-run provenance.

`epistemic-pipeline` is the **research orchestration and evidence-synthesis plane** of the three-repository research toolchain. This contract separates implemented execution behavior from scientific interpretation and from future interoperability work.

## 1. Bounded system role

The current main chain is:

`validated graph -> role/provider execution -> state-specific quality gates -> evidence/confidence synthesis -> trace/checkpoint -> terminal result`

The repository can structure and inspect this process. It does not prove that model output is true, that a confidence value is a calibrated probability, or that a completed run is scientifically valid.

## 2. Evidence-unit contract

A research claim SHOULD carry enough context to distinguish the claim from its evidence and from the mechanism that transformed it. Preferred fields are:

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

`confidence_semantics` is mandatory whenever a value could be mistaken for a probability.

## 3. Gatekeeper semantics

`core/gatekeeper.py` currently loads `validators/epistemic.rules.yaml`, but the executable checks in `check_quality_gates()` are dispatched through explicit `state_id` prefix branches and recognized gate IDs/rule text.

Therefore:

- the rules YAML is **not** a generic executable policy interpreter;
- adding a new state prefix requires an explicit code path and contract test;
- a declared rule that has no executable branch must not be presented as enforced merely because it exists in YAML;
- structured-output validation reduces format drift but does not eliminate hallucination or establish semantic truth.

## 4. Confidence semantics

`core/confidence_net.py` implements a bounded weighted iterative heuristic inspired by simplified belief propagation. For each connected node, neighbor values are transformed by relationship type, combined by weights, and mixed with the node's initial value before clipping to `[0, 1]`.

This implementation is **not a Bayesian network posterior calculator** and does not turn heuristic inputs into calibrated probabilities. Convergence means that the configured numerical update reached its configured delta threshold within its iteration bound. It does not imply consensus, truth, robustness, or scientific certainty.

The optional temperature-scaling hook is likewise only a mechanism. A real calibration claim requires a named calibration dataset, target definition, metric, fitting procedure, and held-out evaluation.

## 5. Run provenance and recovery

A run should be interpreted through a bundle of mutually supporting records:

- graph/configuration identity;
- run identifier;
- node-level structured outputs;
- quality-gate outcomes;
- trace records and hash-chain head;
- checkpoint identity and resume status;
- provider/model metadata when a real provider exists;
- failure classification and unexecuted downstream scope.

A hash chain is tamper-evident under its declared construction; it is not an external timestamp, digital signature, or immutable storage guarantee.

## 6. OpenTelemetry GenAI boundary

The OpenTelemetry GenAI semantic conventions now live in the dedicated `semantic-conventions-genai` repository. The repository's tracer uses selected GenAI-style field names as a **naming alignment**, not as a claim of full OpenTelemetry SDK instrumentation or semantic-convention compliance.

In particular, a local `run_id` is a run/correlation identifier. It must not be interpreted as proof that the run corresponds to a provider-defined conversation/session. Future tracer evolution should keep project-local run identity distinct from optional provider conversation identity.

## 7. Reproducibility levels

The following are local project terms, not an external standard:

- **R0 — Traceable**: run and evidence references exist.
- **R1 — Replay-addressable**: graph/config/input identities, code revision, and deterministic fixture assumptions are recorded.
- **R2 — Environment-bounded**: provider/runtime/dependency versions and stochastic settings are recorded.
- **R3 — Reproduced**: an independent rerun has been performed and compared under a declared criterion.

Checkpoint availability or deterministic mock output alone does not justify `R3`.

## 8. Cross-repository handoff contract

Preferred input from `auto-doc-engine` or another source layer:

```text
artifact_id
content_sha256
source_refs[]
provenance_ref
validation_status
```

Preferred output for an upper-layer research bundle or `sci-render-kit`:

```text
run_id
graph_id_or_digest
claims_registry_ref
evidence_registry_ref
confidence_semantics
trace_ref
trace_hash_head
checkpoint_ref
terminal_status
```

These are interoperability fields. The repositories remain independently runnable and are not claimed to have direct runtime coupling.

## 9. RO-Crate interoperability target

RO-Crate 1.3, published 2026-06-22, is a useful current target for packaging research objects and their contextual metadata. For `epistemic-pipeline`, RO-Crate 1.3 is **proposed interoperability only**.

A future mapping could represent inputs/outputs as data entities and a bounded research run as an action/provenance entity, but no current trace, checkpoint, or manifest should be called an RO-Crate without a conforming exporter and validation tests.

## 10. Scientific-integrity rules

1. Structured output is not truthful output by definition.
2. Numerical convergence is not epistemic certainty.
3. Heuristic confidence is not probability unless separately calibrated and validated.
4. A passed gate proves only the executable predicate that was actually evaluated.
5. Recovery/checkpoint success is not evidence that skipped external side effects were idempotent.
6. Observability naming alignment is not protocol/SDK compliance.
7. Experimental graphs remain experimental until wired into and verified through the canonical execution path.

## 11. Primary references

Retrieved 2026-08-23:

- RO-Crate 1.3 Specification: https://www.researchobject.org/ro-crate/1.3/
- FAIR Principle R1.2: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- OpenTelemetry GenAI semantic conventions repository: https://github.com/open-telemetry/semantic-conventions-genai
