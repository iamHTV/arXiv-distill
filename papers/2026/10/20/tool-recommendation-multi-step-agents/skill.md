# Skill: tool-recommendation-multi-step-agents
Source: 2610.23707v1
Type: framework

## Khi nào dùng skill này
- Hệ thống agent có nhiều công cụ (catalog lớn, thay đổi hằng ngày) và agent không thể nhận định nghĩa toàn bộ công cụ trên mỗi request.
- Muốn giảm chi phí invoiced và số token đầu vào cho tác vụ agent đa bước mà không giảm tỷ lệ hoàn thành.
- Có một gateway giữa agent và công cụ có thể thực thi lệnh gọi dưới quyền người dùng cuối và kiểm tra phân quyền.

## Tình huống KHÔNG nên dùng
- Catalog công cụ nhỏ (dưới 25-28 công cụ) và ổn định → danh sách tĩnh (static list) rẻ hơn.
- Agent tìm kiếm quá nhiều (trên 0,63 lần trên mỗi lệnh gọi công cụ) → mỗi lần tìm kiếm chi thêm một lượt, recommendation không tiết kiệm.

## Input cần có
- 1 Arcade gateway (hoặc tương đương) đứng giữa agent và catalog công cụ.
- Danh sách công cụ có định nghĩa (name, description, argument documentation) để lập chỉ mục (index).
- 2 mô hình xếp hạng: mô hình truy xuất融 hợp (BM25 + dense) và cross-encoder reranker (hoặc có thể thay bằng mô hình tương đương).
- Hệ thống ghi lại quyền đồng ý (consent) của người dùng cho từng dịch vụ/công cụ.
- Agent client có thể gọi ba công cụ cố định: SelectTools, UseTool, ListApps.

## Các bước thực hiện
1. Thiết lập gateway recommendation giữa agent và catalog; agent không nhận catalog trực tiếp, chỉ nhận ba công cụ cố định qua MCP.
2. Lập chỉ mục từng công cụ (tên, mô tả, tài liệu tham số) vào chỉ mục tìm kiếm kết hợp lexical (BM25) và dense retrieval.
3. Khi agent mô tả một tác vụ, SelectTools truy xuất ứng viên cho mỗi mô tả tác vụ bằng sự kết hợp BM25 và dense, rồi cross-encoder sắp xếp lại ứng viên hàng đầu (khi các ứng viên xếp hạng cao đạt điểm gần nhau).
4. Trả về định nghĩa của 5 công cụ xách hàng đầu cho mỗi mô tả tác vụ; agent chọn và gọi công cụ qua UseTool dưới quyền người dùng cuối.
5. Kiểm tra phân quyền hai lần: người dùng đã đồng ý với dịch vụ của công cụ, và công cụ nằm trong phạm vi hợp lệ (eligible scope) của gateway.
6. Đánh giá chất lượng bằng Completeness@10 (tỷ lệ truy vấn có tất cả công cụ cần trong top-10) thay vì chỉ Recall@10, vì thiếu một công cụ trong chuỗi khiến tác vụ thất bại.
7. Đo chi phí session end-to-end (tổng hóa đơn, không chỉ input tokens) so với danh sách tĩnh 100 công cụ; nếu agent tìm kiếm trên 0,63 lần/mỗi lệnh gọi công cụ, hãy dùng danh sách tĩnh thay vì recommendation.

## Output mong đợi
- Agent nhận được mọi công cụ nó cần từ catalog lớn, chi phí hóa đơn giảm (đã giảm 13,6% tổng hợp trong 14 phiên chạy), tỷ lệ hoàn thành tác vụ không thay đổi.

## Ví dụ áp dụng
- Solopreneur chạy agent chăm sóc khách hàng kết hợp Gmail, Slack, Google Drive, Salesforce: thay vì cấp 100 công cụ tĩnh trên mọi request, cài gateway recommendation, agent gọi SelectTools khi cần công cụ từ một ứng dụng, nhận định nghĩa 5 công cụ xách hàng đầu, chạy qua UseTool, chi phí session giảm khoảng 20%.

## Gotchas
- Không so sánh điểm số tuyệt đối giữa các hệ thống xếp hạng chạy trong harness khác; chỉ so sánh lift (tăng trưởng) so với BM25 của chính harness đó.
- Không báo cáo chi phí chỉ qua input tokens; prompt caching làm cached tokens được tính rẻ hơn gấp 10 lần, phải báo cáo theo dollars.
- Completeness@10 là thước đo nghiêm ngặt hơn Recall@10; thiếu một công cụ trong chuỗi nhiều bước khiến tác vụ thất bại.
- Mỗi lần tìm kiếm thêm một lượt gửi lại toàn bộ cuộc trò chuyện; tìm kiếm 3 lần trở lên có thể dùng nhiều input hơn danh sách tĩnh.
- Hệ thống chỉ có sẵn qua Arcade; không tái tạo được kết quả session bên ngoài Arcade.

## Kiểm tra kỹ năng (self-check)
- Người không đọc paper gốc có follow được 7 bước trên không? [YES] — từng bước là action cụ thể.
- Bước nào mơ hồ nhất? Bước 2-3 (lập chỉ mục BM25+dense và cross-encoder rerank) cần chi tiết triển khai cụ thể.
- Input section có đủ không? [YES] — gateway, catalog, 2 mô hình xếp hạng, hệ thống consent, agent client.

## Dry run (tình huống giả)
- Tình huống: Solopreneur có agent hỗ trợ Verkauf sử dụng 200 công cụ trên Slack, HubSpot, Gmail; catalog thay đổi hàng tuần khi thêm tích hợp mới.
- Chạy skill: (1) Cài gateway recommendation giữa agent và 200 công cụ; (2) lập chỉ mục tên+mô tả+tham số của mỗi công cụ; (3) agent gọi SelectTools khi cần thực hiện một tác vụ (ví dụ "tìm lead trong HubSpot rồi gửi email"); (4) nhận 5 định nghĩa công cụ xách hàng đầu, gọi UseTool theo quyền người dùng; (5) kiểm tra consent và eligible scope trước khi thực thi; (6) đánh giá Completeness@10 trên 50 tác vụ thực; (7) đo tổng hóa đơn so với danh sách tĩnh 100 công cụ, nếu tìm kiếm <0,63 lần/lệnh gọi công cụ thì giữ recommendation.

## Verdict: [SKILL VALID]
