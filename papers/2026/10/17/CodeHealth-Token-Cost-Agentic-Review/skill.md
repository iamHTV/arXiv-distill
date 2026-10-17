# Skill: codehealth-token-cost-prediction
Source: 2610.21914v1
Type: evaluation-method

## Khi nào dùng skill này
- Ước đoán chi phí suy luận (inference cost) của agent review và fix mã nguồn trước khi chạy.
- Có điểm chất lượng code (CodeHealth hoặc tương tự) cho các tệp trong PR.
- Cần dự đoán chi phí token của ống dẫn agent review và fix dựa trên chất lượng code, không chỉ kích thước PR.

## Tình huống KHÔNG nên dùng
- Không có điểm chất lượng code cho các tệp.
- Chỉ cần ước tính chi phí dựa trên kích thước PR (diện tích PR).
- Không có ống dẫn agent review và fix để đo chi phí thực tế.

## Input cần có
- Điểm chất lượng code (CodeHealth, thang 1-10) cho các tệp trong PR.
- Diện tích PR (PR footprint) — kích thước diff, số dòng.
- Thông tin về ngôn ngữ lập trình và kho lưu trữ (repository).
- Ống dẫn agent review và fix để đo chi phí token thực tế (nếu muốn xác thực).

## Các bước thực hiện
1. Thu thập điểm CodeHealth (hoặc chất lượng tương tự) cho mỗi tệp trong PR.
2. Thu thập diện tích PR (kích thước diff, số dòng đã thay đổi).
3. Lắp mô hình hỗn hợp (mixed model) của log tokens trên CodeHealth và log diện tích PR, với một ngẫu nhiên kho lưu trữ (repository random intercept).
4. Hệ số CodeHealth là âm với khoảng tin cậy 95% không bao gồm không — mỗi điểm CodeHealth liên kết với 3.5% đến 6.1% chi phí token thấp hơn.
5. Kiểm tra xem liên kết có do kích thước PR hay không (diện tích PR không liên quan đến CodeHealth cơ bản).
6. Xác định liên kết nằm trong giai đoạn xem xét (review stage) — các agent lặp lại nhiều hơn trên mã nguồn không khỏe.
7. Điều chỉnh cho kích thước các tệp đã chấm điểm — liên kết có thể bị hấp thụ (mediation by file size).

## Output mong đợi
- Ước đoán chi phí token cho agent review và fix dựa trên điểm CodeHealth.
- Mỗi điểm CodeHealth cao hơn liên kết với 3.5% đến 6.1% chi phí token thấp hơn.

## Ví dụ áp dụng
- Đối với một PR có điểm CodeHealth trung bình 4 (thấp), dự kiến chi phí token sẽ cao hơn một PR có điểm CodeHealth 8 (cao) khoảng 14% đến 24% (4 điểm × 3.5% đến 6.1%).

## Gotchas
- Nghiên cứu quan sát tiên nghiệm (pre-registered observational study) — không thể kết luận nhân quả.
- Mỗi PR chỉ chạy một lần.
- Tập trung trên 3 LLM cụ thể.
- Điều chỉnh cho kích thước các tệp đã chấm điểm hấp thụ liên kết — quan hệ có thể do kích thước tệp, không phải chất lượng bản thân.
