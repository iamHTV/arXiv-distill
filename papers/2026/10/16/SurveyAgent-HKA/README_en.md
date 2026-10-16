# [2609.05938v1] SurveyAgent-HKA: A multi-agent framework for scientific survey generation with LLMs and human knowledge augmentation

## Problem
Automatic scientific survey generation has become an important task in scientific documentation, but current systems do not effectively combine LLMs with human knowledge augmentation to create high-quality surveys in terms of structure and content.

## Contribution
- Introduce SurveyAgent-HKA: a multi-agent framework for scientific survey generation with LLMs and human knowledge augmentation.
- Evaluate on two domains: computer science and medicine.
- Citation quality: CS domain (14.95% Precision, 19.53% Recall, 16.94% F1), Medical domain (16.78% Precision, 22.95% Recall, 19.39% F1).
- Key-point recall: 53.85% (CS) and 57.07% (medicine).
- H1 match F1: 38.53%, H2 match F1: 33.42%.
- With human knowledge augmentation: citation F1 increased by 3.86% (CS), H1 match +9.31%, H2 match +6.19%; Medical: citation F1 +2.62%, H1 +4.92%, H2 +6.71%.

## Method (core summary)
SurveyAgent-HKA is a multi-agent framework combining LLMs and human knowledge augmentation to generate scientific surveys. The framework includes agents responsible for different stages (planning, searching, writing, revising) and combines human knowledge to improve quality.

## Key Findings
- Citation quality: CS (14.95% P, 19.53% R, 16.94% F1), Medicine (16.78% P, 22.95% R, 19.39% F1).
- Key-point recall: 53.85% (CS), 57.07% (medicine).
- H1 match F1: 38.53%, H2 match F1: 33.42%.
- Human knowledge augmentation improves citation F1 (+3.86% CS, +2.62% Medicine), H1 match (+9.31% CS, +4.92% Medicine), H2 match (+6.19% CS, +6.71% Medicine).
- Components like citation expansion, re-ranking, clustering, few-shot learning all have significant impact on quality (removing each component reduces F1 from 2.15% to 7.02%).

## Actionable Insights
- Combining human knowledge into the LLM survey generation process significantly improves quality. Apply: solopreneur using LLM to write surveys or resource documents should combine human review and editing, not let LLM write completely independently.
- Components like citation expansion, re-ranking, clustering, few-shot learning are all important. Apply: when building LLM document generation system, keep these steps, don't skip them to optimize cost.

## Assumptions & Limitations
- Requires reference documents and human knowledge to augment; doesn't apply without reference sources.
- Paper admits: evaluated on two domains (CS and medicine); may differ on other domains.
- Limitation paper doesn't mention: not evaluated on real cost of human augmentation, not tested on many domains beyond science.

## Metadata
- Year: 2026
- Authors: Tong Bao, Mir Tafseer Nayeem, Yi Zhao, Davood Rafiei, Chengzhi Zhang (Nanjing University of Science and Technology, University of Alberta, Anhui University)
- arXiv category: cs.AI, cs.CL
- PDF link: https://arxiv.org/pdf/2609.05938
