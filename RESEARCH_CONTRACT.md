# Research Contract — epistemic-pipeline

**Calibration:** 2026-08-27  
**Status:** active contract for runtime semantics, claim/evidence structure, recovery identity, process disclosure, claim verification, provenance and cross-repository handoff

`epistemic-pipeline` is the **evidence-aware research execution / claim-audit plane** of the three-repository research toolchain.

This contract defines what repository artifacts can and cannot establish. It is not GitHub merge policy and not a scientific-review standard.

## 1. Canonical role

```text
upstream artifact/evidence refs
        ↓
validated graph + state definitions
        ↓
provider / role contract
        ↓
runtime-policy evaluation
        ↓
claim / evidence / conflict structures
        ↓
initial / final bounded heuristic scores
        ↓
trace + checkpoint
        ↓
PROV-aligned lineage
        ↓
claim-verification@1
        ↓
evidence-envelope@2
```

The repository does not automatically determine scientific truth, source credibility, causal validity, statistical validity, authorship, peer review or journal acceptance.

## 2. Core evidence surfaces

The repository intentionally keeps five surfaces distinct.

### 2.1 Trace

```text
epistemic-pipeline/trace@2
```

Answers:

> What runtime events were recorded?

Does not establish:

- scientific correctness;
- immutable/tamper-proof external logging;
- provider conversation identity from local run ID.

### 2.2 Checkpoint

```text
epistemic-pipeline/checkpoint@2
```

Answers:

> Which successful node results may be reused under the same graph identity?

Does not establish independent reproduction or external side-effect idempotency.

### 2.3 PROV-aligned lineage

```text
epistemic-pipeline/prov@2
```

Answers:

> How do recorded entities, activities and software agents relate?

It is project JSON aligned with W3C PROV concepts. It is not PROV-O RDF.

### 2.4 Claim Verification

```text
epistemic-pipeline/claim-verification@1
```

Answers:

> What evidence bindings, runtime consistency observations, conflicts, score observations and process context were recorded for each claim?

It deliberately does not emit a scientific `verified=true` flag.

### 2.5 Evidence Envelope

```text
epistemic-pipeline/evidence-envelope@2
```

Answers:

> Which graph/run/evidence artifacts and profiles should travel to another tool?

It is a project-owned handoff index, not an external scientific-evidence standard.

## 3. Graph and recovery contract

Executable graph validation covers:

- duplicate node IDs;
- unknown dependencies;
- cycles;
- reachability.

Graph identity uses both:

```text
graph_id
graph_sha256
```

Checkpoint resume requires matching graph identity.

Hard boundary:

```text
same graph ID != same graph definition
checkpoint reuse != reproduction
```

## 4. Provider contract

Provider interface:

```text
LLMProvider.complete(system, user, schema) -> dict
LLMProvider.describe() -> bounded process metadata
```

`MockProvider` is deterministic synthetic fixture behavior.

Provider disclosure may include human-readable provider/model/version/mode fields.

It does **not** prove:

- the provider/model string is externally verified;
- model identity implies capability;
- model capability implies output validity;
- external API behavior was exercised by a mock run.

## 5. Runtime-policy contract

Active semantics:

```text
epistemic-pipeline/runtime-policy@1
```

Machine behavior comes from explicit `check` + parameters.

Human prose is explanatory unless an executable mechanism exists.

A runtime-policy success establishes only the declared machine predicate over the current structured output.

```text
runtime-policy pass != scientific validity
runtime-policy pass != source credibility
runtime-policy pass != peer review
```

Historical Gatekeeper/quality-gate names remain compatibility surfaces only.

## 6. Claim / evidence / conflict contract

The runtime keeps:

```text
claims_registry
evidence_chains
conflict_registry
```

as distinct structures.

### Claim identity

Claim IDs/hashes provide audit identity for repository records. Hashing the claim record does not prove claim truth.

### Evidence binding

Evidence refs establish declared linkage, not sufficiency or credibility.

```text
evidence bound != evidence sufficient
citation present != citation faithful
source cited != source credible
```

### Conflict records

Conflicts preserve disagreement/limitation information. Absence of a conflict does not imply correctness or consensus.

## 7. Claim Verification contract

Project profile:

```text
epistemic-pipeline/claim-verification@1
```

### 7.1 Claim record fields

A record may contain:

```text
claim_id
origin_state_id
claim_record_sha256
source_refs[]
evidence_refs[]
evidence_relations[]
observations.internal_consistency
observations.cross_source
conflicts[]
heuristic_scores.initial
heuristic_scores.final
audit_state
truth_claim=false
citation_verification_claim=false
```

Full claim prose is not duplicated into the sidecar by default.

### 7.2 Audit states

Current states are descriptive process labels:

```text
indexed_only
evidence_bound
structurally_checked
conflict_recorded
structurally_checked_with_conflict
```

They answer:

> Which audit structures/observations exist for this claim?

They do not answer:

- whether the claim is scientifically accepted;
- whether it is true/false;
- whether it passed peer review;
- whether its evidence is sufficient;
- whether statistical/causal design is valid.

### 7.3 Why no accepted/rejected state

Research systems such as Brain Researcher demonstrate the value of explicit scientific claim qualification using accepted/qualified/revised/blocked/rejected/deferred outcomes.

This repository does not implement the independent domain scientific-review authority required to make those labels defensible.

Therefore `claim-verification@1` retains narrower structural/process states.

## 8. Score contract

Active profile:

