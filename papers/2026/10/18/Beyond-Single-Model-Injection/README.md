# [2609.22949v1] Beyond Single-Model Injection: A Threat Model and Defense Architecture for Prompt Injection in Multi-Agent Systems

## Problem
Nghiên cứu chẵnprompt injection hiện tại tập trung vào các kịch bản chatbot đơn mô hình, nơi kẻ tấn công thao thác một LLM thông qua đầu vào được thiết kế. Hệ thống multi-agent làm tăng mối hiểm này thông qua ba cơ chế không có trong cài đặt đơn mô hình: truyền thông giữa các agent tạo kênh chặn không thể nhìn thấy được bởi các phòng thủ biên, quyền truy cập công cụ chung cho phép leo thang đặc quyền qua ranh giới agent, và lan truyền niềm tin cho phép một agent bị xâm phạm ảnh hưởng đến orchestrators trên lưu.

## Contribution
- Xây dựng một mô hình đe d撃 liệt kê 14 vector tấn công trong bốn loại: chển tiếp trực tiếp qua đầu vào người dùng (3 vector), chển tiếp gián tiếp qua đầu ra công cụ (4 vector), chển tiếp giữa các agent qua truyền thông (4 vector), và chển tiếp lan cascading thông qua thao tạc orchestrator (3 vector).
- Kiểm tra tất cả 14 vector trên một hệ thống 6-agent đại diện cho sản xuất, tìm ra 67% agent dễ bị tấn công ít nhất một vi phạm phạm vi ngay cả khi có các quy tắc bảo vệ cấp system-prompt, và chển tiếp gián tiếp qua đầu ra công cụ thành công trong 43% lần thử.
- Khái báo bốn phòng thủ kiến trúc giảm tỷ lệ thành công ch cał inject tổng thể từ 31.2% xuống 4.2%: ký thông điệp với theo dõi nguồn gốc (chển tiếp giữa các agent giảm 91%), làm sạch đầu vào/đầu ra ở ranh giới agent (chển tiếp gián tiếp giảm 78%), quyền truy cập công cụ theo phạm vi đặc quyền theo vai trò agent (leo thang đặc quyền bị loại bỏ hoàn toàn), và phát hiện bất thường trên mẫu truyền thông giữa các agent (84% nỗ lực cascading được bắt).

## Method
- Hệ thống đánh giá: 6-agent cấu hình đại diện cho các triển khai doanh nghiệp: orchestrator (aO), retrieval agent (aR), code agent (aC), analysis agent (aA), compliance agent (aX), và output agent (aW).
- Orchestrator điều chỉnh phân rã tác vụ và tổng hợp kết quả. Mỗi agent chuyên môn xử lý sub-task trong lĩnh vực của mình.
- Đánh giá trên ba LLM backend: GPT-4o (2024-08-06), Claude 3.5 Sonnet, và Llama 3 70B-Instruct, đánh giá mỗi vector trên cả ba và báo cáo tỷ lệ thành công cao nhất quan sát được.
- Các agent hoạt động trong một pipeline phân tích tài liệu tài chính: retrieval agent nạp hồ sơ SEC, code agent thực hiện tính toán phân tích, và compliance agent xác thực đầu ra đối với các ràng buộc quy định.
- Đối với mỗi trong 14 vector tấn công, xây dựng 50 payload sử dụng quá trình ba giai đoạn: xây dựng hạt thủ công bởi hai nghiên cứu viên bảo mật, tăng cường dựa trên mẫu với sự thay đổi biến số cho tên thực thể và định dạng, và tinh chỉnh đối đầu nơi các payload thất bại trong các vòng sớm được lặp đi lặp lại để tránh các quy tắc bảo vệ cấp system-prompt của agent mục tiêu.

