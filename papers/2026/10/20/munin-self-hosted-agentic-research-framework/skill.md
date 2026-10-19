# Skill: Triển khai agent harness tự lưu trữ + chứng nhận abstention (theo Munin)
Source: 2610.23480v1
Type: framework / evaluation-method

## Khi nào dùng skill này
- Cần xây assistant đọc tài liệu riêng (corpus nội bộ, tài liệu chưa công bố) mà không gửi dữ liệu ra service bên ngoài.
- Cần nâng cấp chất lượng câu trả lời của RAG system mà không đổi model đắt hơn.
- Cần đo lường và chứng nhận hệ thống biết từ chối (abstention) khi corpus thiếu nguồn, thay vì bịa citation.
- KHÔNG nên dùng: task không cần retrieval/verification (chat thông thường); không có corpus riêng để ingest; hardware dưới 1 GPU 24GB VRAM.

## Input cần có
- Corpus tài liệu (PDF/URL/DOI) của nhóm, tối thiểu vài chục tài liệu.
- 1 GPU ≥24GB VRAM (VD: RTX 5090 32GB) cho model 20B–27B (gpt-oss-20b MXFP4 hoặc Qwen3.8-27B AWQ/INT4).
- Munin (github.com/elgetilab/munin, Apache-2.0, release v1.0.0).
- Test set đánh giá: ≥100 câu hỏi có đáp án biết trước (lấy từ chính corpus), + 50–100 mục "tài liệu giả" (DOI không tồn tại verified against Crossref, hoặc title/claim của paper không có thật).
- 244 query mẫu đã gán nhãn profile (chat/research/code) để huấn luyện router; 18 anchor cases viết tay.

## Các bước thực hiện
1. Ingest corpus: chạy ingestion pipeline của Munin trên corpus — parse PDF, chunk (chỉ chunk tài liệu vượt context window), xây vector store + citation graph. Verify tất cả tài liệu resolve được trong index.
2. Cấu hình per-turn router: embed query bằng BGE-base-en-v1.5 (768 chiều), kNN vote k=8 trên 244 labelled queries, margin 0.10, OOD cosine threshold 0.45, pin prior 0.5. Slash command /research, /code, /chat buộc profile. Viết 18 anchor cases (disjoint với example set) — chỉ deploy harness change khi trajectory pass rate >0.95.
3. Cấu hình harness: 3 profile (chat/research/code); 4 sub-agents (source, search, deep_research, computer) với interior context cô lập; ~45 tools qua core tools + tool_search. Bắt buộc mọi sub-agent trả compact result gắn outcome tag (resolved/not_found/thin_evidence) — KHÔNG nhét toàn văn paper vào outer window.
4. Cấu hình source agent: chấp nhận reference ở 5 dạng (DOI, arXiv ID, internal ID, URL, title + tác giả + năm) — KHÔNG bắt buộc DOI (bắt DOI sẽ gây bịa DOI). Mỗi call: resolve → extract full text → answer trong 1 LM call. Trả về outcome taxonomy 5 giá trị (not_found / extraction_failed / ambiguous / out_of_scope / resolution miss), mỗi giá trị có caller contract riêng.
5. Cấu hình egress gate theo request: off (không mạng), oa_only (chỉ scholarly APIs), full (+ web search/fetch). Bật post-turn citation audit — gắn warning vào câu trả lời lưu trữ nếu reference không verify được.
6. Chạy evaluation suite (1 lệnh) — 3 arm trên cùng test set: (a) bare model, (b) naive RAG top-5, (c) agentic full harness. Tiêu chuẩn đạt: agentic − bare ≥ +0.30 accuracy; RAG − bare ≤ 0 (nếu RAG cao hơn bare → kiểm tra lại retrieval quality trước khi tin kết quả). So sánh paired difference với bootstrap 95% CI; bỏ qua difference <3 điểm (run-to-run noise ±0.035).
7. Chứng nhận abstention: (a) Test C1 — chạy 100 mục tài liệu giả với egress=full, yêu cầu refusal rate ≥0.95 và 0 confabulated local citation; (b) Test C2b — tạo shadow corpus (bỏ 49–50 source papers + chunks của chúng), chạy 50 câu hỏi single-source 2 lần (production vs shadow) với egress=off, yêu cầu abstention ≥0.80 khi thiếu nguồn.
8. Đặt certification thresholds làm regression gates: lưu scorecards (per-question verdicts + faithfulness) của lần chạy đạt chuẩn. Mỗi lần đổi model backbone hoặc sửa harness → chạy lại suite; chỉ deploy khi accuracy không giảm >3 điểm, refusal ≥0.95, abstention ≥0.80.

## Output mong đợi
- Scorecards 54+ file với per-question verdicts, faithfulness scores cho từng arm/backbone.
- Bộ số liệu ra quyết định: accuracy 3 arm (bare/RAG/agentic), faithfulness, refusal rate, abstention rate, recovery rate, tool calls/query, wall-clock/query.
- Quyết định deploy/go/no-go cho backbone mới hoặc harness change, dựa trên ngưỡng chứ không phải cảm giác.

## Ví dụ áp dụng
Freelancer content Việt Nam cài Munin trên corpus 200 bài blog + tài liệu khách hàng, chạy Qwen3.8-27B trên 1 GPU. Trước khi swap sang model mới: chạy suite — ablation cho bare 0.35 → agentic 0.82; C1: 96/100 refusal, 0 citation bịa; C2b: abstention 0.84 khi xóa source. Đạt ngưỡng → deploy model mới, lưu scorecard làm baseline cho lần đổi tiếp theo.

## Gotchas
- Bắt buộc DOI trong interface → model bịa DOI (DOI bịa không phân biệt được với DOI thật). Luôn cho phép title + tác giả + năm.
- Naive RAG (prepend top-5 docs, 1 completion) có thể KÉM HƠN cả bare model (−0.18 đến −0.31 accuracy) — đừng mặc định bật RAG mà không có verification loop.
- Abstention detect bằng text marker → retrieval sai paper (trích đúng định dạng nhưng sai nguồn) là vô hình với scorer. Cần spot-check thủ công 13/100 refusals có kèm citation thật.
- Sub-agent context cô lập là thiết kế cốt lõi: nếu nhét full paper vào outer window sẽ mất cả accuracy lẫn grounding.
- Bare/RAG arm sample temp 0.7 khác với agentic research profile — so sánh arm cần lưu ý asymmetry này.
- Egress=off vẫn có thể bị model "gọi" web tool (gọi bị intercept ở guard) — đây là bình thường, log vẫn ghi đủ tool call.
- Run-to-run noise ±0.035: difference <3 điểm là noise, đừng kết luận model tốt hơn.
