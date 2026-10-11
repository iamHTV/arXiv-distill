# 2605.17079 Can LLMs Think Like Consumers? ConsumerSimBench

## Problem

LLMs are increasingly used as "digital consumers" to simulate public opinion, pre-test marketing decisions, and anticipate audience response. But existing evaluations rarely ask whether models can reconstruct the concrete reaction patterns real consumers surface in public discourse. Sharp gap between technical-benchmark performance and socially grounded consumer intuition.

## Contribution

1. ConsumerSimBench — 1,553 real Chinese social-media topics, 23,122 atomic rule-audited criteria across 4 reaction families. Decomposed into auditable yes-no decisions.
2. Three-judge agreement: 65.8% → 92.1% with atomic decomposition. 98.4% agreement with human-majority labels.
3. Discovery: technical benchmark strength ≠ consumer intuition.

## Method (core summary)

Collect 1,553 hot topics, decompose into atomic reaction criteria (14.9/topic avg), evaluate 13 frontier models on coverage of real reactions. GPT-5.2 as fixed judge with cross-validation.

## Key Findings

- Best model (Gemini-3.1-Pro): only 47.8% coverage
- GPT-5.2 and Claude-4.6 trail despite technical strength
- Structured reasoning DECREASES coverage
- Multi-agent pipeline improves: 32.9% → 37.6%
- 4 categories: Society (37%), Entertainment (33%), Sports (17%), Lifestyle (12%)

## Actionable Insights

1. DON'T use LLM as sole consumer simulator — best covers only 47.8%. False confidence risk.
2. Structured reasoning HURTS consumer prediction — over-reasoning vs intuition.
3. Multi-agent generate-reflect improves predictions — Agent predicts, Agent critiques, iterate.

## Assumptions & Limitations

- Chinese social media only — may not transfer to other markets
- Social media reactions ≠ purchase decisions
- Coverage metric doesn't measure precision (false positives)

## Metadata

- Year: 2026
- Authors: Tianyu Wang, Jiajun Li, Jianghao Lin
- Category: cs.AI, cs.CL
- PDF: https://arxiv.org/pdf/2605.17079
- Citation count: N/A
- Classification: [applied]
- Skill: N/A — benchmark, cautionary finding
