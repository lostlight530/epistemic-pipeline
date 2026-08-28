# Frontier Alignment — Epistemic Pipeline

**Repository:** `epistemic-pipeline`  
**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-29  
**Normative boundaries:** `RESEARCH_CONTRACT.md`, `CLAIM_AUDIT_CONTRACT.md`, `CLAIM_TRANSFER_CONTRACT.md`, `ASSERTION_BASIS_AND_AUDIT_COVERAGE.md`

## Current research question

The 2026 frontier increasingly asks not only whether an agent completed a workflow, but whether the resulting record can be reopened, audited and safely handed forward:

```text
Can artifacts be attributed to actions?
Can claims be linked to evidence?
Can conflicts/qualification be inspected?
Can the basis of a recorded assertion be identified?
Can audit coverage be measured without pretending it is truth?
Can a claim move downstream without losing its constraints?
Can human/AI process context be disclosed?
```

Epistemic Pipeline addresses these at the research-execution/evidence-contract layer.

## Day-5 architecture response

The repository separates:

```text
claim/evidence content
assertion / observation basis
dimensional audit coverage
provenance lineage
scientific validity
```

Coverage counts how many indexed claims carry particular audit dimensions. It is not a scientific-quality or probability score.

## Day-6 architecture response: claim transfer

A claim ID is not enough for long-horizon research. If it moves downstream without its evidence refs, conflicts, observations and score semantics, the new context can silently overstate it.

`core/claim_transfer.py` therefore emits `epistemic-pipeline/claim-transfer` as a bounded subset contract over an existing claim-verification sidecar.

Every transferred claim carries explicit non-inheritance constraints:

```text
scientific_validity_inherited: false
evidence_sufficiency_inherited: false
peer_review_inherited: false
conflicts_must_remain_visible: true
heuristic_scores_must_retain_non_probability_semantics: true
```

```text
transfer != acceptance
inheritance != validation
conflict preservation != conflict adjudication
```

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
trace != provenance != claim audit != claim transfer != evidence envelope
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

Borrowed: coverage as a measurable structural dimension and conflict visibility as a first-class audit concern.

Not claimed: provenance soundness.

### Praxist — solution/evidence lineages

**Praxist: From Experimental Artifacts to Solution Lineages** (arXiv:2608.25955, 26 Aug 2026) argues that isolated attempts and logs lose causal/useful research inheritance, and materializes typed evidence/solution lineage across generations.

Borrowed principle: downstream generations should inherit explicit records of unresolved claims, useful constraints and evidence relationships rather than reconstruct them from conversation history.

Not borrowed: Praxist's full generational R&D loop, evaluator authority or benchmark claims.

### ReproAgent — persistent contracts

**ReproAgent: Contract-Guided Paper-to-Code Reproduction** (arXiv:2608.24291, 25 Aug 2026) persists implementation requirements and reference evidence across planning, generation and repair.

Borrowed principle: constraints/evidence context should survive long agent trajectories as explicit contracts.

Not borrowed: its paper-to-code reproduction task or reported benchmark authority.

### AI detection versus disclosure

Detection is a separate inference problem from explicit disclosure.

This repository uses provider-adapter metadata/caller declarations and records `automatic_ai_detection_used: false`; it does not classify prose to infer AI authorship/use.

## Neighbouring systems

Adjacent systems include scientific RAG/evidence systems, typed scientific runtimes, autonomous-scientist systems, generational R&D systems, reproduction agents, domain research agents and workflow/provenance tooling.

Epistemic Pipeline's focus is the bounded contract between:

```text
claim/evidence/conflict structure
runtime-policy observations
heuristic-score semantics
assertion basis
claim audit coverage
claim transfer constraints
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
- automatic accepted/rejected claim verdicts;
- automatic downstream scientific acceptance from claim-transfer metadata.

These absences are truthful architecture boundaries.

## Research-engineering interpretation

```text
execution -> inspectable evidence-bearing record
not
execution -> truth
```

Day 6 adds:

```text
claim-verification -> bounded claim-transfer -> downstream use
not
claim reference -> inherited scientific authority
```

## Cross-repository frontier position

```text
auto-doc-engine
  artifact identity / assertion basis / artifact coverage / artifact lineage
        ↓
epistemic-pipeline
  claim-evidence execution / observation basis / claim coverage / claim transfer / provenance
        ↓
sci-render-kit
  claim-aware communication / communication coverage / figure evidence / communication transfer
```

Together the repositories explore evidence-aware research infrastructure with explicit inheritance boundaries.

## Hard boundaries

```text
assertion basis != correctness
audit coverage != scientific validity
coverage ratio != probability
coverage != provenance soundness
evidence binding != evidence sufficiency
claim transfer != acceptance
inheritance != validation
provider identity != output validity
human review != peer review
provenance != truth
```
