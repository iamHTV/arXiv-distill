# Skill: Multi-Agent Compliance-First Workflow for Insurance Underwriting

Source: 2609.37454v1
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng multi-agent để tự động hóa xử lý hồ sơ có yêu cầu tuân thủ nghiêm ngặt (bảo hiểm, tài chính, pháp lý).
- Bạn cần đảm bảo dữ liệu nhạy cảm không bị rò rỉ ra đám mây.
- Bạn muốn quy tắc tuân thủ được thi hành theo cấu trúc (structural governance), không chỉ kiểm tra sau sự việc.

## Tình huống KHÔNG nên dùng
- Quy trình đơn giản không yêu cầu tuân thủ nghiêm ngặt.
- Bạn không có hệ thống backend cục bộ để xử lý dữ liệu nhạy cảm.

## Input cần có
- Danh sách quy tắc tuân thủ (STOP và WARN) cho domain của bạn.
- Danh sách trường dữ liệu nhạy cảm cần giữ cục bộ.
- Mô hình LLM cục bộ (ví dụ: Gemma 2) và mô hình LLM đám mây (ví dụ: Claude Sonnet).
- Thư viện LangGraph hoặc tương đương để xây dựng state graph.

## Các bước thực hiện
1. Thiết kế LangGraph state graph với các nút agent và các edge condition kiểm tra compliance trước khi chuyển trạng thái.
2. Chia agent thành hai tầng: tầng cục bộ xử lý dữ liệu nhạy cảm, tầng đám mây xử lý điểm số đã ẩn danh.
3. Đặt các quy tắc hard-stop (STOP) dưới dạng hàm Python định danh, không phụ thuộc vào output LLM.
4. Mỗi agent chỉ có quyền gọi công cụ được ràng buộc, mỗi lần gọi được ghi log vào dấu vết kiểm tra (audit log).
5. Nếu compliance trả về FAIL, định tuyến đến lệnh khắc phục con người (human escalation), không cho phép agent tiếp tục.
6. Nếu confidence score dưới ngưỡng (ví dụ: 0.80), định tuyến đến human escalation interrupt.

## Output mong đợi
- Một multi-agent workflow có tuân thủ được rãs vào cấu trúc đồ thị.
- Dữ liệu nhạy cảm không bao giờ rời khỏi môi trường cục bộ.
- Dấu vết kiểm tra đầy đủ cho mọi hành động agent.
- Hard-stop được thi hành chính xác và có thể tái tạo.

## Ví dụ áp dụng
Bạn xây dựng agent tự động xử lý đơn xin vay ngân hàng. Các quy tắc STOP (ví dụ: điểm tín dụng quá thấp, thu nhập không xác minh) được viết bằng Python định danh và đặt làm điều kiện trên edge giữa các agent. Nếu bất kỳ quy tắc STOP nào không đạt, đơn được định tuyến đến nhân viên ngân hàng phê duyệt, không cho agent tự quyết định. Dữ liệu khách hàng nhạy cảm (CMND, số tài khoản) chỉ được xử lý cục bộ, agent đám mây chỉ nhận điểm số rủi ro đã ẩn danh.

## Gotchas
- Các công cụ bên ngoài là synthetic stubs trong bản nguyên mẫu, chưa kết nối API thực.
- Quy tắc STOP dựa trên trường được trích xuất ở nhiệt độ 0, độ chính xác phụ thuộc vào chất lượng trích xuất trường.
- Suy luận trên thiết bị làm framework chậm hơn mỗi đơn so với một prompt đám mây đơn lẻ.