# Skill: Validated Agent-Economy Simulation — ledger bảo toàn + ablation ghép hạt giống + kiểm định horizon
Source: 2609.11108v1
Type: evaluation-method

## Khi nào dùng skill này
- Bạn xây dựng simulation (mô phỏng) nhiều LLM agents (tác tử mô hình ngôn ngữ lớn) trong môi trường kinh tế/marketplace (sàn giao dịch) và cần kết quả đáng tin, không phải "hợp lý trên giấy".
- Bạn muốn test một shock (cú sốc: cầu, chuyển tiền, policy — chính sách) và đo nó truyền qua hệ thống thế nào.
- Bạn định report một kết luận "hệ thống ổn định/đóng băng" và cần chắc đó không phải ảo ảnh của thời gian quan sát quá ngắn.

## Tình huống KHÔNG nên dùng
- Task agent đơn lẻ, không có tương tác kinh tế/giao dịch giữa các agents.
- Bạn chỉ cần benchmark accuracy (độ chính xác) per-episode (mỗi tập) — dùng AgentBench/WebArena-style thay thế.

## Input cần có
- Định nghĩa môi trường: agents, nơi giao dịch, công cụ (tools), nguồn tiền vào/ra duy nhất.
- Budget (ngân sách) inference (suy luận) cho nhiều runs (lần chạy) × seeds (hạt giống) × horizon (quãng thời gian).
- Pre-registration (đăng ký trước): conditions, seed list, exclusion rule (quy tắc loại trừ) — commit TRƯỚC khi thu thập dữ liệu.

## Các bước thực hiện
1. Thiết kế closed economy (kinh tế khép kín) với money conservation (bảo toàn tiền tệ) làm invariant (bất biến): ledger (ghi sổ) mọi transaction (giao dịch); tổng tiền hệ thống = tổng ví + số dư ngân hàng của mọi agent tại mỗi pulse (nhịp); tiền chỉ vào/ra qua 2 tài khoản ngoại vi ledger.
2. Chạy 2 validator (bộ kiểm định) độc lập: live validator (TypeScript) + offline recomputation (tính lại offline) bằng ngôn ngữ thứ hai (Python), bao gồm per-agent ledger reconciliation (đối chiếu sổ): Δ số dư agent = tổng signed (có dấu) transactions của chính agent đó.
3. Thiết kế treatment (xử lý) với manipulation check (kiểm định thao tác): xác nhận shock đến đúng (δ = 1.00 separation, p_adj < 0.001) trước khi đo downstream (hậu quả) — null downstream không thể đổ lỗi cho shock yếu.
4. Phân tách response (phản ứng) thành extensive margin (biên độ rộng — bao nhiêu đơn vị tham gia) + intensive margin (biên độ sâu — mỗi đơn vị mạnh cỡ nào); kiểm tra multiplication identity (đẳng thức nhân): 1.504 × 3.067 ≈ 4.62.
5. Matched-seed ablation (loại trừ ghép hạt giống): seeds dùng chung giữa các arm; chạy placebo (placebo — giả dược: layout), no-memory, cross-model; report Δ% (độ thay đổi %) + p (Wilcoxon signed-rank — kiểm định hạng có dấu Wilcoxon).
6. Horizon ladder (thang horizon): chạy ≥3 horizon (ví dụ 2/12/26 tuần); đo persistence ρ (bền vững) + quintile mobility (khả năng di chuyển ngũ phân vị) ở mỗi mức trước khi kết luận "frozen" (đóng băng).
7. Report per-tool failure rate (tỷ lệ thất bại từng công cụ), không chỉ aggregate success rate (tỷ lệ thành công chung); log frequency (tần số) của từng error reason (lý do lỗi).

## Output mong đợi
- Kết quả simulation có audit trail (dấu vết kiểm toán): mọi headline number (con số nổi bật) tính lại được từ raw CSV exports.
- Cơ chế được xác định (ví dụ: truyền dẫn tiền tệ dừng ở firm) với decomposition (phân tách) chính xác + randomized transfer experiment xác nhận chéo.
- Kết luận có ghi horizon đi kèm; dataset (tập dữ liệu) released để reanalysis (phân tích lại).

## Ví dụ áp dụng
Bạn mô phỏng 50 agent khách hàng cho loyalty program (chương trình khách hàng thân thiết): ledger mọi giao dịch điểm thưởng, chạy shock "tặng 5,000 điểm cho 10 agent ngẫu nhiên", đo 96% điểm còn giữ sau 300 pulses → MPC 3–4% → kết luận "khuyến mãi không lưu thông" thay vì "chương trình thành công 96%".

## Gotchas
- Aggregate success rate 96% có thể che 1 class hành động fail 94–100% (paper: invite_to_talk fail 94–97% nhưng economic tools 96% success) — luôn tách per-tool.
- Self-hosted serving quirks (vấn đề đặc thù phục vụ): FP8 KV-cache quantization (lượng tử hóa) gây garbage tokens (6.0% → 3.3% khi tắt); tool-name normalization (chuẩn hóa tên công cụ) cứu 16–35% actions — hãy replay recorded production requests (yêu cầu production đã ghi) khi probe (dò) độ tin cậy.
- Pre-commit exclusion rule (quy tắc loại trừ) trước khi thu thập: paper loại 1 run theo pre-committed 3σ floor dù nó chạy xong — rule (quy tắc) quyết định, không phải analyst (người phân tích).
- Null result (kết quả null) với 6 seeds = "chưa phát hiện", KHÔNG phải "không có effect" (paper: memory null underpowered).
