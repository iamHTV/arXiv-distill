# Skill: Few-shot Optimal Selection (Lựa chọn Tối ưu Few-shot)
Nguồn: 2509.13196
Loại: prompt-pattern (khuôn mẫu prompt)

## Khi nào dùng skill này
- Khi build (xây dựng) few-shot prompts cho LLM classification tasks
- Khi optimize (tối ưu hóa) number of examples trong prompts
- Khi avoid (tránh) over-prompting problem

## KHÔNG nên dùng khi
- Zero-shot sufficient (không cần few-shot)
- Large models (70B+) với strong long-context capabilities
- Non-classification tasks

## Input cần có
- Training examples pool
- LLM being used (cần biết model size)
- Target task description
- Evaluation metric

## Các bước thực hiện

### Bước 1 — Select Examples bằng TF-IDF (chọn ví dụ)
1. Compute TF-IDF vectors cho all training examples
2. Compute similarity giữa test input và training examples
3. Select top-K most similar examples
4. Output: ranked examples by relevance

### Bước 2 — Find Optimal Quantity (tìm số lượng tối ưu)
1. Start với 5 examples
2. Test performance
3. Gradually increase: 10, 15, 20, 25, 30
4. Find turning point: performance drops = over-prompting
5. Output: optimal K per LLM

### Bước 3 — Stratified Selection (lựa chọn phân tầng)
1. Ensure examples cover different classes
2. Balance representation
3. Output: balanced few-shot prompt

### Step 4 — Deploy (triển khai)
1. Use optimal K examples
2. Monitor performance
3. Adjust if model updates
4. Output: optimized few-shot prompt

## Output mong đợi
- Optimal number of few-shot examples per LLM
- Better performance with fewer examples
- Avoidance of over-prompting

## Ví dụ áp dụng
**Tình huống**: Classify customer support tickets. Using LLaMA-3.1-8B.

**Áp dụng**:
1. TF-IDF: find 50 most similar training tickets
2. Test: 5, 10, 15, 20, 25 examples
3. Result: 10-20 examples optimal. 25+ = performance drops
4. Deploy: use 15 TF-IDF-selected examples
5. Result: surpasses SOTA by 1%

## Lưu ý quan trọng
1. **Less is more**: More examples ≠ better. Find optimal K
2. **TF-IDF selection**: Better than random or semantic embedding
3. **Model size threshold**: 8B parameters may be threshold. Smaller = fewer examples
4. **Task-specific**: Optimal K varies by task. Test yours
5. **Large models more robust**: DeepSeek-V3, GPT-4o handle more examples consistently
