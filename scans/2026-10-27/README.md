# Báo cáo distill arXiv — ngày 2026-10-27

Tổng hợp 6 bài paper đã distill hôm nay (chọn từ 10 bài tốt nhất quét trên arXiv). Mỗi bài đã qua 6 bước distill, commit+push lên GitHub.

## Tổng quan
- Tổng bài distill: **6**
- Tất cả đều có ứng dụng thực tế ([applied] — có thí nghiệm, bộ dữ liệu thật, tiêu chuẩn đánh giá cụ thể).

## Danh sách 6 bài hôm nay

### [1] Mining the Design Space of Multi-Agent Workflows (arXiv 2610.31709)
**Làm gì:** Nghiên cứu cách thiết kế quy trình làm việc của nhiều agent AI (hệ thống nhiều tác nhân AI phối hợp, multi-agent workflow). Paper khẳng định không nên bắt đầu bằng mô hình fan-out độc lập (phân phối tác vụ ra nhiều nhánh không giao tiếp với nhau) mà nên dùng tài liệu chia sẻ liên tục (shared memory — tài liệu nhiều người cùng cập nhật) và mẫu lệnh nhắc cụ thể (prompt template), giúp hiệu quả không kém việc chọn cách agent giao tiếp.

**Học được gì:** Chia agent làm việc riêng lẻ rồi hợp nhất một lần làm giảm hiệu quả. Viết lệnh nhắc chi tiết với các ô trống đặt tên (named placeholder) quan trọng bằng cách chọn cấu trúc liên lạc giữa các agent.

**Áp dụng cho bạn:** Khi xây dựng đội content AI, để các thành viên viết cùng một Google Doc (tài liệu chia sẻ liên tục/shared memory) thay vì mỗi người viết bản nháp riêng rồi người trưởng nhóm hợp nhất một lần.

### [2] DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks (arXiv 2610.32305)
**Làm gì:** Tiêu chuẩn đánh giá khả năng "tự kiềm chế" (self-restraint — khả năng dừng hoặc chuyển hướng khi bằng chứng cho thấy điều kiện chưa đạt) của agent AI trong các tác vụ phân tích nhiều giai đoạn. Kết quả: 13 mô hình đạt 92% trên quyết định tiếp tục (GO) nhưng chỉ 19% trên quyết định dừng (NO-GO), và 47% quyết định NO-GO vẫn thực hiện hành động trên bằng chứng không hợp lệ.

**Học được gì:** Agent AI có thể đoán đúng vấn đề nhưng vẫn thực hiện hành động sai nếu không kiềm chế bản thân. Việc dừng đúng lúc quan trọng bằng việc tiếp tục.

**Áp dụng cho bạn:** Trước khi tự động hóa quy trình bán hàng, thiết lập bước kiểm tra (gate) để hệ thống xác nhận tất cả điều kiện (ví dụ: khách hàng đã đồng ý, thanh toán đã xác nhận) trước khi thực hiện, tránh thực hiện sai bước.

### [3] CauProphet: Teaching Agents to Develop Causal Cognition like Humans (arXiv 2610.32477)
**Làm gì:** Agent phát triển và cập nhật tri thức nhân quả (causal knowledge — hiểu biết về mối quan hệ nguyên nhân và kết quả) từ trải nghiệm để ra quyết định trong tài chính. Cải thiện 25,4% về tương quan hạng (mean rank correlation) so với agent baseline; nâng độ chính xác dự đoán từ 21,3% lên 28,6%.

**Học được gì:** Agent thông minh không chỉ cần ghi nhớ kinh nghiệm, mà cần hiểu rõ mối quan hệ nhân quả giữa các yếu tố để áp dụng vào tình huống mới.

**Áp dụng cho bạn:** Khi phân tích doanh số bán hàng, lưu lại giả thuyết về nguyên nhân doanh số tăng/giảm (ví dụ: giảm giá, sản phẩm mới, thời tiết) cùng bằng chứng, thay vì chỉ nhớ con số, để áp dụng vào mùa sale sau.

### [4] Not Every Agent Needs the Strongest Model: Unified Prompt–Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (arXiv 2610.31743)
**Làm gì:** Không phải mọi agent AI trong hệ thống nhiều agent (heterogeneous — đa dạng) đều cần mô hình mạnh nhất. UniMASO phân bổ mô hình theo vai trò và tối ưu hóa đồng thời lệnh nhắc (prompt) và mô hình, đạt điểm 70,40 (tăng từ 69,79) đồng thời giảm chi phí triển khai có trọng số token (token-weighted deployment cost) 85,2% so với dùng mô hình mạnh nhất cho mọi agent.

