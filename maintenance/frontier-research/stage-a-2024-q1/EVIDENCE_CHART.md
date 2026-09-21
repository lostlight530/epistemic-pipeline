# Evidence Chart — Stage A / 2024-Q1

## 0. Identity

- **Repository:** `lostlight530/epistemic-pipeline`
- **Stage:** `A / 2024-Q1`
- **Charting date:** `2026-09-21`
- **Method:** single-producer structured extraction
- **Coverage:** `SEARCH_BOUNDED`

## 1. Questions served

RQ1 evidence envelopes; RQ2 verification limits; RQ3 revision/comparability.

## 2. Variables

| Variable | Meaning |
|---|---|
| claim_type | truthfulness/safety/preference/proxy risk/long-context/etc. |
| evidence_object | benchmark/corpus/report/run |
| evidence_version | dataset/tool/model/report state |
| evaluation_condition | task/trigger/context/prompt/judge conditions |
| relation_to_evidence | supported/contradicted/unsupported-in-context/proxy/preference/etc. |
| revision_state | initial/revised/corrected |
| independence | source-family relation |
| transfer_limit | what cannot be inferred |

## 3. Object chart

| Object | Claim/evaluation target | Evidence mechanism | Version/revision issue | Main epistemic limit |
|---|---|---|---|---|
| O1 TrustLLM | multidimensional trustworthiness | >30 datasets, 6 benchmarked dimensions | toolkit evolves Jan-Mar | dimension scores != universal trust probability |
| O2 Sleeper Agents | persistence of conditional backdoor behavior | constructed models + safety-training experiments | experimental setup fixed to study | proof-of-concept != prevalence |
| O3 RAGTruth | hallucination under RAG | source-linked manual span annotation | Feb annotation/data update | source present != claim supported |
| O4 Gemini 1.5 | long-context/multimodal capability | provider benchmarks/technical report | Feb announcement -> Mar report | task result != universal long-context reliability |
| O5 Chatbot Arena | human preference | pairwise crowdsourced votes + statistics | live platform changes over time | preference != truth/safety |
| O6 WMDP | hazardous-knowledge proxy/unlearning | 3,668 MCQ benchmark + method tests | Mar 8 correction; Apr later correction | proxy score != complete real-world risk |

## 4. Finding chart

| ID | Observation | Sources | Evidence class | Boundary |
|---|---|---|---|---|
| F1 | TrustLLM decomposes trustworthiness into typed dimensions | S1,S2 | benchmark taxonomy | dimensions remain method-dependent |
| F2 | TrustLLM executable tooling changes within Q1 | S2 | project revision history | same benchmark name != same execution surface |
| F3 | Sleeper Agents shows tested safety-training regimes can leave engineered conditional behavior | S3,S4 | proof-of-concept experiment | no prevalence inference |
| F4 | RAGTruth links hallucination annotations to source information | S5,S6 | annotated corpus | retrieval != entailment |
| F5 | RAGTruth adds `implicit_true` in February | S6 | annotation revision | unsupported-in-context != false |
| F6 | Gemini 1.5 February announcement reports 1M-token experimental private preview | S7 | provider report | availability/evaluation scoped |
| F7 | Gemini March technical report broadens evaluation record | S8 | technical report | later evidence != earlier public state |
| F8 | Arena paper uses pairwise human preference and >240K votes | S9 | platform evaluation | preference != factual correctness |
| F9 | WMDP calls itself a proxy benchmark for hazardous knowledge | S10,S11 | benchmark definition | proxy != full risk |
| F10 | WMDP dataset changes on Mar 8 | S12 | correction | result must bind revision |
| F11 | WMDP changes again Apr 23 | S12 | post-Stage correction | future comparisons must preserve Q1 state |
| F12 | benchmark evidence is a versioned envelope | cross-object synthesis | analytic | not a universal scoring formula |

## 5. Counterevidence / narrowing matrix

| Simplistic claim | Narrowing evidence | Resolution |
|---|---|---|
| benchmark score = capability truth | multiple typed/proxy/preference tasks | rejected |
| safety pass = globally safe | conditional backdoor study | rejected |
| retrieved evidence = supported output | RAGTruth | rejected |
| long context = reliable reasoning over all content | task-specific Gemini evaluations | not established |
| preference rank = truthfulness rank | Arena measures preference | rejected |
| same benchmark name = directly comparable | in-quarter dataset/tool revisions | rejected |

## 6. Negative space

- no model evaluations rerun in this research;
- no independent replication of provider/model claims;
- no quantitative score-delta analysis across benchmark revisions;
- no evidence that one benchmark subsumes the others;
- no inference of model mental state or hidden intention;
- no universal probability attached to qualitative evidence classes.

## 7. Analytic note

Across Q1, the dominant pattern is that the **evidence envelope itself becomes an object with state**. A claim should carry not just evidence links but the versioned conditions under which that evidence was produced.
