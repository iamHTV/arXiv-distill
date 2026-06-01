# [2509.23040] ReMemR1: Look Back to Reason Forward — Revisitable Memory for Long-Context LLM Agents

## Problem
LLMs face challenges in long-context QA — key evidence dispersed across millions of tokens. Existing "memorize while reading" methods: linear document scan, memory buffer dynamically updated. But suffers from: pruning of latent evidence, information loss through overwriting, sparse RL signals.

## Contribution
1. **ReMemR1**: Integrates memory retrieval into memory update process — enables selective callback of historical memories for non-linear reasoning.
2. **History-Augmented State**: State = (current memory, callback query) — agent searches over entire memory history, not just current memory.
3. **Multi-level Reward Design**: Trajectory-level outcome rewards + dense step-level state rewards for effective memory use.

## Method (core summary)
ReMemR1: (1) Agent maintains current memory m_t + generates callback query q_t; (2) Searches over entire memory history {m_i}_{i≤t} using word overlap retrieval; (3) State = (m_t, q_t) — non-linear reasoning paths; (4) Multi-level reward: trajectory-level (final answer correctness) + step-level (relative information gain at each step); (5) GRPO optimization with normalized rewards.

## Key Findings
- Significantly outperforms SOTA baselines on long-context QA
- Negligible computational overhead
- Non-linear reasoning paths enabled
- Information degradation mitigated
- Dense step-level rewards improve supervision

## Actionable Insights
1. **Look back to reason forward**: When building long-context agents, enable memory callback — agent can revisit past memories. Example: when AI assistant processes long document, allow it to search back through previous sections when encountering new evidence.

2. **Multi-level rewards**: Don't just reward final answer. Add dense step-level rewards for intermediate memory use. Example: when training reasoning agent, reward both final correctness AND quality of memory retrieval at each step.

3. **Non-linear reasoning**: Agent shouldn't be confined to forward-only processing. Enable backtracking through memory. Example: when building document QA system, allow agent to jump back to earlier sections when new context triggers relevant recall.

## Assumptions & Limitations
**Conditions for method to work:**
- Long-context documents with dispersed evidence
- Memory retrieval mechanism available
- GRPO training infrastructure

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED]

**Limitations the paper does NOT mention:**
- Memory history size limits
- Retrieval accuracy dependency
- Training cost for RL
- Very long documents (millions of tokens) scalability

## Metadata
- Year: 2025
- Authors: Yaorui Shi, Yuxin Chen, Siyuan Wang, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2509.23040
- Citation count: [EXTRACTION FAILED]
