# Epistemic Pipeline

> Evidence-aware state-machine execution for research workflows, with explicit claim/evidence structure, runtime policy, recovery identity, provenance, claim verification, assertion basis, dimensional audit coverage, and cross-tool handoff.

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md) · [Assertion Basis & Audit Coverage](ASSERTION_BASIS_AND_AUDIT_COVERAGE.md) · [Customization](CUSTOMIZATION_GUIDE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Five-Day Consolidation](FIVE_DAY_CONSOLIDATION.md)

## Positioning

Epistemic Pipeline treats research execution as an inspectable state-transition system rather than an opaque “agent trajectory”.

```text
discover -> analyze -> verify -> synthesize -> archive
```

Canonical evidence path:

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
claim-verification
  ├─ assertion / observation basis
  └─ dimensional claim audit coverage
    ↓
evidence-envelope
  ├─ upstream-reference coverage
  └─ compact cross-tool handoff
```

A completed run is not automatically evidence. Structural checks are not scientific verification. Coverage is not correctness. Scores are not probabilities. Provenance is not truth.

## Stable internal identifiers

Project-owned identifiers are intentionally unversioned:

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

Real external standards/runtime versions remain explicit where genuinely applicable. Alignment language is not standards conformance.

## Core modules

| Module | Role | Boundary |
|---|---|---|
| `core/dependency_graph.py` | DAG validation/topology | structural semantics only |
| `core/engine.py` | state execution, runtime policy, retry/timeout, checkpoint | run success != scientific validity |
| `core/llm_harness.py` | provider-neutral structured output + provider disclosure | real providers injected; unknown metadata stays unknown |
| `core/gatekeeper.py` | explicit machine runtime predicates | not a scientific reviewer |
| `core/confidence_net.py` | bounded weighted heuristic propagation | `[0,1]` != calibrated probability |
| `core/calibration.py` | monotone score transform | transform != empirical calibration |
| `core/run_tracer.py` | project JSONL trace + internal hash chain | not OTel exporter / tamper-proof ledger |
| `core/provenance.py` | PROV-aligned project lineage | not PROV-O RDF conformance |
| `core/claim_audit.py` | per-claim observations + assertion basis + audit coverage | never truth verdict |
| `core/evidence_envelope.py` | compact handoff + upstream reference coverage | not proof object/database |
| `core/run_bundle.py` | evidence-bearing composition | coordinates artifacts without redefining validity |

Experimental modules remain outside this canonical path unless deliberately integrated.

## Runtime policy

State definitions use explicit machine checks such as:

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

Human-readable prose is not parsed into executable policy. Unknown checks fail explicitly.

```text
runtime-policy pass != scientific validity
runtime-policy pass != peer review
runtime-policy pass != evidence credibility
```

## Claim verification

`core/claim_audit.py` emits:

```text
claim-audits/<run>.claim-audit.json
epistemic-pipeline/claim-verification
```

Each claim may retain:

```text
claim identity
source refs
evidence refs / relations
internal-consistency observation
cross-source observation
conflicts
initial heuristic score
final heuristic score
audit state
assertion / observation basis
```

Descriptive states remain deliberately weak:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

They are not accepted/rejected scientific-review decisions.

## Assertion / observation basis

Day 5 records how audit fields entered the record:

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
synthetic-fixture-runtime
runtime-harness-state
caller-declared
runtime-observed-local-filesystem
```

Examples:

```text
claim/source/evidence refs -> structured analyze output
consistency/conflicts      -> structured verify output
heuristic scores           -> structured state output
provider metadata          -> provider adapter report
human review               -> caller declaration when supplied
```

