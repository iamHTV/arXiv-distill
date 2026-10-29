# Skill: effect-typed-tool-agent-training (huấn luyện agent gọi công cụ có khai báo hiệu ứng)

Source: 2610.35981v1
Type: framework / workflow

## Khi nào dùng skill này

- Bạn đang xây dựng agent nhỏ (small open language model — mô hình ngôn ngữ mở nhỏ, ≤4B tham số) gọi công cụ bên ngoài (API, email, lịch, đơn hàng) và muốn agent gọi ít hơn, an toàn hơn.
- Bạn cần agent biết trước tác dụng của mỗi cuộc gọi (xóa, gửi, sửa, chỉ đọc) thay vì chỉ kiểm tra cú pháp gọi hàm.
- Bạn có dữ liệu huấn luyện công cụ công khai (Nemotron-Agentic, Hermes, ToolACE…) và muốn tránh việc mẫu từ chối (refusal templates) dạy agent không gọi công cụ.

Tình huống KHÔNG nên dùng:
- Agent chỉ truy xuất thông tin chỉ đọc (read-only), không có hành động thay đổi trạng thái.
- Agent lớn (frontier model, >70B) đã gọi công cụ ổn định, không cần tối ưu token.

## Input cần có

- Danh sách công cụ agent sẽ gọi, mỗi công cụ có: tên, mô tả, tham số, loại hiệu ứng (pure/read/write/destructive), cờ idempotent, bước chân (footprint — tài nguyên đọc/ghi).
- System prompt có 5 quy tắc: xác nhận trước hành động không thể đảo ngược; không lặp lại ghi không idempotent; đọc trạng thái trước khi sửa; hỏi khi thiếu thông tin; không gọi khi không cần.
- Bộ dữ liệu huấn luyện gọi công cụ (có thể kết hợp dữ liệu EffectWorld và dữ liệu công khai đã lọc mẫu từ chối).
- Mô hình backbone nhỏ (ví dụ Qwen3-4B, Qwen3-1.7B, Phi-4-mini, Falcon3-3B) và môi trường huấn luyện LoRA.

## Các bước thực hiện

1. Khai báo hiệu ứng cho mỗi công cụ: gán loại hiệu ứng (pure, read, write, destructive), cờ idempotent, và bước chân tài nguyên đọc/ghi. Viết khai báo này vào mô tả công cụ (schema), theo kiểu chú thích MCP (Model Context Protocol — giao thức nối agent với công cụ).
2. Viết system prompt nêu 5 quy tắc hiệu ứng: xác nhận trước khi hủy; không lặp lại ghi tạo/gửi/thanh toán; đọc trước khi sửa; hỏi khi thiếu thông tin; không gọi khi không công cụ nào phù hợp.
3. Chuẩn bị dữ liệu huấn luyện: sinh vết dấu vàng (gold traces — chuỗi gọi chuẩn tối ưu) và vết dấu thô (naive traces — đúng nhưng thải phế) từ các máy sinh tác vụ; dùng trình tối ưu hóa vết dấu (trace optimizer) để loại bỏ cuộc gọi không cần (loại đọc thừa, cuộc gọi chết, gói lệnh hàng loạt, lên lịch lượt gọi).
4. Lọc dữ liệu công khai: loại bỏ các lượt có mẫu từ chối kiểu mẫu (refusal templates như "I don't have access to a tool that can do that"), giới hạn lượt không gọi ở lượt đầu ở 5%.
5. Huấn luyện LoRA adapter (bộ điều chỉnh cấp thấp) trên mô hình backbone bằng SFT (huấn luyện giám sát) trên dữ liệu đã lọc, hai epochs.
6. Đánh giá agent trên tác vụ thực: đếm thành công tác vụ, cuộc gọi hủy chưa xác nhận, số token đầu ra, số lượt gọi.

## Output mong đợi

- Agent gọi ít công cụ hơn (khoảng 1/3 token đầu ra so với mô hình cơ sở).
- Tác vụ thành công cao (99% trong phân phối, 81% trên phân đoạn khó, 83% trên miền chưa thấy như mua sắm trực tuyến).
- Không có cuộc gọi hủy chưa xác nhận (effect-safe trace — vết dấu an toàn về hiệu ứng).
- Agent không gọi công cụ khi yêu cầu không liên quan (irrellevance detection — phát hiện yêu cầu không liên quan).

## Ví dụ áp dụng

Solopreneur xây dựng agent xử lý đơn hàng online: agent cần tìm sản phẩm, thêm vào giỏ, đặt hàng (hủy không thể hoàn tác), hủy đơn. Áp dụng skill: khai báo "place order" là destructive, idempotent=false; "get product" là pure; "add to cart" là write, idempotent=false. System prompt yêu cầu xác nhận trước khi place order, đọc giỏ hàng trước khi thay đổi, không gọi tool nếu người dùng chỉ hỏi giá. Huấn luyện LoRA trên dữ liệu EffectWorld + dữ liệu công khai đã lọc từ chối. Kết quả: agent đặt hàng chỉ sau khi người dùng xác nhận, không lặp lại đặt hàng, giảm 2/3 token so với không tối ưu.

## Gotchas

- Mẫu từ chối trong dữ liệu công khai (refusal templates) có thể dạy agent không gọi công cụ, làm sapped BFCL non-live accuracy từ 88.0 xuống 31.4 — phải lọc trước khi huấn luyện.
- Mẫu tiêu cực (negative examples) không thay thế mẫu dương: unlikelihood, NPO, DPO trên mẫu tiêu cực không thắng nhóm đối chứng SFT trên bất kỳ phân đoạn kiểm tra nào; chúng chỉ thay đổi mức độ agent sẵn sàng gọi.
- Xác nhận trước khi hủy không chuyển dịch tốt sang công cụ chưa thấy: trên phân đoạn mua sắm, các adapter làm 24–37 cuộc gọi hủy chưa xác nhận so với 7 của mô hình cơ sở.
- Công cụ EffectWorld nhỏ (9 loại tác vụ, một miền huấn luyện), kết quả có thể khác trên agent lớn hơn 4B tham số hoặc dữ liệu thực tế ngoài mô phỏng.
- Trình xác thực phát lại (replay verifier) kiểm tra bằng phát lại vết dấu đã ghi, không chứng minh cho mọi trạng thái có thể xảy ra.