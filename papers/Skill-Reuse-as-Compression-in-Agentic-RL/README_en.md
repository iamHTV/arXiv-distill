# [2605.31509v1] Skill Reuse as Compression in Agentic RL

## Problem
Prior work fails to address generalization of LLM agents trained with RL because agents learn task-specific shortcuts rather than reusable skills. Prior work like SkillRL and ERL accumulate self-generated trajectories but do not enforce shared compositional patterns across trajectories, leading to reasoning collapse.

## Contribution
1. **ReuseRL**: Framework grounding agentic RL in the Minimum Description Length (MDL) principle — compresses successful trajectories into a shared skill dictionary and penalizes idiosyncratic behaviors
2. **PAC-Bayes generalization bound**: Formally proves that if a dictionary tightly compresses an observed successful batch, the expected description length on future trajectories is bounded
3. **Unifying interpretation**: Proves SkillRL and ERL are implicit partial MDL minimizers — ReuseRL explicitly minimizes the full MDL objective

## Method (core summary)
3-step pipeline: (1) Extract atomic skills from successful trajectories via rule-based mapping over action verbs; (2) Greedy BPE-style merging — repeatedly merge highest-frequency phrase pairs in the successful cluster, accept only if batch MDL objective decreases; (3) Augment GRPO reward with segmentation cost = seg(s, 𝒞)/T — penalize trajectories using many non-reusable phrases. Global success buffer (FIFO) stabilizes the EM process.

## Key Findings
- ALFWorld IID: ReuseRL achieves 97.14% vs vanilla GRPO 84.29% (+12.85%), vs pure round-length 96.43% (+0.71%)
- ALFWorld OOD: 93.28% vs 79.85% (+13.43%), vs 91.79% (+1.49%)
- TW-Cooking Pass@1: 81.73% vs 74.97% (+6.76%)
- Countdown-Stepwise Pass@1: 80.37% vs 68.46% (+11.91%)
- Case study ALFWorld: GRPO has 40.4% repeat actions, ReuseRL only 14.4%; invalid actions: 23.5% → 1.8%
- Case study TW-Cooking: pure round-length has 74% burned failures, ReuseRL only 3.3%
- Largest gains on OOD split — structural compression drives reasoning generalization

## Actionable Insights
1. **Compress successful behaviors into reusable patterns**: When training AI agents, don't just optimize for task completion but compress successful behaviors into reusable patterns. Example: when training a chatbot for customer complaints, extract common response patterns (identify issue → empathize → offer solution → follow up) and reward responses that follow these patterns, rather than making each response unique.

2. **Penalize idiosyncratic behaviors, reward composable ones**: Instead of only rewarding short trajectories, reward trajectories that use a shared skill vocabulary. Example: sales team — don't reward fast deal closes, reward process reuse: qualify lead → demo → handle objection → close — shared patterns across deals.

3. **Global success buffer stabilizes learning**: Store successful trajectories in a global buffer to stabilize learning. Example: company knowledge base — learn not just from current batch but retain best practices from the past to guide future training.

## Assumptions & Limitations
**Conditions for the method to work:**
- Successful trajectories must admit shared reusable decomposition with bounded dictionary complexity (Assumption 2)
- Requires rule-based skill projection φ — manual schema design for each new domain
- Greedy BPE is an approximation for NP-hard optimal dictionary search — gap grows with vocabulary size

**Limitations the paper acknowledges:**
- Skill projection φ is rule-based per-environment mapping — needs manual schema design for new domains
- Greedy BPE approximation gap grows with |Σ| (alphabet size)
- Assumption 2 can fail in unstructured reasoning domains
- Only tested on text-based benchmarks with 1.5-1.7B parameter models

**Limitations the paper does NOT mention:**
- No comparison with experience replay methods in a fair setting
- Rule-based φ is limiting — no exploration of learned skill extraction
- No discussion of compute cost of BPE merging overhead
- 1.5-1.7B models too small for real-world agent deployment

## Metadata
- Year: 2026
- Authors: Zhikun Xu, Yu Feng, Jacob Dineen, Taiwei Shi, Jieyu Zhao, Ben Zhou
- Category: cs.LG, cs.AI
- PDF: https://arxiv.org/pdf/2605.31509v1
- Citation count: [EXTRACTION FAILED]
