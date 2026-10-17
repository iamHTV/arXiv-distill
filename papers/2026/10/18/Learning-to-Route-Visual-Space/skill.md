# Skill: Huấn luyện Multi-Step Embedding Retriever cho Tìm kiếm Hình ảnh

Source: 2609.38743v2
Type: framework

## Khi nào dùng skill này
- Bạn xây dựng hệ thống tìm kiếm tác nhân hình ảnh (visual agentic search) và muốn giảm chi phí token cũng như cải thiện tỷ lệ thành công.
- Bạn có một mô hình embedding hiện có và muốn biến nó thành retriever đa bước mà không cần fine-tune agent LLM.
- Bạn cần xử lý truy vấn hình ảnh nơi dấu hiệu trực quan khó mô tả bằng văn bản.

## Tình huống KHÔNG nên dùng
- Tìm kiếm chỉ văn bản (text-only retrieval) không cần multi-hop.
- Bạn không có dữ liệu hình ảnh để huấn luyện retriever đa bước.

## Input cần có
- Bộ dữ liệu hình ảnh (image corpus) và các truy vấn multimodal.
- Mô hình embedding cơ bản (ví dụ: Qwen3-VL-Embedding-2B).
- Các quỹ đạo vàng (gold trajectories) cho SFT.
- Oracle guidance cho Online IL.

## Các bước thực hiện
1. Huấn luyện SFT dạy next-hop retrieval: mã hóa trạng thái (hướng dẫn + stack ảnh hiện tại) và căn chỉnh với hình ảnh vàng tiếp theo bằng mục tiêu InfoNCE. Hai giai đoạn: đầu freeze action encoder, cập nhật chỉ state encoder; sau đó cùng tối ưu cả hai.
2. Huấn luyện Online IL dạy khôi phục và dừng lại: thu thập các lượt chạy mới bằng chính sách hiện tại, lấy hướng dẫn oracle, khám phá ngõ tắc (dead-end exploration). Cập nhật state encoder và các cổng điều khiển bằng tổn thất theo từng trạng thái.
3. Huấn luyện RLVR tối ưu tỷ lệ thành công câu trả lời cuối: lấy mẫu G lượt chạy cho mỗi truy vấn, gán phần thưởng 1 chỉ khi chính sách dừng với câu trả lời hợp lệ, dùng PPO-style clipped surrogate với DAPO-style asymmetric clipping.
4. Khi suy luận, chính sách hoạt động决定论: dừng nếu xác suất dừng ≥ 0.5, nếu không chọn ảnh có điểm số cosine cao nhất.
5. Trả về chuỗi hình ảnh liên kết trong một công cụ gọi duy nhất, không yêu cầu agent định nghĩa truy vấn văn bản trung gian.

## Output mong đợi
- Một retriever đa bước có thể điều hướng trên không gian embedding hình ảnh.
- Truy xuất chuỗi hình ảnh liên kết trong một lần gọi công cụ.
- Giảm số lượng ảnh trong ngữ cảnh và cắt tải trọng API.
- Tỷ lệ thành công nhiệm vụ cao hơn đáng kể so với retriever đơn bước.

## Ví dụ áp dụng
Bạn xây dựng agent tìm kiếm trong kho ảnh sản phẩm của cửa hàng điện tử. Thay vì để agent gửi nhiều truy vấn văn bản để tìm món hàng, bạn dùng VHop-Router — retriever đa bước tự điều hướng trên không gian embedding hình ảnh, trả về chuỗi các ảnh liên quan trong một lần gọi. Agent chỉ cần kiểm tra chuỗi ảnh kết quả và đưa ra câu trả lời. Giảm 61% token so với cách agent tự làm multi-hop retrieval.

## Gotchas
- Cần dữ liệu hình ảnh và quỹ đạo vàng để huấn luyện SFT.
- Huấn luyện độc quyền trên mức độ khó L4, tổng quát hóa sang L1–L5 nhưng có thể không hoạt động tốt trên các domain hình ảnh completamente khác.
- Cổng dừng/backtrack cần được điều chỉnh nhiệt độ (gate temperature) để hoạt động ổn định.