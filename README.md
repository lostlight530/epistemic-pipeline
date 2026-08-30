# Epistemic Pipeline

> Evidence-aware state-machine execution for research workflows, with explicit claim/evidence/conflict structure, runtime policy, recovery identity, provenance, claim verification, claim transfer, assertion basis, dimensional audit coverage, compact evidence handoff, and phase-aware maintenance

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Claim Audit Contract](CLAIM_AUDIT_CONTRACT.md) · [Claim Transfer Contract](CLAIM_TRANSFER_CONTRACT.md) · [Assertion Basis & Audit Coverage](ASSERTION_BASIS_AND_AUDIT_COVERAGE.md) · [Maintenance](MAINTENANCE_CADENCE.md) · [Document Status](DOCUMENT_STATUS.md) · [August Stage Close](STAGE_2026_08_MAINTENANCE.md) · [Customization](CUSTOMIZATION_GUIDE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md)

## Positioning

Epistemic Pipeline treats research execution as an inspectable state-transition and evidence-contract system rather than an opaque agent trajectory

```text
discover -> analyze -> verify -> synthesize -> archive
```

Canonical evidence path

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
optional claim-transfer
  ├─ selected portable claim context
  ├─ conflicts preserved
  └─ non-inheritance constraints
    ↓
evidence-envelope
  ├─ upstream-reference coverage
  └─ compact cross-tool handoff
```

A completed run is not automatically evidence. Structural checks are not scientific verification. Transfer is not acceptance. Coverage is not correctness. Scores are not probabilities. Provenance is not truth

## Stable internal identifiers

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
epistemic-pipeline/claim-transfer
epistemic-pipeline/process-disclosure
epistemic-pipeline/upstream-reference
epistemic-pipeline/evidence-envelope
epistemic-pipeline/reference-rules
epistemic-pipeline/maintenance-cadence
epistemic-pipeline/maintenance-report
```

Project-owned identifiers are intentionally unversioned. Real external standards/runtime versions remain explicit where genuinely applicable. Alignment language is not standards conformance

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
| `core/claim_transfer.py` | portable selected claim context + constraints | transfer != acceptance |
| `core/evidence_envelope.py` | compact handoff + upstream reference coverage | not proof object/database |
| `core/run_bundle.py` | evidence-bearing composition | coordinates artifacts without redefining validity |
| `core/maintenance_cadence.py` | read-only daily/weekly/monthly structural maintenance evidence | clean maintenance != scientific validity |

Experimental modules remain outside this canonical path unless deliberately integrated

## Runtime policy

State definitions use explicit machine checks such as

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

Human-readable prose is not parsed into executable policy. Unknown checks fail explicitly

```text
runtime-policy pass != scientific validity
runtime-policy pass != peer review
runtime-policy pass != evidence credibility
```

## Claim verification

`core/claim_audit.py` emits

```text
claim-audits/<run>.claim-audit.json
epistemic-pipeline/claim-verification
```

Each claim may retain

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

Descriptive states remain deliberately weak

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

They are not accepted/rejected scientific-review decisions

## Assertion / observation basis

Audit fields record how they entered the record

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

Examples

```text
claim/source/evidence refs -> structured analyze output
consistency/conflicts      -> structured verify output
heuristic scores           -> structured state output
provider metadata          -> provider adapter report
human review               -> caller declaration when supplied
```

```text
assertion basis != correctness
structured-verify-output != external scientific verification
provider-adapter-reported != vendor certification
```

The process-disclosure path records `automatic_ai_detection_used: false`. The repository does not infer AI authorship/use from output prose

## Dimensional claim audit coverage

`claim-verification` reports separate counts/ratios for indexed claims carrying

```text
source refs
evidence refs
internal-consistency observations
cross-source observations
conflicts
initial heuristic scores
final heuristic scores
```

Example

```text
evidence_refs_ratio = 0.80
```

means 80% of indexed claims carry at least one evidence reference in structured run output

It does not mean 80% correctness, evidence sufficiency, provenance soundness, or probability of truth

```json
{"aggregate_score": null}
```

The repository measures only the coverage dimensions it can actually compute. It does not claim provenance soundness

## Claim transfer

`core/claim_transfer.py` emits

```text
epistemic-pipeline/claim-transfer
```

It selects existing claim records from a valid `epistemic-pipeline/claim-verification` sidecar and preserves bounded downstream context

```text
source refs
evidence refs / relations
internal / cross-source observations
conflicts
initial / final heuristic scores
audit state
```

Requested missing claim IDs fail explicitly rather than being fabricated

Transfer constraints preserve

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

