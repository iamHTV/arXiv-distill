# [2605.17288v1] When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack

## Problem
Hệ thống cascade LLM (cascade LLMs) được thiết kế để cân bằng giữa hiệu quả và hiệu năng bằng cách xử lý các truy vấn với mô hình nhẹ (lightweight models) và chọn lọc việc thangcao (escalate) các trường hợp phức tạp đến các mô hình mạnh hơn. Hệ thống này tìm cách giảm chi phí tính toán và độ trễ (latency) trong khi duy trì hiệu năng tác vụ, làm cho nó trở thành một lựa chọn hấp dẫn cho việc triển khai quy mô lớn. Tuy nhiên, thiết kế cascade giới thiệu các lỗ hổng mới (vulnerabilities).

## Contribution
- Khám phá rằng hệ thống cascade LLM có thể bị kích hoạt thất bại lan rộng (cascade failure) dưới tấn công đối thủ (adversarial attack).
- Phương pháp tấn công có thể giảm độ chính xác dự đoán (prediction accuracy) lên đến 84.6%, tăng chi phí token chuẩn hóa (normalized token cost) lên 148.9%, và tăng thời gian thực thi (execution time) lên đến 108.9%.
- Trong các kịch bản jailbreak (mở tùy chặt), tấn công tăng tỷ lệ thành công tấn công (attack success rate) lên đến 81.4%.

## Method (tóm cốt lõi)
Nghiên cứu hệ thống cascade LLM dưới tấn công đối thủ. Đo độ chính xác dự đoán, chi phí token, thời gian thực thi, và tỷ lệ thành công tấn công. Thử nghiệm các phương pháp tấn công đối thủ trên các hệ thống cascade khác nhau.

## Key Findings
- Phương pháp tấn công giảm prediction accuracy lên đến 84.6%.
- Tăng normalized token cost lên 148.9%.
- Tăng execution time lên đến 108.9%.
- Tăng attack success rate lên đến 81.4% (trong các kịch bản jailbreak).
- Hệ thống cascade có độ bền kém hơn so với mô hình đơn lẻ trước tấn công đối thủ.

## Actionable Insights
- Không nên tin tưởng hệ thống cascade LLM là an toàn trước tấn công đối thủ: cascade design giới thiệu các lỗ hổng mới. Áp dụng: solopreneur dùng hệ thống cascade LLM nên thêm các cơ chế phòng thủ (defense mechanisms) như input sanitization, output validation, và rate limiting.
- Nên đánh giá độ bền (robustness) của hệ thống cascade trước khi triển khai production. Áp dụng: khi xây hệ thống cascade LLM, hãy thử nghiệm với các tấn công đối thủ để tìm ra các lỗ hổng và khắc phục trước khi đưa ra sản phẩm.

## Assumptions & Limitations
- Điều kiện: có hệ thống cascade LLM và dữ liệu truy vấn thật; không áp dụng nếu chỉ có một mô hình đơn lẻ.
- Paper thừa nhận: đánh giá trên các hệ thống cascade cụ thể; có thể khác trên các hệ thống khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen khác ngoài các tác vụ đã dùng, chưa test chi phí thực tế của các cơ chế phòng thủ.

## Metadata
- Năm: 2026
- Tác giả: Zehan Sun, Dingfan Chen, Songze Li (Southeast University, Max Planck Institute for Intelligent Systems)
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.17288
