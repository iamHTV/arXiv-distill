# Skill: iterate-on-llm-serve-on-slm
Source: 2610.14576v1
Type: workflow

## Khi nào dùng skill này
- Có 1 tác vụ agent hẹp, lặp lại (ví dụ: phân loại yes/no, xác định caregiver cho ca làm việc) cần chạy hàng ngàn lần/ngày.
- Hành vi mong muốn còn đang thay đổi và cần lặp lại nhanh (nhiều lần/ngày) trước khi ổn định.
- Có frontend đã chạy trên frontier model (mô hình ranh giới/tiền tiến) và có thể ghi lại toàn bộ trace (dòng vết thực thi) production.

## Tình huống KHÔNG nên dùng
- Hành vi thay đổi liên tục mỗi giờ, chưa tới giai đoạn hội tụ (converge).
- Tác vụ cần reasoning rộng mở (open-ended reasoning), không phải quyết định hẹp.

## Input cần có
- 1 frontier model đã triển khai để chạy tác vụ trong giai đoạn phát triển.
- Hệ thống ghi lại mọi production trace (prompt + tool call đã thực hiện).
- Công cụ prompt builder + serializer tương đồng với live evaluator để replay byte-exact.
- 1 SLM candidate (ví dụ: Qwen3-8B) và công cụ LoRA-tune (tinh chỉnh cấp thấp).
- 1 chuyên gia/domain expert để đánh giá mù (blinded evaluation) khi có bất đồng giữa SLM và teacher.

## Các bước thực hiện
1. Chạy agent trên frontier model trong production, thu thập mọi trace và phản hồi live traffic; thay đổi prompt nhanh cho đến khi hành vi ổn định (giai đoạn 1).
2. Khi hành vi đã hội tụ, replay (phát lại byte-exact) từng batch đã ghi lại bằng cùng prompt builder và serializer mà live evaluator dùng, tạo ngữ cảnh chat giống như lúc phục vụ thực tế.
3. Ghép mỗi ngữ cảnh đã replay với tool call đã ghi lại làm target (mục tiêu) huấn luyện.
4. Áp dụng contract filtering (lọc theo hợp đồng): loại mẫu training có reasoning thiếu lý do xung đột cứng (hard-conflict justification); deduplicate (loại trùng), giữ quyết định mới nhất; chia train/validation theo source batch.
5. LoRA-tune SLM trên corpus train đã lọc (ví dụ: Qwen3-8B, khoảng 1.023 optimizer steps, khoảng 1B token, context 65,536).
6. Đánh giá SLM trên tập validation: tính agreement với các quyết định đã ghi lại, so với noise floor của teacher (tự đồng ý của teacher trên các prompt riêng lẻ).
7. Nếu SLM vượt noise floor và vượt đánh giá mù bởi chuyên gia, triển khai SLM phục vụ production (giai đoạn 2).

## Output mong đợi
- 1 SLM đã được tinh chỉnh (fine-tuned) chạy tác vụ hẹp với agreement cao hơn teacher, chi phí và độ trễ thấp hơn đáng kể, và được chuyên gia đánh giá là chính xác hơn.

## Ví dụ áp dụng
- Home-care agency: agent đưa quyết định yes/no cho từng caregiver-shift pair, lên đến 1.000 quyết định mỗi lượt outreach. Sau khi hành vi ổn định trên GPT-5.4-nano, distill 11.621 quyết định production vào Qwen3-8B qua LoRA → đạt 0.913 agreement, latency 2.9s p50, chi phí ~$0.28 trên 1.000 quyết định.

## Gotchas
- Không distill quá sớm trước khi hành vi ổn định — SLM sẽ học được hành vi đang thay đổi, phải retraining lại.
- Không dùng dữ liệu tổng hợp (synthetic data) làm target — phải dùng production trace thực để có edge case thực tế.
- Base SLM zero-shot có thể ra malformed output (kết quả sai định dạng) lên đến 23% — không chạy production mà không fine-tune.
- Noise floor của teacher chỉ 72.7% — đừng mong SLM đạt 100% agreement với teacher, mục tiêu là vượt mức nhất quán tự nhiên của teacher.
- Mọi số liệu ở trên là offline replay; cần online A/B test trước khi khẳng định chi phí và độ chính xác trong production thực sự.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 7 bước trên không? [YES] — từng bước là action cụ thể, không cần bối cảnh paper.
- Bước nào mơ hồ nhất? Bước 2 (replay byte-exact) cần hiểu rõ prompt builder/serializer của hệ thống hiện có.
- Input section có đủ không? [YES] — đủ frontier model, trace storage, replay tool, SLM, LoRA, chuyên gia đánh giá.

## Dry run (tình huống giả)
- Tình huống: Solopreneur muốn phân loại tin nhắn khách hàng thành "cần trả lời ngay" vs "có thể đợi" trên 5.000 tin/ngày.
- Chạy skill: (1) Dùng GPT-5.4-nano để phân loại, thu trace từ 2 tuần chạy thật; (2) Thay đổi prompt dựa trên phản hồi khách hàng ngay khi thấy sai; (3) Sau 2 tuần hành vi ổn định, replay 10.000 trace đã ghi lại; (4) Lọc bỏ mẫu không có lý do rõ ràng; (5) LoRA-tune Qwen3-8B trên 8.000 mẫu còn lại; (6) Đánh giá trên 2.000 mẫu validation, so với teacher self-agreement; (7) Nếu SLM vượt teacher và chuyên gia phê SLM nhiều hơn khi có bất đồng → triển khai SLM thay GPT-5.4-nano, giảm chi phí xuống ~1/10.

## Verdict: [SKILL VALID]
