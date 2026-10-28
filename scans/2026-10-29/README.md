# Báo cáo distill arXiv — ngày 2026-10-29

Tổng hợp 3 bài paper đã distill hôm nay. Mỗi bài đã qua 6 bước distill, commit+push lên GitHub.

## Tổng quan
- Tổng bài distill: 3
- Tất cả đều có ứng dụng thực tế cho solopreneur và hệ thống AI agent (tác nhân AI có thể thực hiện hành động).

### [1] Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses (arXiv 2610.36114v1)

**Làm gì:** Paper nghiên cứu lý do agent AI (tác nhân AI tự hành) thường mất bằng chứng khi gọi công cụ (tool). Máy bọc agent (agent harness — phần mềm nằm giữa model AI và công cụ) cắt kết quả công cụ theo vị trí ký tự chứ không theo giá trị, nên bằng chứng quan trọng ở cuối bị xóa hoàn toàn trong khi cửa sổ ngữ cảnh (context window — vùng nhớ chứa đoạn văn model đang xử lý) vẫn trống 93%. Trên 11.189 kết quả công cụ, 34% bị cắt và thành JSON hỏng (JavaScript Object Notation — định dạng trao đổi dữ liệu). Lỗi chẩn đoán sai có thể nằm ở máy bọc chứ không phải model.

**Học được gì:** Không nên chỉ đo độ chính xác (accuracy — tỷ lệ kết quả đúng) khi đánh giá hệ thống agent. Cần đo tỷ suất kết quả (yield — tỷ lệ bằng chứng đã đến model so với đã sản xuất) tại mỗi ranh giới (boundary — điểm giao nối giữa các bước) của đường truyền thông tin, và đếm số lần gọi công cụ. Một agent có đường đi khác sẽ tìm cách khác trước khi trả lời sai, nên tổn thất đầu tiên là công việc dư thừa chứ không phải sai sót ngay.

**Áp dụng cho bạn:** Khi xây dựng hệ thống agent gọi API (ví dụ agent chăm sóc khách hàng gọi API đơn hàng), hãy thiết bị đo (instrument — cài công cụ theo dõi) mỗi ranh giới pipeline (ống truyền — chuỗi các bước xử lý dữ liệu), đếm bằng chứng đã đến so với đã sản xuất, và báo cáo yield bên cạnh accuracy trên mọi bản đánh giá. Thay cắt theo ký tự, hãy cắt theo dòng hoặc theo trường JSON để không xóa bằng chứng quan trọng.

### [2] Do We Need an LLM to Know Why Sources Conflict? Decision Models for Knowledge-Conflict Typing in RAG (arXiv 2610.36915v1)

**Làm gì:** Paper giới thiệu decision model (mô hình quyết định — trả về xác suất các lựa chọn cố định trong một lần xử lý forward pass, không sinh văn bản) để phân loại loại xung đột giữa các nguồn thông tin trong hệ thống RAG (tìm kiếm bổ trợ sinh văn bản — kĩ thuật tìm kiếm thông tin ngoài để sinh câu trả lời). 11 mô hình quyết định từ 7 nhà cung cấp phân loại đúng gần bằng LLM nhưng tốn 4–39× ít chi phí và nhanh 2.6–6.0 lần. Độ tin cậy (confidence — mức độ chắc chắn của model) xếp hạng được lỗi, nên có thể chỉ gửi phần truy vấn không tự tin lên LLM cao cấp (cascade — thang thăng, chuyển phần khó sang model đắt hơn) với chi phí chỉ 25–37% của LLM.

**Học được gì:** Phân loại (classify — gán nhãn) rẻ hơn sinh (generate — viết văn bản). Trong hệ thống RAG, hãy thay prompt LLM dài (lệnh nhắc dài) bằng một decision model rẻ để phân loại xung đột giữa các nguồn tìm kiếm, sau đó chỉ sinh câu trả lời theo loại đó. Gửi 25% truy vấn không tự tin nhất đến LLM cao cấp, giữ 75% cho decision model — giảm 63–75% chi phí LLM trong khi giữ độ chính xác ngang LLM.

**Áp dụng cho bạn:** Nếu bạn dùng RAG để trả lời khách hàng từ nhiều nguồn (website, tài liệu, email) và các nguồn mâu thuẫn, hãy dùng một decision model rẻ để phân loại loại xung đột (thông tin bổ sung, ý kiến trái charg, thông tin cũ, thông tin sai), chỉ gọi LLM đắt tiền cho phần không tự tin. Ví dụ: phân loại email khách hàng thành chủ đề cố định (khiếu nại, hỏi giá, hỗ trợ kỹ thuật) bằng decision model, chỉ leo thăng (chuyển lên cấp cao hơn) email không tự tin lên LLM cao cấp hoặc nhân viên người.

