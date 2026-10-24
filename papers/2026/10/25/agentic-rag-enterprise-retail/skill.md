# Skill: Xây dựng tác tử RAG cho bán lẻ doanh nghiệp trên nhiều nguồn dữ liệu (RetailRAG)

Source: 2610.25096v1
Type: workflow

## Khi nào dùng skill này

- Cần xây dựng tác tử truy xuất dữ liệu doanh nghiệp trên nhiều nguồn dữ liệu khác nhau (bảng SQL, văn bản, API).
- Truy vấn yêu cầu kết nối bằng chứng qua nhiều nguồn (multi-source chaining) chứ không chỉ truy xuất từ một nguồn đơn.
- Muốn giảm chi phí API call và cải thiện độ chính xác cho tác tử truy xuất dữ liệu bán lẻ/doanh nghiệp.

## Tình huống KHÔNG nên dùng

- Dữ liệu chỉ nằm ở một nguồn đơn nhất và truy vấn không cần kết nối bằng chứng qua nhiều nguồn.
- Không cần hiểu lược đồ dữ liệu trước khi lập kế hoạch truy vấn.
- Không cần khôi phục cục bộ khi bước gọi hàm thất bại.

## Input cần có

- Cơ sở dữ liệu doanh nghiệp đa dạng (bảng có cấu trúc và văn bản không cấu trúc).
- Lược đồ dữ liệu (schema): tên bảng, tên cột, kiểu dữ liệu, ràng buộc giá trị phân loại, khóa căn chỉnh thực thể, chỉ số phân tích dẫn xuất.
- Mô hình LLM backbone có khả năng gọi hàm và lập kế hoạch multi-bước.
- Công cụ truy xuất: SQL engine cho bảng, retrieval engine cho văn bản.
- Môi trường gọi API LLM với khả năng theo dõi số lần gọi.

## Các bước thực hiện

1. Xây dựng bản tóm tắt lược dữ liệu (auto-schema briefing): kiểm định tự nhiên từng cột (numeric, categorical, free-text), LLM tổ chức thành 4 phần (tóm tắt lượcadro và siêu dữ liệu, ràng buộc giá trị phân loại, khóa căn chỉnh thực thể, chỉ số phân tích dẫn xuất).
2. Chèn bản tóm tắt lược dữ liệu vào prompt của lập kế hoạch trước khi lập kế hoạch bắt đầu.
3. Lập kế hoạch multi-bước (source-routed plan chaining): adaptive router đánh giá độ phức tạp truy vấn, định tuyến truy vấn đơn giản trực tiếp đến một công cụ, giữ vòng lập kế hoạch cho truy vấn đa nguồn. Lập kế hoạch sinh toàn bộ chuỗi trong một lần đi, mỗi bước chỉ định nguồn và truy vấn tìm kiếm, các bước sau tham chiếu kết quả trước đó dưới dạng biến.
4. Thực thi từng bước kế hoạch trên công cụ được khai báo, thay thế giá trị trước đó theo kiểu định danh (deterministically substituted) vào bước kế tiếp.
5. Khi bước thất bại giữa chuỗi, chỉ sửa bước thất bại (diagnostic plan revision): diagnose — LLM nhận diện lỗi từ tín hiệu thực thi (kết quả rỗng, tổng hợp bằng không) và gán nguyên nhân kiểu (schema mismatch, over-restrictive filter); revision — LLM viết lại chỉ bước thất bại dựa trên nguyên nhân đã chẩn đoán, giữ các bước đã hoàn thành intact.
6. Đánh giá: tính độ chính xác (Acc) và LLM-as-judge trên tập truy vấn đa nguồn, theo 3 chẩn đoán (độ sâu suy luận, độ đa dạng nguồn, kiểu bằng chứng).

## Output mong đợi

- Một tác tử truy xuất dữ liệu doanh nghiệp có thể chạy trên nhiều nguồn, đạt độ chính xác cao trên truy vấn đa nguồn multi-hop.
- Giảm số lần gọi API so với các cơ sở agentic RAG truyền thống.
- Khả năng khôi phục từ lỗi tại bước thất bại mà không cần bắt đầu lại toàn bộ quy trình.

## Ví dụ áp dụng

Solopreneur tại Việt Nam xây dựng tác tử hỗ trợ quản lý bán hàng online: truy xuất từ bảng đơn hàng (SQL) và đánh giá khách hàng (văn bản) để trả lời "sản phẩm nào có đánh giá cao nhất trong tháng qua và tổng doanh thu từ đơn hàng của sản phẩm đó là bao nhiêu". Tác tử dùng auto-schema briefing để hiểu cấu trúc bảng đơn hàng và bảng đánh giá, định tuyến bước 1 đến bảng đánh giá (văn bản) để tìm sản phẩm có đánh giá cao, bước 2 đến bảng đơn hàng (SQL) để tính tổng doanh thu, kết nối bằng chứng qua hai bước.

## Gotchas

- Đa nguồn chaining là Bottleneck (måg thắt cổ chai) dominante: hầu hết các cơ sở giảm mạnh khi truy vấn cần kết nối qua nhiều nguồn, không phải chỉ truy xuất mỗi bước.
- Mở rộng mô hình (scaling alone) không giải quyết được vấn đề; cần phối hợp đa nguồn rõ ràng.
- Text retrieval là Bottleneck kiểu bằng chứng dominante: truy vấn văn bản chỉ suy yếu hơn truy vấn bảng SQL.
- Khả năng kết nối đa nguồn tăng theo quy mô mô hình, không phải theo loại mô hình.
- Không có Limitations section rõ rệt trong paper (kết thúc tại Conclusion rồi sang References).
- Không đánh giá chi phí lưu trữ và bảo trì, không đánh giá độ ổn định khi dữ liệu thay đổi theo thời gian.