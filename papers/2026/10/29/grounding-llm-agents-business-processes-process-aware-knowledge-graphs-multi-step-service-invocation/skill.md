# Skill: enterprise-api-process-aware-retrieval
Source: 2610.37242
Type: workflow

## Khi nào dùng skill này
- Bạn đang xây dựng agent LLM gọi nhiều API doanh nghiệp theo thứ tự (ví dụ tạo đơn mua, sau đó xác nhận nhập kho) và muốn giảm lỗi sai mã, khóa thiếu, gọi sai thứ tự.
- Doanh nghiệp của bạn công bố metadata OData và/hoặc có quy trình tham chiếu BPMN (hoặc có thể viết quy trình đó).
- Bạn chấp nhận chi phí tạo bản đồ hoạt động (activity-to-EntitySet mapping) thủ công, khoảng 20 phút mỗi hoạt động.

## Tình huống KHÔNG nên dùng
- API tự do không có cấu trúc quy trình (chunk-RAG vẫn là lựa chọn tốt hơn).
- Bạn không có metadata dịch vụ có cấu trúc (OData/OpenAPI) để nhập vào đồ thị.

## Input cần có
- Tài liệu metadata OData $metadata của các dịch vụ mục tiêu (EntitySet, EntityType, Property, NavigationProperty, ValueHelp).
- Tệp quy trình tham chiếu BPMN 2.0 (hoặc danh sách các hoạt động theo thứ tự cho từng quy trình kinh doanh).
- Một bản ánh xạ thủ công từ mỗi hoạt động đến các EntitySet nó đọc/ghi (USES ENTITY SET edges).
- Một mô hình embedding (ví dụ qwen3-embedding:8b) và cơ sở dữ liệu đồ thị chạy Cypher (ví dụ FalkorDB).
- Một agent ReAct có công cụ hybrid retrieval, GET, và POST, cùng một lớp kiểm tra payload (mock hoặc thực).

## Các bước thực hiện
1. Xây dựng typed property graph: chạy OData parser để tạo nút EntityType/EntitySet/Property/Navigation/ValueHelp và cạnh HAS PROPERTY, NAVIGATE FROM, NAVIGATE TO, HAS VALUE HELP (lưu cardinality trên nút Navigation). Chạy BPMN parser để tạo nút Process/Activity và cạnh HAS NEXT từ luồng trình tự.
2. Viết bản ánh xạ hoạt động-tập thực thể (activity-to-EntitySet mapping): liên kết mỗi hoạt động BPMN với các EntitySet nó đọc hoặc ghi (ví dụ tạo đơn mua → PurchaseOrder, PurchaseOrderItem). Giới hạn 45 cạnh, đủ nhỏ để xem xét toàn bộ.
3. Lập chỉ mục bản tóm tắt EntitySet bằng FAISS (dense retrieval) để có hạt giống (seed) cho truy vấn.
4. Triển khai hybrid retrieval: cho mỗi truy vấn, chạy top-k dense retrieval trên bản tóm tắt EntitySet; cho mỗi hạt giống, chạy truy vấn Cypher có giới hạn theo cạnh HAS NEXT để lấy các EntitySet tiếp theo trong chuỗi xử lý; gộp kết quả, loại trùng, giữ thứ tự dense, trả về mỗi endpoint cùng ngữ cảnh schema (các khóa bắt buộc, cardinality, danh sách mã hợp lệ).
5. Cấu hình agent ReAct: công cụ hybrid retrieval trả về toàn bộ thông số kiểu trong một cuộc gọi; agent dùng GET/POST được kiểm tra bởi một lớp validator. Agent chọn endpoint, xây dựng payload với các khóa bắt buộc và mã từ ValueHelp, tuân thủ thứ tự xử lý.
6. Đánh giá: Recall@k, MRR, nDCG@10 cho bước truy xuất; Completion rate và Invalid/run cho bước agent. Chạy kiểm tra độ trung thành xây dựng (coverage và exactness của đồ thị so với nguồn).

## Output mong đợi
- Một typed property graph chứa metadata OData và quy trình BPMN, liên kết hoạt động với EntitySet.
- Cho mỗi truy vấn: danh sách các endpoint đề xuất kèm ngữ cảnh schema (khóa bắt buộc, cardinality, mã hợp lệ, thông tin chuỗi xử lý).
- Số liệu: Recall@3, Completion rate, Invalid call rate, số lần gọi công cụ mỗi chạy, độ trễ.

## Ví dụ áp dụng
Bạn xây dựng agent đặt mua doanh nghiệp. Truy vấn: "tạo đơn mua cho nhà cung cấp 4711 với mã loại hợp lệ, sau đó xác nhận nhập kho." Bước 1–3 xây dựng đồ thị từ OData $metadata và quy trình BPMN "tạo đơn mua → nhập hàng". Bước 4 tìm PurchaseOrder qua dense, mở rộng thêm MaterialDocumentHeader qua cạnh xử lý, trả về danh sách mã loại đơn (NB/UB/FO) và cardinality 1:N của mục đơn. Bước 5 agent chọn PurchaseOrderType=NB từ danh sách mã, gửi POST, sau đó gửi POST MaterialDocumentHeader với mã tham chiếu đơn mua.

## Gotchas
- Lợi ích chỉ xuất hiện trên truy vấn có tín hiệu xử lý (low lexical overlap). Không có cải thiện trên các dịch vụ OpenAPI không có tầng xử lý.
- Bản đồ hoạt động sai làm suy giảm hiệu năng — hiệu năng phụ thuộc vào bản đồ đúng. Hãy kiểm tra bản đồ bằng xác thực nguồn gốc (provenance split) và kiểm tra độ trung thành xây dựng.
- Validator giả lập chia sẻ cùng metadata với đồ thị, nên kết quả gọi không hợp lệ thấp cho thấy việc căn cứ ground-truth khóa thất bại mode theo thiết kế, không đo hiệu năng đối với backend độc lập.
- Nỗ lực tạo bản đồ là thách thức chính: khoảng 20 phút mỗi hoạt động, khoảng 2 ngày làm việc cho 41 hoạt động. Có thể bán tự động bằng LLM đề xuất cạnh (độ chính xác 0.79, độ hồi giữa 0.93) và người kiểm tra.
- Tốc độ hoàn thành vẫn thấp cho cả hai phương pháp (0.387 vs 0.103), hệ thống chưa sẵn sàng cho triển khai thực tế.
