# [2609.38660v2] Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation

## Problem
Long-form subtitle translation is harder than conventional machine translation: a single episode may contain hundreds of sentences whose meanings depend on long-range discourse and cultural context spanning the entire episode or even series, while translation quality also requires maintaining consistent terminology and style throughout the series. Existing approaches remain limited: single-LLM methods operate at the sentence level and cannot keep long-range context.

## Contribution
- Introduce SMART: a self-evolving multi-agent system for long-form subtitle translation, with series-level memory, dynamic router + Mixture-of-Agents, and judge-refiner that updates prompts without retraining.
- Evaluated on 15 Subtitle Arena directions, 14 genres, 15 locales; wins all 15 directions, reduces average penalty 6.9% vs strongest agent baseline.
- SMART reduces mean Overall penalty from 0.41 to 0.37 (10.0% relative reduction), achieves the lowest Overall score.

## Method (core summary)
SMART splits content into overlapping windows of size 5, 10, and 20 with 50% overlap. Uses series-level memory to accumulate terminology and style across episodes. Dynamic router selects the right agent for each segment. Judge-refiner (judge + refiner) updates prompts based on feedback without retraining the model. First 30% of content used for test-time training, remaining 70% for held-out inference.

## Key Findings
- Wins all 15 Subtitle Arena directions, reduces average penalty 6.9% vs strongest competing agent system.
- Overall MQM penalty: 1.11 (SMART) vs 1.20 (TransAgent), 6.9% relative reduction.
- Mean Overall penalty: 0.37 (SMART) vs 0.41 (TransAgent), 10.0% relative reduction.
- Mean Accuracy penalty drops from 0.63 to 0.57, about 9.5% relative reduction.
- Uses Claude Sonnet 4.6 as default backbone but still outperforms agent systems using larger models.

## Actionable Insights
- Use multi-agent with judge-refiner to update prompts continuously without retraining: suitable for long content needing consistent terminology (e.g. movie subtitles, educational videos). Apply: solopreneur doing multi-channel content translation should build an agent system that scores and auto-refines prompts after each segment.
- Accumulate series-level memory to maintain terminology and style consistency across episodes. Apply: when translating a video series, save the glossary and style from previous episodes to use for the next ones.

## Assumptions & Limitations
- Requires long-form content with episode/series structure to have long-range context; doesn't apply to single-sentence translation.
- Paper admits: default backbone is Claude Sonnet 4.6, not evaluated on large open-source models.
- Limitation paper doesn't mention: not tested on low-resource languages, not evaluated on real inference cost.

## Metadata
- Year: 2026
- Authors: Haibo Jin, Xinjie Li, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu (UIUC, Amazon)
- arXiv category: cs.AI, cs.CL
- PDF link: https://arxiv.org/pdf/2609.38660
