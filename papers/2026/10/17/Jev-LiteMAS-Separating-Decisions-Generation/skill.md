# Skill: jev-litemas-decision-routing
Source: 2610.21411v1
Type: framework

## Khi nào dùng skill này
- Xây dựng multi-agent system cần giảm chi phí token cho các quyết định điều phối (routing và review).
- Có các chuyên gia (expert agents) chuyên biệt và cần chọn chuyên gia phù hợp cho mỗi nhiệm vụ.
- Cần kiểm tra artifact trung gian trước khi quyết định bước tiếp theo.

## Tình huống KHÔNG nên dùng
- Nhiệm vụ không có nhiều chuyên gia riêng biệt.
- Không cần giảm chi phí token (chỉ quan tâm đến chất lượng tuyệt đối).
- Không có dữ liệu về các chuyên gia và vai trò (expert roles) đã định trước.

## Input cần có
- Danh sách các chuyên gia (expert roles) và vai trò (legal actions) đã định trước.
- Nhiệm vụ (task) và đầu ra của các chuyên gia trước đó (prior expert outputs).
- Mô hình quyết định nhẹ (lightweight decision model - Jev).
- Mô hình generative LLM để thực thi tác vụ và review artifact.

## Các bước thực hiện
1. Phân tích nhiệm vụ và chọn chuyên gia động từ nhiệm vụ và đầu ra chuyên gia trước đó, dùng ngữ cảnh tích lũy để căn cảnh thực thi sau này.
2. Chuyên gia thực thi nhiệm vụ và tạo artifact trung gian.
3. Jev sàng lọc artifact trung gian dựa trên tiêu chí nhiệm vụ: artifact đạt tiêu chuẩn tiếp tục trực tiếp, artifact bị cõi đánh dấu trải qua LLM re-review để chấp nhận (ACCEPT) hoặc phản hồi khắc phục (REVISE).
4. Đánh giá trên các benchmark và hai backbone (ví dụ: DeepSeek-V4-Flash, GPT-5).
5. Theo dõi số token generative-LLM và độ chính xác.

## Output mong đợi
- Giảm token generative-LLM bởi 12.7–54.6% so với LAS.
- Duy trì độ chính xác trong khoảng 1.34 điểm phần trăm.
- Giảm độ trễ trong bảy của tám thiết lập.

## Ví dụ áp dụng
- Xây dựng multi-agent system để xử lý các tác vụ phức tạp: dùng Jev để chọn chuyên gia động (ví dụ: chuyên gia code, chuyên gia test, chuyên gia doc), kiểm tra artifact trung gian trước khi quyết định bước tiếp theo, chỉ gọi LLM review khi artifact cần sửa.

## Gotchas
- Feedback-driven routing hoạt động trên một nhóm chuyên gia và các hành động hợp lệ đã định trước.
- Framework không tạo động các chuyên gia mới.
- Đánh giá trên 4 benchmark và 2 backbone.
