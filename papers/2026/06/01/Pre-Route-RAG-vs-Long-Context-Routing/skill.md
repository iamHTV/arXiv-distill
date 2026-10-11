# Skill: Pre-Route RAG vs Long-Context Routing
Source: 2605.10235
Type: framework

## Khi nào dùng skill này

- Khi build RAG system mà có documents dài (10K+ tokens) và cần quyết định query nào nên dùng RAG (retrieve snippets) vs Long Context (full document) — đặc biệt khi cost là concern
- Khi Self-Route (failure-driven fallback) không hiệu quả — model hay output "unanswerable" quá conservative hoặc quá confident
- Khi muốn routing decisions interpretable (có thể giải thích) và cost-efficient

- KHÔNG dùng khi: documents ngắn (<4K tokens, luôn dùng full context); chỉ dùng 1 strategy (always-RAG hoặc always-LC); không có access to LLM for routing reasoning

## Input cần có

- Document corpus với varying lengths (10K-128K+ tokens)
- LLM capable of structured reasoning (GPT-4-class trở lên cho prompt-only; có thể distill xuống 1.7B)
- Evaluation queries với ground-truth answers
- Cost model: per-token pricing cho RAG retrieval vs full context processing

## Các bước thực hiện

1. **Collect Lightweight Metadata** — Với mỗi document/query pair, gather: (a) document type (report, novel, manual, email); (b) document length; (c) head snippet (200 tokens đầu). KHÔNG cần expensive metadata extraction — Head-only metadata (length + head) gần bằng Full-Meta.

2. **Structured Routing Prompt** — Design prompt template: "Given document type: {type}, length: {length} tokens, opening: {snippet}. Question: {query}. Analyze: (1) Task type — is this comparison, fact-retrieval, or synthesis? (2) Information distribution — is answer concentrated in specific sections or scattered? (3) Coverage estimate — can retrieved snippets cover the answer? (4) Recommendation: RAG or Long-Context, with reasoning." LLM outputs routing decision + explanation.

3. **Execute Routing Decision** — Nếu RAG: run retrieval pipeline, concatenate top-k snippets với query, generate answer. Nếu LC: feed full document + query vào LLM. Track routing decisions để analyze patterns (queries nào consistently need LC?).

4. **Distill to Small Model** — Nếu cần deploy lightweight: (a) Chạy large model (235B) làm teacher trên training set, collect routing decisions + reasoning chains; (b) Fine-tune small model (1.7B) với reasoning-chain supervision; (c) Small model inherits routing logic, deploy on edge.

5. **Evaluate Cost-Effectiveness** — Tính: accuracy per token cost, route accuracy (% routing decisions match oracle), LC usage rate (% queries routed to LC). Compare với Self-Route, Always-RAG, Always-LC baselines.

## Output mong đợi

- Route accuracy >80% (routing decisions match oracle)
- LC usage reduction so với Self-Route (fewer unnecessary LC calls)
- Higher QA score so với Always-RAG (better quality when LC needed)
- Distilled 1.7B model achieves ~90% routing accuracy của large teacher

## Ví dụ áp dụng

Scenario: Legal tech company build contract analysis tool. Documents: 50-200 page contracts. Pre-Route deployment: (1) User uploads contract → system collects metadata (type: contract, length: 85K tokens, head: "This Agreement dated..."); (2) User asks: "What are the termination conditions?" → routing prompt: "Fact-retrieval question, answer concentrated in specific clause → RAG"; (3) User asks: "Compare indemnification obligations across all sections" → routing prompt: "Comparison task, information scattered → LC"; (4) Result: 70% queries routed to RAG (cheaper), 30% to LC (higher quality when needed). Cost: 40% reduction vs always-LC. Accuracy: +3% vs always-RAG.

## Gotchas

- Routing prompt quality matters: vague prompts → inconsistent routing. Template must include specific analysis dimensions (task type, information distribution, coverage).
- 74.3% of small model errors tilt toward LC (safer option) — distillation helps but small models still biased. Need to calibrate LC threshold.
- Metadata can be misleading: short documents might need LC if comparison-heavy; long documents might work with RAG if question is localized. Routing prompt must consider task type, not just length.
- Binary routing limitation: some queries benefit from hybrid approach (RAG first, then targeted LC on specific sections). Pre-Route doesn't capture this nuance.
