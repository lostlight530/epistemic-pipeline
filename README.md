# Epistemic Pipeline

> Evidence-aware state-machine execution for research workflows, with explicit claim/evidence structure, runtime policy, recovery identity, provenance, claim verification, and cross-tool handoff.

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md) · [Customization](CUSTOMIZATION_GUIDE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md)

## Positioning

Epistemic Pipeline is not a framework for “several agents chatting in sequence”. It treats research execution as an inspectable state-transition system:

```text
discover -> analyze -> verify -> synthesize -> archive
```

The canonical path separates concerns that are often collapsed into one opaque agent trajectory:

```text
validated graph
    ↓
provider-neutral structured outputs
    ↓
runtime policy predicates
    ↓
claim / evidence / conflict structures
    ↓
bounded heuristic score propagation
    ↓
trace + checkpoint
    ↓
PROV-aligned lineage
    ↓
claim verification record
    ↓
evidence envelope
```

A completed run is not automatically scientific evidence. A structural check is not scientific verification. A score is not a probability. Provenance is not truth.

## Stable internal identifiers

Project-owned profile identifiers are intentionally **unversioned**. They are stable semantic names, not release numbers:

```text
epistemic-pipeline/engine
epistemic-pipeline/runtime-policy
epistemic-pipeline/trace
epistemic-pipeline/checkpoint
epistemic-pipeline/prov
epistemic-pipeline/confidence-heuristic
epistemic-pipeline/network-input
epistemic-pipeline/claim-index
epistemic-pipeline/claim-verification
epistemic-pipeline/process-disclosure
epistemic-pipeline/upstream-reference
epistemic-pipeline/evidence-envelope
epistemic-pipeline/reference-rules
```

External standard versions remain explicit where they actually matter. For example, W3C PROV terminology and OpenTelemetry semantic-convention names are external references; this repository does not invent versions for them and does not claim full standards conformance unless implemented and evidenced.

## Core modules

| Module | Role | Boundary |
|---|---|---|
| `core/dependency_graph.py` | DAG validation, deterministic topological structure and parallel groups | structural graph semantics only |
| `core/engine.py` | state execution, runtime policy, retry/timeout, checkpoint/resume | run success is not scientific validity |
| `core/llm_harness.py` | provider-neutral structured-output contract | repository ships only a synthetic `MockProvider`; real providers must be injected |
| `core/gatekeeper.py` | machine-readable runtime-policy predicates | not a scientific reviewer; historical `Gatekeeper` API remains compatibility-only |
| `core/confidence_net.py` | bounded weighted heuristic score propagation | `[0,1]` does not mean calibrated probability |
| `core/calibration.py` | monotone score transform | does not become empirical probability calibration without labelled fit/evaluation |
| `core/run_tracer.py` | JSONL trace with internal SHA-256 chain | not an OpenTelemetry exporter or tamper-proof ledger |
| `core/provenance.py` | PROV-aligned project JSON lineage | not PROV-O RDF or complete W3C serialization conformance |
| `core/claim_audit.py` | per-claim verification observations | never emits `verified=true` or a truth label |
| `core/evidence_envelope.py` | compact cross-tool handoff index | references evidence artifacts rather than duplicating all payloads |
| `core/run_bundle.py` | evidence-bearing wrapper | coordinates trace/checkpoint/provenance/claim audit/envelope |

Experimental modules remain separate from this canonical path unless explicitly documented as integrated.

## Runtime policy

State definitions use `runtime_policies`. The legacy `quality_gates` key remains a compatibility fallback only.

Rules execute through explicit machine checks such as:

```text
min_items
non_empty
every_item_fields
claim_evidence_ratio
numeric_min
numeric_max_exclusive
conflicts_have_fields
mapping_required_keys
```

Human-readable `rule` text is not interpreted as code. Unknown checks fail explicitly rather than being silently accepted.

A runtime-policy pass means only that the declared machine predicates passed for the current outputs.

```text
runtime policy pass != scientific validity
runtime policy pass != peer review
runtime policy pass != evidence credibility
```

## Claim and evidence model

The analyze stage can emit:

```text
claims_registry
evidence_chains
methodology_index
```

The verify stage can emit:

```text
internal_consistency_report
cross_source_matrix
conflict_registry
confidence_seed
coverage
```

The synthesize stage can emit the final bounded score-network result. These structures are retained separately because they answer different questions.

## Claim verification record

`core/claim_audit.py` emits `<run_id>.claim-audit.json` with profile:

```text
epistemic-pipeline/claim-verification
```

Each claim record can carry:

```text
claim_id
origin_state_id
claim_record_sha256
source_refs[]
evidence_refs[]
evidence_relations[]
internal-consistency observation
cross-source observation
conflicts[]
initial heuristic score
final heuristic score
audit_state
```

Current descriptive audit states are deliberately weak:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

They are not accepted/rejected scientific-review decisions.

```text
structurally_checked != scientifically verified
evidence_bound != evidence sufficient
no conflict recorded != truth
initial/final score != probability
score increase != probability increase
```

## Heuristic score semantics

`ConfidenceNetwork` preserves its historical class name for API continuity. Its actual semantics are bounded weighted heuristic propagation.

```text
score in [0,1] != calibrated probability
numerical convergence != certainty
threshold stability != truth
```

