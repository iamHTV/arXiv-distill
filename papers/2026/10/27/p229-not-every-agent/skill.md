# Skill: unimaso-prompt-model-optimization

Source: 2610.31743
Type: framework

## Khi nào dùng skill này

- Xây dựng hệ thống multi-agent LLM với nhiều agent có vai trò khác nhau.
- Muốn giảm chi phí suy luận mà không hy sinh chất lượng tác vụ.
- Có thể đo đạc chi phí suy luận của từng mô hình và hiệu suất tác vụ.

## Tình huống KHÔNG nên dùng

- Hệ thống chỉ có một agent.
- Tất cả agent đều cần cùng mức độ năng lực suy luận.

## Input cần có

- Danh sách các agent và vai trò trong hệ thống multi-agent.
- Không gian mô hình có sẵn (model pool) với các mức năng lực khác nhau.
- Bộ dữ liệu đánh giá tác vụ và công cụ đo chi phí suy luận.

## Các bước thực hiện

1. Phân loại agent theo vai trò và yêu cầu suy luận: Xác định哪些 agent cần suy luận sâu và哪些 agent chỉ cần xử lý định dạng.
2. Thiết lập không gian tìm kiếm chứa các cặp (prompt, mô hình) cho mỗi vai trò agent.
3. Dùng tìm kiếm Pareto có nhận thức chi phí (cost-aware Pareto search) để tìm các trade-off chất lượng–chi phí hữu ích.
4. Đánh giá ứng viên qua phản hồi đa cấp: cục bộ, tiếp cận và toàn cầu.
5. Điều phối cập nhật theo cấu trúc liên lạc (topology-aware co-evolution) dựa trên vai trò agent và phụ thuộc.
6. Lưu trữ thành công và thất bại vào bộ nhớ quỹ đạo crosses cấp (cross-level trajectory memory) để hướng dẫn vòng tiếp theo.
7. Áp dụng phân bổ mô hình và prompt tối ưu cho mỗi vai trò agent.

## Output mong đợi

- Phân bổ mô hình tối ưu cho mỗi vai trò agent.
- Prompt tối ưu cho mỗi vai trò agent.
- Các trade-off chất lượng–chi phí được xác định.
- Giảm chi phí triển khai so với cấu trúc đồng nhất dùng mô hình mạnh nhất.

## Ví dụ áp dụng

Đội xây dựng hệ thống agent chăm sóc khách hàng: agent xử lý câu hỏi thường dùng dùng mô hình nhỏ (rẻ), agent xử lý khiếu nại phức tạp dùng mô hình lớn. Dùng UniMASO để tối ưu hóa đồng thời prompt và mô hình cho mỗi vai trò, giảm chi phí triển khai 85,2% so với dùng mô hình mạnh nhất cho mọi agent trong khi duy trì chất lượng tương đương.

## Gotchas

- Không phải mọi agent đều cần mô hình mạnh nhất.
- Tối ưu hóa prompt riêng rẽ bỏ qua sự tương tác giữa prompt và mô hình.
- Cần cân nhắc cả chất lượng và chi phí, không chỉ chất lượng.
- Bộ nhớ quỹ đạo crosses cấp giúp tránh lặp lại các thất bại trong quá trình tối ưu hóa.