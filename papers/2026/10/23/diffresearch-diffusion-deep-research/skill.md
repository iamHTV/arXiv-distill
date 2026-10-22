# Skill: Thay backbone diffusion vào deep research (DiffResearch 3 giai đoạn)
Source: 2610.28909
Type: framework

## Khi nào dùng skill này
- Hệ thống deep research / viết báo cáo dài đang dùng LLM autoregressive và bị chậm ở giai đoạn lập kế hoạch, viết bài.
- Cần giảm độ trễ end-to-end mà không thay đổi agent scaffold, retrieval code, prompt, đánh giá.
- KHÔNG dùng khi vấn đề chính là độ chính xác nguồn thông tin, hoặc khi cần văn bản cuối cùng chính xác từng từ.

## Input cần có
- Agent scaffold hiện có (phân loại ý định, viết lại truy vấn, lập kế hoạch, truy xuất, viết).
- Diffusion LLM có thể chạy qua Hugging Face runtime (ví dụ diffusiongemma, LLaDA, Dream, Mercury).
- Mô hình AR tương đồng để dùng làm baseline so sánh.
- Bộ tác vụ đánh giá (benchmark) và thang điểm (ví dụ RACE).

## Các bước thực hiện
1. Giữ nguyên agent scaffold, code truy xuất, prompt, đánh giá; chỉ thay đổi backbone sinh văn bản giữa diffusion LLM và AR model để so sánh kiểm soát.
2. Triển khai 5 giai đoạn cốt lõi: phân loại ý định, viết lại truy vấn, lập kế hoạch, truy xuất (dùng Semantic Scholar / Serper API, deterministik, không LLM trong vòng lặp), viết; thêm đánh giá tùy chọn.
3. Chạy chế độ full (dFull): diffusion sinh toàn bộ báo cáo đến hết, parse JSON, đánh giá RACE.
4. Chạy chế độ fast decomposition (dFast): đọc trạng thái lấy nhiễu trung gian của diffusion, trích xuất danh sách subqueries sớm khi đối tượng JSON hợp lệ xuất hiện, gửi truy xuất trước khi sinh xong.
5. Đo latency và chất lượng RACE cho cả 3 cấu hình (dFull, dFast, AR), so sánh trên cùng bộ tác vụ.

## Output mong đợi
- Hệ thống deep research chạy trên diffusion backbone nhanh khoảng 6× end-to-end so với AR, chất lượng RACE không giảm (dFast 0,3969 vs AR 0,3904 trên thang 0-1).
- dFast cung cấp 1.99× tốc độ trung vị cho bước phân tích phân giải truy vấn, không làm giảm chất lượng báo cáo.

## Ví dụ áp dụng
- Agent viết báo cáo nghiên cứu nội bộ dùng 3 công cụ tìm kiếm: thay backbone AR bằng diffusion LLM, giữ nguyên 5 giai đoạn, đo latency trên 100 tác vụ → giảm từ ~71s xuống ~12s end-to-end, RACE giữ nguyên.

## Gotchas
- Phải đo trên phần cứng tương tự (H200 pod) và cùng backend truy xuất để kết quả so sánh đáng tin cậy.
- dFast không giúp giảm độ trễ end-to-end nếu truy xuất bị giới hạn tốc độ (rate-limited) và chỉ chiếm phần nhỏ tổng thời gian.
- Chỉ một cặp backbone được thử nghiệm, chưa quét rộng họ mô hình và kích thước.
- Kiểm tra nguồn cho thấy chỉ 28% 주장 được hỗ trợ đầy đủ — giảm độ trễ không giải quyết vướng vấn về chất lượng truy xuất.