## Key Findings
- 67% agent (4 trên 6) dễ bị tấn công ít nhất một vi phạm phạm vi dù có các quy tắc bảo vệ cấp system-prompt.
- Orchestrator là mục tiêu dễ bị tấn công nhất, xuất hiện như mục tiêu trong 8 trên 14 vector.
- Chển tiếp gián tiếp qua đầu ra công cụ là loại nguy hiểm nhất, tỷ lệ thành công tổng hợp 43%.
- Chển tiếp giữa các agent qua truyền thông thành công ở mức 31%, không thể nhìn thấy bởi các phòng thủ biên vì chặn đi qua các kênh thông điệp nội bộ mà các bộ lọc đầu vào không bao giờ kiểm tra.
- Chển tiếp cascading thông qua orchestrator có tỷ lệ thành công 28% nhưng có tác động cao nhất mỗi nỗ lực thành công, vì nó chuyển một sự xâm phạm agent đơn vào một sự thất bại hệ thống-wide.
- Bốn phòng thủ kiến trúc giảm tỷ lệ thành công ch cał inject tổng thể từ 31.2% xuống 4.2% (giảm 86,5%).

## Actionable Insights
1. Sử dụng ký thông điệp với theo dõi nguồn gốc cho mọi thông điệp giữa các agent. Áp dụng: mọi thông điệp giữa các agent đều mang chữ ký mã hóa và hồ sơ nguồn gốc (origin agent, tác vụ tạo ra, chuỗi các người đóng góp trước). Agent nhận xác thực chữ ký trước khi xử lý và isolate các thông điệp không ký. Bước đầu: Thêm chữ ký Ed25519 vào mọi thông điệp giữa các agent trong hệ thống của bạn.
2. Triển khai làm sạch đầu vào/đầu ra ở ranh giới agent. Áp dụng: mọi thông điệp đi vào hoặc đi ra từ một agent đều đi qua một bộ làm sạch ranh giới. Bộ làm sạch áp dụng ba kiểm tra: xác thực cấu trúc đối với lược đồ đầu ra mong đợi, phát hiện hướng dẫn qua một bộ phân loại nhẹ được huấn luyện để phân biệt nội dung dữ liệu từ nội dung hướng dẫn, và thực thi độ dài nội dung để ngăn ngừa ô nhiễm khung ngữ cảnh. Bước đầu: Xây dựng một bộ làm sạch ranh giới kiểm tra cấu trúc đầu ra và phát hiện hướng dẫn trong mỗi thông điệp agent.
3. Áp dụng quyền truy cập công cụ theo phạm vi đặc quyền theo vai trò agent. Áp dụng: mỗi agent nhận mã thông báo truy cập công cụ được giới hạn theo vai trò: retrieval agent có thể truy vấn tài liệu nhưng không thể thực thi code, code agent có thể chạy tính toán trong sandbox nhưng không thể truy cập cơ sở dữ liệu quy định. Các quy tắc cổng API thực thi các chính sách này ở tầng cơ sở hạ tầng, không phải thông qua hướng dẫn prompt. Bước đầu: Thiết lập ánh xạ vai trò-công cụ không thể thay đổi ở tầng cơ sở hạ tầng.
4. Sử dụng phát hiện bất thường trên mẫu truyền thông giữa các agent. Áp dụng: mô hình truyền thông giữa các agent dự kiến như một đồ thị có hướng nơi các cạnh đại diện cho luồng thông điệp được phép. Bộ phát hiện bất thường cắm các sự lệch: người nhận thông điệp không dự kiến, khối lượng thông điệp không bình thường, mẫu nội dung không điển hình, hoặc dãy truyền thông vi phạm quy trình công việc dự kiến. Bước đầu: Xây dựng một đồ thị truyền thông giữa các agent dự kiến và phát hiện các sự lệch.

## Assumptions & Limitations
- Mô hình đe d击 chỉ nhắm vào các hệ thống multi-agent dựa trên văn bản. Các agent đa phương thức có các bề mặt chặn bổ sung mà chúng tôi không giải quyết.
- Sử dụng một bộ cố định 50 payload cho mỗi vector; các đối thủ thích ứng có thể đạt tỷ lệ thành công cao hơn.
- Đánh giá trên một hệ thống 6-agent; các triển khai sản xuất với hàng trăm agent có thể cần xấp xỉ cho đồ thị phát hiện bất thường.
- Chắn prompt là một mối đe d击 trong số nhiều; nhiễm dữ liệu, trích xuất mô hình, và sự xâm phạm chuỗi cung cấp cần xử lý riêng biệt.

## Metadata
- Năm: 2026, tác giả: Rudrendu Kumar Paul (Boston University), Sourav Nandy (University of Texas at Austin), category arXiv: cs.AI, link PDF: https://arxiv.org/pdf/2609.22949v1