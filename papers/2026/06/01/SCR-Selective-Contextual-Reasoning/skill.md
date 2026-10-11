# Skill: SCR — Cập nhật Tri thức qua Suy luận Ngữ cảnh
Nguồn: 2503.05212
Loại: workflow

## Khi nào dùng skill này
- Khi update (cập nhật) LLM knowledge mà không muốn edit parameters
- Khi external knowledge base available
- Khi model editing methods insufficient

## KHÔNG nên dùng khi
- Simple knowledge updates có thể handle bằng prompt
- No external knowledge base
- Parameter editing required cho specific tasks

## Input cần có
- External knowledge base với updated facts
- LLM with contextual reasoning capabilities
- Query scope assessment capability

## Các bước thực hiện

### Bước 1 — Setup External Knowledge Base (thiết lập cơ sở tri thức)
1. Maintain external KB với updated facts
2. Organize by topics/domains
3. Update independently of LLM
4. Output: current knowledge base

### Bước 2 — Assess Query Scope (đánh giá phạm vi)
1. LLM assesses: query có fall within KB scope không?
2. If yes → retrieve relevant knowledge
3. If no → answer directly
4. Output: scope decision

### Bước 3 — Contextualize & Reason (ngữ cảnh hóa & suy luận)
1. If in scope: inject relevant knowledge texts into context
2. LLM reasons over contextualized knowledge
3. Generate answer based on updated information
4. Output: updated answer

## Output mong đợi
- Updated knowledge without parameter editing
- Better than model editing methods
- Training-free, parameter-free

## Ví dụ áp dụng
**Tình huống**: Company LLM has outdated product info. Products change monthly.

**Áp dụng**:
1. External KB: product catalog updated monthly
2. Query: "What's the price of Product X?"
3. SCR: query in scope → inject current price from KB
4. Answer: correct, updated price
5. No model retraining needed

## Lưu ý quan trọng
1. **Don't edit parameters**: Model editing has shortcomings. Use external KB
2. **Selective is key**: Only contextualize when query in scope
3. **External KB maintenance**: Update independently, frequently
4. **Context window limits**: Large KB may exceed context. Prioritize relevant facts
5. **Scope assessment accuracy**: Critical for correct behavior
