# Skill: intuitive-prompting-agent-simulation
Source: 2609.30563v1
Type: framework

## Khi nào dùng skill này
- Xây dựng agent mô phỏng phản hồi của người dùng cụ thể trên mạng xã hội (social media simulation).
- Cần đánh giá độ trung tín (fidelity) của agent so với phản ứng thực tế của người dùng.
- Có thể thu thập hồ sơ người dùng giàu (rich profile): questionnaire, phỏng vấn sâu, bản trình bày bản thân.

## Tình huống KHÔNG nên dùng
- Mô phỏng phản hồi của dân số chung (population-level) thay vì cá nhân cụ thể.
- Không có dữ liệu hồ sơ chi tiết về người dùng mục tiêu.
- Chỉ cần ước tính tổng thể, không quan tâm đến sự khác biệt cá nhân (individual differences).

## Input cần có
- Hồ sơ người dùng: questionnaire (đặc điểm dân số, niềm tin, giá trị, hoạt động, vị trí chính trị), phỏng vấn sâu (transcript), bản trình bày bản thân tự viết (free-text self-presentation).
- Bộ bài viết mạng xã hội để agent phản hồi (like/dislike).
- ít nhất một LLM để sinh phản hồi.
- Thước đo độ trung tín (fidelity metric, ví dụ: Matthews correlation coefficient).

## Các bước thực hiện
1. Profil người dùng: thu thập questionnaire, phỏng vấn sâu, và bản trình bày bản thân tự viết từ từng người dùng mục tiêu.
2. Xây dựng bộ bài viết mạng xã hội (stimulus set), bao gồm cả bài về chủ đề được bao gồm trong hồ sơ và chủ đề chưa được bao gồm (out-of-domain).
3. Tạo năm điều kiện nhắc nhở (prompt conditions): V4 demographics (thông tin nhân khẩu học cơ bản), V3 questionnaire (thêm toàn bộ câu trả lời questionnaire), V1 interview (thêm transcripts phỏng vấn và bản trình bày bản thân — hồ sơ giàu nhất), V2 inference (nội dung như V1 cộng với hướng dẫn suy luận phản ứng từ sự kết hợp các đặc điểm), V5 intuitive (nội dung như V1 nhưng hướng dẫn phản hồi ngay lập tức thay vì phân tích thiết analy).
4. Chạy mỗi mô hình dưới mỗi điều kiện nhắc nhở trên từng hồ sơ người dùng, thu thập phản hồi like/dislike cho tất cả bài viết.
5. Đánh giá độ trung tín (fidelity) bằng cách so sánh phản hồi của agent với phản ứng thực tế của người dùng, dùng Matthews correlation coefficient (MCC) làm thước đo chính.
6. Đo nén các khác biệt cá nhân (compression of individual differences) bằng độ lệch chuẩn giữa các người dùng.
7. So sánh các điều kiện nhắc nhở để xác định điều kiện nào cho độ trung tín cao nhất.

## Output mong đợi
- Agent mô phỏng phản hồi người dùng với độ trung tín cao nhất dưới điều kiện intuitive prompting (MCC lên đến 0.473 so với 0.300 cho demographics đơn thuần).
- Giảm nén các khác biệt cá nhân từ 10.24× (demographics) xuống 3.14× (intuitive), gần mức con người (1.00×).

## Ví dụ áp dụng
- Xây dựng agent mô phỏng phản hồi của khách hàng đối với các bài đăng mạng xã hội về sản phẩm mới: thu thập hồ sơ khách hàng qua questionnaire và phỏng vấn, dùng điều kiện intuitive prompting (hướng dẫn agent phản hồi ngay lập tức, không cân nhắc các đặc điểm lẫn nhau), đánh giá độ trung tín bằng MCC so với phản ứng thực tế của khách hàng.

## Gotchas
- Chỉ 8 người tham gia, tất cả ở Serbia; kết quả có thể không chuyển tiếp đến dân số khác.
- Các mô hình được biết đến đại diện cho công chúng phương Tây giàu có chính xác hơn, nên hiệu suất có thể bị sott-estimate ở nơi khác.
- Mỗi cấu hình chỉ chạy một lần, phản ứng được rút gọn thành lựa chọn nhị phân.
- Hướng dẫn intuitive kết hợp áp lực tốc độ, cấm biện minh, và cho phép rời khỏi hồ sơ — không rõ yếu tố nào mang lại hiệu ứng.
