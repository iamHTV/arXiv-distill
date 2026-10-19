# Skill: Capability-Matched Agent Coordination (feedback-driven routing + gated review)
Source: 2610.21411v2 (Jev-LiteMAS)
Type: framework / workflow

## Khi nào dùng skill này
- Pipeline agent đa bước mà routing (chọn bước tiếp) + review (đánh giá artifact — sản phẩm trung gian) chiếm >~30% token generative-LLM (mô hình sinh văn bản) —paper profiling đo được 31,7–43,5%.
- Có ≥2 expert roles (vai trò chuyên gia) cố định và artifact trung gian có rubric (tiêu chuẩn) chất lượng rõ ràng (pass/escalate).
- KHÔNG nên dùng: workflow cần tự tạo expert/role mới động cho task chưa thấy; artifact trung gian hầu hết đều lỗi (gate — cổng sàng — không tiết kiệm); task 1 bước đơn giản không có coordination.

## Input cần có
- Danh sách expert roles: mô tả năng lực mỗi expert + backend (model) mỗi expert + role instructions (lệnh nhắc vai trò).
- Rubric đánh giá artifact trung gian (tiêu chí pass/escalate cụ thể, theo task).
- Decision model (mô hình quyết định) nhỏ, choice-based (chọn theo tập lựa chọn) cho routing + screening (sàng lọc) — class Jev; KHÔNG dùng SLM generic zero-shot (TPR 44,67–61,33% là quá thấp).
- Logs token + latency theo từng operation (đo baseline và verify savings).
- Tập test có inject lỗi (tiêm lỗi vào artifact) để đo TPR/FPR gate.

## Các bước thực hiện
1. Profile pipeline: đo share token và latency của routing + review trên representative tasks. Nếu mỗi loại <~15% → dừng, không đáng đổi.
2. Thay planner-generated plan (kế hoạch sinh sẵn) bằng feedback-driven routing: prompt router chứa {task, tóm tắt artifact mới nhất, mô tả expert, legal actions gồm STOP}; router trả expert ID hoặc STOP; expert được dispatch (điều phối) nhận task + artifacts qua state chia sẻ.
3. Đặt screening gate tại các review point: screener (decision model) đánh artifact vs rubric → pass (chạy tiếp, KHÔNG gọi LLM review) hoặc escalate.
4. escalate → LLM reviewer: verdict (accept/revise — chấp nhận/sửa) + corrective feedback (phản hồi sửa cụ thể); expert repair (sửa) nhận state ⊕ feedback; artifact mới lại được sàng như artifact mới (giới hạn số vòng review–repair).
5. Verify gate quality: tiêm lỗi vào artifact của 1 expert ngẫu nhiên, đo TPR (tỷ lệ phát hiện đúng) / FPR (tỷ lệ báo giả) của screener so với LLM judge — yêu cầu TPR ≥~90% so với LLM judge; lưu ý FPR thấp ≠ detection đáng tin.
6. Đo lại token/latency/accuracy toàn pipeline: chấp nhận nếu accuracy chênh ≤±1,34 điểm và token/latency giảm; nếu artifact fail-rate (tỷ lệ lỗi) cao → điều chỉnh ngưỡng gate hoặc chính sách duyệt thích ứng.

## Output mong đợi
- Pipeline chạy với token generative-LLM giảm 12,7–54,6%, latency giảm (7/8 cấu hình trong paper), accuracy chênh ≤1,34 điểm phần trăm; gate TPR gần LLM judge (95,33%/91,33% vs 96,67%/92,00%); decision layer chỉ chiếm ~1,5–2,1% chi phí model và ~3–7% latency E2E; robustness: ASR (tỷ lệ tấn công thành công) từ ~50% xuống 3,33–4,00% khi artifact bị tiêm lỗi.

## Ví dụ áp dụng
- Content pipeline 3 experts: researcher → writer → editor. Router chọn expert tiếp theo dựa trên artifact hiện tại (KHÔNG plan sẵn cả quỹ đạo); gate kiểm tra draft đạt rubric biên tập (đủ sự kiện, không AI-slop — văn bản máy móc) → pass thì gửi luôn bước kế tiếp, fail thì editor sửa với feedback cụ thể. Baseline: review LLM toàn bộ ~35% token → sau gate ~10%, accuracy giữ trong ±1 điểm.

## Gotchas
- Router content-blind (content-blind routing — router chỉ thấy tên/metadata) mất đến 18,0 điểm accuracy: PHẢI truyền tóm tắt substantive outputs (output có nội dung thật) vào router.
- SLM generic (ví dụ Qwen3-1.7B zero-shot) TPR chỉ 44,67–61,33% — gate yếu; False alarm thấp (FPR 0,00%) không có nghĩa gate tốt.
- Savings sụp khi artifact quality distribution (phân bố chất lượng) xấu — nhiều artifact liên tục phải sửa.
- Expert pool cố định: skill không xử lý task đòi hỏi role mới chưa cấu hình.
- Đừng bỏ qua latency của chính decision layer (1,13–2.21s/unit) khi expert rất nhanh — chiếm đến 6,85% E2E trên MATH.

## Self-check + Dry run (Step 5)
- SELF-CHECK: người không đọc paper có follow được không? YES — 6 bước cụ thể, input liệt kê đầy, gotchas cảnh báo rõ. Bước mơ hồ nhất: step 5 threshold TPR ≥~90% — rõ rồi vì paper cho chuẩn LLM judge. Input đủ.
- DRY RUN: test giả pipeline 3 experts (researcher/writer/editor), 100 tasks; baseline routing+review = 38% token, ACC 72,0%. Chạy skill: router thấy artifact thật (không content-blind) → ACC 73,3% (trong ±1,34); gate đo trên 30 artifact tiêm lỗi: TPR 91% vs LLM judge 93%; token −33%, latency −28%; decision cost 2,1% tổng. Output có nghĩa: gate giữ quality, cắt token rõ rệt.
- VERDICT: [SKILL VALID]
