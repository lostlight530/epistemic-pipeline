# Frontier Research Part B2 — Benchmark Revision and Contamination

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

When benchmark content is corrected or contamination is suspected, what changes: benchmark identity, result comparability, interpretation, or all three

## Objects and sources

- O2 WMDP April correction
- O3 ConStat
- S3 https://github.com/centerforaisafety/wmdp
- S4 https://arxiv.org/abs/2405.16281

## WMDP observation

On 2024-04-23 the WMDP project reported modifying multiple-choice questions because of formatting and Unicode issues

It removed some excessively long WMDP-Cyber questions and some WMDP-Bio questions judged to have insufficient dual-use potential, republished the modified dataset to mirrors, and simplified the unlearning method from CUT to RMU with similar reported performance

This is a direct benchmark and method state transition

## ConStat observation

ConStat, submitted 2024-05-25, defines contamination operationally as benchmark-specific performance inflation that does not generalize to suitable reference data

The method compares a primary benchmark against related reference benchmarks relative to reference models, allowing contamination evidence without requiring direct access to hidden training data

## Analysis

The two objects expose different change axes

    WMDP
    -> benchmark content and method revision changed

    ConStat
    -> interpretation of observed performance may change
       without exact training-lineage knowledge

Therefore these identities should remain separable

- benchmark family and revision
- model revision
- execution protocol
- contamination-assessment method
- observation date

A contamination detector can support benchmark-specific performance inflation without proving the exact training-data path that caused it

## Counterevidence

WMDP correction does not invalidate every earlier observation

ConStat is a statistical method with assumptions and error modes, not an oracle for hidden provenance

## Conclusion

SUPPORTED_OBSERVATION

Benchmark revision and contamination are evidence-state transitions, not reasons to silently erase prior results
