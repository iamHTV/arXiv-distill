# [2605.28409] Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning

## Problem
Post-training using online RL is an important training step for LLMs, including code-generating models. But online RL for code generation involves LLM inference and verification — takes considerable time and resources. Prior work has not explored offline RL for code generation effectively.

## Contribution
1. **Offline RL for code generation**: Leverages existing code datasets — avoids expensive online RL inference + verification.
2. **Effective for small LLMs**: Especially beneficial for small models and challenging coding problems.
3. **Improves pass@1 and pass@10**: Under strict computational constraints with highly imbalanced dataset.

## Method (core summary)
Offline RL: leverages existing code datasets for training. Applies on-policy online algorithms in an offline setting. Verifiable rewards: functional correctness (code passes tests). Trains models without expensive online inference loops.

## Key Findings
- Improves both pass@1 and pass@10
- Pronounced gains on challenging problems
- Effective under strict computational constraints
- Works with highly imbalanced dataset
- Especially beneficial for small LLMs

## Actionable Insights
1. **Offline RL for code generation**: When training code LLMs, use existing code datasets instead of expensive online RL. Example: when fine-tuning code model, use offline RL with existing code solutions — cheaper, effective.

2. **Small LLMs benefit more**: Offline RL especially helpful for smaller models. Example: when deploying code assistant on edge devices (small model), use offline RL to improve performance without online costs.

3. **Challenging problems benefit most**: Gains most pronounced on hard problems. Example: when training code model for complex algorithms, offline RL provides biggest improvement on difficult tasks.

## Assumptions & Limitations
**Conditions for method to work:**
- Existing code datasets available
- Verifiable rewards (functional correctness)
- Computational constraints acceptable

**Limitations the paper acknowledges:**
- No systematic exploration of learning rates, reward formulations, batch sizes
- Highly imbalanced dataset — simple heuristics only
- Purely offline — no online interaction
- Directly applies on-policy algorithms in offline setting

**Limitations the paper does NOT mention:**
- Code quality beyond correctness (runtime, memory, security)
- Generalization to other domains
- Dataset quality dependency
- Long-term maintenance of offline-trained models

## Metadata
- Year: 2026
- Authors: Mingze Wu, Abhinav Anand, Shweta Verma, Mira Mezini
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.28409
- Citation count: [EXTRACTION FAILED]