If the optional temperature transform is used without labelled empirical fitting, the output remains a score transform and explicitly carries `probability_calibration_claim: false`.

## Trace and checkpoint

Trace records use:

```text
epistemic.run.id
epistemic.node.id
epistemic.stage
gen_ai.operation.name
```

The use of `gen_ai.operation.name` is scoped naming alignment with OpenTelemetry GenAI semantic conventions. This repository is not an OTel exporter, does not claim OTel span compliance, and does not map the project run ID to a provider conversation ID.

The trace SHA-256 chain verifies internal linkage for records currently present. Without an externally anchored head/count it is not a tamper-proof ledger and may not detect every tail truncation.

Checkpoint resume requires the declared graph identity to match. It is a recovery/replay identity check, not proof that external tools or models will reproduce identical outputs.

## PROV-aligned lineage

`core/provenance.py` writes a project-owned JSON representation using PROV concepts:

```text
Entity
Activity
SoftwareAgent
used
wasGeneratedBy
wasDerivedFrom
wasAssociatedWith
```

It records graph/output/trace/checkpoint identities while avoiding full research-payload duplication.

```text
PROV-aligned != PROV-O RDF
lineage != truth
hash identity != semantic equivalence
```

## Evidence Envelope

`core/evidence_envelope.py` writes the stable handoff profile:

```text
epistemic-pipeline/evidence-envelope
```

It references:

```text
graph
trace
checkpoint
provenance
claim verification
claim index
provider/process disclosure
upstream artifact refs
upstream evidence refs
```

Existing local upstream refs receive file SHA-256 identity. URI or opaque refs are retained without network dereferencing.

The envelope stays compact. It does not become a second copy of every node payload.

## Evidence-bearing CLI

```bash
python core/run_bundle.py graphs/linear.yaml \
  --human-review partial \
  --upstream-artifact-ref ../auto-doc-engine/output/report.artifact.json \
  --upstream-evidence-ref ./inputs/source-evidence.json
```

Outputs can include:

```text
traces/<run>.jsonl
checkpoints/<run>/checkpoint.json
provenance/<run>.prov.json
claim-audits/<run>.claim-audit.json
evidence/<run>.evidence.json
```

`run_bundle()` materializes upstream reference iterables once so programmatic callers can safely pass lists, tuples or generators without consuming them before final reference counts are recorded.

## Provider disclosure

The built-in `MockProvider` is a deterministic synthetic fixture only:

```text
provider: epistemic-pipeline
model: null
version: null
mode: synthetic_fixture
external_model_call: false
```

There is intentionally no invented fixture/model version. Real integrations must implement `LLMProvider` and may return only metadata they can actually know.

Provider identity does not prove output authenticity, reliability or scientific validity.

## Three-repository handoff

```text
auto-doc-engine
artifact identity + process context
        ↓
epistemic-pipeline
claim/evidence/conflict + claim verification + lineage
        ↓
sci-render-kit
claim-aware scientific communication + communication audit
```

Preferred upstream Auto Doc identifier:

```text
auto-doc-engine/artifact-record
```

Preferred downstream Sci Render identifiers:

```text
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

These are loose interoperability contracts. The repositories do not import one another at runtime.

## Reproducibility semantics

Shared project terminology:

- **R0 Traceable** — source/artifact identity can be located.
- **R1 Replay-addressable** — intended inputs/configuration/run identity can be located.
- **R2 Environment-bounded** — relevant environment/dependency assumptions are also recorded.
- **R3 Reproduced** — a genuinely separate rerun occurred and was compared using a declared criterion.

A checkpoint, trace, hash, claim audit or evidence envelope alone does not establish R3.

## 2026 global research calibration

Current design was rechecked against recent research rather than inferred from repo naming alone:

- Nature Computational Science, *Provenance grounds trust in autonomous science* (20 Aug 2026): complete, re-openable records are central to auditing and correcting autonomous-science processes.
- Nature Computational Science, *Responsible and transparent use of AI in scientific publishing* (20 Aug 2026): transparency, accountability and human oversight remain central.
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (18 Aug 2026): model-call logs alone are insufficient for claim/artifact/evidence auditability.
- *Brain Researcher* (20 Aug 2026): defensible claims require explicit evidence constraints and review; this repository borrows the separation principle, **not** its domain scientific-review verdict labels.
- *From Trajectories to Evidence* (5 Aug 2026): completed trajectories are not automatically evidence; artifact verification and post-execution claim qualification must be separated.
- *EarthVerse* (24 Aug 2026): strong local task performance can coexist with much weaker strict end-to-end scientific consistency.

These publications motivate design choices. They do not validate, certify or endorse this repository.

## Scientific-integrity boundaries

- Provenance is not truth.
- Claim indexing is not truth adjudication.
- Claim verification records are observations, not scientific verdicts.
- Provider identity is not output validity.
- Human review is not peer review.
- Runtime-policy success is not scientific validation.
- Numerical convergence is not certainty.
- Scores are not probabilities unless separately calibrated and empirically evidenced.
- A completed trajectory is not automatically evidence.

## Governance boundary

No GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge gates are part of this research architecture. Existing local checks are optional maintenance aids. No test suite is used as the completion criterion for the 2026-08-27 consolidation.
