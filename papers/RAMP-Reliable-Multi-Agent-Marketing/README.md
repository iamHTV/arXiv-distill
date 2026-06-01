# [2508.11120] RAMP: Hệ thống Đa tác nhân Đáng tin cậy cho Ứng dụng Marketing qua Phản chiếu, Bộ nhớ, và Lập kế hoạch

## Vấn đề
LLM-based AI agents có thể plan (lập kế hoạch) và interact với tools để complete complex tasks. Nhưng literature on reliability (độ tin cậy) trong real-world applications vẫn limited. Cụ thể trong marketing: audience curation (tạo đối tượng) — agents cần filter, verify, refine results — nhưng agents thường hallucinate (ảo giác) và add unnecessary filters (bộ lọc không cần thiết).

## Đóng góp
1. **RAMP framework**: Multi-agent cho marketing audience curation. Plans, calls tools, verifies output, generates suggestions
2. **Long-term memory store**: Knowledge base client-specific facts + past queries
3. **Iterative verification/reflection**: +20 pp recall trên ambiguous queries, higher user satisfaction
4. **Results**: +28 pp accuracy trên 88 evaluation queries

## Phương pháp (tóm tắt cốt lõi)
RAMP: (1) Planner generates step-by-step plan using table metadata; (2) Actor executes plan — NL2Code translates filters to Python functions; (3) Verifier checks output quality; (4) Reflector generates suggestions for improvement. Long-term memory: semantic memory (client facts) + episodic memory (past queries). Iterative: verify → reflect → refine loop cho ambiguous queries.

## Kết quả chính
- Baseline (Actor Only): 58.3% accuracy
- Actor + Planner: 63.3% (+5 pp)
- Actor + Semantic Memory: 70.6% (+12.3 pp)
- Actor + Planner + Semantic Memory: 87.0% (+28.7 pp)
- Iterative verification: +20 pp recall trên ambiguous queries
- Models without memory hallucinate — add unnecessary filters
- Memory count: recall increases with more memory, precision peaks at 6 memories

## Insight có thể áp dụng ngay
1. **Semantic memory là crucial**: Without memory, models hallucinate, add unnecessary filters. Always provide client-specific facts. Ví dụ: khi build AI marketing agent, maintain knowledge base về client's products, past campaigns, audience segments — don't rely on metadata alone.

2. **Planner + Memory combination is key**: Either alone helps, but combined = +28 pp. Ví dụ: marketing automation — first plan (what filters to apply), then execute with memory (what worked before).

3. **Iterative verification cho ambiguous queries**: More verify/reflect iterations → better recall. Ví dụ: when audience query is ambiguous ("high-value customers"), iterate: verify output → reflect on quality → refine filters.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Table metadata available (column names, data types, sample values)
- Client-specific knowledge base
- GPT-4.1 tested — other models untested

**Hạn chế paper thừa nhận:**
- Only tested OpenAI GPT 4.1
- Narrow marketing domain
- Reflect/verify can be tedious for users

**Hạn chế paper KHÔNG nói:**
- 88 queries limited evaluation set
- Memory management overhead
- Hallucination still possible even with memory
- Cost of iterative verification
- Privacy concerns with client-specific memory

## Metadata
- Năm: 2025
- Tác giả: Lorenzo Jaime Yu Flores, Junyi Shen, Goodman Gu
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2508.11120
- Citation count: [EXTRACTION FAILED]
