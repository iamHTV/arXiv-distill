# Skill: ceo-arena-multi-agent-business-competition
Source: 2609.34821v1
Type: evaluation-method

## Khi nào dùng skill này
- Đánh giá agent quản lý kinh doanh (giá, marketing, R&D) trong môi trường cạnh tranh dài hạn.
- Muốn biết tác động của agent đối với đối thủ và toàn thị trường, không chỉ lợi nhuận agent riêng lẻ.
- Có thể mô phỏng thị trường với nhiều công ty đối thủ.

## Tình huống KHÔNG nên dùng
- Đánh giá agent đơn lẻ không có đối thủ cạnh tranh.
- Không thể mô phỏng điều kiện thị trường giống hệt để so sánh thay thế.

## Input cần có
- Môi trường mô phỏng kinh doanh (giá, sản lượng, marketing, R&D, kho hàng).
- Nhiều CEO-agent LLM có thể được định cấu hình.
- Thời gian mô phỏng dài (ví dụ 500 ngày) để thấy tác động dài hạn.

## Các bước thực hiện
1. Thiết lập mô phỏng thị trường với N công ty, mỗi công ty do một CEO-agent quản lý.
2. Chạy mô phỏng trong khoảng thời gian dài (ví dụ 500 ngày), mỗi agent ra quyết định giá, marketing, R&D.
3. Áp dụng matched replacement evaluation: thay thế một agent bằng agent khác trong cùng điều kiện thị trường, đo sự thay đổi của operating return và tác động đến đối thủ/thị trường.
4. So sánh win rate và operating return của các agent trên cùng điều kiện.
5. Phân tích xem agent có private gain nhưng gây market loss hay không.

## Output mong đợi
- Win rate và operating return của từng CEO-agent trên cùng điều kiện thị trường.
- Nhận biết agent có lợi nhuận cá nhân nhưng gây thiệt hại cho thị trường (market loss).

## Ví dụ áp dụng
Solopreneur dùng agent quản lý giá cho cửa hàng online: thay vì chỉ đoán lợi nhuận của agent, hãy mô phỏng thị trường với các đối thủ và thay thế agent quản lý giá bằng một chiến lược khác trong cùng điều kiện, xem tác động đến doanh thu toàn thị trường.

## Gotchas
- Nhiều agent có private gain nhưng gây market loss (thất suất thị trường) — không chỉ đoán lợi nhuận agent riêng lẻ.
- Matched replacement evaluation yêu cầu điều kiện thị trường giống hệt, khó triển khai trên production thực tế.
- Horizon 500 ngày có thể chưa đủ để thấy tác động dài hạn hoàn toàn.
