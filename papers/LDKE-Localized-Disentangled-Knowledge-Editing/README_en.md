# 2605.29826 LDKE: Localized and Disentangled Knowledge Editing for Multimodal LLMs

## Problem

MKE methods effectively modify target facts but fail to generalize to related queries and cause unintended alterations on unrelated information. Two failure modes: Causal Misalignment (edits confined to specific samples) and Feature Entanglement (unintended changes to coupled but irrelevant info).

## Contribution

1. Formalize 2 failure modes: Causal Misalignment, Feature Entanglement.
2. LDKE framework: localize fact-specific layers + disentangle relevant from irrelevant inputs.
3. Fast Localization + Disentanglement Classifier.

## Method (core summary)

Fast Localization: gradient-based attribution identifies critical layers. Targeted Update: edit only critical layers. Disentanglement Classifier: routes relevant inputs through edited pathway, irrelevant through original pathway.

## Key Findings

- Superior propagation — edits generalize to related contexts
- High locality — unrelated knowledge preserved
- Solves both failure modes
- Fast Localization more efficient than brute-force

## Actionable Insights

1. Localize fact-specific layers before editing — don't update all layers.
2. Disentanglement prevents unintended alterations on related-but-irrelevant facts.
3. Fast Localization applicable to other model editing tasks (bias mitigation).

## Assumptions & Limitations

- Facts stored in identifiable layers (may be distributed)
- Disentanglement Classifier needs training data
- MLLMs tested — adaptation needed for text-only LLMs
- Edits may have unforeseen cascading effects

## Metadata

- Year: 2026
- Authors: Leijiang Gu, Zhen Zeng, Feng Li, Xinjian Gao, Zenglin Shi
- Category: cs.AI, cs.CL
- PDF: https://arxiv.org/pdf/2605.29826
- Citation count: N/A
- Classification: [applied]
- Skill: ldke-knowledge-editing
