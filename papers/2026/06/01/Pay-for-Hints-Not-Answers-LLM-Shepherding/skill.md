# Skill: LLM Shepherding Cost Optimization
Source: 2601.22132
Type: framework

## Khi nào dùng skill này

- Khi cần giảm LLM inference cost (chi phí suy luận) trong production mà vẫn giữ accuracy cao — đặc biệt khi có SLM (Small Language Model) capable nhưng chưa đủ accuracy standalone
- Khi deployment có cả LLM (API hoặc self-hosted) và SLM (edge device, local server) — muốn tận dụng cả hai mà không tốn full LLM cost cho mỗi query
- Khi tasks là reasoning hoặc code generation — "hint" (gợi ý dạng prefix) từ LLM đủ để guide SLM

- KHÔNG dùng khi: chỉ có 1 model (không có cả LLM lẫn SLM); tasks là open-ended generation (creative writing, summarization) mà "đầu" response không chứa key info; SLM quá yếu để utilize hints

## Input cần có

- LLM access (API hoặc self-hosted) với ability set max_new_tokens
- SLM (local hoặc edge) capable of following hints
- Training dataset với ground-truth answers để train hint predictor (ít nhất 1K+ queries)
- Quality threshold τ — accuracy level cần đạt
- Cost model: per-token pricing cho LLM input/output

## Các bước thực hiện

1. **Oracle Analysis** — Chạy LLM và SLM trên eval dataset. Với mỗi query, determine: (a) SLM có solve được không? (b) Nếu cần hint, minimum hint size n* là bao nhiêu? Label n* bằng cách evaluate SLM accuracy ở 10% increments (0%, 10%, ..., 90%) của full LLM response. Chọn smallest n* đạt quality threshold τ.

2. **Analyze Hint Distribution** — Plot distribution của n* values. Typically: 80% queries có n*=0 (SLM solve được), 20% span 10-90% (heavy-tailed). Xác định class imbalance ratio để configure weighted sampling.

3. **Train Two-Stage Predictor** — (a) Stage 1: Binary classifier — hint needed? Input: query features (embeddings), Output: probability hint > 0. Dùng weighted sampling để handle class imbalance. (b) Stage 2: Huber regression — predict log(1+n*) cho positive cases. Joint loss: λ·BCE + (1-λ)·Huber.

4. **Choose Deployment Mode** — (a) Proactive Shepherding: router predicts hint size BEFORE SLM runs → lower latency nhưng cần accurate prediction; (b) Reactive Shepherding: SLM runs first, features từ SLM response dùng để predict hint → higher accuracy nhưng thêm 1 SLM inference.

5. **Deploy with Threshold** — At test time: predictor cho hint probability p và hint size n. Nếu p < threshold → no hint, SLM alone. Nếu p ≥ threshold → request n-token hint từ LLM, concatenate với query, SLM generate final response. Tune threshold để match target accuracy-cost tradeoff.

6. **Evaluate ACE** — Tính Accuracy-per-Cost Efficiency: ACE = (A_π - A_s) / (C_π - C_s) × (C_l - C_s) / (A_l - A_s). So sánh ACE với routing và cascading baselines. Target: ACE > 1.5 trên math, > 2.0 trên code tasks.

## Output mong đợi

- Cost reduction 42-94% so với LLM-only inference
- ACE 1.25-2.78 tùy task difficulty
- Cross-domain generalization: train trên 1 domain, apply được domain khác
- Negligible latency overhead (<10ms/query cho hint predictor)

## Ví dụ áp dụng

Scenario: E-commerce company chạy customer support chatbot. Hiện tại: mỗi query gọi GPT-4 ($0.03/query). Solution: (1) Deploy Llama-3.2-3B làm SLM local; (2) Train hint predictor trên 5K historical queries với labeled answers; (3) 80% queries: SLM handle alone (free); 4) 20% complex queries: request 20-token hint từ GPT-4 (~$0.002), SLM generate full response; (5) Total cost giảm từ $0.03 xuống ~$0.006/query (80% savings). Accuracy drop: <2%.

## Gotchas

- Class imbalance lớn: 80% no-hint → weighted sampling bắt buộc, nếu không classifier sẽ always predict "no hint"
- Non-monotonic quality: thêm hint tokens KHÔNG phải lúc nào cũng tốt hơn. Quá nhiều hint có thể confuse SLM. Cần tune max hint size cẩn thận.
- Training label quality: nếu SLM accuracy noisy (sampling variability), n* labels sẽ unreliable. Recommend 5-7 independent trials per query + majority voting.
- Cross-domain transfer tốt cho structured tasks (math, code) nhưng chưa test cho open-ended tasks. KHÔNG assume transfer được cho text generation.
- Output token cost dominant: hint-based savings mainly từ output tokens. Nếu LLM pricing input-heavy, savings ít hơn.
