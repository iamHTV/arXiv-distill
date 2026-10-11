# [2602.07079] Đánh giá Toàn diện LLMs trên Tác vụ Kỹ thuật Phần mềm: Benchmark Đa nhiệm

## Vấn đề
LLMs có remarkable capabilities trong software engineering (kỹ thuật phần mềm), nhưng comprehensive benchmarks covering diverse SE activities vẫn limited. Prior benchmarks focus trên code correctness — bỏ lỡ efficiency metrics (chỉ số hiệu quả). Cần đánh giá cả quality (chất lượng) và efficiency (hiệu suất) across multiple SE tasks.

## Đóng góp
1. **Multi-task evaluation**: 11 LLMs trên 5 SE tasks: bug fixing, feature development, code refactoring, technical copywriting, research synthesis
2. **Automated verification framework**: Đo lường output quality VÀ completion efficiency
3. **Efficiency variance discovery**: 22× speed, 49× tool efficiency, 53× cost variation among models achieving identical perfect scores

## Phương pháp (tóm tắt cốt lõi)
Evaluate 11 frontier LLMs (GPT-5.1, Gemini-3 Pro, Deepseek-Chat, GLM-4.7, etc.) trên 5 tasks. Automated verification: quality scores + completion time + tool calls + estimated cost. Statistical analysis: Pearson correlation, efficiency metrics. Release all data + scripts cho reproducibility.

## Kết quả chính
- 4 models achieved perfect scores: GPT-5.1, Gemini-3 Pro, Deepseek-Chat, GLM-4.7
- Efficiency variance: 22× speed (33s vs 732s), 49× tool calls (3.8 vs 188 avg), 53× cost
- No correlation giữa tool usage và success (r=0.077, p=0.575)
- GPT-5.1: 18.8s, 3 tools. Gemini-3 Flash: 625s, 917 tools — SAME SCORE
- Two inefficiency patterns: loop inefficiency (repeat tool sequences), inference inefficiency (slow correct solutions)
- Coding tasks: 100% success. Research tasks: 90.9%
- OpenAI models: consistently fastest (avg 54s), best speed-quality tradeoff

## Insight có thể áp dụng ngay
1. **Efficiency > accuracy khi choose LLM**: Models với same accuracy có 49× tool efficiency difference. Choose based on efficiency, not just accuracy. Ví dụ: khi deploy code assistant, compare models trên tool calls + cost, không chỉ task success.

2. **More tools ≠ better results**: Tool usage count không correlate với success. Avoid models với loop inefficiency. Ví dụ: khi monitor AI agent, track tool call count — nếu >100 calls cho simple task → loop inefficiency, consider switching model.

3. **Loop vs inference inefficiency**: Loop = agent repeats tool sequences without recognizing failure. Inference = model generates correct solutions slowly. Ví dụ: when debugging slow AI agent, identify type — loop needs stopping logic, inference needs faster model.

## Giả định & Hạn chế
**Điều kiện để benchmark work:**
- 5 SE tasks representative
- Automated verification accurate
- Cost estimation reliable

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- 5 tasks may not cover all SE activities
- Cost estimation may differ from real costs
- Model versions change rapidly
- Task complexity may vary

## Metadata
- Năm: 2026
- Tác giả: Go Frendi Gunawan, Mukhlis Amien
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2602.07079
- Citation count: [EXTRACTION FAILED]
