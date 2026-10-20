# 2610.24087 OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners

## Problem
- Các benchmark (tiêu chuẩn đánh giá) OR (operations research — nghiên cứu vận hành) hiện có bắt đầu từ mô tả bài toán tự chứa hoặc task (nhiệm vụ) đã định nghĩa sẵn → bỏ qua bước khó nhất thực tế: dịch tài liệu khách hàng gốc (thường không đầy đủ) thành solution (giải pháp) được chuyên gia xác nhận.

## Contribution
- OR-License: benchmark end-to-end (từ đầu đến cuối), 31 instances (bài toán) trong 10 kịch bản công nghiệp, lấy từ hợp đồng OR trả phí tổng $3.68M (phí $67.1k–$131.6k, trung bình 4.7 tháng, 2.16 chuyên gia).
- ORSim: client simulator (máy mô phỏng khách hàng) tiết lộ business facts (sự thật nghiệp vụ), tối đa 3 facts ngoài brief (tóm tắt) mỗi query (truy vấn), nhưng không cấp chuyên môn OR.
- DAQ (Deployment-Adjusted Quality — chất lượng hiệu chỉnh theo triển khai): điểm 0 cho deliverable (sản phẩm bàn giao) không khả thi; DAQ = Feasibility (tính khả thi) × conditional quality (chất lượng có điều kiện).
- Hidden verifier (bộ kiểm tra ẩn) kiểm tra feasibility; objective quality (chất lượng mục tiêu) được tính lại độc lập từ decision (quyết định) agent nộp.

## Method
- Agent (tác nhân) nhận brief + input files đã gỡ nhận dạng; query ORSim trong suốt formulation (xây mô hình), solving (giải), refinement (tinh chỉnh); phải xuất decision chạy được cho mọi test case.
- 11 frontier LLM với Claude Code harness (khung chạy), 5 runs mỗi model-task, trọng số task bằng nhau; so sánh thêm harness Codex ở appendix (phụ lục).
- Phân tích chuỗi HCAEU: Hypothesis (giả thuyết) → mechanistic explanation (giải thích cơ chế — C) → executed diagnostic experiment (thí nghiệm chẩn đoán đã chạy — A) → evidence interpretation (diễn giải bằng chứng — E) → evidence-grounded update (cập nhật dựa trên bằng chứng — U).

## Key Findings
- Feasibility chênh 43.23 điểm phần trăm: Hy3 45.16% → Grok 4.6 88.39%. Conditional quality chỉ chênh 4.09 điểm (96.92%–101.01%).
- Nhiều model vượt expert reference (chuẩn chuyên gia = 100%) về conditional quality, nhưng TẤT CẢ đều dưới expert về DAQ. Cao nhất: Grok 4.6 DAQ 86.55% — gap 13.45 điểm = 11.61 điểm do deliverable không khả thi + 1.84 do objective shortfall (thiếu hụt mục tiêu) → ~86% thua lỗ đến từ bàn giao thất bại, không phải toán kém.
- GPT-5.6 Sol: feasibility 84.52%, DAQ 85.02%. Gemini 3.8 Flash: 82.58% / 82.94%. Claude Opus 5: 77.42% / 77.44%.
- Tỷ lệ hoàn thành chuỗi HCAEU đầy đủ: 24% (Muse Spark 1.3) → 45% (Grok 4.6), mọi model dưới 50%.
- GPT-5.6 Sol không tạo giả thuyết kiểm chứng được trong 41% cơ hội; Qwen3.8-Max dừng ở HC và HCAE 21% mỗi loại.

## Actionable Insights
1. Đánh giá agent theo "khả thi × chất lượng", không theo "chất lượng khi khả thi". Ví dụ: chấm agent tối ưu lịch giao hàng, deliverable nào vi phạm constraint (ràng buộc) thì điểm = 0 rồi mới nhân chất lượng.
2. Thu thập thông tin phải tiếp tục sau clarification (làm rõ) ban đầu. Ví dụ: thiết kế agent nghiệp vụ có checkpoint hỏi khách hàng giữa task (giới hạn 3 facts/lần như ORSim) ở giai đoạn xây mô hình và xác thực.
3. Đo completion (hoàn thành) chuỗi H-C-A-E-U trên log, không chỉ câu trả lời cuối. Ví dụ: agent dừng ở "giải thích" mà không có evidence-grounded update (cập nhật dựa trên bằng chứng) → flag là research chain (chuỗi nghiên cứu) hở.

## Assumptions & Limitations
- Cần expert reference solution (giải pháp chuẩn) được khách hàng chấp nhận + programmatic verifier (bộ kiểm tra lập trình) mỗi instance — khó xây cho task nghiệp vụ mờ như viết content.
- De-identification (gỡ nhận dạng) có thể xóa thông tin người làm thực tế sẽ có; ORSim facts do chuyên gia tuyển, không phải khách hàng thật.
- 5 runs/model-task; spread (độ phân tán) là within-task, không phải standard error (sai số chuẩn) của benchmark mean (trung bình).
- Paper không so sánh thời gian/chi phí agent vs chuyên gia trong body → [NO BENCHMARK] về cost (chi phí).

## Metadata
- Năm 2026; tác giả: Peisong Wang (HKUST-GZ), Feixue Liu (HKU), Yize Meng (Qingzhi Optimization), Bowen Liu (HKUST-GZ/Tencent Hunyuan), ... Zuo-Jun Max Shen, Yong-Hong Kuo (HKU), Jia Li (HKUST-GZ); category: cs.CL, cs.AI; PDF: https://arxiv.org/pdf/2610.24087; citation count: [NO DATA — paper mới 2026-10-16]
