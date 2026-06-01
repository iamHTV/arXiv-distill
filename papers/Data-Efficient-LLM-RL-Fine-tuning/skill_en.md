# Skill: Data-Efficient RL Fine-tuning
Source: 2506.05316
Type: workflow

## When to use this skill

- When RL fine-tuning LLMs (GRPO, PPO, RLOO) with excessive training time/cost — want 40%+ time reduction while matching performance
- When training pool is large (>5K questions) but not all questions are informative
- When wanting difficulty-based curriculum learning without expensive human annotation

- Do NOT use when: training pool small (<1K); tasks lack clear correctness signal; RL algorithm is off-policy (DPO offline)

## Input needed

- RL training dataset (5K+ questions with verifiable answers)
- Base LLM for GRPO training
- Small reference model for difficulty estimation
- Rule-based reward function (answer correctness)
- GPU cluster for GRPO training

## Steps

1. **Setup Reference Set** — Random sample 256 questions from pool. Run model on reference set, 8 rollouts/question. Compute per-question accuracy = % correct rollouts. Store (question_embedding, accuracy) pairs.

2. **Train Difficulty Predictor** — Freeze reference model backbone. Train 3-layer MLP adapter + calibration head (BCE) on reference set. Input: question embedding. Output: predicted accuracy. Target correlation >0.7.

3. **Online Difficulty-Targeted Sampling** — Each step: (a) Compute adaptive difficulty = 1 - predicted_accuracy; (b) Sample batch proportional to difficulty — focus on 20-80% accuracy range; (c) Run GRPO on selected batch.

4. **Rollout Replay** — (a) Maintain replay buffer (size = batch_size × 2); (b) Add fresh rollouts after each step; (c) Next step: with p=0.5, replace fresh rollouts with buffer samples; (d) FIFO eviction.

5. **Monitor and Tune** — Track: average selected difficulty, training loss stability, wall-clock time to baseline performance.

## Expected output

- 23-62% training time reduction to match GRPO performance
- Average 40.7% time savings
- Consistent outperformance at each wall-clock point

## Example application

Scenario: Fine-tune Qwen2.5-Math-7B on 10K math problems with GRPO. Original: 60 steps × 8 rollouts = 480K rollouts, ~48 GPU-hours. With DOTS+RR: 256 reference → difficulty predictor (10 min) → online sampling + replay → match accuracy in ~28 GPU-hours (42% savings).

## Gotchas

- Reference set 256 is minimum — for diverse pools (10+ domains), increase to 512-1024
- Replay ratio p=0.5 is starting point — too high → stale bias, too low → minimal savings. Tune 0.3-0.7.
- MLP adapter is backbone-specific — retrain if changing base model
- Moderate difficulty 20-80% is heuristic — optimal range is task-dependent
- Rule-based reward required — learned reward model creates circular difficulty estimation
