# Skill: heart-tool-use-planner-router-verifier
Source: 2609.01736v1
Type: framework

## Khi nào dùng skill này
- Agent cần gọi tool (tìm kiếm, tính toán, lấy dữ liệu) nhiều lần trong một tác vụ.
- Muốn giảm chi phí API khi gọi tool (tối đa 85%).
- Muốn cải thiện độ chính xác tool use trên các tác vụ thực tế.

## Tình huống KHÔNG nên dùng
- Agent không gọi tool nào, chỉ trả lời từ kiến thức nội bộ.
- Chỉ gọi tool một lần đơn giản, không cần quản lý luồng gọi tool phức tạp.

## Input cần có
- Kho tool primitives (công cụ nguyên thủy tái sử dụng) đã có sẵn hoặc cần xây dựng.
- Mô hình LLM lớn (planner) và mô hình nhỏ (router/executor).
- Các tác vụ đòi hỏi multi-step tool use.

## Các bước thực hiện
1. Xây dựng tool primitives: thư viện hàm tái sử dụng cho các tác vụ phổ biến (tìm kiếm, tính toán, lấy dữ liệu, v.v.).
2. Thiết lập Planner: mô hình lớn lập kế hoạch các bước tool cần gọi cho tác vụ.
3. Thiết lập Router: định tuyến mỗi bước đến tool primitive phù hợp.
4. Thiết lập Verifier: xác thực kết quả tool trước khi trả lời người dùng (chống hallucination, sai sót).
5. Kết hợp mô hình lớn và nhỏ: lớn cho kế hoạch, nhỏ cho thực hiện tool call đơn giản (giảm chi phí lên đến 85%).

## Output mong đợi
- 84% task completion trên 50 tác vụ thực tế (3.8× so với các mô hình thương mại định hướng).
- Giảm chi phí API lên đến 85% so với dùng mô hình lớn cho mọi bước.
- 0.0% attack success rate dưới các cuộc tấn công prompt injection.

## Ví dụ áp dụng
Solopreneur xây agent viết bài nghiên cứu thị trường: Planner lên kế hoạch các bước (tìm kiếm đối thủ, lấy giá, tổng hợp), Router định tuyến mỗi bước đến tool tìm kiếm hoặc tool tính toán, Verifier kiểm tra dữ liệu trước khi viết bài. Sử dụng mô hình lớn cho kế hoạch, mô hình nhỏ cho tìm kiếm/tính toán → giảm chi phí API hơn 75%.

## Gotchas
- SFT-based models gần như thất bại hoàn toàn trên dynamic agentic tool scenarios (các tình huống công cụ động) — không nên dùng SFT đơn thuần cho tool use phức tạp.
- Cần kho tool primitives đã curate; nếu không có, phải xây dựng từ đầu.
- Chi phí giảm 85% là trên trường hợp kết hợp mô hình lớn và nhỏ, không phải mọi trường hợp.
