# Skill: storebench-live-commerce-evaluation
Source: 2610.10942v1
Type: framework

## Khi nào dùng skill này
- Đánh giá agent thương mại điện tử (e-commerce agent) trong môi trường mô phỏng live-commerce (live-commerce environment).
- Cần đánh giá agent dưới sự không chắc chắn (uncertainty): khách hàng đặt hàng liên tục, nhà cung cấp thay đổi giá và thất bại, chấn đoạn thị trường.
- Muốn đánh giá sự ổn định dài hạn (long-horizon stability) và phán quyết kinh tế (economic judgment) của agent.

## Tình huống KHÔNG nên dùng
- Đánh giá agent trên tác vụ có biên (bounded tasks) đơn lẻ.
- Không có môi trường mô phỏng thương mại điện tử (live-commerce environment).
- Không cần đánh giá sự ổn định dài hạn (long-horizon stability).

## Input cần có
- Môi trường thương mại điện tử (live-commerce environment) với cửa hàng áo phông (online apparel store).
- 29 công cụ bán hàng (merchant tools) qua Model Context Protocol.
- Khách hàng đặt hàng liên tục (around the clock), nhà cung cấp thay đổi giá và thất bại, chấn đoạn thị trường (market shocks).
- Ngân sách thao tác cửa sổ (windowed operation budget).
- Các tác vụ (scenarios) từ 30 đến 45 ngày và một năm mô phỏng đầy đủ (full simulated year).

## Các bước thực hiện
1. Xây dựng môi trường thương mại điện tử trực tuyến (live-commerce environment) với cửa hàng áo phông trung bình (mid-size online apparel store) trên nền tảng thương mại cấp doanh nghiệp (production-grade commerce backend).
2. Thiết lập 29 công cụ bán hàng (merchant tools) qua Model Context Protocol.
3. Thiết lập khách hàng đặt hàng liên tục (around the clock), nhà cung cấp thay đổi giá và thất bại, chấn đoạn thị trường (market shocks).
4. Thiết lập ngân sách thao tác cửa sổ (windowed operation budget) để thời gian mô phỏng (simulated time) là hàm của các hành động (actions).
5. Đánh giá agent trên 11 kịch bản (scenarios) từ 30 đến 45 ngày và một năm mô phỏng đầy đủ (full simulated year).
6. Sử dụng ngưỡng vượt qua (pass thresholds) được chuẩn hóa (calibrated) dựa trên chính sách trick脚本 (scripted anchor policies).
7. Sử dụng phần thưởng (reward) được làm cứng (hardened) chống lại các lỗ hổng thưởng (reward hacks).
8. Mọi phiên (episode) phát lại giống hệt nhau sau một chuỗi hành động (sequence of actions) nhất định.

## Output mong đợi
- Agent đánh giá trên môi trường thương mại điện tử trực tuyến (live-commerce environment).
- Điểm tổng hợp (composite score) của agent so với con người (human experts) và chính sách trick脚本 (scripted smart-triage policy).
- Model tốt nhất đạt 49% so với heuristic 97%; con người đạt 0.708 vs model 0.700.

## Ví dụ áp dụng
- Xây dựng agent thương mại điện tử (e-commerce agent): dùng môi trường mô phỏng StoreBench để đánh giá agent dưới sự không chắc chắn, với khách hàng đặt hàng liên tục, nhà cung cấp thay đổi giá và thất bại, chấn đoạn thị trường. Đánh giá agent dựa trên điểm tổng hợp (composite score) so với con người và chính sách trick脚本 (scripted smart-triage policy).

## Gotchas
- Đánh giá trên một cửa hàng áo phông đơn lẻ (single apparel business) với đối thủ được viết kịch bản (scripted competitors) và nhu cầu tham số (parametric demand).
- Môi trường (engine) bị giữ kín (withheld) để giữ bộ đánh giá không bị ô nhiễm (uncontaminated).
- Đào tạo hậu kỳ (post-training) dùng một mô hình cơ sở (base model) và một lần chạy (one run).
