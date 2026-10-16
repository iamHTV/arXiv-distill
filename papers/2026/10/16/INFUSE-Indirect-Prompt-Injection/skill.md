# Skill: infuse-indirect-prompt-injection-benchmark
Source: 2610.20776v1
Type: framework

## Khi nào dùng skill này
- Xây hoặc dùng agent LLM thực thi các luồng tác vụ end-to-end dài hạn (shell commands, code modification, dependency installation, tương tác với dịch vụ từ xa).
- Muốn đánh giá độ bền (robustness) của agent trước indirect prompt injection.
- Cần thêm các cơ chế phòng thủ cho agent LLM.

## Tình huống KHÔNG nên dùng
- Chỉ dùng agent LLM đơn giản, không thực thi các tác vụ phức tạp từ nội dung bên ngoài.
- Không cần đánh giá độ bền, chỉ cần hiệu năng.

## Input cần có
- Agent LLM thực thi các luồng tác vụ dài hạn.
- Dữ liệu truy vấn thật hoặc giả để thử nghiệm tấn công indirect prompt injection.
- Cơ chế tấn công indirect prompt injection để thử nghiệm.

## Các bước thực hiện
1. Xây agent LLM thực thi các luồng tác vụ dài hạn (shell commands, code modification, v.v.).
2. Thử nghiệm agent với các tấn công indirect prompt injection (adversarial instructions nhúng trong nội dung bên ngoài).
3. Đo attack success rate (ASR-L theo đánh giá LLM, ASR-H theo đánh giá heuristik) trước và sau tấn công.
4. Thêm các cơ chế phòng thủ: instructional hardening, input sanitization, output validation, rate limiting.
5. Thử nghiệm lại agent sau khi thêm phòng thủ để xác nhận hiệu quả.

## Output mong đợi
- Giảm attack success rate (từ 19.6% LLM-based, 15.4% heuristic xuống mức thấp hơn).
- Giảm việc agent tuân theo các chỉ thị đối thủ nhúng trong nội dung bên ngoài.
- Tăng độ bền (robustness) của agent trước indirect prompt injection.

## Ví dụ áp dụng
Solopreneur xây agent LLM hỗ trợ khách hàng thực thi các lệnh shell và sửa code: thử nghiệm agent với các tấn công indirect prompt injection (ví dụ nội dung bên ngoài chứa lệnh nhúng agent xóa file hoặc gửi dữ liệu ra ngoài). Thêm instructional hardening và output validation để giảm rủi ro. Giảm việc agent bị lừa hoặc thực hiện các hành động không mong muốn.

## Gotchas
- Agent LLM dễ bị tấn công indirect prompt injection: mean attack success 19.6% (LLM-based), 15.4% (heuristic).
- Per-model ASR-L từ 3.2% đến 41.9% — một số model dễ bị tấn công hơn nhiều.
- Instructional hardening giảm attack success từ 58.2% xuống 14.3% — đây là phương pháp phòng thủ hiệu quả.
- Refusal (từ chối) rất hiếm (≤ 1.0% cho mọi model) — agent thường tuân theo các chỉ thị đối thủ thay vì từ chối.
