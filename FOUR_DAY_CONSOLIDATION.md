# Four-Day Consolidation — epistemic-pipeline

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** evidence-aware research execution / claim-audit plane  
**Status:** implementation and architecture consolidation snapshot

## 1. Four-day trajectory

### 24 Aug — runtime semantics became explicit

The repository was tightened from generic “multi-agent pipeline” language into a
bounded research-execution system:

```text
Graph + State
  -> Provider contract
  -> RuntimePolicyEvaluator
  -> claim / evidence / conflict structures
  -> bounded heuristic score propagation
  -> trace + checkpoint
  -> PROV-aligned lineage
  -> evidence envelope
```

Important corrections included:

- runtime policy instead of truth/quality-gate language;
- graph-digest-bound checkpoint resume;
- project JSONL trace rather than pretending to be an OpenTelemetry exporter;
- W3C PROV-aligned project JSON, not PROV-O RDF;
- bounded score values, not calibrated probabilities;
- R0–R3 reproducibility language with R3 requiring a real separate rerun.

### 25 Aug — frontier positioning

The repository was placed beside typed scientific execution, evidence graphs,
scientific RAG and autonomous-science systems while keeping its own center of
gravity: explicit epistemic semantics and research-run evidence contracts.

### 26 Aug — claim index and process disclosure

`evidence-envelope@2` made two previously implicit surfaces first-class:

- a payload-minimizing claim index linking claim IDs to source/evidence refs;
- provider/process disclosure plus declared human-review state.

This made the handoff more inspectable without turning the Evidence Envelope
into a copy of every provider payload.

### 27 Aug — claim verification becomes a separate artifact

The repository now writes:

```text
epistemic-pipeline/claim-verification@1
```

The key design choice is **not** to output `verified: true|false`.

Instead each claim can carry separate audit dimensions:

```text
claim identity
source refs
evidence refs
internal-consistency observation
cross-source observation
conflict records
initial heuristic score
final heuristic score
audit_state
provider/review context
```

The Evidence Envelope remains `@2` and only references the claim-audit sidecar.
This keeps lineage/indexing separate from verification observations.

## 2. Why a completed run is not evidence by itself

Recent 2026 work makes this distinction increasingly explicit.

*From Trajectories to Evidence: Auditable Experimental Records for Industrial
Research Agents* (arXiv:2608.05235) argues that a completed research-agent
trajectory is not automatically evidence. Its framework separates artifact
verification, execution validity/attribution and post-execution claim
qualification.

Borrowed principle:

> completion status should never be silently promoted into scientific evidence.

This repository therefore keeps:

```text
run_status
runtime_policy_pass
claim audit state
heuristic scores
human review declaration
scientific validity
```

as different semantic surfaces.

## 3. Brain Researcher: claim scope matters

*Bringing analytic rigor to agentic AI for science: The Brain Researcher
platform for neuroimaging data analysis* (arXiv:2608.19902, 20 Aug 2026) argues
that an analytic output becomes a defensible claim only after alternatives are
weighed and the claim is limited to what the evidence supports. Its scientific
review process uses outcome states such as accepted, qualified, revised,
blocked, rejected and deferred.

Borrowed principle:

> claim qualification is a first-class research operation.

Deliberately **not** borrowed:

> those review labels themselves.

`epistemic-pipeline` does not currently contain an independent scientific-review
authority, so `claim-verification@1` uses descriptive structural audit states
only:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

These states report what the runtime recorded, not whether a claim should be
accepted by science.

## 4. Artifact-centered claim-aware observability

Yin et al., *Artifact-centered Claim-aware Observability for Autonomous
Scientific Agents* (arXiv:2608.18312), argues that logging model calls is not
enough. Scientific audits need claims, evidence bindings, artifacts and
verification records as portable first-class relations.

This is very close to the repository's Day-4 decomposition:

```text
trace
  = execution events

provenance
  = lineage relations

claim index
  = portable claim/evidence identity map

claim verification
  = claim-specific checks/conflicts/score observations

evidence envelope
  = cross-tool index/handoff
```

One generic log cannot answer all five questions faithfully.

## 5. EarthVerse: local competence is not chain consistency

EarthVerse (arXiv:2608.23525, 24 Aug 2026) reports 405 reproducible tasks across
199 documented events and 19 hazard families. Its reported best mean
answer-unit accuracy is much stronger than its strict end-to-end performance,
illustrating that agents can perform local steps while still failing to
maintain a consistent scientific chain across evidence, scale, units,
calculation and interpretation.

