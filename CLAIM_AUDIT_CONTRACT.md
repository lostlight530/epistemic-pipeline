# Claim Audit Contract — Epistemic Pipeline

**Calibration:** 2026-08-27  
**Implemented profile:** `epistemic-pipeline/claim-verification`  
**Scope:** claim identity, evidence bindings, structural observations, conflicts, bounded heuristic scores and process context

## 1. Why a separate claim audit exists

Run-level telemetry answers when operations happened. Provenance answers lineage questions. Neither is enough to answer:

```text
Which claim was indexed?
Which evidence refs were attached?
Was any structural consistency observation recorded?
Was a cross-source observation recorded?
Were conflicts recorded?
What initial/final heuristic score observations existed?
What provider/review context surrounded the run?
```

`core/claim_audit.py` therefore writes a separate `<run_id>.claim-audit.json` sidecar.

## 2. It is not a truth graph

The sidecar intentionally contains no universal `verified` boolean.

A claim can be structurally checked and still be wrong. Evidence can be linked and still be weak, irrelevant or misinterpreted. No recorded conflict does not imply independent corroboration.

## 3. Claim record fields

A normalized claim audit can contain:

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
```

Full claim prose is not duplicated into this sidecar by default.

## 4. Audit states

Current states describe only the observed structural/audit situation:

- `indexed_only`
- `evidence_bound`
- `structurally_checked`
- `conflict_recorded`
- `structurally_checked_with_conflict`

They are not scientific-review outcomes.

In particular, this repository does **not** map them to `accepted`, `rejected`, `validated`, `confirmed`, `proven`, or similar verdict language.

## 5. Structural observations

`internal_consistency_report` and `cross_source_matrix` are retained as provider/runtime observations.

They can show what the current workflow recorded, but the audit layer does not independently rerun external experiments, inspect every source, or establish scientific correctness.

## 6. Conflict records

Conflicts are linked to a claim when the claim ID appears as the declared source or target of a conflict item. The audit record keeps:

```text
other_ref
relation
severity
conflict_record_sha256
```

The hash identifies the recorded conflict structure. The repository does not automatically adjudicate which side is correct.

## 7. Heuristic scores

The audit preserves two distinct observations when available:

```text
initial -> verify-stage seed
final   -> synthesize-stage propagated score
```

Both remain heuristic values.

```text
score != calibrated probability
score change != probability update
final score != truth score
```

## 8. Process context

The audit keeps minimal provider disclosure and declared human-review state.

Unknown provider/model/version values remain `null`; they are never guessed from class names, prompts or external marketing names.

The built-in `MockProvider` declares no model and no version because neither exists as an independently meaningful provider release.

## 9. Relationship to the Evidence Envelope

```text
claim-verification sidecar
        ↓ referenced by
evidence-envelope
```

The Evidence Envelope records the sidecar path/hash where locally available. It does not copy every audit record into the envelope.

This keeps the envelope compact and makes claim audit independently inspectable.

## 10. Relationship to upstream/downstream artifacts

Upstream Auto Doc records may be carried as references:

```text
auto-doc-engine/artifact-record
```

Downstream Sci Render can reference this claim audit through `research_context.claim_audit_ref`, allowing a scientific figure to state which upstream claim-audit artifact informed its communication context.

A reference does not inherit truth.

## 11. Privacy and payload minimization

The audit stores claim IDs, hashes and references rather than duplicating full claim/source payloads by default. This improves portability and limits accidental duplication of sensitive research text.

It is not a confidentiality guarantee; callers remain responsible for what they place in IDs, refs, notes and upstream artifacts.

## 12. Global research calibration

Recent 2026 work strengthens the need for this separation:

- artifact-centered claim-aware observability argues that model-call logs alone are insufficient;
- *From Trajectories to Evidence* explicitly separates completed trajectories from auditable evidence;
- *Brain Researcher* emphasizes evidence-bounded claim qualification and scientific review;
- *EarthVerse* shows local task success can coexist with weak strict end-to-end scientific consistency.

This repository borrows the architectural lesson: **record verification dimensions separately from scientific verdicts**. It does not copy domain-review verdict labels that the runtime is not qualified to produce.

## 13. Forbidden interpretations

```text
indexed_only -> false
structurally_checked -> true
no conflict -> corroborated
human_review=reviewed -> peer reviewed
provider declared -> provider authenticated
claim_record_sha256 -> semantic truth
```

None of those implications is valid.
