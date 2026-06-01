# 2506.05316 Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-Targeted Selection and Rollout Replay

## Problem

RL fine-tuning has become effective for LLM reasoning enhancement but remains highly resource-intensive. Existing work largely overlooks data efficiency — all training data treated equally, not prioritizing samples that produce informative learning signals. Rollout costs dominate training time, and every rollout is discarded after each step.

## Contribution

1. Propose DOTS (Difficulty-Targeted Online Data Selection) — prioritize moderate-difficulty questions that produce informative learning signals. Too easy → model already knows; too hard → noisy gradients. Adaptive difficulty estimated via attention-based framework needing rollouts for only 256 reference questions.
2. Propose RR (Rollout Replay) — reuse recent rollouts instead of regenerating each step, inspired by experience replay in traditional RL. Reduces per-step computation while maintaining stable updates.
3. Demonstrate: 23-62% training time reduction across 6 LLM-dataset combinations while matching original GRPO performance.

## Method (core summary)

DOTS: (1) Maintain 256-question reference set, run rollouts to compute per-question accuracy; (2) Freeze Qwen2.5-Math-1.5B-Instruct backbone, train 3-layer MLP adapter + calibration head (BCE loss) to predict difficulty via embedding similarity; (3) Adaptive difficulty = 1 - model_accuracy; (4) Sample training batch proportional to adaptive difficulty — focus on moderate difficulty range. RR: (5) Maintain replay buffer of recent rollouts; (6) With probability p, replace fresh rollout with replayed one; (7) Buffer updated each step.

## Key Findings

- 6 combinations: Qwen2.5-Math-1.5B/3B/7B × MATH/DeepScaleR/ORZ/DeepMath
- Average 40.7% time reduction to match GRPO's final accuracy
- Range: 23% to 62% time reduction
- DOTS+RR consistently outperforms original GRPO at each wall-clock point
- Reference set size 256 sufficient
- Works across model scales (1.5B, 3B, 7B)
- Simple rule-based reward (correctness only)

## Actionable Insights

1. When RL fine-tuning LLMs, DON'T treat all training data equally — prioritize moderate-difficulty questions. Example: filter out >95% solvable (too easy) and <5% (too hard), focus on 20-80% difficulty range. 40% training time reduction.
2. Implement rollout replay buffer — reuse recent rollouts. Example: GRPO with 8 rollouts/prompt, replay buffer holds 50% from previous step → 30-50% inference cost reduction.
3. Difficulty estimation is cheap: only 256 reference questions × 8 rollouts = 2,048 rollouts for calibration, rest estimated via embedding similarity.

## Assumptions & Limitations

- Assumption: moderate-difficulty questions are always informative — may vary by domain
- Limitation: Reference set 256 fixed — may not represent diverse pools
- Limitation: MLP adapter on Qwen2.5-Math backbone — may not transfer architectures
- Limitation: Only math reasoning tasks tested
- Limitation (observed): Replay buffer introduces off-policy bias — variance increase not analyzed

## Metadata

- Year: 2026
- Authors: Yifan Sun, Jingyan Shen, Yibin Wang, Tianyu Chen, Zhendong Wang, Mingyuan Zhou, Huan Zhang
- Category: cs.LG, cs.AI
- PDF: https://arxiv.org/pdf/2506.05316
- Citation count: N/A
- Classification: [applied]
- Skill: data-efficient-rl-finetuning
