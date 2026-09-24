# E3 — QuestBench Underspecification and Information Acquisition

## Research question
Can performance on well-specified reasoning tasks stand in for the ability to recognize missing information and ask the right clarification question?

## Evidence
Google DeepMind's QuestBench publication page is dated 2025-03-28. It formalizes underspecified tasks as constraint-satisfaction problems with a missing variable assignment and evaluates whether a model can identify the minimal necessary question. It includes Logic-Q, Planning-Q, GSM-Q and GSME-Q.

Source: https://deepmind.google/research/publications/121987/

## Analysis
QuestBench adds an epistemic state before ordinary task solving:

```text
problem statement
-> detect underspecification
-> identify missing variable/information
-> ask bounded clarification
-> receive information
-> solve
```

A model can succeed on the fully specified task yet fail to identify what information is missing. Therefore:

```text
reasoning_on_complete_input
!= information_acquisition_competence
```

This distinction maps directly to preserving UNKNOWN and missing-evidence states rather than forcing premature completion.

## Outcome
`SUPPORTED_OBSERVATION / DIRECTLY_RELEVANT_TO_EPISTEMIC_BOUNDARY`
