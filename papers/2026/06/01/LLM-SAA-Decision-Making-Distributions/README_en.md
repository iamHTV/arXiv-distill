# 2602.06357 LLM-SAA: LLM-persona Generated Distributions for Decision Making

## Problem

Many business decisions depend on outcome distributions: pricing needs willingness-to-pay, inventory needs demand, assortment needs preferences. LLMs can generate simulated distributions from product descriptions, but: are they practically useful? And what metrics to evaluate them?

## Contribution

1. LLM-SAA framework — LLM-generated distributions for decision optimization.
2. Decision-aware metrics — evaluate by decision quality, not distribution similarity. Wasserstein distance can be misleading.
3. LLM-SAA is practically useful, especially in low-data regimes.

## Method (core summary)

Prompt LLM with product description → generate simulated preferences/WTP/demand → construct empirical distribution → optimize decision under simulated distribution → evaluate decision quality.

## Key Findings

- Practically useful, especially low-data regimes
- 3 problems: assortment, pricing, newsvendor
- Wasserstein distance misleading — good distribution similarity ≠ good decision quality
- Decision-aware metrics more appropriate
- Persona-sampling and few-shot improve quality
- Competitive with real data when scarce

## Actionable Insights

1. Use LLM for simulated distributions when lacking real data. Example: startup, no historical data → simulate 100 consumers' WTP → optimize price.
2. Evaluate by DECISION QUALITY, not Wasserstein distance.
3. Persona-sampling improves simulation — diverse personas → realistic distribution.

## Assumptions & Limitations

- Assumption: LLM has sufficient world knowledge
- 3 canonical problems only
- Product description quality matters
- Systematic biases in preference simulation

## Metadata

- Year: 2026
- Authors: Jackie Baek, Yunhan Chen, Ziyu Chi, Will Ma
- Category: cs.AI, cs.CL, econ.GN
- PDF: https://arxiv.org/pdf/2602.06357
- Citation count: N/A
- Classification: [applied]
- Skill: llm-saa-decision-simulation