Hard rule:

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor certification
```

The repository also records `automatic_ai_detection_used: false` on its process-disclosure path. It does not infer AI authorship/use from output prose.

See [ASSERTION_BASIS_AND_AUDIT_COVERAGE.md](ASSERTION_BASIS_AND_AUDIT_COVERAGE.md).

## Dimensional claim audit coverage

`claim-verification` reports separate counts/ratios for indexed claims carrying:

```text
source refs
evidence refs
internal-consistency observations
cross-source observations
conflicts
initial heuristic scores
final heuristic scores
```

Example:

```text
evidence_refs_ratio = 0.80
```

means 80% of indexed claims carry at least one evidence reference in the structured run output.

It does **not** mean 80% correctness, evidence sufficiency, provenance soundness or probability of truth.

The record deliberately emits:

```json
{"aggregate_score": null}
```

Current research on claim-level auditability motivates measuring coverage as a distinct dimension; this repository does **not** claim provenance soundness because it does not implement the required external verification authority.

## Heuristic score semantics

```text
score in [0,1] != calibrated probability
numerical convergence != certainty
score increase != probability increase
```

Initial and final scores remain observations with stage/basis metadata. An unfitted transform remains a transform, not probability calibration.

## Trace and checkpoint

Trace fields may borrow selected OpenTelemetry GenAI naming, but the repository is not an OTel exporter and does not claim span compliance.

The internal SHA-256 chain establishes linkage among currently present records only; it is not an externally anchored tamper-proof ledger.

Checkpoint graph identity supports bounded resume/replay addressing. It does not prove external providers/tools will reproduce identical outputs.

## PROV-aligned lineage

`core/provenance.py` uses PROV concepts such as Entity, Activity, SoftwareAgent, `used`, `wasGeneratedBy`, `wasDerivedFrom`, and `wasAssociatedWith`.

```text
PROV-aligned != PROV-O RDF conformance
lineage != truth
hash identity != semantic equivalence
```

## Evidence Envelope

`core/evidence_envelope.py` emits:

```text
epistemic-pipeline/evidence-envelope
```

It references graph, trace, checkpoint, provenance, claim verification, claim index, process disclosure and optional upstream artifact/evidence refs.

Day 5 adds dimensional upstream-reference coverage:

```text
reference_count
by_resolution
local_file_ratio
aggregate_score: null
```

A local-file ratio means only that a declared path resolved locally and could be hashed at envelope-generation time.

```text
local resolution != source credibility
opaque URI != invalid evidence
reference coverage != evidence quality
```

The envelope stays compact and references the separate claim-verification sidecar rather than duplicating it.

## Provider disclosure

Base provider metadata is `provider-adapter-reported`; the synthetic fixture declares `synthetic-fixture-runtime`; no-provider state declares `runtime-harness-state`.

Built-in MockProvider remains:

```text
provider: epistemic-pipeline
model: null
version: null
mode: synthetic_fixture
external_model_call: false
```

No fake model/version is invented.

```text
provider identity != output validity
provider metadata != AI-text detection
```

## Evidence-bearing CLI

```bash
python core/run_bundle.py graphs/linear.yaml \
  --human-review partial \
  --upstream-artifact-ref ../auto-doc-engine/output/report.artifact.json \
  --upstream-evidence-ref ./inputs/source-evidence.json
```

Typical evidence artifacts:

```text
traces/<run>.jsonl
checkpoints/<run>/checkpoint.json
provenance/<run>.prov.json
claim-audits/<run>.claim-audit.json
evidence/<run>.evidence.json
```

## Five-day research calibration

The 2026-08-24 → 2026-08-28 architecture was calibrated against:

- autonomous-science provenance and re-openable records;
- transparent AI use / human oversight in scientific publishing;
- artifact-centered claim-aware observability;
- trajectory-to-evidence qualification;
- Brain Researcher evidence-bounded claims/review;
- EarthVerse end-to-end scientific consistency gaps;
- claim-level auditability work separating provenance coverage, soundness, contradiction transparency and audit effort;
- current AI-detection reporting, reinforcing that detection and explicit disclosure are separate mechanisms.

Borrowed: explicit audit objects, dimensional coverage, contradiction visibility, evidence-bounded qualification and assertion provenance.

Not claimed: provenance soundness, universal scientific-review verdicts, citation correctness, calibrated truth probability, peer review or independent reproduction.

See [FIVE_DAY_CONSOLIDATION.md](FIVE_DAY_CONSOLIDATION.md).

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
epistemic-pipeline/claim-verification
  claim audit coverage + observation basis
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

Repositories remain loosely coupled through files/references.

## Reproducibility semantics

- **R0 Traceable** — source/artifact identity locatable.
- **R1 Replay-addressable** — intended inputs/config/run identity locatable.
- **R2 Environment-bounded** — relevant environment/dependency assumptions recorded.
- **R3 Reproduced** — genuinely separate rerun + declared comparison.

No trace/checkpoint/provenance/claim audit/envelope self-awards R3.

## Scientific-integrity boundaries

```text
Provenance != Truth
Assertion basis != correctness
Audit coverage != scientific validity
Coverage ratio != probability
Claim indexing != truth adjudication
Claim verification record != scientific verdict
Evidence ref != evidence sufficiency
Conflict absent != corroboration
Provider identity != output validity
Human review != peer review
Runtime-policy success != scientific validation
Convergence != certainty
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions and merge gates remain outside this research architecture. Local checks are optional maintenance aids; test execution is not the completion criterion for this consolidation.
