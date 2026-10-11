# Skill: Data-Efficient RL Fine-tuning
Source: 2506.05316
Type: workflow

## Khi nào dùng skill này

- Khi RL fine-tune LLM (GRPO, PPO, RLOO) mà training time/cost quá cao — muốn giảm 40%+ training time mà giữ nguyên performance
- Khi training pool lớn (>5K questions) nhưng không phải mọi câu hỏi đều informative cho model
- Khi muốn implement difficulty-based curriculum learning (học theo giáo trình dựa trên độ khó) mà không cần expensive human annotation

- KHÔNG dùng khi: training pool nhỏ (<1K, không đủ để phân loại difficulty); tasks không có clear correctness signal (creative writing, open-ended); RL algorithm không phải on-policy (DPO offline)

## Input cần có

- RL training dataset (5K+ questions với verifiable answers)
- Base LLM for GRPO training (Qwen2.5-Math series recommended)
- Small reference model for difficulty estimation (Qwen2.5-Math-1.5B-Instruct)
- Rule-based reward function (answer correctness)
- GPU cluster for GRPO training

## Các bước thực hiện

1. **Setup Reference Set** — Random sample 256 questions từ training pool. Run model (untrained hoặc lightly trained) trên reference set, 8 rollouts/question. Compute per-question accuracy = % rollouts with correct answer. Store (question_embedding, accuracy) pairs.

2. **Train Difficulty Predictor** — Freeze reference model backbone. Train 3-layer MLP adapter + calibration head (binary cross-entropy) trên reference set. Input: question embedding. Output: predicted accuracy. Evaluate on held-out set — target: correlation >0.7 với actual accuracy.

3. **Online Difficulty-Targeted Sampling** — Mỗi training step: (a) Compute adaptive difficulty = 1 - predicted_accuracy cho all questions in pool; (b) Sample batch proportional to difficulty — focus on moderate range (20-80% accuracy); (c) Run GRPO on selected batch.

4. **Rollout Replay** — (a) Maintain replay buffer (size = batch_size × 2); (b) After each step, add fresh rollouts to buffer; (c) Next step: with probability p=0.5, replace fresh rollouts with buffer samples; (d) Buffer FIFO — oldest rollouts evicted first.

5. **Monitor and Tune** — Track: (a) Average difficulty of selected batch over time (should stay in moderate range); (b) Training loss stability (replay shouldn't increase variance); (c) Wall-clock time to match baseline performance.

## Output mong đợi

- 23-62% training time reduction to match original GRPO performance
- Average 40.7% time savings across model-dataset combinations
- Consistent outperformance of original GRPO at each wall-clock training point

## Ví dụ áp dụng

Scenario: Fine-tune Qwen2.5-Math-7B trên 10K math problems với GRPO. (1) Original: 60 training steps × 8 rollouts/prompt = 480K rollouts, ~48 GPU-hours; (2) With DOTS+RR: sample 256 reference → train difficulty predictor (10 min) → online sampling moderate-difficulty questions + replay buffer → match same accuracy in ~28 GPU-hours (42% savings); (3) Total savings: ~20 GPU-hours per training run.

## Gotchas

- Reference set size 256 là minimum — nếu training pool rất diverse (10+ domains), increase to 512-1024
- Replay buffer ratio p=0.5 là starting point — too high → stale data bias, too low → minimal savings. Tune between 0.3-0.7.
- MLP adapter backbone specificity — nếu change base model architecture, retrain adapter trên new reference set
- Moderate difficulty range definition — 20-80% accuracy là heuristic, optimal range task-dependent
- Rule-based reward requirement — nếu dùng learned reward model, difficulty estimation becomes circular
