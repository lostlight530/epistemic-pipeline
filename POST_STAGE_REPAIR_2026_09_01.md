# Post-Stage Repair — epistemic-pipeline — 2026-09-01

**Status:** current repair note for the closed August evidence-infrastructure stage  
**Stage remains closed:** 2026-08-24 → 2026-08-31

This repair hardens the current evidence stack without rewriting or reopening the closed stage.

## Repairs

### Claim identity/origin ambiguity

Repeated `claim_id` values are no longer silently represented by the first observed state/hash when multiple structured occurrences exist.

The claim-verification sidecar now records:

```text
origin_state_ids[]
claim_record_sha256s[]
claim_origin_ambiguous
claim_identity_ambiguous
```

Singular compatibility fields remain populated only when the source is actually singular.

### Claim-transfer preservation

Claim Transfer now carries the ambiguity sets/flags and explicit constraints requiring them to remain visible downstream.

```text
ambiguity preserved != ambiguity adjudicated
identity ambiguity != scientific contradiction
```

### Maintenance-report portability and scope

The deterministic maintenance scanner now uses repository-relative portable paths, binds configuration bytes by SHA-256, rejects configured scan paths escaping the repository root, and records optional report-output writes accurately.

## External calibration checked through 2026-09-01

Current scientific-agent evaluation continues to show that terminal correctness can diverge from trajectory honesty and that intermediate errors can propagate through a research workflow. The repository borrows only the process-inspection lesson: repeated claim identities and intermediate provenance ambiguity should remain explicit rather than being hidden by final-state aggregation.

Scientific-agent work involving physical experiment interfaces also reinforces the broader separation between an action completing and a scientific conclusion being valid. This repository remains at the evidence/claim layer and does not claim physical-instrument execution authority.

## Boundaries

```text
claim identity ambiguity != contradiction
multiple origins != invalid claim
transfer preservation != scientific acceptance
config hash != configuration correctness
scope containment != provenance soundness
maintenance clean != claim truth
provenance != truth
```

No GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates are introduced. No test execution is used as completion evidence.
