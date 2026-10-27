# Skill: ant-or-contrastive-annotation-framework
Source: 2610.32415v1
Type: optimization-method

## Khi nào dùng skill này
- Cần đánh giá hệ thống gán nhãn LLM theo sự phù hợp với phân phối phán đoán của con người (distribution-aware evaluation).
- Muốn xây dựng hệ thống gán nhãn đa agent có thể thích ứng với hướng dẫn tác vụ chi tiết và nhiều trường hợp ranh giới.
- Muốn biến thành công và thất quả của gán nhãn vào kiến thức quyết định có cấu trúc có thể tái sử dụng.

## Tình huống KHÔNG nên dùng
- Tác vụ gán nhãn có đáp án rõ ràng, không mập mờ (không cần hệ thống đa agent phức tạp).
- Không có annotator con người chuyên nghiệp để tạo nhãn tham chiếu và hướng dẫn chi tiết.

## Input cần có
- Tập dữ liệu gán nhãn với hướng dẫn tác vụ chi tiết (annotation guidelines).
- Nhóm annotator con người (ví dụ: 10 annotator, mỗi mẫu gán bởi 5 người).
- Các mô hình LLM làm annotator và verifier (temperature = 0.1).
- Cơ sở lưu trữ mẫu đúng và sai (contrastive sample pools).

## Các bước thực hiện
1. Xây dựng tiêu chí đánh giá đa annotator: thu thập 5 nhãn độc lập từ annotator con người cho mỗi mẫu, sử dụng Fleiss' κ để đánh giá sự phù hợp của model với phân phối gán nhãn con người.
2. Triển khai kiến trúc annotator–verifier: 3 annotator độc lập tạo nhãn và lý luận bằng các prompt được tối ưu hóa riêng biệt, 1 verifier so sánh lý luận để xác định nhãn cuối cùng.
3. Khai phá kiến thức tương phản: khi agent dự đoán sai (không khớp ít nhất 2/5 nhãn người), lấy hai mẫu đúng tương tự về mặt ngữ nghĩa, tạo contrastive tuple, dùng LLM để tóm tắt kích thước phân biệt (discriminative dimension) từ các trường hợp gây nhầm lẫn.
4. Lưu kích thước phân biệt vào knowledge base với số hỗ trợ (support count); giữ lại chỉ kích thước có hỗ trợ ≥ 2.
5. Tiêm coupling mẫu-kích thước vào prompts: chọn top-K mẫu có điểm số cao nhất và các kích thước phân biệt liên quan.
6. Thực hiện tối ưu hóa prompt hướng dẫn bởi gán lỗi: gán lỗi cho các agent chịu trách nhiệm, tinh chỉnh prompt bằng LLMOpt(pa; {(q−, r)}, s+, d).
7. Đánh giá lại trên batch hiện tại, giữ lại prompt đã cập nhật chỉ nếu hiệu suất cải thiện, nếu không quay lại (rollback).
8. Lặp đi lặp lại qua nhiều kỳ (epochs): đánh giá, cập nhật cơ sở kiến thức, tinh chỉnh prompt.

## Output mong đợi
- Độ chính xác agreement@≥2 và Fleiss' κ cho hệ thống gán nhãn.
- Cơ sở kiến thức quyết định có cấu trúc (structured decision knowledge base).
- Prompt đã được tối ưu hóa cho mỗi agent.

## Ví dụ áp dụng
Công ty cần gán nhãn các ticket hỗ trợ khách hàng vào các danh mục (billing, technical, general). Hướng dẫn gán nhãn chi tiết có quy tắc cho các trường hợp ranh giới (ví dụ:票 cùng có vấn đề thanh toán và kỹ thuật thì gán vào billing). Áp dụng ANT-OR: thu thập 5 nhãn người cho mỗi ticket, triển khai 3 annotator + 1 verifier, sau mỗi dự đoán sai khai phá kích thước phân biệt và lưu vào knowledge base. Kết quả: độ chính xác agreement@≥2 cải thiện 4.5 điểm so với baseline, Fleiss' κ trong 2 điểm so với đồng nhất giữa annotator người.

## Gotchas
- Cần 5 annotator độc lập mỗi mẫu để đánh giá distribution-aware — chi phí cao (USD $4078 cho 7 dataset × 1.500 mẫu).
- ANT-OR chi phí tối ưu hóa cao hơn SPO ($101.43 vs $65.94) nhưng đạt độ chính xác tốt hơn (+4.7 điểm).
- Cần hướng dẫn tác vụ chi tiết trước khi bắt đầu — không áp dụng được cho tác vụ gán nhãn không có hướng dẫn.
- Kiến thức quyết định cần được lưu trữ và truy xuất đúng cách để tái sử dụng trong các kỳ tối ưu hóa sau.