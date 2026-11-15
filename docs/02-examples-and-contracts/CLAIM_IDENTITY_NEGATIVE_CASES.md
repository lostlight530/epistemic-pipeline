# Claim identity and transfer — source-derived negative cases

**Document class:** durable claim/evidence research-method companion  
**Source baseline:** `main@12f203ffb78e7ee97b96f3438811a60b53cac934`, inspected 2026-11-15  
**Owners:** [Claim Audit](./CLAIM_AUDIT_CONTRACT.md), [Claim Transfer](./CLAIM_TRANSFER_CONTRACT.md), [Assertion Basis](./ASSERTION_BASIS_AND_AUDIT_COVERAGE.md)  
**Implementation:** `core/claim_audit.py`, `core/claim_transfer.py`, `core/evidence_envelope.py`

## Identity model

One `claim_id` may appear in more than one structured claim body or originating state, so it must not silently stand for a unique proposition, source version, or scientific verdict

```text
results[state_id].outputs.claims_registry
  -> claim_id + origin_state_ids + claim_record_sha256s
evidence_chains + consistency observations + conflict_registry
  -> bounded documentary audit state
claim audit sidecar -> selection -> transfer
  -> claim IDs + references + ambiguity + conflict + observations
     [not the complete original claim prose]
```

## Negative-case matrix

| ID | Input variation | Exact code surface | Supported observation and limit |
| --- | --- | --- | --- |
| E-1 | Same `claim_id` in two state outputs with distinct record bodies | `build_claim_verification` | Multiple record digests and origin IDs retained, not first-body authority |
| E-2 | Evidence refs exist without independent source inspection | `_audit_state` | `evidence_bound` records linkage, not evidence sufficiency |
| E-3 | Conflict and structural observation coexist | `_audit_state` | `structurally_checked_with_conflict` takes precedence, conflict not erased |
| E-4 | Two reference IDs derive from one common original source | source/evidence refs | Reference multiplicity is not independent corroboration |
| E-5 | Select an explicitly requested absent `claim_id` | `claim_transfer.py::_select_claims` | Raises `ValueError`, does not fabricate selected claim |
| E-6 | Transfer a record with origin/identity ambiguity and conflicts | `_select_claims` | Copies ambiguity and conflicts instead of resolving them |
| E-7 | Populate all audited metadata categories | `_coverage_summary` | Ratios describe field presence; `aggregate_score=None` |

## Reproducibility boundary

A future executed fixture should retain exact `run_result` JSON, `state_id`, original claim records, all record SHA values, claim audit JSON, selected transfer JSON, run ID, code revision, command, environment, and result

To verify conflict precedence, inspect `_audit_state` directly rather than interpreting a high heuristic score as conflict resolution

A downstream review that needs exact claim wording must recover the original record by preserved identity, because transfer does not copy full natural-language claim prose

**Evidence status:** current code examined, new test invocations `NOT_EXECUTED`, external proposition evaluation `NOT_PERFORMED`