Borrowed principle:

> preserve identity and semantics at each transition rather than assuming an
> apparently good final answer proves the intermediate chain was coherent.

That motivates this repository's separation of graph identity, state outputs,
claim/evidence relations, conflict records, score semantics and provenance.

## 6. Provenance and process transparency

The 20 Aug 2026 Nature Computational Science comment *Provenance grounds trust
in autonomous science* emphasizes complete, re-openable records that can be
audited and corrected.

The same issue's editorial *Responsible and transparent use of AI in scientific
publishing* emphasizes transparency, accountability and human oversight.

Borrowed principles:

- preserve enough run context to reopen a decision path;
- keep provider/model metadata explicit where declared;
- keep human-review state explicit rather than inferred.

Boundaries:

```text
provider identity != output validity
human review != peer review
provenance != truth
```

## 7. OpenTelemetry boundary

OpenTelemetry semantic-convention work remains useful for naming and
observability vocabulary. The repository continues to reuse only selected GenAI
operation naming where appropriate.

It does **not** claim:

- OTel SDK instrumentation;
- exporter conformance;
- that local `run_id` is a provider conversation/session ID;
- that the project JSONL trace is an OpenTelemetry span stream.

This boundary remains important while GenAI semantic conventions continue to
evolve independently.

## 8. Current Day-4 canonical evidence stack

```text
[upstream artifact/evidence refs]
             ↓
Graph + State definitions
             ↓
StateMachineEngine @2
             ↓
Provider / Role contract
             ↓
RuntimePolicyEvaluator @1
             ↓
claim / evidence / conflict structures
             ↓
initial heuristic scores @ verify
             ↓
final heuristic scores @ synthesize
             ↓
Trace @2 + Checkpoint @2
             ↓
PROV-aligned lineage @2
             ↓
Claim Verification @1
             ↓
Evidence Envelope @2
```

## 9. Claim verification semantics

`claim-verification@1` keeps each dimension visible.

Example conceptual record:

```json
{
  "claim_id": "c1",
  "evidence_refs": ["src_1#segment_4"],
  "observations": {
    "internal_consistency": "...",
    "cross_source": "..."
  },
  "conflicts": [],
  "heuristic_scores": {
    "initial": {"value": 0.5},
    "final": {"value": 0.62}
  },
  "audit_state": "structurally_checked",
  "truth_claim": false
}
```

Interpretation:

```text
evidence bound != evidence sufficient
consistency observed != true
conflict absent != correct
score increased != probability increased
structurally checked != scientifically verified
```

## 10. Upstream artifact handoff

`run_bundle.py` now accepts repeatable:

```text
--upstream-artifact-ref
--upstream-evidence-ref
```

Existing local files are hashed when referenced by the Evidence Envelope;
opaque URI/reference values are retained without network dereferencing.

This enables a loose handoff from `auto-doc-engine/artifact-record@1` without
introducing a direct Python dependency.

## 11. Cross-repository Day-4 chain

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

## 12. Deliberate non-goals

- a universal scientific truth oracle;
- automatic source-credibility scoring presented as truth;
- Bayesian/probability claims without real calibration evidence;
- automatically accepting/rejecting scientific claims;
- replacing domain-specific statistical review;
- turning every conflict into a failure;
- storing complete provider payloads in every evidence sidecar;
- converting project JSON into fake PROV-O/OTel conformance;
- GitHub Actions / CI / CodeQL / merge-gate architecture.

## 13. Primary references

Checked through 2026-08-27:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). https://doi.org/10.1038/s43588-026-01043-4
3. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
4. **EarthVerse: Benchmarking and Advancing AI Agents for Global Earth Science.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
5. Chen Z, Lu N, Li X, et al. **Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis.** arXiv:2608.19902. https://arxiv.org/abs/2608.19902
6. Zhuang Z, Lao C, Xu P, et al. **From Trajectories to Evidence: Auditable Experimental Records for Industrial Research Agents.** arXiv:2608.05235. https://arxiv.org/abs/2608.05235
7. W3C PROV overview: https://www.w3.org/TR/prov-overview/
8. OpenTelemetry GenAI semantic conventions repository: https://github.com/open-telemetry/semantic-conventions-genai

## 14. Bottom line

The Day-4 shift is from **“a run produced claims”** to:

> **a run produced claims whose evidence bindings, structural verification
> observations, conflicts, score evolution, process context and lineage remain
> separately inspectable.**

That is the repository's research-engineering role; it is deliberately weaker
and more defensible than claiming the pipeline verifies scientific truth.
