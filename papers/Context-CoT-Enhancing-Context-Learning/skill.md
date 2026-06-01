# Skill: Context-CoT Data Synthesis
Source: 2605.25354
Type: framework

## Khi nào dùng skill này

- Khi cần fine-tune open-source LLM để hiểu domain-specific documents (legal, technical, medical) tốt hơn — model cần "học từ ngữ cảnh" thay vì dựa vào pre-trained knowledge
- Khi tạo synthetic training data mà muốn tránh answer leakage (rò rỉ đáp án) và post-hoc rationalization (hợp lý hóa hậu nghiệm)
- Khi muốn distill reasoning capability từ large teacher model xuống smaller student model mà vẫn giữ được contextual grounding

- KHÔNG dùng khi: chỉ cần few-shot prompting cho general tasks (không cần fine-tune); khi không có access to multiple strong teacher models; khi budget API không cho phép sampling nhiều CoT candidates

## Input cần có

- Domain-specific documents hoặc knowledge base cần model học
- Access to ít nhất 1 strong teacher model (GPT-4-class trở lên) để generate CoT candidates
- Target student model để fine-tune (ví dụ: Qwen3.5-4B, Llama3.2-3B)
- Evaluation rubrics (tiêu chí đánh giá) cho từng context-learning task
- Budget cho API calls (pipeline cần sample nhiều candidates)

## Các bước thực hiện

1. **Tạo Context-Task Instances** — Tạo dataset context-learning tasks từ domain documents. Mỗi instance gồm: long context document, context-dependent question, reference answer, fine-grained evaluation rubrics. Phủ 4 categories: Domain Knowledge Reasoning, Rule System Application, Procedural Task Execution, Empirical Discovery & Simulation.

2. **Multi-Stage CoT Sampling** — Với mỗi (context, question) pair, guide teacher model qua 2 stages: (a) Stage 1: extract task-relevant intermediate representations từ context — model phải distill long context thành key evidence trước khi reasoning; (b) Stage 2: generate full CoT reasoning over extracted evidence. Sample k=5-8 diverse CoT candidates per instance.

3. **Rubric-Based Minimum-Leakage Filtering** — (a) Ẩn reference answers và full rubrics khi judge CoT quality; (b) Chỉ provide minimal failed-rubric feedback khi CoT vi phạm; (c) Re-generate CoT với feedback minimal; (d) Filter out bất kỳ trajectory nào leak answer hoặc vi phạm context-specific criteria. Áp dụng structural filter để remove malformed trajectories (abnormal length).

4. **Student-Aware CoT Selection** — Với mỗi filtered CoT candidate, tính: (a) Step-wise alignment score S_step — measure perplexity distribution across reasoning steps, ensure difficulty smoothly distributed; (b) Reasoning gain score — measure improvement over base model; (c) Combined score với weight λ=0.4 (tối ưu từ ablation). Chọn top-1 CoT per instance.

5. **Fine-Tune Student Model** — Fine-tune target student model bằng SFT với LoRA adapters trên ~4K selected CoT samples. LoRA apply lên attention projection layers (q_proj, k_proj, v_proj, o_proj) và MLP projection layers.

6. **Evaluate trên CL-Bench** — Test trên CL-Bench benchmark (1,899 tasks, 4 categories). Task counted correct only if ALL rubrics satisfied. Run statistical tests (paired bootstrap resampling, McNemar's exact test) để validate improvement significance.

## Output mong đợi

- Fine-tuned student model có context-learning capability cải thiện (target: +3-4 absolute points trên CL-Bench)
- Synthetic training dataset ~4K high-quality context-grounded CoT samples
- Significant reduction trong context-neglect errors (model ít dùng parametric recall hơn)

## Ví dụ áp dụng

Scenario: Công ty luật muốn fine-tune LLM để hiểu legal contracts. Thay vì chỉ RAG, tạo Context-CoT dataset: (1) Extract clauses từ 100 contracts, tạo context-dependent questions về obligations, penalties, conditions; (2) GPT-5 generate CoT reasoning về mỗi clause mà KHÔNG thấy reference answer; (3) Filter CoT nào leak answer hoặc reasoning sai; (4) Select CoT align với target model (Qwen3.5-4B); (5) Fine-tune với 4K samples. Result: model hiểu contracts tốt hơn, không hallucinate khi gặp clause mới.

## Gotchas

- API cost cao: cần sample nhiều CoT candidates từ multiple teachers, mỗi instance cần 5-8 candidates + re-generation khi filter
- Rubric quality quyết định hết: rubrics không đủ fine-grained → filtering không hiệu quả → garbage in, garbage out
- λ=0.4 là optimal trên CL-Bench nhưng có thể khác trên domain-specific tasks — cần ablation study riêng
- Offline limitation: model không tự improve qua interaction, cần periodic re-training với new data
- Teacher model phải đủ mạnh: nếu teacher chỉ ngang student, CoT quality không đủ để distill
