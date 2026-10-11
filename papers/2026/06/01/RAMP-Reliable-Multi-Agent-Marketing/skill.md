# Skill: RAMP — Marketing Multi-Agent với Memory + Reflection
Nguồn: 2508.11120
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) AI marketing agents cần reliability (độ tin cậy)
- Khi cần audience curation (tạo đối tượng) từ structured data
- Khi agents hallucinate (ảo giác) hoặc add unnecessary filters

## KHÔNG nên dùng khi
- Simple tasks không cần multi-agent
- No structured data available
- No client-specific knowledge base

## Input cần có
- Customer data với table metadata
- Client-specific knowledge base (semantic memory)
- Past query history (episodic memory)
- Evaluation queries cho testing

## Các bước thực hiện

### Bước 1 — Setup Memory Store (thiết lập kho bộ nhớ)
1. Semantic memory: client facts, products, campaigns, audience segments
2. Episodic memory: past queries + results
3. Store in retrievable format
4. Update after each interaction

### Bước 2 — Build RAMP Pipeline (xây dựng quy trình RAMP)
1. Planner: generates step-by-step plan using table metadata
2. Actor: NL2Code — translates filters to Python functions
3. Verifier: checks output quality
4. Reflector: generates improvement suggestions

### Bước 3 — Execute with Memory (thực thi với bộ nhớ)
1. Retrieve relevant memories trước khi plan
2. Planner uses memories to avoid hallucination
3. Actor executes plan with memory context
4. Verify output against expectations

### Bước 4 — Iterate for Ambiguous Queries (lặp lại cho truy vấn mơ hồ)
1. If query ambiguous → trigger verify/reflect loop
2. Verify: check output quality
3. Reflect: suggest improvements
4. Refine: apply suggestions
5. Repeat until quality acceptable

## Output mong đợi
- +28 pp accuracy vs baseline
- +20 pp recall on ambiguous queries
- Higher user satisfaction
- Fewer hallucinations

## Ví dụ áp dụng
**Tình huống**: Marketing team needs audience curation from customer database.

**Áp dụng**:
1. Memory: client facts (products, past campaigns)
2. Query: "Find high-value customers in NY"
3. RAMP: plan → execute → verify → reflect
4. Without memory: adds unnecessary filters → wrong audience
5. With memory: correct filters → right audience (+28 pp accuracy)

## Lưu ý quan trọng
1. **Semantic memory is crucial**: Without it, models hallucinate. Always provide client-specific facts
2. **Planner + Memory = best**: Combined gives +28 pp. Either alone gives less
3. **Iterative verification for ambiguous**: More iterations → better recall
4. **Memory count matters**: Recall increases with more memory, precision peaks at 6
5. **Hallucination risk**: Even with memory, possible. Verify output always
6. **User experience**: Reflect loops can be tedious. Balance quality vs speed
