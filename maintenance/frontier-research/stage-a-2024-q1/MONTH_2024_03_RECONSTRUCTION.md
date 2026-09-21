# March 2024 Reconstruction — Stage A

## Month frame

March contains the quarter's densest cluster of evaluation-state events: Chatbot Arena's preference-evaluation paper, WMDP's proxy benchmark and immediate correction, Gemini 1.5 technical-report evidence, and a TrustLLM toolkit revision.

Coverage: `SEARCH_BOUNDED`.

## M1 — WMDP, 2024-03-05; correction 2024-03-08

Paper: https://arxiv.org/abs/2403.03218  
Project: https://github.com/centerforaisafety/wmdp  
Website: https://www.wmdp.ai/

WMDP publishes 3,668 multiple-choice questions across biosecurity, cybersecurity, and chemical security as a proxy for hazardous knowledge and an evaluation surface for unlearning methods.

The project records a 2024-03-08 correction to WMDP-Cyber because of choice-randomization issues.

### Research significance

The correction occurs only days after publication, making version identity immediately material. “WMDP score” without dataset revision is underspecified for longitudinal work.

The benchmark's own word `proxy` is also epistemically significant. A proxy measure should not be silently promoted to complete real-world risk measurement.

## M2 — Chatbot Arena paper, 2024-03-07

Source: https://arxiv.org/abs/2403.04132

The paper describes pairwise crowdsourced preference evaluation and reports analysis over more than 240K votes, including comparison with expert raters.

### Research significance

Preference is a distinct claim type. A pairwise vote supplies evidence about what a participant preferred under a specific interaction. Aggregated rankings are statistical products of that process.

They do not automatically transfer to truthfulness, safety, or scientific correctness.

## M3 — Gemini 1.5 technical report, 2024-03-08

Source: https://arxiv.org/abs/2403.05530

The technical report provides a richer evaluation record than the February announcement, including multimodal long-context tests and expanded model details.

### Temporal significance

February product announcement and March technical report are related but distinct evidence events. A later technical report can refine the evidence envelope without rewriting what was publicly documented in February.

## M4 — TrustLLM v0.2.4, 2024-03-20

Project: https://github.com/HowieHwong/TrustLLM

The repository reports bug fixes and Gemini Pro API support. This is direct evidence that executable evaluation tooling can change while the benchmark concept retains the same name.

## M5 — Post-Stage WMDP correction as forward evidence

On 2024-04-23, outside Q1, the WMDP project later changed questions for formatting/unicode, excessive length, and insufficient dual-use potential, and simplified its unlearning method.

This event is **not part of March**. It is recorded only as a later correction demonstrating why the March benchmark state must remain recoverable.

## March synthesis

March exposes four distinct evidence classes:

- human preference observations;
- provider technical-report claims;
- proxy benchmark scores;
- executable toolkit/data revisions.

A sound pipeline should not collapse these into one “verified” state.

## March negative space

Not established:

- that Arena preference equals factual quality;
- that WMDP fully measures malicious-use risk;
- that Gemini long-context results independently reproduce;
- that TrustLLM results before/after tooling updates are numerically identical;
- the quantitative impact of WMDP's March correction on all model scores.

## Quarter-close implication

By March, the quarter supports a coherent conclusion: model-evaluation claims are versioned relations between a claim and an evidence envelope. **The envelope itself can change.**
