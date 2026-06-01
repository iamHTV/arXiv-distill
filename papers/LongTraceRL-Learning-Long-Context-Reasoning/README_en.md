# [2605.31584v1] LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards

## Problem
Prior work fails to solve long-context reasoning for two reasons: (1) training data uses random distractors that are too easy to filter, so models learn trivial noise-filtering rather than deep reasoning; (2) reward signals are outcome-only (correct/wrong at the end), providing no supervision over intermediate reasoning steps — models can guess correctly by luck without truly understanding the reasoning chain.

## Contribution
1. **Tiered distractors from search agent trajectories**: Instead of random distractors, uses real search agent behavior — documents the agent read but did not cite (Tier-1, high confusability) and documents that appeared in results but were never opened (Tier-2, low confusability). These distractors are 50% harder than random ones.
2. **Rubric reward — entity-level process supervision**: Uses gold entities in the reasoning chain as reward signal, not just outcome. Reward is only applied to correct answers (positive-only strategy) to prevent reward hacking.
3. **Consistent gains across scales**: Tested on 3 models (4B-30B), 5 benchmarks, always improves.

## Method (core summary)
4-step pipeline: (1) Random walk on Wikipedia knowledge graph to generate multi-hop questions with 8 reasoning steps; (2) Deploy search agent, record full trajectory (search → open → cite); (3) Split documents into Tier-1 (agent read but did not cite) and Tier-2 (appeared in results but not opened) as distractors; (4) Assemble 128K token context, shuffle. RL training uses GRPO with composite reward: r = (1-α)·r_outcome + α·r_rubric, where r_rubric = recall of gold entities in response. Positive-only: reward > 0 only when outcome is correct.

## Key Findings
- Qwen3-4B achieves average 59.0 across 5 benchmarks, +5.7 improvement over base model, +2.5 over strongest baseline (LongRLVR)
- AA-LCR benchmark: 33.2 → 41.8 (+8.6 points)
- DeepSeek-R1-8B: 42.7 → 43.8
- Qwen3-30B: 60.5 → 63.7 (+3.2)
- Ablation: removing rubric reward → average drops from 59.0 to 53.7 (rubric reward is the main driver)
- Distractor difficulty ranking: random (1.35% entity overlap) < search (15.0%) < traj-random (42.16%) < traj-tiered (50.03%)
- α=0.3 is optimal; α=0.5 too high → model learns entity enumeration shortcut
- Training: 2,815 examples, 32×H800 GPUs, 200 iterations

## Actionable Insights
1. **Use agent behavior as training signal**: When building RL training data for LLMs, instead of random noise, use real agent behavior (documents read, documents skipped) as distractors. Example: when training a chatbot for complex questions, use retrieval system logs — documents users clicked but didn't use — as hard negative examples.

2. **Process reward over outcome reward**: Only rewarding final correct/wrong outcomes is insufficient. Intermediate steps need supervision. Example: when evaluating AI-written reports, don't just check the final result but also check each reasoning step — whether correct sources were cited, whether important information was missed.

3. **Positive-only reward prevents hacking**: When using process reward, only apply it to correct responses. If applied to all, the model will learn to enumerate entities without genuine reasoning. Example: employee KPIs — only reward good process when outcomes are correct, otherwise employees optimize procedures without caring about results.

## Assumptions & Limitations
**Conditions for the method to work:**
- Needs a knowledge graph with multi-hop paths (here: Wikipedia)
- Needs a capable search agent to generate meaningful trajectories
- Needs sufficient compute (32×H800 GPUs for 2,815 examples)

**Limitations the paper acknowledges:**
- Only uses KILT Wikipedia snapshot → reasoning patterns may lack diversity
- Distractor quality depends on search agent capability — weaker agent → lower quality distractors

**Limitations the paper does NOT mention:**
- Not tested on non-English languages — transferability unclear
- 8-hop questions may be too artificial, not reflecting real-world queries
- 128K token context still lower than many real-world scenarios (1M+ tokens)
- No cost-effectiveness comparison — 32×H800 GPUs practical for most teams?

## Metadata
- Year: 2026
- Authors: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li (Tsinghua University)
- Category: cs.CL, cs.AI, cs.LG
- PDF: https://arxiv.org/pdf/2605.31584v1
- GitHub: https://github.com/THU-KEG/LongTraceRL
- Citation count: [EXTRACTION FAILED]
