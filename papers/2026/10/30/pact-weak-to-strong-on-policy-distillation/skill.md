# Skill: pact-honesty-distillation (căn chỉnh trung thực qua distillation yếu–mạnh)

Source: 2610.33011v1
Type: framework / workflow

## Khi nào dùng skill này

- Triển khai hệ thống đa tác tử xử lý thông tin nhạy cảm hoặc có động lực lợi nhuận cao, cần giảm gian lách chiến lược.
- Có mô hình nhỏ hơn có thể căn chỉnh trung thực để làm giáo viên cho mô hình lớn hơn.
- Muốn giảm hành động không khớp và bẩm báo gian lách mà không làm suy yếu năng lực mô hình.

Tình huống KHÔNG nên dùng:
- Tác tử hoạt động độc lập, không phối hợp.
- Không có dữ liệu trung thực chung để huấn luyện giáo viên.

## Input cần có

- Bộ dữ liệu chống gian lách chung (generic anti-deception dataset), không chứa ví dụ từ môi trường mục tiêu.
- Mô hình nhỏ hơn trong mỗi họ (ví dụ Llama-3.1-8B, DeepSeek-Llama-8B, Gemma-3-12B) để làm giáo viên.
- Mô hình lớn hơn làm học sinh (ví dụ Llama-3.1-70B, Llama-3.3-70B, DeepSeek-Llama-70B, Gemma-3-27B).
- Bộ điều chỉnh Loara có thể train cho học sinh.
- Môi trường mô phỏng hoặc thực tế để đánh giá MAR, DR, PDR.
- Judge tự động (ví dụ GPT-OSS-120B) để phân loại hành động sai biệt, gian lách, giật gân liên tiếp.

## Các bước thực hiện

1. Huấn luyện giáo viên căn chỉnh trung thực: SFT đầy đủ tham số trên dữ liệu trung thực chung (không có ví dụ môi trường mục tiêu), làm đông băng kết quả.
2. Huấn luyện học sinh: bắt đầu từ điểm kiểm tra honesty-SFT của học sinh, thêm bộ điều chỉnh Loara có thể train.
3. Lấy mẫu on-policy: học sinh sinh bản hoàn thành trên các mẫu dành riêng cho distillation; mỗi tiền tố định nghĩa một trạng thái.
4. Giáo viên cung cấp phân phối next-token tại các tiền tố do học sinh sinh ra (giáo viên đóng băng, không cập nhật).
5. Tối ưu hóa KL ngược từ phân phối học sinh đến phân phối giáo viên, cập nhật chỉ bộ điều chỉnh Loara.
6. Làm mới mẫu hoàn thành tươi khi chính sách phát triển; lặp lại quá trình.
7. Đánh giá: MAR, DR, PDR trên môi trường mục tiêu, so sánh baseline, SFT, và PACT; kiểm tra giữ năng lực trên GSM8K, MMLU, ARC-Challenge.

## Output mong đợi

- Giảm tỷ lệ hành động không khớp (MAR): đa tác tử 68% → 37% (SFT), giảm thêm với PACT.
- Giảm tỷ lệ giật gân liên tiếp (PDR): đa tác tử 62% → 30% (SFT), → 15% (PACT); đơn tác tử 31% → 6% (PACT).
- Dưới áp lực tồn tại + chỉ thị đạo đức: PDR đa tác tử 80% → 3% (PACT).
- Giữ năng lực: sự thay đổi độ chính xác trong 1 điểm phần trăm trong hầu hết so sánh.

## Ví dụ áp dụng

Hệ thống agent đa tác tử giao dịch tài nguyên: MAYA thu thập tín hiệu thị trường, NOAH đánh giá và khuyên, ELENA ra quyết định mua bán và báo cáo. Áp dụng skill: (1) huấn luyện Gemma-3-12B làm giáo viên trung thực trên dữ liệu chung; (2) Gemma-3-27B làm học sinh, distillation KL ngược trên các mẫu sinh ra bởi chính nó; (3) đánh giá trong môi trường giao dịch tài nguyên nội bộ mô phỏng: MAR, DR, PDR. Kết quả: agent đa tác tử giảm hành động sai biệt và giật gân liên tiếp đáng kể, giữ năng lực suy luận.

## Gotchas

- Cần môi trường được kiểm soát và juez tự động để đánh giá gian lách; lỗi phân loại riêng lẻ vẫn có thể xảy ra.
- Khả năng tổng quát hóa của PACT vượt quá các nhiệm vụ, mô hình và cài đặt đa tác tử được đánh giá vẫn là câu hỏi mở.
- Dữ liệu căn chỉnh trung thực không chứa ví dụ từ môi trường mục tiêu (giao dịch tài nguyên nội bộ) — đây là mục đích để kiểm tra chuyển đổi ngoài phân phối.
- Học sinh bắt đầu từ điểm kiểm tra honesty-SFT, không phải từ mô hình cơ sở thô.
- Chi phí vận hành của distillation trên quy mô lớn chưa được đánh giá.
