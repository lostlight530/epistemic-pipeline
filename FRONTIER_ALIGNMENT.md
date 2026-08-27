# Frontier Alignment — 2026-08-27

**Repository:** `epistemic-pipeline`  
**Status:** non-normative research-positioning snapshot  
**Normative boundaries:** `RESEARCH_CONTRACT.md` and `CLAIM_AUDIT_CONTRACT.md`

## 1. Current research question

The relevant 2026 frontier is no longer only “can an agent complete a workflow?” It increasingly asks:

```text
Can the resulting scientific record be reopened?
Can artifacts be attributed to actions?
Can claims be linked to evidence?
Can conflicts and qualification be inspected?
Can human/AI process context be disclosed?
Can the system avoid turning execution success into scientific truth?
```

Epistemic Pipeline addresses these questions at the research-execution/evidence-contract layer.

## 2. Verified external signals

### Provenance grounds trust in autonomous science

Nature Computational Science (20 Aug 2026) emphasizes complete, re-openable records of reasoning/actions/measurements as a basis for audit and correction in autonomous science.

Borrowed design lesson:

> Preserve inspectable lineage and run artifacts.

Not borrowed:

> The publication does not certify this repository or prove its records are scientifically correct.

### Responsible and transparent AI in scientific publishing

Nature Computational Science (20 Aug 2026) emphasizes transparency, accountability and human oversight.

Borrowed design lesson:

> Provider/process disclosure and declared human-review context should remain visible.

Boundary:

> `human_review=reviewed` is not peer review.

### Artifact-centered claim-aware observability

The 18 Aug 2026 preprint argues that model-call logs alone are insufficient for autonomous scientific agents; artifacts, claims, evidence and verification records need portable relations.

Borrowed design lesson:

```text
trace != provenance != claim audit != evidence envelope
```

Each object should answer a different audit question.

### Brain Researcher

The 20 Aug 2026 work emphasizes evidence-constrained claim formulation and explicit scientific review outcomes.

Borrowed design lesson:

> Keep claim qualification and evidence support explicit.

Not borrowed:

> This repository does not adopt `accepted/rejected/qualified` as runtime truth states because it has no independent domain scientific-review authority.

### From Trajectories to Evidence

The 5 Aug 2026 work makes an important distinction: a completed trajectory is not automatically evidence.

Borrowed design lesson:

> Execution validity, artifact identity, attribution and claim qualification should remain distinct.

### EarthVerse

The 24 Aug 2026 benchmark demonstrates that scientific agents can perform many local steps while strict end-to-end consistency remains substantially harder.

Borrowed design lesson:

> Record the chain across evidence, calculations, interpretation and claims instead of treating local success as global correctness.

## 3. Neighbouring systems

Current adjacent systems include scientific RAG/evidence systems, typed scientific runtimes, autonomous-scientist systems, domain research agents and workflow/provenance tooling.

The closest architectural overlap is around:

- typed/scoped scientific execution;
- evidence graphs;
- provenance;
- tool-use transparency;
- claim-aware auditability.

Epistemic Pipeline's distinct focus is the bounded contract between **claim/evidence/conflict structure, runtime-policy observations, heuristic score semantics, lineage and cross-tool handoff**.

This is a positioning observation, not a claim of global uniqueness or superiority.

## 4. Current internal architecture response

The repository now exposes stable project-owned identifiers without decorative release suffixes:

```text
epistemic-pipeline/trace
epistemic-pipeline/prov
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

The key four-day change is the explicit claim-verification sidecar:

```text
claim identity
+ evidence binding
+ consistency observations
+ conflicts
+ initial/final heuristic scores
+ process context
```

without a universal `verified=true` verdict.

## 5. Why internal version suffixes were removed

Identifiers such as `profile@1` or `profile@2` looked like standards/releases without an actual published compatibility regime. They created documentation churn and could imply stronger stability guarantees than existed.

The repository now prefers stable semantic profile names. Real external standard versions remain explicit where they are genuine external standards.

## 6. What remains intentionally absent

- built-in production LLM provider;
- scientific truth oracle;
- automatic citation-content verification against the literature;
- automatic scientific peer review;
- empirically calibrated probabilities by default;
- tamper-proof external trace anchoring;
- PROV-O RDF serializer;
- automatic acceptance/rejection of scientific claims.

These absences are part of the truthful architecture, not missing marketing labels.

## 7. Research-engineering interpretation

The repository's useful contribution is not “an agent that knows science”. It is infrastructure that makes an agent-assisted research run easier to inspect without falsely upgrading metadata into scientific authority.

```text
execution -> evidence-bearing record
not
execution -> truth
```

## 8. Cross-repository frontier position

```text
auto-doc-engine
research artifact identity / process context
        ↓
epistemic-pipeline
claim-evidence execution / verification observations / provenance
        ↓
sci-render-kit
claim-aware scientific communication / communication audit
```

Together the three repositories explore an evidence-aware research infrastructure shape. Adjacent mature tools exist at every individual layer; the value proposition is the explicit semantic handoff across the layers.