**Học được gì:** Phân loại agent theo vai trò và gán mô hình phù hợp (mô hình nhỏ cho công việc đơn giản, mô hình lớn cho suy luận phức tạp) giúp giảm chi phí lớn mà không làm giảm chất lượng.

**Áp dụng cho bạn:** Trong đội chăm sóc khách hàng, dùng mô hình AI nhỏ và rẻ để trả lời câu hỏi thường gặp (FAQ), chỉ dùng mô hình lớn cho các khiếu nại phức tạp — giảm tổng chi phí vận hành mà không ảnh hưởng chất lượng dịch vụ.

### [5] CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments (arXiv 2610.32004)
**Làm gì:** Tiêu chuẩn đánh giá agent sử dụng công cụ trong môi trường doanh nghiệp có trạng thái (stateful — hệ thống ghi nhớ trạng thái giữa các bước). Gồm 555 tác vụ đa lượt trên 9 miền kinh doanh; strict success (thành công nghiêm ngặt — phải đúng mọi bước) trên 16 hệ thống nằm trong khoảng 64,32% đến 83,60%, cho thấy agent hiện tại vẫn khó thực hiện quy trình doanh nghiệp đa giai đoạn chính xác.

**Học được gì:** Agent trả lời đúng câu trả lời cuối cùng không đủ — agent phải thực hiện đúng mọi bước, công cụ, tham số và thứ tự trong quy trình doanh nghiệp.

**Áp dụng cho bạn:** Khi dùng agent AI xử lý đơn hàng hoặc tickets chăm sóc khách hàng, hãy viết ra danh sách kiểm tra (checklist) mỗi bước (gọi công cụ đúng, truyền tham số đúng, thứ tự đúng) và đánh giá agent theo danh sách này, không chỉ đánh giá câu trả lời cuối cùng.

### [6] Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale (arXiv 2609.24152)
**Làm gì:** Phương pháp huấn luyện hệ thống tìm kiếm hình ảnh kết hợp (composed image retrieval — tìm kiếm bằng kết hợp hình ảnh và văn bản) trên độ liên quan phân cấp (4 cấp thay vì nhị phân có/không) bằng VLM (mô hình ngôn ngữ thị giác) tự động tạo dữ liệu. Tăng 4,9%–5,9% NDCG@10 (đo độ chính xác xếp hạng trên 10 kết quả đầu) và đã triển khai production (triển khai thực tế) tại Walmart phục vụ lưu lượng tìm kiếm trực quan thực.

**Học được gì:** Trong tìm kiếm sản phẩm, nhiều sản phẩm có thể thỏa mãn một phần truy vấn của khách hàng. Dùng nhãn liên quan phân cấp (hoàn toàn khớp, khớp phần lớn, khớp một phần, không khớp) giúp hệ thống xếp hạng tốt hơn nhãn có/không.

**Áp dụng cho bạn:** Nếu bạn bán hàng online, hãy gán mức độ phù hợp (phù hợp hoàn toàn, một phần, không phù hợp) cho sản phẩm trong kết quả tìm kiếm thay vì chỉ nhãn có/không, để hệ thống đề xuất chính xác hơn.

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

1. Dùng tài liệu chia sẻ liên tục (shared memory) thay vì mỗi agent làm việc độc lập rồi hợp nhất. Ví dụ: đội content viết cùng một Google Doc thay vì mỗi người viết bản nháp riêng rồi hợp nhất một lần.
2. Phân loại agent theo vai trò, gán mô hình AI nhỏ cho việc đơn giản và lớn cho việc phức tạp. Ví dụ: trong chăm sóc khách hàng, dùng mô hình nhỏ rẻ trả lời FAQ, chỉ dùng mô hình lớn cho khiếu nại phức tạp — giảm chi phí vận hành mà không ảnh hưởng chất lượng.
3. Thiết lập bước kiểm tra (gate) trước khi thực hiện hành động quan trọng. Ví dụ: trước khi triển khai tự động hóa bán hàng, hệ thống phải xác nhận tất cả điều kiện (khách hàng đồng ý, thanh toán xác nhận) trước khi thực hiện.
4. Lưu tri thức nhân quả (nguyên nhân doanh số tăng/giảm) cùng bằng chứng để dùng lại sau. Ví dụ: khi phân tích doanh số, lưu lại giả thuyết nguyên nhân (giảm giá, sản phẩm mới, thời tiết) cùng bằng chứng, áp dụng vào mùa sale sau.
5. Dùng nhãn liên quan phân cấp thay vì có/không trong tìm kiếm sản phẩm. Ví dụ: gán mức độ phù hợp cho sản phẩm trong kết quả tìm kiếm online, hệ thống đề xuất chính xác hơn.

---
Báo cáo viết lại từ dữ liệu distill thực của 6 bài paper hôm nay (#226–#231), không gọi lại mô hình ngôn ngữ.
