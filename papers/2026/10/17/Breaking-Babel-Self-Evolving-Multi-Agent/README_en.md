# [2609.38660v2] Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation

## Problem
- Long-form subtitle translation faces challenges beyond conventional machine translation: a single episode may contain hundreds of sentences whose meanings depend on long-range discourse and cultural context spanning the entire episode or even series, while translation quality also requires maintaining consistent terminology and style throughout the series.

## Contribution
- SMART (Self-evolving Multi-Agent system for long-form subtitle Translation) — a self-evolving multi-agent system for long-form subtitle translation.
- SMART operates in two stages: during test-time training, it builds a persistent series-level memory and iteratively translates a subset of sentences through a dynamic graph router and a Mixture-of-Agents translation layer, equipped with tool-calling modules for terminology verification, subtitle constraint validation, and contextual retrieval; a judge-refiner loop scores each candidate translation and back-propagates textual critiques that refine agent prompts and the routing policy, without retraining the underlying LLMs.
- During test-time inference, this evolved configuration translates the remaining sentences of the series.
- To evaluate subtitle translation at scale, we introduce Subtitle Arena, covering 14 genres, 2–198 episodes per series, production years from 1959 to 2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories.
- SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing the average penalty by 6.9% over the strongest competing agent system.
- On a public benchmark, MuSC, SMART obtains the best model result across all 4 language pairs.
- SMART also achieves the best result in human evaluation with an overall score of 4.50/5.

## Method (core summary)
- Two-stage system: offline test-time training and online inference.
- Offline stage: builds persistent series-level memory and translates a subset of sentences through a dynamic graph router and a Mixture-of-Agents translation layer, equipped with tool-calling modules for terminology verification, subtitle constraint validation, and contextual retrieval.
- A judge-refiner loop scores each candidate translation and back-propagates textual critiques that refine agent prompts and the routing policy, without retraining the underlying LLMs.
- Online stage: the evolved configuration translates the remaining sentences of the series.
- Evaluated on Subtitle Arena: 14 genres, 2–198 episodes per series, production years from 1959 to 2023, and 15 target locales, together with SubMQM, a subtitle-adapted MQM framework with seven dimensions and 19 error categories.

## Key Findings
- 7 authors from University of Illinois Urbana-Champaign and Amazon, arXiv category: cs.CL.
- SMART achieves the best overall MQM score in all 15 Subtitle Arena directions, reducing the average penalty by 6.9% over the strongest competing agent system.
- On a public benchmark, MuSC, SMART obtains the best model result across all 4 language pairs.
- SMART also achieves the best result in human evaluation with an overall score of 4.50/5.

## Actionable Insights
1. Use self-evolving multi-agent system for long-form subtitle translation. Application: use a multi-agent system with dynamic graph router and Mixture-of-Agents translation layer to translate long-form subtitles.
2. Use persistent series-level memory to maintain terminology and style across multiple episodes. Application: use series-level memory to maintain terminology and style consistently across multiple episodes.

## Assumptions & Limitations
- Evaluated on 14 genres, 2–198 episodes per series, 15 target locales.
- No detailed information about training time and computational cost.

## Metadata
- Year: 2026, authors: Haibo Jin, Xinjie Li, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu (University of Illinois Urbana-Champaign, Amazon), arXiv category: cs.CL, PDF link: https://arxiv.org/pdf/2609.38660v2
