# Skill: Kiến trúc phòng thủ Chắn prompt cho Multi-Agent System

Source: 2609.22949v1
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng hệ thống multi-agent và muốn bảo vệ chống chắn prompt injection.
- Bạn cần hiểu các bề mặt tấn công đặc thù của multi-agent (không chỉ chắn prompt đơn mô hình).
- Bạn muốn triển khai các phòng thủ kiến trúc thay vì chỉ dựa vào system-prompt guardrails.

## Tình huống KHÔNG nên dùng
- Hệ thống agent đơn (không có truyền thông giữa các agent).
- Bạn không cần bảo mật cao cho hệ thống agent của mình.

## Input cần có
- Hệ thống multi-agent với các agent có vai trò và công cụ khác nhau.
- Cơ sở hạ tầng để triển khai ký thông điệp, làm sạch ranh giới, quyền truy cập công cụ theo phạm vi, và phát hiện bất thường.
- Máy mã hóa chữ ký (Ed25519) cho thông điệp giữa các agent.

## Các bước thực hiện
1. Xây dựng mô hình đe d击 cho hệ thống multi-agent của bạn: liệt kê các vector tấn công (trực tiếp qua đầu vào người dùng, gián tiếp qua đầu ra công cụ, giữa các agent qua truyền thông, cascading qua orchestrator).
2. Triển khai ký thông điệp với theo dõi nguồn gốc: mọi thông điệp giữa các agent mang chữ ký mã hóa và hồ sơ nguồn gốc, agent nhận xác thực chữ ký trước khi xử lý.
3. Triển khai làm sạch đầu vào/đầu ra ở ranh giới agent: xác thực cấu trúc, phát hiện hướng dẫn, thực thi độ dài nội dung.
4. Thiết lập quyền truy cập công cụ theo phạm vi đặc quyền theo vai trò agent: mỗi agent chỉ có quyền truy cập công cụ được phép theo vai trò của mình, thực thi ở tầng cơ sở hạ tầng.
5. Triển khai phát hiện bất thường trên mẫu truyền thông giữa các agent: mô hình truyền thông dự kiến như đồ thị có hướng, phát hiện sự lệch.

## Output mong đợi
- Một hệ thống multi-agent có khả năng chống chắn prompt injection mạnh mẽ hơn.
- Tỷ lệ thành công tấn công chắn prompt giảm từ 31.2% xuống 4.2%.
- Các tầng phòng thủ phân lớp: ký thông điệp, làm sạch ranh giới, quyền truy cập công cụ theo phạm vi, phát hiện bất thường.

## Ví dụ áp dụng
Bạn xây dựng hệ thống multi-agent để xử lý tài liệu tài chính. Các agent trao đổi thông điệp nội bộ (retrieval agent gửi dữ liệu cho analysis agent, analysis agent gửi kết quả cho compliance agent). Bạn triển khai ký thông điệp để mỗi thông điệp giữa các agent được xác thực, làm sạch ranh giới để ngăn chặn hướng dẫn được nhúng vào đầu ra công cụ, quyền truy cập công cụ theo phạm vi để ngăn code agent truy cập cơ sở dữ liệu quy định, và phát hiện bất thường để bắt các nỗ lực routing manipulation. Tỷ lệ thành công tấn công chắn prompt giảm từ 31.2% xuống 4.2%.

## Gotchas
- System-prompt guardrails không đủ — agent không thể phân biệt chính xác giữa hướng dẫn được tiêm và tin nhắn hợp lệ khi cả hai đều đi qua cùng kênh văn bản.
- Bộ phân loại ranh giới giới thiệu tỷ lệ sai dương 2.3% và có thể không tổng quát hóa sang các định dạng chắn prompt chưa thấy.
- Các đối thủ thích ứng có thể đạt tỷ lệ thành công cao hơn so với các payload cố định.