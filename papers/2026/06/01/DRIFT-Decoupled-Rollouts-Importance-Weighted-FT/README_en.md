# [2605.31455v1] DRIFT: Decoupled Rollouts and Importance-Weighted Fine-Tuning for Efficient Multi-Turn Optimization

## Problem
LLMs are increasingly deployed in multi-turn interactive settings where users or environments provide lightweight feedback. Optimizing such behavior presents a dilemma: online RL effectively addresses multi-turn dynamics but is prohibitively expensive due to generating full correction trajectories at every update. Offline SFT is efficient but suffers from distribution shift and behavioral collapse.

## Contribution
1. **DRIFT framework**: Decouples rollout from optimization. Samples offline interaction trajectories from fixed reference policy, derives return-based importance weights, optimizes via weighted SFT.
2. **Theoretical insight**: KL-regularized RL objective is equivalent to importance-weighted supervised learning — DRIFT operationalizes this insight.
3. **Empirical results**: Matches or exceeds multi-turn RL baselines while maintaining SFT efficiency.

## Method (core summary)
DRIFT: (1) Sample multi-turn correction trajectories once from frozen reference policy — no repeated rollouts needed; (2) Assign each trajectory exponential weight derived from KL-regularized multi-turn objective; (3) Train target model using importance-weighted SFT. Key: decouples trajectory generation (offline, once) from optimization (online, efficient). Avoids repeated rollouts during training while optimizing accuracy and efficiency across turns.

## Key Findings
- Qwen2.5-3B-Instruct: DRIFT matches or surpasses RL baselines on most benchmarks
- Qwen2.5-7B-Instruct: DRIFT improves all-benchmark average from 64.8% → 68.3%
- Training efficiency: DRIFT comparable to SFT-based methods, much faster than RL
- Multi-turn correction rate: DRIFT achieves higher correction rate in early turns
- Single-turn training: improves turn 1 accuracy but little gain on later turns
- Multi-turn training: learns correction under negative feedback, substantial improvements beyond math

## Actionable Insights
1. **Decouple rollout from optimization**: When training multi-turn AI agents, don't need repeated online rollouts. Sample trajectories once from reference policy, optimize offline. Example: when training customer service AI, generate correction trajectories once, then fine-tune offline — saves compute.

2. **Importance weighting for offline training**: Use return-based weights to upweight useful behaviors in collected trajectories. Example: when training AI advisor, weight successful correction trajectories higher than failed ones — model learns from successes.

3. **Multi-turn training > single-turn**: Single-turn only improves turn 1. Multi-turn training learns to correct under negative feedback. Example: when training AI coding assistant, train with multi-turn corrections (try → fail → fix → succeed), not just single-shot solutions.

## Assumptions & Limitations
**Conditions for method to work:**
- Short-horizon, verifier-guided correction with lightweight deterministic feedback
- Verifier provides unambiguous correctness signal
- Small number of correction attempts per episode

**Limitations the paper acknowledges:**
- Intended for short-horizon correction — not suitable for stochastic/preference-based feedback
- Offline rollout coverage limitation — only upweights behaviors in collected trajectories
- May miss strategies online RL could discover through exploration

**Limitations the paper does NOT mention:**
- Tested primarily on math reasoning — generalizability unclear
- 3B-8B models only — larger models untested
- Assumes verifier availability — real-world verification harder
- Fixed reference policy quality limits upper bound
- No quantitative cost savings comparison

## Metadata
- Year: 2026
- Authors: Jian Mu, Tianyi Lin, Chengwei Qin, Zhongxiang Dai, Yao Shu
- Category: cs.LG, cs.CL
- PDF: https://arxiv.org/pdf/2605.31455v1
- Citation count: [EXTRACTION FAILED]
