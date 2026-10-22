# Skill: Chọn kỹ thuật nhắc dựa trên đặc điểm nhiệm vụ (prompt selection)
Source: 2610.24913
Type: workflow

## Khi nào dùng skill này
- Cần chọn kỹ thuật nhắc cho hệ thống LLM trên một domain cụ thể.
- Có dữ liệu đánh giá đại diện cho nhiệm vụ mục tiêu.
- KHÔNG dùng khi coi kỹ thuật nhắc phức tạp hơn luôn tốt hơn mà không đánh giá thực nghiệm.

## Input cần có
- Tập dữ liệu đánh giá đại diện cho nhiệm vụ thực tế.
- Mô hình LLM (ví dụ GPT-4o-mini).
- Các kỹ thuật nhắc ứng viên: Zero-Shot, Few-Shot, RAG, PE2.
- Nhóm ví dụ theo nhiệm vụ (100–300 ví dụ).

## Các bước thực hiện
1. Chạy thử nghiệm nhỏ trên tập dữ liệu đại diện với các kỹ thuật Zero-Shot, Few-Shot (100/200/300 ví dụ), RAG (nhóm ví dụ 100/200/300, truy xuất k=5), và PE2.
2. Đo accuracy trên mỗi kỹ thuật và cấu hình.
3. So sánh cấu hình cao nhất và thứ hai bằng kiểm định statiscally (McNemar test, điều chỉnh Holm).
4. Chọn kỹ thuật đạt kết quả tốt nhất trên nhiệm vụ mục tiêu thay vì chọn mặc định dựa trên độ phức tạp.
5. Với nhiệm vụ lý tính có cấu trúc, ưu tiên RAG với nhóm ví dụ lớn hơn (tối đa 300).

## Output mong đợi
- Kỹ thuật nhắc phù hợp nhất cho nhiệm vụ mục tiêu.
- Hiểu rõ sự phụ thuộc vào domain và nhiệm vụ (không có kỹ thuật nào tối ưu hóa rộng rãi).

## Ví dụ áp dụng
- Hệ thống trả lời câu hỏi doanh nghiệp: chạy thử nghiệm nhỏ trên tập câu hỏi thực tế với Zero-Shot, Few-Shot, RAG, chọn kỹ thuật đạt accuracy cao nhất thay vì mặc định dùng Few-Shot 300 ví dụ.

## Gotchas
- Không có kỹ thuật nhắc nào vượt trội trên tất cả domain; không có sai số statiscally significant giữa cấu hình cao nhất và thứ hai.
- Tăng số lượng ví dụ không nhất quán cải thiện hiệu suất.
- Kết quả chỉ đối với GPT-4o-mini, có thể không chuyển giao sang mô hình khác.