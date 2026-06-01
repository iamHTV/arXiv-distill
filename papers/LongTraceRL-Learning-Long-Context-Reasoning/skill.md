# Skill: Rubric Reward cho Long-Context RL Training
Nguồn: 2605.31584v1
Loại: framework

## Khi nào dùng skill này
- Khi train LLM reasoning trên long-context (10K+ tokens) với nhiều distractor
- Khi cần fine-grained process supervision, không chỉ outcome reward
- Khi build RL training data cho multi-hop question answering

## KHÔNG nên dùng khi
- Task đơn giản, short-context (< 4K tokens)
- Không có knowledge graph hoặc structured data nguồn
- Không đủ compute budget (< 8 GPUs)

## Input cần có
- Knowledge graph hoặc structured data source (Wikipedia, internal KB)
- Search agent hoặc retrieval system có logging capability
- Base reasoning LLM (4B+ parameters)
- Target context length (đề xuất 128K tokens)
- Multi-hop questions hoặc ability to generate them

## Các bước thực hiện

### Bước 1 — Tạo Multi-Hop Questions
1. Build knowledge graph từ data source (dùng hyperlinks, entity relations)
2. Random walk trên graph, 8 bước, mỗi bước LLM chọn entity tiếp theo relevant nhất
3. Prompt powerful LLM (GPT-4+) tạo câu hỏi yêu cầu reasoning qua tất cả entities
4. Constraint: phải paraphrase identifying info, answer phải unique
5. Output: question + answer + list gold entities {e1, e2, ..., ek}

### Bước 2 — Collect Search Agent Trajectories
1. Deploy search agent (search → open → cite capabilities)
2. Sample K=5 trajectories per question
3. Filter: chỉ giữ trajectories agent trả lời đúng
4. Record complete trajectory: τ = [(action_type, document), ...]

### Bước 3 — Extract Tiered Distractors
1. Tier-1 (high confusability): documents agent opened & read nhưng KHÔNG cite trong response
2. Tier-2 (low confusability): documents hiện trong search results nhưng agent KHÔNG mở
3. Ưu tiên Tier-1 trước khi fill context

### Bước 4 — Assemble Training Context
1. Start với gold evidence passages
2. Add Tier-1 distractors trước (challenging hơn)
3. Nếu chưa đủ target length → thêm Tier-2
4. Shuffle toàn bộ documents (prevent positional shortcuts)
5. Target: 128K tokens per example

### Bước 5 — RL Training với Rubric Reward
1. Algorithm: GRPO (Group Relative Policy Optimization), group size G=8
2. Outcome reward: binary (1 nếu answer đúng, 0 nếu sai)
3. Rubric reward: r_rubric = |gold entities appear in response| / |total gold entities|
4. Group-level normalization: chia cho max trong group
5. Positive-only: chỉ apply rubric reward khi outcome = 1
6. Combined: r = (1-α)·r_outcome + α·r_rubric, α=0.3
7. Train 200 iterations, learning rate 2e-6

## Output mong đợi
- Model reasoning tốt hơn trên long-context benchmarks
- Response grounded in evidence hơn (higher entity recall)
- Longer, more deliberate reasoning chains
- Cải thiện: +3-6 điểm average trên long-context benchmarks

## Ví dụ áp dụng
**Tình huống**: Company có internal knowledge base 10K documents. Muốn train AI assistant trả lời câu hỏi phức tạp cần thông tin từ nhiều documents.

**Áp dụng**:
1. Build KG từ internal docs (entity extraction + linking)
2. Generate multi-hop questions: "What is the revenue growth rate of the division that acquired Company X in Q3?"
3. Deploy search agent, collect trajectories khi agent cố trả lời
4. Tier-1: docs agent đọc nhưng không cite (cùng topic, dễ confuse)
5. Tier-2: docs hiện trong search nhưng agent không mở
6. Train với rubric reward: check model có mention đúng entities (division name, acquisition date, revenue figure) không

## Lưu ý quan trọng
1. **α quá cao (≥0.5)**: Model học enumerate entities thay vì reasoning thật → giữ α=0.3
2. **Distractor quá dễ**: Random distractor không challenge đủ → phải dùng agent trajectory
3. **Reward hacking**: Nếu apply rubric cho cả wrong answers → model liệt kê entities lung tung → positive-only strategy
4. **Context length**: 128K tokens cần nhiều GPU memory → có thể cần gradient checkpointing
5. **Agent quality**: Agent yếu → distractor kém chất lượng → training signal yếu
6. **Data size**: Chỉ 2,815 examples nhưng đủ vì quality cao; không cần data lớn nếu distractor khó