```text
claim transfer != acceptance
inheritance != validation
evidence ref != evidence sufficiency
conflict visibility != conflict adjudication
```

## Heuristic score semantics

```text
score in [0,1] != calibrated probability
numerical convergence != certainty
score increase != probability increase
```

Initial and final scores remain observations with stage/basis metadata. An unfitted transform remains a transform, not probability calibration

## Trace, checkpoint, and PROV-aligned lineage

Trace fields may borrow selected OpenTelemetry GenAI naming, but the repository is not an OTel exporter and does not claim span compliance

The internal SHA-256 chain establishes linkage among currently present records only; it is not an externally anchored tamper-proof ledger

Checkpoint graph identity supports bounded resume/replay addressing. It does not prove external providers/tools will reproduce identical outputs

`core/provenance.py` uses W3C PROV concepts in project JSON

```text
PROV-aligned != PROV-O RDF conformance
lineage != truth
hash identity != semantic equivalence
```

## Evidence Envelope

`core/evidence_envelope.py` emits `epistemic-pipeline/evidence-envelope`

It references graph, trace, checkpoint, provenance, claim verification, claim index, process disclosure, optional upstream artifact/evidence refs, and the independent claim-transfer surface when supplied by downstream workflows

Upstream reference coverage remains dimensional

```text
reference_count
by_resolution
local_file_ratio
aggregate_score: null
```

```text
local resolution != source credibility
opaque URI != invalid evidence
reference coverage != evidence quality
```

The envelope stays compact and references separate audit artifacts rather than duplicating them into one proof object

## Provider disclosure

Base provider metadata is `provider-adapter-reported`; the synthetic fixture declares `synthetic-fixture-runtime`; no-provider state declares `runtime-harness-state`

Built-in MockProvider remains

```text
provider: epistemic-pipeline
model: null
version: null
mode: synthetic_fixture
external_model_call: false
```

No fake model/version is invented

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

Typical artifacts

```text
traces/<run>.jsonl
checkpoints/<run>/checkpoint.json
provenance/<run>.prov.json
claim-audits/<run>.claim-audit.json
evidence/<run>.evidence.json
```

A bounded claim transfer can be generated separately from an existing claim audit

```bash
python core/claim_transfer.py claim-audits/<run>.claim-audit.json \
  --claim-id claim-001 \
  --purpose downstream-figure \
  --output handoff/claim-transfer.json
```

## Daily / weekly / monthly maintenance

Maintenance is defined in [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)

Current document authority is defined in [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)

The closed August baseline is [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

The scanner reports local structural maintenance evidence plus date-derived calendar/stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` remain historical snapshots rather than current contracts

## Stage-close research calibration

The 2026-08-24 → 2026-08-31 stage was calibrated against work on

- autonomous-science provenance and re-openable records
- transparent AI use / human oversight in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency
- claim-level auditability separating provenance coverage, soundness, contradiction transparency, and audit effort
- Praxist-style solution/evidence lineage
- ReproAgent-style persistent contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level long-horizon evaluation beyond final scores
- durable project-state / reviewed-route patterns in persistent agent runtimes

Borrowed: explicit audit objects, dimensional coverage, contradiction visibility, persistent constraints, process segmentation, and evidence-bounded qualification

Not claimed: provenance soundness, universal scientific-review verdicts, citation correctness, calibrated truth probability, peer review, or independent reproduction

See [FRONTIER_ALIGNMENT.md](FRONTIER_ALIGNMENT.md)

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

Repositories remain loosely coupled through files/references and no scientific validity is inherited through transfer

## Reproducibility semantics

- **R0 Traceable** — source/artifact identity locatable
- **R1 Replay-addressable** — intended inputs/config/run identity locatable
- **R2 Environment-bounded** — relevant environment/dependency assumptions recorded
- **R3 Reproduced** — genuinely separate rerun + declared comparison

No trace/checkpoint/provenance/claim audit/claim transfer/envelope/maintenance baseline self-awards R3

## Scientific-integrity boundaries

```text
Provenance != Truth
Assertion basis != correctness
Audit coverage != scientific validity
Coverage ratio != probability
Claim indexing != truth adjudication
Claim verification record != scientific verdict
Claim transfer != acceptance
Evidence ref != evidence sufficiency
Conflict absent != corroboration
Provider identity != output validity
Human review != peer review
Runtime-policy success != scientific validation
Convergence != certainty
Maintenance clean != scientific validity
Calendar-month close != reproduction
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, and merge gates remain outside this research architecture. Local/manual checks are optional maintenance aids; test execution is not the completion criterion for this stage-close reconciliation
