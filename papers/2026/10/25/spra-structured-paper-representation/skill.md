# Skill: Xây dựng knowledge base cấu trúc cho bài báo khoa học (SPRA)

Source: 2610.21424v2
Type: workflow

## Khi nào dùng skill này

- Cần xây dựng hệ thống tra cứu kiến thức từ các bài báo nghiên cứu hoặc tài liệu kỹ thuật, nơi tác tử AI cần tra cứu nhanh và xác minh nguồn gốc.
- Có lượng lớn bài báo (hàng trăm nghìn đến triệu bản) và muốn biểu diễn nội dung dưới dạng đối tượng có cấu trúc thay vì văn bản thô.
- Muốn giảm chi phí token khi tác tử truy xuất thông tin từ nhiều bài báo cùng lúc.

## Tình huống KHÔNG nên dùng

- Nhiệm vụ yêu cầu hiểu rõ ngữ cảnh đầy đủ của bài báo (ví dụ: tổng hợp Top-5 cần toàn văn).
- Không cần xác minh nguồn gốc và chỉ cần tóm tắt nhanh.
- Không có nguồn tài liệu được phân tích thành Markdown có nhận diện section.

## Input cần có

- Bộ sưu tập bài báo đã phân tích thành Markdown có nhận diện section với dấu chỉ nguồn (source markers).
- Mô hình LLM mạnh để trích xuất cấu trúc (5 cuộc gọi LLM cốt lõi: census đơn vị, lập kế hoạch quan hệ, điền Problem/Method/Evidence, hai lần trích dẫn).
- Công cụ phân tích section-aware (ví dụ: MinerU).
- Quyền truy cập Sciverse platform hoặc cài đặt cục bộ Paper Schema API.
- Môi trường lưu trữ JSON và truy vấn quan hệ.

## Các bước thực hiện

1. Phân tích bài báo nguồn thành Markdown có nhận diện section với dấu chỉ nguồn.
2. Chạy lịch kiểm tra đơn vị chung (shared unit census) để xác định các đối tượng nghiên cứu.
3. Lập kế hoạch quan hệ (relation planning) giữa các đối tượng theo 6 vai trò: Problem, Contribution, Component, ExperimentSetup, Measure, Finding.
4. Điền nội dung theo vai trò: Problem (vấn đề/khoảng trống), Contribution (đóng góp), Component (thành phần), ExperimentSetup (thiết lập thí nghiệm), Measure (thước đo), Finding (kết quả).
5. Chạy hai lần trích dẫn (citation passes) để nối vai trò và tín hiệu nguyên văn với siêu dữ liệu bibliographic theo khóa trích dẫn.
6. Kiểm tra hợp đồng quan hệ (schema validity): kiểm tra kiểu, đầu cuối (endpoints), nguồn gốc và phạm vi kiểm tra.
7. Lưu trữ đối tượng và quan hệ dưới dạng JSON có cấu trúc, tách biệt trích dẫn ngoài trong tầng riêng biệt.
8. Xây dựng giao diện truy vấn (API) để tác tử có thể tra cứu, duyệt quan hệ và mở rộng trích dẫn (citation expansion).

## Output mong đợi

- Một tập đối tượng nghiên cứu có cấu trúc (SPRA instances) với quan hệ được trích lập và ràng buộc nguồn.
- Giao diện API (Paper Schema) cho phép tác tử tra cứu, duyệt và tái sử dụng nội dung bài báo.
- Giảm chi phí token so với truy xuất đoạn văn (passage retrieval) và văn bản đầy đủ.

## Ví dụ áp dụng

Doanh nghiệp tại Việt Nam muốn xây dựng trợ lý nghiên cứu cho nhóm R&D: thu thập 10.000 bài báo AI về xử lý ngôn ngữ tự nhiên, phân tích thành Markdown có section, trích xuất 6 vai trò và quan hệ giữa chúng, lưu vào knowledge base. Tác tử AI có thể tra cứu "phương pháp nào được dùng nhất để giải quyết vấn đề phân loại văn bản trong 3 năm qua" bằng cách duyệt quan hệ compares_to và evaluates thay vì đọc toàn bộ 10.000 bài báo.

## Gotchas

- Văn bản đầy đủ (Full Compact) chưa nhất định tối ưu cho mọi tác vụ: trên Top-5 synthesis, cấu trúc thu gọn kém hơn toàn văn về grounding và qualification. Hãy đánh giá theo nhu cầu của từng tác vụ.
- Cấu trúc thu gọn phải được đánh giá theo nhu cầu thông tin của từng tác vụ — không phải lúc nào cấu trúc đầy đủ cũng tốt hơn.
- Không tách biệt được đóng góp của từng nhãn vai trò hoặc từ khóa quan hệ từ đánh giá tổng thể.
- Dịch vụ lưu trú (Sciverse) có thể thay đổi hành vi khi cập nhật; kết quả chỉ đặc trưng cho lần gọi dịch vụ đã ghi nhận.
- Trích xuất tự động có thể bỏ sót hoặc sai lệch về hạn nợ (qualifications), ảnh hưởng đến cách hiểu claim của nghiên cứu.