# Skill: tool-failure-honesty-detection
Source: 2609.14758v1
Type: workflow

## Khi nào dùng skill này
- Xây dựng agent dùng công cụ (tool-augmented agent) và cần đảm bảo agent không khẳng định giá trị khi công cụ thất bại.
- Có công cụ (tool) trả về trạng thái (status) OK/FAILED.
- Cần giảm phản hồi không trung thực (dishonest response) khi công cụ thất bại.

## Tình huống KHÔNG nên dùng
- Không có công cụ (tool) trong agent workflow.
- Không cần kiểm tra độ trung thực (honesty) của agent khi công cụ thất bại.
- Công cụ luôn trả về giá trị hợp lệ (không có thất bại).

## Input cần có
- Agent có thể gọi công cụ (tool) và nhận được phản hồi (response).
- Công cụ trả về trạng thái (status) OK/FAILED hoặc giá trị (value).
- Agent có thể sinh phản hồi (response) dựa trên công cụ và trạng thái.

## Các bước thực hiện
1. Thêm một câu yêu cầu agent khai báo công cụ OK/FAILED trước khi trả lời.
2. Agent kiểm tra trạng thái công cụ (OK/FAILED) trước khi trả lời.
3. Nếu công cụ thất bại (FAILED), agent không khẳng định giá trị mà công cụ không cung cấp.
4. Nếu công cụ thành công (OK), agent có thể sử dụng giá trị từ công cụ để trả lời.
5. Giám sát tỷ lệ phản hồi không trung thực (dishonest response) trước và sau khi áp dụng kỹ thuật.

## Output mong đợi
- Giảm tỷ lệ phản hồi không trung thực từ 14.10% xuống 0.87%.
- Cờ (flag) được phát ra (emitted) là trung thực (faithful) trong 99.7–99.9% các khai báo.

## Ví dụ áp dụng
- Xây dựng agent truy xuất thông tin (information retrieval agent) sử dụng công cụ tìm kiếm (search tool). Khi công cụ tìm kiếm thất bại (ví dụ: không tìm thấy kết quả), agent không bịa ra giá trị mà báo cáo thất bại.

## Gotchas
- Khi công cụ thất bại, agent cần được yêu cầu xác nhận trạng thái (OK/FAILED) trước khi trả lời.
- Không dùng từ "significantly", "substantially", "considerably" — thay bằng con số.
- Khi công cụ trả về status:error, tỷ lệ không trung thực là không (0.0%); khi công cụ trả về status:ok với giá trị bị che đi, hỏng hóc, cũ, sai định dạng, trống hoặc bị cắt bớt, tỷ lệ không trung thực đạt 45.3%.
