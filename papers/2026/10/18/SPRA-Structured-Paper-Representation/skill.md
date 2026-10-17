# Skill: Xây dựng Biểu diễn Bài báo Có Cấu trúc cho Agent (SPRA)

Source: 2610.21424v1
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng hệ thống nghiên cứu AI hoặc agent văn học và cần biểu diễn bài báo có cấu trúc để agent truy vấn, duyệt, và tái sử dụng.
- Bạn muốn giảm chi phí token khi đưa bài báo vào LLM agent so với việc nhập toàn bộ bài báo.
- Bạn cần kết nối phát hiện nghiên cứu với phương pháp, điều kiện, và so sánh giữa các bài báo.

## Tình huống KHÔNG nên dùng
- Bạn chỉ cần lưu trữ văn bản thô của bài báo, không cần truy vấn cấu trúc nghiên cứu.
- Bạn không có dữ liệu bài báo đủ lớn để xây dựng corpus có cấu trúc.

## Input cần có
- Bộ bài báo nghiên cứu đã được phân tích thành Markdown có nhận thức section với các dấu hiệu nguồn.
- Schema JSON quy định vai trò nghiên cứu (Vấn đề, Đóng góp, Thành phần, Thiết lập thí nghiệm, Đo lường, Kết quả) và quan hệ gõ giữa chúng.
- API truy cập programmatic để agent có thể truy vấn các đối tượng nghiên cứu.

## Các bước thực hiện
1. Phân tích bài báo nguồn thành Markdown có nhận thức section với các dấu hiệu nguồn (source markers).
2. Trích xuất các đơn vị nghiên cứu (research units) theo sáu vai trò: Vấn đề, Đóng góp, Thành phần, Thiết lập thí nghiệm, Đo lường, Kết quả.
3. Xây dựng quan hệ nội bộ (part_of, co_contribution, compares_to, evaluates, about, supports, motivates, resolves) giữa các đơn vị.
4. Xây dựng quan hệ trích dẫn (builds_on, uses_component, compares_with) nối bài báo với công trình trước.
5. Gắn vị trí nguồn (source locators) cho mỗi đơn vị và quan hệ để hỗ trợ xác thực.
6. Xuất dữ liệu qua API có cấu trúc (Paper Schema API) để agent truy vấn.

## Output mong đợi
- Một bộ sưu tập bài báo có cấu trúc với các đối tượng nghiên cứu và quan hệ gõ.
- Agent có thể truy vấn, duyệt, và tái sử dụng các đối tượng nghiên cứu cấp bài báo.
- Giảm chi phí token so với việc nhập toàn bộ bài báo vào LLM.
- Nguồn gốc (provenance) có thể xác thực cho mọi đối tượng nghiên cứu.

## Ví dụ áp dụng
Bạn xây dựng agent hỗ trợ nghiên cứu AI. Thay vì để agent đọc toàn bộ bài báo (tốn nhiều token), bạn trích xuất bài báo thành các đối tượng có cấu trúc: Vấn đề (cách tiếp cận hiện tại chưa giải quyết được gì), Đóng góp (bài báo giải quyết gì), Kết quả (điểm số trên benchmark). Agent truy vấn các đối tượng này qua Schema-RAG, kết nối Kết quả của bài báo A với Thiết lập thí nghiệm của bài báo B để so sánh phương pháp. Giảm 95,3% token so với việc nhập toàn bộ bài báo.

## Gotchas
- Điểm Overall trong tác vụ tạo ý tưởng thấp hơn hơi Full Compact (0,067/5), trade-off chất lượng với hiệu quả token.
- Cần bộ dữ liệu bài báo đủ lớn và có chất lượng để xây dựng corpus có cấu trúc.
- Việc trích xuất các đơn vị nghiên cứu cần mô hình hoặc quy trình trích xuất tốt để đảm bảo độ chính xác.