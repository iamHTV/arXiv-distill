# [2506.17863] LLMs cho Tạo và Đánh giá Nội dung Marketing Tùy chỉnh ở Quy mô Lớn

## Vấn đề
Các nghiên cứu trước chưa giải quyết được bài toán tạo offsite marketing content (nội dung tiếp thị bên ngoài) hiệu quả vì: hầu hết nội dung hiện tại overly generic (quá chung chung), template-based (dựa trên mẫu), và poorly aligned (căn chỉnh kém) với landing pages (trang đích). Cách tiếp cận thủ công tốn kém, không scalable (mở rộng được), và dẫn đến limited audience engagement (tương tác khán giả hạn chế).

## Đóng góp
1. **MarketingFM**: Retrieval-augmented system (hệ thống tăng cường truy xuất) tích hợp nhiều data sources (nguồn dữ liệu) để generate keyword-specific ad copy (bản sao quảng cáo theo từ khóa) với minimal human intervention (can thiệp tối thiểu của con người)
2. **AutoEval-Main**: Automated evaluation system (hệ thống đánh giá tự động) kết hợp rule-based metrics (chỉ số dựa trên quy tắc) + LLM-as-a-Judge (LLM làm giám khảo) — 89.57% agreement (đồng thuận) với human reviewers
3. **AutoEval-Update**: LLM-human collaborative framework (khung hợp tác LLM-người) để dynamically refine evaluation prompts (tinh chỉnh prompt đánh giá) theo shifting criteria (tiêu chí thay đổi)

## Phương pháp (tóm tắt cốt lõi)
MarketingFM dùng RAG (Retrieval-Augmented Generation — tạo tăng cường truy xuất) với search page products context (ngữ cảnh sản phẩm từ trang tìm kiếm) để ground (nền tảng) ad generation trong real-time product data (dữ liệu sản phẩm thời gian thực). Task chaining (chuỗi tác vụ): generate → rewrite → evaluate. AutoEval-Main: rule-based checks (kiểm tra quy tắc) + LLM-as-a-Judge scoring (chấm điểm) trên relevance (liên quan) và generalization (khái quát hóa) scales 0-5. AutoEval-Update: active sampling (lấy mẫu chủ động) → human review → critic LLM generates alignment report (báo cáo căn chỉnh) → refine evaluation prompt → iterate (lặp) until convergence (hội tụ).

## Kết quả chính
- Online A/B test (10,000 keywords): +9% CTR (tỷ lệ nhấp chuột), +12% impressions (lượt hiển thị), -0.38% CPC (chi phí mỗi nhấp)
- Mobile: +121 bps CTR lift (p=0.055), +8% clicks (p=3.89e-6)
- Desktop: +9% clicks (p=2.56e-3), +12% impressions (p=1.01e-5)
- AutoEval-Main: 89.57% agreement với human reviewers trên 150,000 ad copies
- Rejection rate giảm từ 15% (semantic retriever) xuống 2.79% (products context retriever)
- "Stanley Cup problem": semantic retriever confuse hockey games với trending water bottles → products context retriever giải quyết
- AutoEval-Update: uncertainty-based sampling tốt nhất cho reducing errors, diversity-based sampling tốt nhất cho coverage

## Insight có thể áp dụng ngay
1. **RAG cho keyword-specific ads**: Thay vì generic templates, dùng RAG với real product data để tạo ad copy specific cho từng keyword. Ví dụ: user search "wireless headphones gym" → RAG retrieve actual gym headphones từ catalog → generate ad mention specific features, price, reviews. Kết quả: +9% CTR.

2. **LLM-as-a-Judge cho ad quality**: Dùng LLM để evaluate ad copy trước khi publish, giảm human review cost. Ví dụ: 10,000 ads generated → AutoEval-Main filter → chỉ ads pass threshold mới human review. 89.57% agreement = gần đúng với human judgment.

3. **AutoEval-Update cho criteria drift**: Evaluation criteria thay đổi theo thời gian → cần iterative refinement. Ví dụ: khi customer concern về product safety tăng → AutoEval-Update tự động refine evaluation prompt để include stricter accuracy metrics, không cần rebuild từ đầu.

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Cần search infrastructure (cơ sở hạ tầng tìm kiếm) với product catalog (danh mục sản phẩm) để RAG hoạt động
- Need large-scale human annotations (chú thích quy mô lớn) để establish benchmark cho AutoEval
- Domain-specific design (thiết kế theo lĩnh vực) — general LLMs thiếu understanding về ad network preferences

**Hạn chế paper thừa nhận:**
- LLM tends to be more conservative than humans — có thể reject acceptable content
- Semantic retriever limitations trong retail domain — "Stanley Cup problem"
- Human oversight still essential cho setting thresholds và validating refinements

**Hạn chế paper KHÔNG nói:**
- Không discuss latency của RAG pipeline — real-time ad generation cần fast retrieval
- Không address cost của running LLM-as-a-Judge at scale (20M keywords/day)
- Không test trên non-English markets
- Không compare với simpler baselines (rule-based templates có đủ tốt cho most cases?)
- AutoEval-Update convergence time không rõ — bao nhiêu iterations cần?

## Metadata
- Năm: 2025
- Tác giả: Haoran Liu (Texas A&M), Amir Tahmasbi, Ehtesham Sam Haque, Purak Jain (Amazon)
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2506.17863
- Citation count: [EXTRACTION FAILED]
