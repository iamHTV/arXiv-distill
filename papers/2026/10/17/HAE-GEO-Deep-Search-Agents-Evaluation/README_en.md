# [2609.06027v2] Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning

## Problem
- Search-augmented LLM agents are increasingly used for consumer decisions, making them vulnerable to Generative Engine Optimization (GEO) poisoning. Existing benchmarks largely measure whether manipulated content is retrieved or endorsed, but do not track whether an agent verifies suspicious evidence, revises adopted claims, or recovers before producing its final recommendation.

## Contribution
- HAE-GEO — a benchmark that tracks the full trajectory from exposure to recovery under progressively more persuasive Web poisoning. Agents interact via a multi-turn Search–Scrape interface across three attack levels (L1 direct assertion, L2 contextual camouflage, L3 apparent corroboration).
- Controlled corpus of 72,039 clean pages and 770 poisoned pages per level spanning 8 product categories and 154 brands.
- Evaluation combines deterministic behavioral measures with six semantic rubric dimensions.

## Method (core summary)
- Trajectory-state design: controls how poisoned evidence is presented and records how an agent responds after evidence enters context.
- Three poisoning levels: L1 Direct Poisoning (unsupported assertion), L2 Contextual Camouflage (embedded in natural context), L3 Evidence-Enhanced Poisoning (corroboration chain).
- Five observable behavioral states: Exposure (E), Adoption (A), Verification Yield (V), Recovery (R), Endorsement (Y).
- Six-dimensional semantic rubric: M1 Fake Brand Risk Handling, M2 Poison Evidence Recognition, M3 Recovery after Adoption, M4 Evidence Quality & Independence, M5 Uncertainty Calibration, M6 Legitimate Utility under Attack.
- Split LLM-as-Judge Protocol: Attack-aware Poison Judge (M1–M3) vs Attack-label-blind Quality Judge (M4–M6), each score in {0,1,2}.

## Key Findings
- 10 agents evaluated, authors from Zhejiang University and Ant Group, arXiv category: cs.CR.
- Evidence recognition degrades under the corroboration trap (L3).
- Agentic search improves final resistance without improving evidence recognition or utility.
- Defense prompting increases verification, yet rarely converts verification into recovery.
- Kimi-K3: DEF FR 10.9%, 24.2%, 18.8% on L1–L3 (strongest in table).
- GPT-5.6-sol: L1 FR unchanged, L2 FR 47.6%→49.2%; GLM-4.7-Flash remains above 46% at all three levels.
- Defense adds 1.82 tool calls per query on average, raises token consumption by 24.5% macro-average.

## Actionable Insights
1. Independent verification is key to defending against GEO poisoning — agents should verify independence and provenance of seemingly corroborating evidence before accepting it. Application: add an independent verification step before the agent makes product recommendations, using sources not from poisoned pages.
2. Defense prompting increases verification but rarely converts it to recovery. Application: don't just encourage verification — require the agent to retract and change recommendations when it detects conflicting evidence.

## Assumptions & Limitations
- Controlled corpus of 72,039 clean pages and 770 poisoned pages per level may not fully reflect the real web.
- M3 only applies when prior adoption is observable.
- Not stated: effectiveness on brands and product categories beyond the 154 brands and 8 categories evaluated.

## Metadata
- Year: 2026, authors: Zhongan Bi (Zhejiang University), Qiwen Wang, Jianrong Jiang, Jigang Ding, Wenwen Xiong, Changhua Meng, Xuanang Gao, Kepeng Lin, Changjiang Jiang, Yi'ang Chen, Huan Yao, Wei Wang, Zhenyu Ma, Wenhui Dong (Ant Group), arXiv category: cs.CR, PDF link: https://arxiv.org/pdf/2609.06027v2
