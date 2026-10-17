# Skill: scalable-multi-task-irl
Source: 2610.00758v1
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống multi-task inverse reinforcement learning trong cùng một môi trường.
- Cần học từ nhiều tác vụ liên quan trong cùng một môi trường dưới giả định thấp-rank.
- Muốn chuyển giao (transfer) đến môi trường đích với sự hối hận thấp hơn các phương pháp cơ sở.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ đơn lẻ không liên quan.
- Không có dữ liệu từ nhiều tác vụ liên quan trong cùng một môi trường.
- Không cần chuyển giao đến môi trường đích.

## Input cần có
- Dữ liệu từ nhiều agent với phần thưởng khác nhau trong cùng một môi trường.
- Giả định thấp-rank (low-rank assumption) cho các tác vụ liên quan.

## Các bước thực hiện
1. Tập hợp dữ liệu từ nhiều agent với phần thưởng khác nhau trong cùng một môi trường.
2. Áp dụng giả định thấp-rank để học biểu diễn chung-cross-task của đầu vào của nhiệm vụ (trong ngữ cảnh này, sở thích của agent).
3. Học phần thưởng cho từng tác vụ từ dữ liệu đã gộp.
4. Chuyển giao đến môi trường đích với sự hối hận thấp hơn các phương pháp cơ sở.
5. Giám sát sự hối hận và chi phí tính toán.

## Output mong đợi
- Hệ thống multi-task inverse reinforcement learning có khả năng học từ nhiều tác vụ liên quan trong cùng một môi trường.
- Mạnh mẽ với sự phủ thất hạn chế (limited coverage).
- Chuyển giao đến môi trường đích với sự hối hận thấp hơn các phương pháp cơ sở.
- Lợi thế tính toán so với các phương pháp cho từng tác vụ (per-task methods) mở rộng hơn khi số tác vụ tăng.

## Ví dụ áp dụng
- Xây dựng hệ thống inverse reinforcement learning để học từ nhiều tác vụ liên quan trong cùng một môi trường (ví dụ: gợi ý sản phẩm cho nhiều khách hàng khác nhau nhưng trong cùng một nền tảng thương mại điện tử). Dùng giả định thấp-rank để học cách đại diện chung-cross-task của đầu vào của nhiệm vụ (trong ngữ cảnh này, sở thích của khách hàng).

## Gotchas
- Đánh giá trên các tác vụ liên quan với cùng một môi trường dưới giả định thấp-rank.
- Không có thông tin chi tiết về thời gian đào tạo và chi phí tính toán.
