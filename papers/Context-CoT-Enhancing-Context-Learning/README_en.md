# 2605.25354 Context-CoT: Enhancing Context Learning via High-Quality Reasoning Synthesis

## Problem

Prior work on Chain-of-Thought (CoT) distillation focuses on reasoning tasks but overlooks context learning — the ability to extract, internalize, and apply new knowledge from complex, task-specific contexts. CL-Bench benchmark reveals frontier models like GPT-5.1 solve only 23.7% of context-dependent tasks, open-source models only 13-15%. The reason: teacher models use parametric shortcuts instead of grounding reasoning in context, and answer-conditioned CoT generates post-hoc rationalizations rather than context-derived reasoning.

## Contribution

1. Propose Context-CoT — a 3-stage framework for generating high-quality CoT data for context learning, distinct from prior CoT distillation in enforcing contextual grounding rather than parametric recall.
2. Introduce rubric-based minimum-leakage filtering — hides reference answers and rubrics during CoT generation, provides only minimal failed-rubric feedback when needed, filters out trajectories that leak answers.
3. Student-aware CoT selection — selects CoT paths aligned with the target model's distribution, ensuring the student can actually learn rather than just mimic the teacher.

## Method (core summary)

3-stage pipeline: (1) Multi-stage CoT sampling — guides the model to distill long context into task-relevant intermediate representations before reasoning, generates multiple candidate CoTs from multiple teacher models; (2) Rubric-based minimum-leakage filtering — hides reference answers, provides only minimal failed-rubric feedback, filters trajectories violating context-specific criteria; (3) Student-aware CoT selection — computes step-wise alignment score and reasoning gain score, selects CoTs matching student model distribution. Fine-tuned via SFT with LoRA adapters on ~4K training samples.

## Key Findings

- Qwen3.5-4B: CL-Bench overall score from 9.06% to 12.85% (+3.79 absolute gain, 95% CI [1.68, 5.03])
- McNemar's exact test: b=83, c=143, p=7.95×10⁻⁵ (statistically significant)
- Answer-only SFT: only marginal gains
- Answer-exposed CoT SFT: performance degradation (worse than base model)
- Largest gains in Domain Knowledge Reasoning category
- Llama3.2-3B also improves, proving pipeline is model-agnostic
- Ablation: removing minimum-leakage filtering causes the largest drop
- Training data scaling: performance increases up to ~3K samples, then diminishing returns
- Optimal student-aware alignment weight λ=0.4

## Actionable Insights

1. When creating synthetic training data for LLMs, do NOT expose reference answers to the teacher model during CoT generation — instead use minimal rubric-based feedback. Example: when building internal knowledge base Q&A training data, generate reasoning chains without showing the model the correct answer, only telling it which rubrics fail.
2. Small-scale fine-tuning (4K samples, LoRA) can significantly improve open-source models on context-dependent tasks. Example: enterprises with domain-specific documents (legal, technical manuals) only need ~4K high-quality context-grounded CoT samples to fine-tune a model to understand those documents better.
3. Student-aware selection matters — not every teacher CoT is suitable for the student. Example: when distilling from GPT-4 to a smaller model, filter CoTs by perplexity alignment score to select trajectories the student can actually learn from.

## Assumptions & Limitations

- Assumption: teacher models are strong enough to generate diverse CoT candidates (requires GPT-5.1-class models)
- Assumption: rubric-based LLM judge is accurate enough to filter leakage
- Limitation (paper acknowledges): High construction cost — sampling many CoTs from multiple teachers incurs API costs
- Limitation (paper acknowledges): Offline distillation — no online feedback from student model
- Limitation (paper acknowledges): Dependence on rubric-based judgments — judge errors may affect selection
- Limitation (observed): Paper only tests on CL-Bench, not validated on real-world enterprise tasks. CL-Bench tasks are synthetic, may not transfer to production scenarios.

## Metadata

- Year: 2026
- Authors: Hongbo Jin, Mingnan Zhu, Jingqi Tian, Xu Jiang, Zhongjing Du, Haoran Tang, Siyi Xie, Qiaoman Zhang, Jiayu Ding
- Institution: Peking University, Xiamen University, Tsinghua University
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2605.25354
- Citation count: N/A (published 25/05/2026)
- Classification: [applied]
- Skill: context-cot-data-synthesis
