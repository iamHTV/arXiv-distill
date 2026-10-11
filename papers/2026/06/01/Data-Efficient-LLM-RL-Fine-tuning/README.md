# 2506.05316 Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-Targeted Selection and Rollout Replay

## Problem

RL (Reinforcement Learning — học tăng cường) fine-tuning đã trở thành effective approach cho LLM reasoning enhancement (cải thiện khả năng suy luận), nhưng remains highly resource-intensive (tốn nhiều tài nguyên). Existing work largely overlook data efficiency (hiệu quả dữ liệu) — toàn bộ training data được treat equally, không ưu tiên samples nào tạo ra informative learning signals (tín hiệu học tập có giá trị). Rollout cost (chi phí tạo mẫu) chiếm phần lớn thời gian training, và mọi rollout bị discard sau mỗi step (bước).

## Contribution

1. Propose DOTS (Difficulty-Targeted Online Data Selection) — prioritize questions có moderate difficulty (độ khó trung bình) vì chúng tạo informative learning signals. Too easy → model already knows; too hard → noisy gradients. Adaptive difficulty (độ khó thích ứng) estimated via attention-based framework chỉ cần rollouts cho 256 reference questions, sau đó estimate difficulty cho remaining questions bằng similarity.
2. Propose RR (Rollout Replay) — reuse recent rollouts thay vì regenerate mỗi step, inspired by experience replay trong traditional RL. Reduces per-step computation while maintaining stable updates.
3. Demonstrate: 23-62% training time reduction across 6 LLM-dataset combinations while matching original GRPO performance.

## Method (tóm tắt cốt lõi)

DOTS: (1) Maintain reference set 256 questions, run rollouts để compute per-question accuracy; (2) Freeze Qwen2.5-Math-1.5B-Instruct backbone, train 3-layer MLP adapter + calibration head (binary cross-entropy) để predict difficulty cho new questions based on embedding similarity to reference set; (3) Adaptive difficulty = 1 - model_accuracy (questions model struggles with = moderate difficulty for training); (4) Sample training batch proportional to adaptive difficulty — focus on moderate difficulty range. RR: (5) Maintain replay buffer of recent rollouts; (6) With probability p, replace fresh rollout with replayed one from buffer; (7) Buffer updated each training step.

## Key Findings

- 6 combinations tested: Qwen2.5-Math-1.5B, Qwen2.5-3B, Qwen2.5-Math-7B × MATH, DeepScaleR-40K, ORZ, DeepMath-103K
- Average 40.7% time reduction to match original GRPO's final accuracy (60 steps)
- Range: 23% to 62% time reduction across combinations
- DOTS+RR consistently outperforms original GRPO throughout training (not just faster, but better at each wall-clock point)
- Reference set size 256 sufficient for accurate difficulty estimation
- 8 rollouts per prompt, batch size 512, mini-batch 64
- Simple rule-based reward (answer correctness only) — no format signals
- Works across model scales (1.5B, 3B, 7B)

## Actionable Insights

1. Khi RL fine-tune LLM, KHÔNG treat all training data equally — prioritize moderate-difficulty questions. Ví dụ: training math reasoning model, filter out questions model already solve >95% (too easy) và <5% (too hard), focus training budget vào 20-80% difficulty range. Giảm 40% training time mà giữ nguyên performance.
2. Implement rollout replay buffer — reuse recent rollouts thay vì regenerate mỗi step. Ví dụ: GRPO training với 8 rollouts/prompt, replay buffer giữ 50% rollouts từ previous step → giảm 30-50% inference cost per step.
3. Difficulty estimation không cần expensive: chỉ 256 reference questions với rollouts, train lightweight MLP adapter → predict difficulty cho thousands of remaining questions. Ví dụ: 10K training pool, chỉ cần 256 × 8 rollouts = 2,048 rollouts cho calibration, rest estimated via embedding similarity.

## Assumptions & Limitations

- Giả sử: moderate-difficulty questions luôn informative — có thể domain-specific tasks có optimal difficulty distribution khác
- Limitation: Reference set 256 fixed — có thể không representative cho diverse training pools
- Limitation: MLP adapter trained on Qwen2.5-Math backbone — may not transfer to other architectures
- Limitation: Only tested on math reasoning tasks — chưa test code generation, general reasoning
- Limitation (tự thấy): Replay buffer introduces off-policy bias — paper claims "stable updates" nhưng không analyze variance increase. Traditional RL experience replay cần careful tuning of buffer size và replay ratio.

## Metadata

- Năm: 2026
- Tác giả: Yifan Sun, Jingyan Shen, Yibin Wang, Tianyu Chen, Zhendong Wang, Mingyuan Zhou, Huan Zhang
- Category: cs.LG, cs.AI
- Link PDF: https://arxiv.org/pdf/2506.05316
- Citation count: N/A
- Nhãn: [applied]
- Skill: data-efficient-rl-finetuning
