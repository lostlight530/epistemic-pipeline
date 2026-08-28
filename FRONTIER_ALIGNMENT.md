# Frontier Alignment — Epistemic Pipeline

**Repository:** `epistemic-pipeline`  
**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-28  
**Normative boundaries:** `RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`

## Current research question

The 2026 frontier increasingly asks not only whether an agent completed a workflow, but whether the resulting record can be reopened and audited:

```text
Can artifacts be attributed to actions?
Can claims be linked to evidence?
Can conflicts/qualification be inspected?
Can the basis of a recorded assertion be identified?
Can audit coverage be measured without pretending it is truth?
Can human/AI process context be disclosed?
```

Epistemic Pipeline addresses these at the research-execution/evidence-contract layer.

## Day-5 architecture response

The repository now separates:

```text
claim/evidence content
assertion / observation basis
dimensional audit coverage
provenance lineage
scientific validity
```

For claim verification, current bases identify whether information came from analyze output, verify output, state output, provider-adapter metadata or caller declaration.

Coverage counts how many indexed claims carry particular audit dimensions. It is not a scientific-quality or probability score.

## External signals

### Provenance in autonomous science

Re-openable provenance supports auditing/correction of autonomous research processes.

Borrowed: preserve lineage and run artifacts.

Not borrowed: provenance makes the science correct.

### Transparent AI use / human oversight

Current scientific-publishing guidance emphasizes transparency, accountability and human oversight.

Borrowed: preserve provider/process disclosure and human-review context.

Boundary: `human_review=reviewed` is not peer review.

### Artifact-centered claim-aware observability

Scientific-agent observability work argues model-call logs alone are insufficient; artifacts, claims, evidence and verification relations should be portable audit objects.

Borrowed:

```text
trace != provenance != claim audit != evidence envelope
```

### From Trajectories to Evidence

Completed execution is not automatically evidence.

Borrowed: execution validity, artifact identity, attribution and claim qualification remain distinct.

### Brain Researcher

Evidence-constrained claim formulation and explicit review outcomes motivate keeping evidence support and qualification visible.

Not borrowed: accepted/rejected/qualified runtime truth states; this repository has no independent domain scientific-review authority.

### EarthVerse

Strong local task performance can coexist with weak strict end-to-end consistency across evidence, scales, units, calculations and interpretation.

Borrowed: record the chain rather than treating local success as global correctness.

### Claim-level auditability

*From Fluent to Verifiable* distinguishes provenance coverage, provenance soundness, contradiction transparency and audit effort.

Day-5 implementation borrows **coverage as a measurable structural dimension**.

It does not claim provenance soundness, because soundness requires stronger verification than the current runtime performs.

### AI detection versus disclosure

Current reporting on AI-detection tools reinforces that detection is a separate inference problem from explicit disclosure.

This repository uses provider-adapter metadata/caller declarations and records `automatic_ai_detection_used: false`; it does not classify prose to infer AI authorship/use.

## Neighbouring systems

Adjacent systems include scientific RAG/evidence systems, typed scientific runtimes, autonomous-scientist systems, domain research agents and workflow/provenance tooling.

Epistemic Pipeline's focus is the bounded contract between:

```text
claim/evidence/conflict structure
runtime-policy observations
heuristic-score semantics
assertion basis
claim audit coverage
lineage
cross-tool handoff
```

This is positioning, not a claim of global uniqueness or superiority.

## What remains intentionally absent

- built-in production LLM provider;
- scientific truth oracle;
- provenance soundness validator;
- automatic citation-content verification;
- automatic AI-text detection;
- scientific peer-review engine;
- calibrated truth probabilities by default;
- tamper-proof external trace anchoring;
- PROV-O RDF serializer;
- automatic accepted/rejected claim verdicts.

These absences are truthful architecture boundaries.

## Research-engineering interpretation

```text
execution -> inspectable evidence-bearing record
not
execution -> truth
```

Day 5 extends this to:

```text
recorded field -> explicit basis
recorded claims -> dimensional coverage
not
basis/coverage -> correctness
```

## Cross-repository frontier position

```text
auto-doc-engine
  artifact identity / assertion basis / artifact coverage
        ↓
epistemic-pipeline
  claim-evidence execution / observation basis / claim coverage / provenance
        ↓
sci-render-kit
  claim-aware communication / communication coverage / figure evidence
```

Together the repositories explore evidence-aware research infrastructure. Mature adjacent tools exist at individual layers; the emphasis here is explicit semantic handoff without inherited truth claims.

## Hard boundaries

```text
assertion basis != correctness
audit coverage != scientific validity
coverage ratio != probability
coverage != provenance soundness
evidence binding != evidence sufficiency
provider identity != output validity
human review != peer review
provenance != truth
```
