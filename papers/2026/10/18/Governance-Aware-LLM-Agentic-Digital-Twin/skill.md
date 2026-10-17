# Skill: Xây dựng Lớp Quản trị cho Agent (Agent Governance Layer)

Source: 2609.22476v1
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng LLM agent cho hệ thống quan trọng an toàn (tài chính, y tế, năng lượng,Control room) và cần đảm bảo agent không thực hiện hành động nguy hiểm mà không kiểm soát.
- Bạn cần ngăn ngừa ảo gezien (hallucination) về con số và sử dụng công cụ không kiểm soát.
- Bạn muốn có kho lưu trữ kiểm tra (audit trail) duy trì cho mọi hành động của agent.

## Tình huống KHÔNG nên dùng
- Ứng dụng không quan trọng, không cần bảo mật cao, agent có thể tự do sử dụng công cụ mà không cần phê duyệt.
- Bạn không có hệ thống backend có thể tính toán xác định để kiểm tra con số LLM sinh ra.

## Input cần có
- Danh sách công cụ backend được phép (whitelist tools) với schema đối với mỗi công cụ.
- Danh sách hành động có tác dụng phụ (side-effect actions) cần sự chấp thuận từ con người.
- Hệ thống backend xác định để tính toán và render các con số.
- Ngân sách bước thực thi (step budget) tối đa cho mỗi phiên agent.

## Các bước thực hiện
1. Xây dựng lớp quản trị (governance layer) nằm giữa LLM và mọi công cụ/backend — LLM không gọi trực tiếp công cụ, chỉ gửi yêu cầuJSON action contract qua lớp quản trị.
2. Chỉ cho phép thực thi các công cụ trong whitelist, validate schema đối số trước khi chạy, từ chối mọi công cụ không xác định hoặc đối số sai định dạng.
3. Đặt ngân sách bước thực thi (ví dụ: 5 bước), agent phải chấm dứt khi đạt giới hạn, đảm bảo thời gian chạy dự đoán được.
4. Yêu cầu sự chấp thuận rõ ràng từ toán tử trước khi thực thi mọi hành động có tác dụng phụ (sửa dữ liệu, gửi thông báo, khởi tạo quy trình bên ngoài). Lưu quyết định chấp thuận vào kho kiểm tra duy trì.
5. Mọi con số trong câu trả lời cho người dùng phải được render từ kết quả backend xác định, kèm đơn vị, biến số, và thời gian — không cho phép LLM tự sinh con số.
6. Lưu trữ mọi lệnh gọi công cụ, đối số, thời gian, trạng thái thực thi, và đầu ra vào kho lưu trữ kiểm tra duy trì (persistent audit store).

## Output mong đợi
- Một agent có lớp quản trị ràng buộc: chỉ công cụ được phép chạy, hành động nguy hiểm cần phê duyệt, con số luôn chính xác từ backend.
- Kho lưu trữ kiểm tra duy trì cho mọi hoạt động agent, hỗ trợ kiểm tra sau sự cố.
- Chi phí quản trị thấp (12-16ms mỗi yêu cầu).

## Ví dụ áp dụng
Bạn xây dựng agent hỗ trợ nhà giao dịch chứng khoán. Agent có thể xem giá cổ phiếu (chỉ đọc) mà không cần phê duyệt, nhưng mỗi lệnh mua/bán (tác dụng phụ) phải được nhà giao dịch phê duyệt qua lớp quản trị trước khi thực thi. Mọi con số về giá, khối lượng giao dịch trong câu trả lời phải được lấy từ hệ thống backend xác định, không được agent tự ước lượng.

## Gotchas
- Xóa lớp quản trị dẫn đến model thực thi tất cả hành động cần phê duyệt mà không có phân quyền (45/45 lần chạy trong thí nghiệm).
- Không có lớp quản trị: chỉ 39.2% câu trả lời có con số được hỗ trợ bởi backend (còn lại là con số LLM tự sinh/ảo gesehen).
- Lớp quản trị phải không thể bị bypass bởi LLM — model không được quyền sửa đổi hoặc bỏ qua các quy tắc quản trị.