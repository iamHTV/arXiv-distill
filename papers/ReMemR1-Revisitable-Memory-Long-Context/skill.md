# Skill: ReMemR1 — Bộ nhớ Có thể Truy cập lại cho Agents Ngữ cảnh Dài
Nguồn: 2509.23040
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) long-context QA agents
- Khi cần non-linear reasoning (suy luận phi tuyến) qua documents
- Khi "memorize while reading" loses information

## KHÔNG nên dùng khi
- Short-context tasks
- Simple linear processing sufficient
- No RL training infrastructure

## Input cần có
- Long-context documents
- QA pairs
- GRPO training infrastructure
- Memory retrieval mechanism

## Các bước thực hiện

### Bước 1 — Setup Memory Agent (thiết lập tác nhân bộ nhớ)
1. Agent maintains current memory m_t
2. Agent generates callback query q_t
3. State = (m_t, q_t)
4. Output: history-augmented memory agent

### Bước 2 — Implement Callback Retrieval (triển khai truy xuất)
1. At each step, generate callback query
2. Search over entire memory history {m_i}_{i≤t}
3. Retrieve relevant past memories
4. Output: non-linear reasoning capability

### Bước 3 — Train với Multi-level Rewards (huấn luyện)
1. Trajectory-level reward: final answer correctness
2. Step-level reward: relative information gain
3. Normalize across trajectories và steps
4. GRPO optimization
5. Output: trained memory agent

### Bước 4 — Deploy & Evaluate (triển khai & đánh giá)
1. Process long documents with callback capability
2. Answer questions requiring multi-hop reasoning
3. Output: long-context QA answers

## Output mong đợi
- Significantly outperforms SOTA on long-context QA
- Negligible computational overhead
- Non-linear reasoning paths

## Ví dụ áp dụng
**Tình huống**: Answer questions from 100-page legal document.

**Áp dụng**:
1. Process document chunk by chunk
2. At chunk 50, question references clause in chunk 10
3. Agent generates callback query → retrieves relevant memory from chunk 10
4. Integrates past evidence → answers correctly
5. Result: correct answer without re-reading entire document

## Lưu ý quan trọng
1. **Look back to reason forward**: Enable memory callback
2. **Multi-level rewards**: Step-level + trajectory-level
3. **Non-linear reasoning**: Don't confine to forward-only
4. **Negligible overhead**: Callback retrieval is cheap
5. **Memory history limits**: Very long documents may need pruning
