# Skill: unimaso-prompt-model-optimization
Source: 2610.31743v2
Type: optimization-method

## Khi nào dùng skill này
- Có hệ thống đa agent LLM với nhiều vai trò khác nhau và muốn tối ưu hóa trade-off chất lượng–chi phí.
- Muốn gán model phù hợp với yêu cầu của mỗi vai trò thay vì dùng model mạnh nhất cho mọi agent.
- Muốn tối ưu hóa chung prompt và model assignment thay vì tối ưu hóa prompt với model cố định.

## Tình huống KHÔNG nên dùng
- Hệ thống chỉ có một agent đơn lẻ.
- Tất cả agent đều có cùng yêu cầu về khả năng (không cần phân biệt model).

## Input cần có
- Hệ thống đa agent dưới dạng đồ thị có hướng G = (V, E) với topologi thực thi.
- Không gian prompt Pi cho mỗi agent vi và nhóm mô hình đồng chất M = {m(1), ..., m(K)}.
- Bộ dữ liệu xác thực D = {(xj, yj)} để đánh giá chất lượng tác vụ.
- Hệ số chi phí mô hình (model-cost coefficients) từ bảng giá nhà cung cấp.

## Các bước thực hiện
1. Mô hình hóa hệ thống N agent dưới dạng đồ thị có hướng: mỗi agent vi có prompt pi ∈ Pi và mô hình mi ∈ M, ghi nhãn zi = (pi, mi).
2. Sinh ứng viên từ quỹ đạo thực thi: lấy mẫu quỹ đạo chứa đầu vào, bối cảnh, đầu ra, và phản hồi; đề xuất ứng viên từ cấu hình hiện tại.
3. Đánh giá ứng viên ở ba phân cấp: độ hợp lệ cục bộ, tiện ích nhìn về trước, sự khớp toàn cục. Công thức tiện ích: Ui(p') = α·qloc_i(p') + β·qlook_i(p') + γ·qglob_i(p'), α + β + γ = 1.
4. Áp dụng tìm kiếm beam có ý thức chi phí: mở rộng ứng viên khi Ui(p')·ηi(p')−λ > uref (λ = 0.2, uref = 0.5). Giữ các ứng viên không bị thống trị về chất lượng–chi phí.
5. Mở rộng ứng viên thành cặp prompt–model z'i = (p'i, m'i). Tìm cập nhật tốt nhất cục bộ ¯zi = (¯pi, ¯mi).
6. Điều phối hệ thống theo topologi: tạo quan điểm tiêu điểm cho mỗi agent logic, đoán hỗ trợ thực nghiệm và trọng số theo độ tập trung: Ai(m) = πi(m)(1 − H̄i). Giải quyết cấu hình dưới ràng buộc khả năng và cân bằng khả năng–chi phí.
7. Lưu quỹ đạo tối ưu hóa: ξt = (zt, at, qt, Ct, bt). Gom thành thành công toàn cục chi phí thấp, thành công cục bộ–thất bại toàn cục, thành công toàn cục chi phí cao. Truy xuất cân bằng theo loại (Kmem = 2 mỗi loại).
8. Chạy 3 vòng tối ưu hóa với độ tìm kiếm 3–2–2; đánh giá cấu hình được chọn trên toàn bộ tập đánh giá.

## Output mong đợi
- Cấu hình prompt–model tối ưu cho mỗi agent trong hệ thống.
- Điểm chất lượng tác vụ và chi phí triển khai (token-weighted deployment cost).
- Phân phối model theo vai trò (ví dụ: Qwen3.5-9B cho structured/summarization, DeepSeek-V4-Flash cho reasoning/verification).

## Ví dụ áp dụng
Công ty có hệ thống đa agent chăm sóc khách hàng với vai trò: Planner (lập kế hoạch), Reasoner (suy luận), Reviewer (xem xét), Aggregator (tổng hợp). Hiện tại mọi agent đều dùng DeepSeek-V4-Pro (chi phí cao). Áp dụng UniMASO: tối ưu hóa chung prompt và model assignment. Kết quả: Planner dùng Qwen3.5-9B (43.5% structured/summarization), Reasoner dùng DeepSeek-V4-Flash (45.5% reasoning/verification). Điểm trung bình 70.40 (tăng 0.61), chi phí giảm 85.2% (30.92M vs 208.28M).

## Gotchas
- Tối ưu hóa chung prompt và model phức tạp hơn tối ưu hóa tuần tự (prompt trước, model sau).
- Cần bộ dữ liệu xác thực để đánh giá chất lượng tác vụ.
- Chi phí tối ưu hóa (meta-optimization) có thể đáng kể — cần cân bằng với chi phí triển khai.
- Kết quả phụ thuộc vào nhóm mô hình có sẵn và topologi thực thi.
- Trajectory memory cần được lưu trữ và truy xuất đúng cách để tái sử dụng kinh nghiệm.