### [3] Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation (arXiv 2610.37242v1)

**Làm gì:** Paper xây dựng hệ thống giúp agent LLM gọi API (điểm kết nối dịch vụ — giao diện cho phần mềm trao đổi dữ liệu) doanh nghiệp tin cậy qua nhiều bước. Agent chọn đúng API nhưng vẫn thất bại vì nó phát mã (hallucinate — tạo ra thông tin/mã không tồn tại), bỏ tham chiếu bắt buộc, hoặc đặt khách sạn trước chuyến bay (vi phạm thứ tự xử lý). Paper kết hợp metadata OData (tiêu chuẩn dịch vụ web đọc và ghi dữ liệu qua HTTP) và quy trình BPMN (tiêu chuẩn mô tả quy trình doanh nghiệp) vào một typed property graph (đồ thị thuộc tính có kiểu — lưu dữ liệu dưới dạng nút và cạnh có hướng, cả hai mang nhãn kiểu và thuộc tính khóa-giá trị), dùng hybrid retrieval (tìm kiếm lai — kết hợp hạt giống dense embedding với mở rộng theo cạnh quy trình). Agent hoàn thành 38.7% tác vụ so với ChunkRAG 10.3%, và tỷ lệ cuộc gọi API không hợp lệ giảm từ 79% xuống 3%.

**Học được gì:** Chọn endpoint đúng (điểm cuối — địa chỉ cụ thể của một hàm API) chưa đủ — agent cần cả ràng buộc thứ tự xử lý (process constraint — quy tắc về thứ tự các bước) và ràng buộc tham số (các khóa bắt buộc, mã hợp lệ) trong ngữ cảnh truy xuất. Cung cấp toàn bộ ngữ cảnh có kiểu (full typed context) trước khi gọi API giúp giảm cuộc gọi không hợp lệ xuống 3%. Lợi ích chỉ xuất hiện trên truy vấn có tín hiệu xử lý.

**Áp dụng cho bạn:** Khi xây dựng agent tự động hóa gọi nhiều API doanh nghiệp theo thứ tự (ví dụ hệ thống đặt vé: chọn chuyến bay → đặt chỗ → đặt khách sạn bằng mã tham chiếu, theo đúng thứ tự và mã hạng ghế hợp lệ), hãy cung cấp schema (cấu trúc dữ liệu) và quy trình xử lý trong ngữ cảnh truy xuất, chứ không chỉ danh sách endpoint. Xây dựng một typed property graph kết hợp metadata dịch vụ và quy trình tham chiếu, liên kết từng hoạt động với dữ liệu nó đọc hoặc ghi.

## CÓ GÌ ÁP DỤNG ĐƯỢC CHO BẠN

1. **Đo yield (tỷ suất kết quả) tại mỗi ranh giới pipeline, không chỉ đo accuracy.** Khi đánh giá agent gọi công cụ, hãy đếm bằng chứng đã đến model so với đã sản xuất, và báo cáo yield cùng accuracy. Ví dụ: agent chăm sóc khách hàng gọi API đơn hàng, hãy theo dõi xem kết quả API có đầy đủ không trước khi model đọc.

2. **Dùng decision model rẻ để phân loại trước khi gọi LLM cao cấp.** Trong hệ thống RAG hoặc phân loại nội dung, hãy thay prompt LLM dài bằng một mô hình quyết định rẻ để gán nhãn, chỉ leo thăng (chuyển lên) phần không tự tin lên LLM đắt. Ví dụ: phân loại email khách hàng bằng decision model, chỉ leo thăng email không tự tin lên nhân viên hoặc LLM cao cấp — giảm 63–75% chi phí.

3. **Cung cấp toàn bộ ràng buộc xử lý và tham số trước khi agent gọi API.** Không chỉ cho agent danh sách endpoint. Hãy cung cấp schema, các khóa bắt buộc, mã hợp lệ và thứ tự xử lý trong ngữ cảnh truy xuất. Ví dụ: agent đặt vé doanh nghiệp cần mã hạng ghế hợp lệ và thứ tự đặt chỗ trước khách sạn — cung cấp quy trình này để tránh cuộc gọi API sai (giảm từ 79% xuống 3% cuộc gọi không hợp lệ).
