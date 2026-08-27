# Five-Day Consolidation — epistemic-pipeline

**Window:** 2026-08-24 → 2026-08-28  
**Repository role:** evidence-aware research execution / epistemic-process plane  
**Status:** implementation and architecture consolidation snapshot

## Five-day trajectory

### Day 1 — execution semantics and reproducibility boundaries

The repository was tightened around explicit graph/state execution, machine-readable runtime policy, graph-sensitive checkpoint identity, project tracing, PROV-aligned lineage and bounded heuristic-score semantics.

### Day 2 — autonomous-science frontier calibration

The architecture was positioned against emerging scientific-agent work without becoming a domain scientific agent. The main distinction became: process observability is necessary, but process correctness does not equal scientific truth.

### Day 3 — claim-aware handoff and process disclosure

Claim identity, source/evidence refs, provider metadata and human-review declarations became first-class portable audit surfaces in the Evidence Envelope.

### Day 4 — claim verification as a separate artifact

`epistemic-pipeline/claim-verification` separated evidence bindings, consistency observations, conflicts, initial/final heuristic scores and audit states from the compact Evidence Envelope. The repository deliberately refused a universal `verified=true` field.

### Day 5 — assertion basis + dimensional audit coverage

Claim records now preserve how their audit fields were obtained and expose coverage across distinct audit dimensions.

```text
structured-analyze-output
structured-verify-output
structured-state-output
provider-adapter-reported
caller-declared
runtime-observed-local-filesystem
```

No aggregate research-quality score is computed.

## Current canonical evidence stack

```text
graph/state execution
       ↓
runtime policy
       ↓
trace + checkpoint
       ↓
PROV-aligned lineage
       ↓
claim-verification
  ├─ claim/source/evidence refs
  ├─ consistency observations
  ├─ conflicts
  ├─ initial/final heuristic scores
  ├─ assertion basis
  └─ dimensional audit coverage
       ↓
evidence-envelope
  ├─ artifact references
  ├─ upstream handoff references
  ├─ reference-resolution coverage
  ├─ provider/review disclosure
  └─ claim-verification reference
```

## Why Day 5 matters

A downstream auditor should be able to distinguish a field emitted by an analysis state from one observed during verification, supplied by a provider adapter, or declared by a human caller.

Likewise, the system should be able to say:

```text
73% of indexed claims carry evidence references
```

without pretending that this means:

```text
73% of claims are true
```

That distinction is the core Day-5 upgrade.

## Global calibration

The five-day design is informed by:

- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*;
- *From Trajectories to Evidence*;
- *Bringing analytic rigor to agentic AI for science: The Brain Researcher platform*;
- *EarthVerse*;
- *From Fluent to Verifiable: Claim-Level Auditability for Deep Research Agents*;
- Nature Computational Science commentary on provenance in autonomous science;
- Nature Computational Science guidance on transparent AI use and human oversight.

Borrowed design ideas:

- claims/evidence/verification as explicit objects;
- provenance coverage and contradiction transparency as measurable dimensions;
- evidence-bounded claim qualification;
- explicit process context;
- end-to-end consistency as a distinct concern from local step success.

Not claimed:

- provenance soundness;
- scientific-review authority;
- universal accepted/rejected claim statuses;
- calibrated probability of truth;
- external citation verification;
- peer review;
- independent reproduction.

## Cross-repository Day-5 chain

```text
auto-doc-engine
  artifact-record
  assertion basis
  artifact audit coverage
        ↓
epistemic-pipeline
  claim-verification
  claim audit coverage
  evidence-envelope
        ↓
sci-render-kit
  figure-claim-audit
  communication coverage
  figure-evidence
```

## Hard boundaries

```text
Execution complete != evidence complete
Evidence ref != evidence sufficient
Assertion basis != correctness
Audit coverage != scientific validity
Structural check != truth
Conflict absent != corroboration
Heuristic score != probability
Convergence != certainty
Provider identity != output validity
Human review != peer review
Provenance != truth
```

## Maintenance boundary

The repository still does not use GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge gates as scientific architecture. Optional local checks are maintenance aids only.
