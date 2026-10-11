# Skill: Context-CoT Data Synthesis
Source: 2605.25354
Type: framework

## When to use this skill

- When fine-tuning an open-source LLM to better understand domain-specific documents (legal, technical, medical) — the model needs to "learn from context" rather than rely on pre-trained knowledge
- When creating synthetic training data and wanting to avoid answer leakage and post-hoc rationalization
- When distilling reasoning capability from a large teacher model to a smaller student model while maintaining contextual grounding

- Do NOT use when: only need few-shot prompting for general tasks (no fine-tune needed); no access to multiple strong teacher models; API budget doesn't allow sampling many CoT candidates

## Input needed

- Domain-specific documents or knowledge base for the model to learn
- Access to at least 1 strong teacher model (GPT-4-class or above) for generating CoT candidates
- Target student model to fine-tune (e.g., Qwen3.5-4B, Llama3.2-3B)
- Evaluation rubrics for each context-learning task
- Budget for API calls (pipeline needs to sample many candidates)

## Steps

1. **Create Context-Task Instances** — Create a dataset of context-learning tasks from domain documents. Each instance: long context document, context-dependent question, reference answer, fine-grained evaluation rubrics. Cover 4 categories: Domain Knowledge Reasoning, Rule System Application, Procedural Task Execution, Empirical Discovery & Simulation.

2. **Multi-Stage CoT Sampling** — For each (context, question) pair, guide the teacher model through 2 stages: (a) Stage 1: extract task-relevant intermediate representations from context — model must distill long context into key evidence before reasoning; (b) Stage 2: generate full CoT reasoning over extracted evidence. Sample k=5-8 diverse CoT candidates per instance.

3. **Rubric-Based Minimum-Leakage Filtering** — (a) Hide reference answers and full rubrics when judging CoT quality; (b) Provide only minimal failed-rubric feedback when CoT violates criteria; (c) Re-generate CoT with minimal feedback; (d) Filter out any trajectory that leaks answers or violates context-specific criteria. Apply structural filter to remove malformed trajectories (abnormal length).

4. **Student-Aware CoT Selection** — For each filtered CoT candidate, compute: (a) Step-wise alignment score S_step — measures perplexity distribution across reasoning steps, ensures difficulty is smoothly distributed; (b) Reasoning gain score — measures improvement over base model; (c) Combined score with weight λ=0.4 (optimal from ablation). Select top-1 CoT per instance.

5. **Fine-Tune Student Model** — Fine-tune target student model via SFT with LoRA adapters on ~4K selected CoT samples. Apply LoRA to attention projection layers (q_proj, k_proj, v_proj, o_proj) and MLP projection layers.

6. **Evaluate on CL-Bench** — Test on CL-Bench benchmark (1,899 tasks, 4 categories). Task counted correct only if ALL rubrics satisfied. Run statistical tests (paired bootstrap resampling, McNemar's exact test) to validate improvement significance.

## Expected output

- Fine-tuned student model with improved context-learning capability (target: +3-4 absolute points on CL-Bench)
- Synthetic training dataset of ~4K high-quality context-grounded CoT samples
- Significant reduction in context-neglect errors (model uses less parametric recall)

## Example application

Scenario: A law firm wants to fine-tune an LLM to understand legal contracts. Instead of just RAG, create a Context-CoT dataset: (1) Extract clauses from 100 contracts, create context-dependent questions about obligations, penalties, conditions; (2) GPT-5 generates CoT reasoning about each clause WITHOUT seeing the reference answer; (3) Filter CoTs that leak answers or have incorrect reasoning; (4) Select CoTs aligned with the target model (Qwen3.5-4B); (5) Fine-tune with 4K samples. Result: model understands contracts better, doesn't hallucinate when encountering new clauses.

## Gotchas

- High API cost: need to sample many CoT candidates from multiple teachers, each instance needs 5-8 candidates + re-generation on filter
- Rubric quality determines everything: rubrics not fine-grained enough → filtering ineffective → garbage in, garbage out
- λ=0.4 is optimal on CL-Bench but may differ for domain-specific tasks — need separate ablation study
- Offline limitation: model doesn't self-improve through interaction, needs periodic re-training with new data
- Teacher model must be strong enough: if teacher is only at student level, CoT quality insufficient for distillation
