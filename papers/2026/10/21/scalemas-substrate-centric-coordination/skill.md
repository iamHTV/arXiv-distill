# Skill: scalemas-substrate-coordination

Source: 2610.16120v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần xây dựng hệ thống đa agent LLM có thể mở rộng theo số agent mà không làm tăng gánh nặng đọc của mỗi agent.
- Khi muốn thiết kế phối hợp agents qua chất đồ thị chung (shared datastore) thay vì dây dritto vào logic của từng agent.
- Khi cần hệ thống agent chịu được sự cố (agent lỗi, agent rời đi, agent mới gia nhập) mà không làm gián đoạn hoạt động nhóm.

## Tình huống KHÔNG nên dùng
- Khi tác vụ đơn giản chỉ cần 1–2 agent, không cần mở rộng nhóm.
- Khi không có kho dữ liệu chung có thể truy xuất hoặc công cụ tìm kiếm để xếp hạng tin nhắn.
- Khi agent phải chạy đồng bộ và chờ nhau (ScaleMAS thiết kế cho không đồng bộ).

## Input cần có
- Kho dữ liệu tin nhắn liên kết chung (append-only sequence of messages).
- Mỗi tin nhắn có 4 trường: tác vụ phụ (u), manufak phẩm (a), lý do (r), tập tham chiếu (R).
- Công cụ tìm kiếm (BM25 hoặc tương đương) để xếp hạng tin nhắn theo nội dung.
- Các agent chạy không đồng bộ, mỗi agent chỉ truy cập kho dữ liệu qua 3 thao tác: publish, search, visit.
- Ngưỡng k (tối đa tin nhắn trả về mỗi lần search) và các tham số trọng số trích dẫn (α, γ).

## Các bước thực hiện
1. Thiết lập kho dữ liệu tin nhắn: mỗi tin nhắn m = (u, a, r, R) ghi lại công việc đã hoàn thành, nhận địa chỉ tiếp theo khi viết, không bao giờ sửa hay xóa, tạo thành đồ thị vô hướng chak qua các tham chiếu.
2. Triển khai 3 thao tác: publish(u,a,r,R) thêm tin nhắn và làm nó có thể đọc được; search(q) trả về tối đa k tin nhắn xếp hạng cao nhất; visit(m₁,…,mⱼ) trả về các tin nhắn theo địa chỉ.
3. Áp dụng quy trình deterministik: publish chỉ chấp nhận nếu mọi tham chiếu tồn tại và lý do tên mọi tham chiếu; trọng số mới bắt đầu s0=0, tăng α(1−sm) khi được trích dẫn, suy γ mỗi bước; tìm kiếm xếp hạng bằng score(q,m) = sm + Rel(q,m)/max Rel.
4. Giới hạn mỗi lần đọc: mỗi lần đọc thêm tối đa k tin nhắn có độ dài bị giới hạn vào ngữ cảnh, bất kể nhóm lớn hay kho dữ liệu lớn đến đâu.
5. Chạy agent không đồng bộ: mỗi agent là LLM agent thông thường dùng công cụ nhiệm vụ và 3 thao tác إضافية, không agent nào giữ vai trò, gửi tin nhắn cho agent khác, hoặc giao công việc cho agent khác.
6. Xử lý sự cố: tin nhắn tồn tại sau khi tác giả rời đi, agent mới đọc kho dữ liệu và bắt kịp bằng tìm kiếm, agent lỗi đơn giản không xuất bản gì.

## Output mong đợi
- Hệ thống đa agent LLM mở rộng được theo số agent, đọc được giới hạn mỗi agent.
- Báo cáo hiệu suất: độ chính xác theo kích thước nhóm, chi phí suy luận (token/ví dụ), số lượt agent.
- Khả năng chịu sự cố: nhóm tiếp tục hoạt động khi agent lỗi hoặc rời đi.

## Ví dụ áp dụng
Một nhóm 16 agent LLM thực hiện nghiên cứu sâu trên kho tài liệu lớn. Mỗi agent viết phát hiện của mình vào kho dữ liệu chung qua publish, tìm kiếm thông tin của người khác qua search (tối đa 10 tin nhắn mỗi lần), và thăm chi tiết qua visit. Tin nhắn được nhiều agent khác trích dẫn sẽ được xếp hạng cao hơn trong tìm kiếm. Khi một agent lỗi, các agent khác tiếp tục làm việc trên tin nhắn đã được xuất bản. Kết quả: trên BrowseComp-Plus, 16 agent ScaleMAS đạt 65.3% so với 38.1% với 1 agent, và tại cùng 20M token/ví dụ, 8 agent ScaleMAS đạt 60.0% so với 16 agent DeLM đạt 26.0%.

## Gotchas
- Không để từ tiếng Anh không giải thích: substrate-centric (tập trung vào chất đồ thị), shared datastore (kho dữ liệu chung), linked messages (tin nhắn liên kết), publish (đăng xuất bản), search (tìm kiếm), visit (thăm), citation weight (trọng số trích dẫn), bounded read (đọc bị giới hạn), lexical relevance (mức liên kết từ vựng), PageRank (hạng trang), DAG (đồ thị vô hướng chak), append-only sequence (danh sách chỉ thêm), deterministic rules (quy trình deterministik), asynchronous agent (agent không đồng bộ), ReAct loop (vòng lặp ReAct), inference compute (chi phí suy luận), token per example (token mỗi ví dụ), dropout (vỡ suất thành viên), resilience (sức kháng lại sự cố), private substrate (kho dữ liệu riêng), blackboard-style (dạng bảng đen), coordinator-based (dựa trên điều phối viên), all-to-all messaging (nhắn tin đều đè), evidence chain (chuỗi bằng chứng), peer citation (trích dẫn từ đồng nghiệp), gold evidence (bằng chứng vàng), division of labor (sự phân công lao động).
- Không có chi phí thiết lập và duy trì kho dữ liệu chung trong thực tế.
- Không đánh giá độ trễ tìm kiếm khi kho dữ liệu rất lớn.
- Không so sánh trực tiếp với các hệ thống phối hợp agent trên sản xuất.
- SWE-bench Verified ổn định sau 8 agent (giới hạn của khả năng LLM).