```text
epistemic-pipeline/confidence-heuristic@1
```

Current `[0,1]` numbers are bounded heuristic scores.

Claim audit can preserve:

```text
heuristic_scores.initial @ verify
heuristic_scores.final   @ synthesize
```

Hard rules:

```text
initial score != prior probability
final score != posterior probability
score delta != probability delta
numerical convergence != certainty
```

Temperature scaling remains a transform unless fitted/evaluated on labelled data under a declared calibration objective.

## 9. Process-disclosure contract

Project profile:

```text
epistemic-pipeline/process-disclosure@1
```

It may carry provider metadata and:

```text
human_review: reviewed | partial | not_reviewed | not_declared
```

Interpretation boundaries:

```text
provider identity != output validity
human review != peer review
reviewed != scientific validation
process metadata != authorship adjudication
```

## 10. Provenance contract

`prov@2` uses W3C PROV-aligned terms in project JSON.

Current lineage can record graph identity, node-output identities, trace/checkpoint refs and relations.

It does not claim:

- PROV-O RDF serialization;
- complete ontological coverage;
- immutable provenance;
- scientific truth.

## 11. Evidence Envelope contract

`evidence-envelope@2` remains deliberately small.

It may reference:

```text
graph
trace
checkpoint
provenance
claim-audit
upstream artifact refs
upstream evidence refs
```

It also carries:

- claim index;
- profile identifiers;
- process disclosure;
- trace-integrity semantics;
- local reproducibility level;
- scientific-validity boundary flags.

The envelope references claim audit instead of embedding it, so the handoff layer does not become a second research database.

## 12. Upstream-reference contract

`run_bundle.py` accepts repeatable:

```text
--upstream-artifact-ref
--upstream-evidence-ref
```

Reference behavior:

- existing local file: hash may be recorded;
- URI: retained as opaque, not dereferenced;
- unresolved local/opaque text: preserved explicitly.

A downstream/upstream link does not transfer scientific validity.

This is the preferred loose-coupling path from `auto-doc-engine/artifact-record@1`.

## 13. Trace / OpenTelemetry boundary

The project trace may align selected naming with evolving OpenTelemetry GenAI semantic conventions.

It does not claim:

- OTel SDK integration;
- exporter compatibility;
- span-event conformance;
- that `epistemic.run.id` is a provider conversation ID.

The distinction remains explicit because GenAI semantic conventions continue to evolve.

## 14. Reproducibility levels

Local project terms:

- **R0 Traceable** — research artifacts/relationships can be associated.
- **R1 Replay-addressable** — stable input/config/graph/artifact identities address intended replay.
- **R2 Environment-bounded** — relevant runtime/dependency assumptions are bounded.
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

Trace/checkpoint/provenance/claim-audit/envelope creation does not self-award R3.

## 15. Cross-repository contract

```text
auto-doc-engine
  artifact-record@1
        ↓
epistemic-pipeline
  upstream-reference@1
  claim-index@1
  claim-verification@1
  evidence-envelope@2
        ↓
sci-render-kit
  research_context.claim_audit_ref
  figure-claim-audit@1
  figure-evidence@2
```

No direct runtime imports are required.

## 16. Global research calibration

The 2026-08-27 architecture borrows bounded design lessons from:

- **Provenance grounds trust in autonomous science** — re-openable corrective provenance;
- **Artifact-centered Claim-aware Observability** — claims/artifacts/verification relations beyond logs;
- **EarthVerse** — local competence does not guarantee end-to-end scientific-chain consistency;
- **Brain Researcher** — explicit claim scope/qualification matters;
- **From Trajectories to Evidence** — a completed trajectory is not automatically admitted evidence;
- W3C PROV and evolving OpenTelemetry GenAI semantics.

These are research directions, not scientific validation, endorsement or standards conformance of this repository.

## 17. Experimental-module rule

Experimental modules remain outside the canonical engine unless deliberately integrated:

- `anti_entropy.py`
- `convergence.py`
- `infinite_regression.py`
- `neuro_symbolic.py`
- `perception.py`
- `thread_collapse.py`

Fixing or documenting an experimental implementation does not promote it.

## 18. Shared hard boundaries

```text
Structured output != truthful output
Runtime policy pass != scientific validity
Evidence binding != evidence sufficiency
Consistency observation != truth
Conflict absence != correctness
Heuristic score != calibrated probability
Numerical convergence != certainty
Audit state != scientific acceptance
Provider identity != output validity
Human review != peer review
Trace integrity != immutable ledger
Provenance != truth
Checkpoint resume != independent reproduction
```

## 19. Maintenance model

Local checks are optional maintenance aids, not GitHub merge policy or scientific-validation evidence.

The repository does not require GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge gates as research architecture.

The 2026-08-27 consolidation does not use test execution as completion evidence.

## 20. Primary references

Checked through 2026-08-27:

- W3C PROV overview: https://www.w3.org/TR/prov-overview/
- OpenTelemetry GenAI semantic conventions: https://github.com/open-telemetry/semantic-conventions-genai
- Nature Computational Science, *Provenance grounds trust in autonomous science*: https://doi.org/10.1038/s43588-026-01035-4
- Yin et al., *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*: https://arxiv.org/abs/2608.18312
- *EarthVerse*: https://arxiv.org/abs/2608.23525
- Chen et al., *Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis*: https://arxiv.org/abs/2608.19902
- Zhuang et al., *From Trajectories to Evidence*: https://arxiv.org/abs/2608.05235
