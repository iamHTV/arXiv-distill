# [2602.11780] RELATE: A Reinforcement Learning-Enhanced LLM Framework for Advertising Text Generation

## Problem
Prior work fails to solve effective ad text generation because: existing industrial systems follow a two-stage paradigm — generate candidate text first, then align with performance metrics like CTR. This decoupling leads to misaligned optimization objectives, low funnel efficiency, and limited global optimality. Additionally, text fatigue — repeatedly showing the same ad to the same user — reduces engagement.

## Contribution
1. **End-to-end framework**: Instead of two separate stages, RELATE unifies generation and objective alignment in a single model via policy learning
2. **Multi-dimensional reward**: Jointly models quality reward, diversity reward, and CTCVR reward with compliance constraints
3. **Granularity-aware credit assignment**: Addresses reward sparsity and delayed feedback by attributing rewards at token level, not just sentence level

## Method (core summary)
RELATE builds on LLMs, uses GRPO (Group Relative Policy Optimization) for training. Reward has 3 components: (1) Quality reward — structural quality (length, format) + semantic quality (correctness, relevance, risk-control); (2) Diversity reward — anti-text-fatigue by rewarding distinct ads; (3) CTCVR reward — conversion-oriented metrics directly from online feedback. Credit assignment strategy: diversity and semantic quality constraints attributed at token level, while structural quality and CTCVR at sentence level.

## Key Findings
- Online deployment: +9.19% CTCVR over production baseline
- Compliance: improved over both production system and SFT baseline
- Diversity: notably higher than baselines
- Ablation study: Model 1 (structural quality only) → Model 2 (+CTCVR) → Model 3 (+diversity) → Model 4 (+semantic quality) → RELATE (+credit assignment). Credit assignment provides clear improvement
- Human evaluation: RELATE outperforms baselines on fluency, relevance, attractiveness

## Actionable Insights
1. **Unify generation and optimization**: Instead of creating content then optimizing separately, integrate business objectives directly into the generation process. Example: when AI writes marketing emails, don't just optimize for open rate — integrate conversion goal into generation so the model creates emails oriented toward conversion, not just opens.

2. **Multi-dimensional reward for content**: Optimizing a single metric (like CTR) is insufficient. Need joint reward: quality + diversity + business outcome. Example: content team KPIs — not just engagement rate but also brand consistency, content variety, and conversion.

3. **Credit assignment at appropriate granularity**: Assign rewards at the right level of detail — semantic constraints at token level, business metrics at sentence level. Example: when evaluating AI-written ad copy, check grammar/relevance per sentence (token level), but check conversion effectiveness for the entire ad (sentence level).

## Assumptions & Limitations
**Conditions for the method to work:**
- Needs online feedback data (CTR, CTCVR logs) from production system
- Needs clear compliance rules to create risk-control reward
- Needs sufficient scale — paper uses large-scale industrial datasets from Baidu

**Limitations the paper acknowledges:**
- Future work: explore richer reward designs like semantic diversity rewards
- Future work: more fine-grained credit assignment strategies

**Limitations the paper does NOT mention:**
- Does not discuss cold start problem — model needs sufficient historical data to train
- Does not address multi-platform — only tested on Baidu's platform
- Does not compare cost-effectiveness of RL training vs simpler approaches
- Does not discuss latency — does end-to-end RL have slower inference?
- Dependency on quality of reward model — if reward model is wrong → policy is wrong

## Metadata
- Year: 2026
- Authors: Jinfang Wang, Jiajie Liu, Jianwei Wu, Ziqin Luo, Zhen Chen, Chunlei Li, Biao Han, Tao Deng, Yi Li, Shuanglong Li, Lin Liu (Baidu Inc.)
- Category: cs.CL, cs.AI
- PDF: https://arxiv.org/pdf/2602.11780
- Citation count: [EXTRACTION FAILED]
