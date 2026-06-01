# [2605.30802v1] Multi-Agent AI Oracle cho Prediction Market Resolution (Phân giải Thị trường Dự đoán)

## Vấn đề
Prediction markets (thị trường dự đoán) aggregate (tổng hợp) collective intelligence (trí tuệ tập thể) để forecast (dự đoán) uncertain events (sự kiện không chắc chắn), nhưng utility (giá trị sử dụng) phụ thuộc vào reliable outcome resolution (phân giải kết quả đáng tin cậy). Existing oracle systems tradeoff (đánh đổi) giữa fast but brittle automation (tự động hóa nhanh nhưng dễ vỡ) và accurate but costly human arbitration (phân xử con người chính xác nhưng tốn kém). Single-LLM oracles inherit (thừa hưởng) tất cả failure modes (chế độ lỗi) của underlying model mà không có self-correction mechanism (cơ chế tự sửa chữa).

## Đóng góp
1. **Independent aggregation tốt hơn deliberative consensus**: Confidence-weighted voting đạt 83.43% accuracy, outperform (vượt trội) best single model (DeepSeek 82.42%) by 1.01 percentage points. Deliberative consensus DEGRADES (xuống cấp) xuống ~76% — dưới mọi single-model baseline
2. **Error correlation limits ensemble gains**: Error correlations across models 0.529-0.689 → aggregation gains rơi xa theoretical Condorcet ceiling (~90%). Shared training data tạo correlated failures
3. **Hybrid AI-human escalation framework**: Unanimous high-confidence questions → 97.87% accuracy trên 47% dataset. Inter-agent disagreement flags (đánh dấu) remainder cho human review

## Phương pháp (tóm tắt cốt lõi)
Test trên 1,189 resolved prediction market questions từ KalshiBench. 3 LLM agents: GPT-5 Nano, DeepSeek-V3, Llama-3.3-70B. Common evidence layer qua Exa, retrieval filtered by publication date. Architecture A: Independent Aggregation — mỗi model resolve independently, majority vote hoặc confidence-weighted vote. Architecture B: Deliberative Consensus — structured debate 2 rounds, models xem reasoning của nhau trước khi submit. Escalation signals: inter-agent agreement (unanimous vs split) + average confidence → composite score.

## Kết quả chính
- Independent aggregation (confidence-weighted): 83.43% accuracy — best overall
- Best single model (DeepSeek): 82.42%
- Deliberative consensus: ~76% — BELOW every single-model baseline
- Unanimous (3-0 agreement): 88.34% accuracy (978 questions)
- Split (2-1 vote): 57.82% accuracy (211 questions) — barely above chance
- Unanimous + high confidence (≥0.91): 97.87% accuracy trên 563 questions (47% dataset)
- Error correlations: r=0.529-0.689 across model pairs
- Category tier: Sports, Financials >92%; Crypto, Companies <67%
- 14% questions resist correction by any multi-agent architecture

## Insight có thể áp dụng ngay
1. **Không dùng deliberative debate cho evidence-based tasks**: Khi có shared evidence (bằng chứng chung), deliberation HẠI accuracy vì confidently wrong models flip correct ones (mô hình sai tự tin lật mô hình đúng). Chỉ dùng deliberation khi cần explore diverse perspectives, không phải khi có ground truth. Ví dụ: financial oracle — dùng independent aggregation, không dùng debate.

2. **Inter-agent disagreement là strongest signal**: Khi 3 models independently disagree (2-1 vote), accuracy drop xuống 57.82% — barely above chance. Dùng disagreement làm escalation trigger. Ví dụ: AI advisory system — khi multiple models disagree, flag cho human review thay vì auto-resolve.

3. **Hybrid routing: auto-resolve high-confidence, escalate rest**: Unanimous + high confidence → 97.87% accuracy. Dùng composite score = unanimous + confidence để route. Ví dụ: customer support AI — auto-resolve khi tất cả models agree với confidence >0.9, escalate khi có disagreement.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Cần multiple diverse LLMs (không cùng architecture/training data)
- Common evidence layer phải available
- Questions phải có binary/clear resolution criteria

**Hạn chế paper thừa nhận:**
- Error correlations 0.529-0.689 limit theoretical gains
- 14% questions resist any multi-agent correction
- Deliberative consensus degrades performance — not always useful
- KalshiBench specific — generalizability unclear

**Hạn chế paper KHÔNG nói:**
- Chỉ test 3 models — không explore larger ensembles
- Không test cost-effectiveness — 3x API cost vs single model
- Evidence quality (Exa retrieval) có thể vary
- Không address dynamic markets — questions evolve over time
- Binary resolution only — không test continuous outcomes
- Không compare với fine-tuned single models

## Metadata
- Năm: 2026
- Tác giả: Tarun Kota
- Category: cs.MA, cs.AI
- Link PDF: https://arxiv.org/pdf/2605.30802v1
- Citation count: [EXTRACTION FAILED]
