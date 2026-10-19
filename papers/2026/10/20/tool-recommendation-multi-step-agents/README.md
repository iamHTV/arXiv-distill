# [2610.23707v1] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs

## Giá trị cốt lõi (1 câu)
Cho agent đa bước toàn bộ catalog công cụ (khoảng 8.200 công cụ) qua giao diện cố định ba công cụ (SelectTools, UseTool, ListApps) chạy ở gateway, giảm token và chi phí invoiced so với danh sách tĩnh (static list) curated, không cần fine-tune trên công cụ của từng tổ chức.

## Problem
Prior work chưa giải quyết được việc agent.invoke chỉ được các công cụ đã được cấp định nghĩa, trong khi danh sách công cụ có thể cần quá lớn để gửi toàn bộ trên mọi request (khoảng 8.200 công cụ, tổng >1.76M token, vượt context window của mọi model được đánh giá), và danh sách curated ngắn hạn gói hạn agent chỉ làm được những tác vụ danh sách dự đoán trước.

## Contribution
- Hệ thống Tool Recommendation (đã triển khai thực tế tại Arcade): agent nhận ba công cụ cố định qua MCP thay vì danh sách công cụ, SelectTools trả về định nghĩa của các công cụ task cần, UseTool chạy công cụ đó dưới quyền bản thân người dùng cuối, ListApps cho biết ứng dụng nào sẵn sàng.
- Đánh giá chất lượng gợi ý trên ToolRet (7.961 truy vấn qua 44.453 công cụ) và chi phí session end-to-end trên hai agent client (Codex, Claude Code), báo cáo cả Recall@10 và Completeness@10 (tỷ lệ truy vấn có TẤT CẢ công cụ cần trong top-10).
- So sánh với BM25 và các hệ thống công bố có gấp 6-9 lần tham số (7.2B-10.4B đối với 1.2B của Tool Recommendation).

## Method
Kiến trúc hai giai đoạn: giai đoạn 1 truy xuất ứng viên cho mỗi mô tả tác vụ bằng sự kết hợp của lexical (BM25) và dense retrieval; giai đoạn 2 sắp xếp lại các ứng viên hàng đầu bằng cross-encoder đọc cùng lúc tác vụ và công cụ, khi các ứng viên xếp hạng cao đạt điểm gần nhau (trên 99,9% yêu cầu production). Cả hai mô hình được Arcade fine-tune trên ví dụ tác vụ và công cụ hoàn thành chúng. Hệ thống chạy ở gateway giữa agent và công cụ, mỗi lệnh gọi được thực thi dưới quyền chứng thực của người dùng cuối và được kiểm tra hai lần: người dùng đã đồng ý với dịch vụ của công cụ, và công cụ nằm trong phạm vi hợp lệ (eligible scope) của gateway. Giao diện cố định ba công cụ (SelectTools, UseTool, ListApps) có tổng định nghĩa 993 token, khoảng 1.800 lần ít hơn catalog.

## KNOWLEDGE — Số liệu & khái niệm
- Khoảng 8.200 công cụ (8.252 công cụ đến 2026-09-14) trong catalog công khai Arcade, định nghĩa cùng nhau khoảng 1,76 triệu token.
- ToolRet: 7.961 truy vấn qua 44.453 công cụ, 3 danh mục (web API, hàm code, ứng dụng tuỳ chỉnh).
- Completeness@10: Tool Recommendation 45,2% so với BM25 28,8% (tăng 57% tương đối), BM25 là xếp hạng từ vựng (lexical ranking) mà tìm kiếm công cụ thương mại cung cấp.
- Recall@10: 55,2 đối với 37,0 của BM25 (gấp 1,49, 95% CI 1,35-1,78).
- Buổi đề xuất đầu tiên bao quát mọi công cụ mà quy trình đòi hỏi trong 304/327 phiên Codex (93%).
- Số token đầu vào: giảm 17,2% với Codex, 39,6% với Claude Code; phiên Codex trung bình dùng ít 19,0% input.
- Tổng hóa đơn (total bill): giảm 13,6% tổng hợp (95% CI 7,4%-18,4%, p=0,006), mọi phiên trong 14 phiên chạy đều rẻ hơn; theo client: Codex -5,5%, Claude Code -21,8%.
- Hoàn thành tác vụ (task completion): 276/327 Codex với recommendation so với 273/327 danh sách tĩnh (McNemar p=0,80), 74/81 Claude Code so với 76/81.
- Thời gian trả lời dịch vụ xếp hạng: 131 ms trung bình / 292 ms p95, reranking 62 ms/195 ms, cuộc gọi SelectTools khoảng 1,4 giây end-to-end.
- Kích thước mô hình: 1,2B tham số đối với các cơ sở công bố 7,2B-10,4B (gấp đến 9 lần).
- Boộ median Arcade gateway được tạo với 30 công cụ, dưới 0,4% catalog đầy đủ.
- Đánh giá chi phí mô hình: phiên điển hình có 3 tin nhắn người dùng, mỗi tin được trả lời với 8 lệnh gọi công cụ, tỉ lệ tìm kiếm 0,12 tìm kiếm/lệnh gọi công cụ qua 30 ngày sử dụng production trong giai đoạn preview miễn phí của hệ thống.
- Danh sách tĩnh rẻ hơn chỉ dưới khoảng 25-28 công cụ, hoặc khi agent tìm kiếm trên 0,63 lần trên mỗi lệnh gọi công cụ (gấp 5 lần tỷ lệ quan sát được).
- Prompt cache: với Codex, 85% input với recommendation và 87% với danh sách tĩnh được phục vụ từ cache prompt.

## INSIGHT — Cơ chế & tại sao
[Completeness@10 quan trọng hơn Recall@10] VÌ [agent thiếu một công cụ trong chuỗi thì tác vụ thất bại, dù Recall@10 có thể cao]. Điều này nghĩa là [nên đánh giá xếp hạng công cụ theo xem có trả về đủ toàn bộ công cụ một tác vụ cần hay không, không chỉ tỷ lệ công cụ đúng].
[Mỗi lần tìm kiếm thêm một lượt (turn) gửi lại toàn bộ cuộc trò chuyện] VÌ [một lần tìm kiếm đơn lẻ trimbursed (trả lại vốn) cho bản thân nó, ba lần thì không]. Điều này nghĩa là [tần suất tìm kiếm quyết định xem recommendation có rẻ hơn danh sách tĩnh hay không; ngưỡng xấp xỉ 0,63 tìm kiếm trên mỗi lệnh gọi công cụ].
[Giảm token đầu vào không dự đoán tốt hóa đơn (bill)] VÌ [prompt caching (bộ nhớ đệm prompt) chiếm ưu thế trong hóa đơn, token được cache được tính khoảng một phần mười giá cả]. Điều này nghĩa là [điều khoản chi phí nên được đưa ra theo đơn vị tiền tệ, với hành vi cache của client được nêu rõ].
[Danh sách tĩnh (static list) rẻ hơn cho catalog nhỏ (<25-28 công cụ) và tra cứu ngắn (short lookups)] VÌ [mỗi lần tìm kiếm chi một lượt mà danh sách ngắn không cần]. Điều này nghĩa là [dùng danh sách tĩnh cho tập công cụ nhỏ, ổn định; dùng recommendation cho catalog lớn và thay đổi hằng ngày].

## IDEA — Áp dụng được gì
Áp dụng giao diện cố định ba công cụ (SelectTools, UseTool, ListApps) cho hệ thống agent của solopreneur có nhiều công cụ: bước đầu là thiết lập gateway recommendation trước agent, agent chỉ nhận 3 công cụ thay vì danh sách đầy đủ.
Dùng Completeness@10 thay vì Recall@10 để đánh giá hệ thống tìm công cụ: bước đầu là định nghĩa "mỗi tác vụ cần tất cả công cụ nào" và đo tỷ lệ tác vụ có đủ công cụ trong top-k.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Cho agent toàn bộ catalog qua giao diện cố định nhỏ rẻ hơn là curated danh sách ngắn, khi catalog lớn và thay đổi thường xuyên. KHÔNG áp dụng khi catalog nhỏ (dưới 25-28 công cụ) ổn định hoặc agent tìm kiếm quá nhiều (trên 0,63 lần trên mỗi lệnh gọi công cụ).

## Assumptions & Limitations
- Điều kiện đúng: hệ thống chạy qua Arcade gateway, công cụ được phục vụ bởi Arcade gateway, catalog có thể thay đổi hằng ngày.
- Limitation paper thừa nhận: chỉ có sẵn qua Arcade, không ai khác có thể tái tạo kết quả session bên ngoài Arcade; ToolRet đo lường xếp hạng, không phải hành vi agent; tài liệu văn bản tĩnh không thể biểu diễn ngữ cảnh nhiều lượt, trạng thái phân quyền hoặc công cụ phụ thuộc vào đầu ra của lệnh gọi trước; điểm số tuyệt đối của các cơ sở công bố không thể so sánh trực tiếp (chạy trong harness khác); đánh giá chi phí session có phạm vi hạn chế (hai client, 30-34 quy trình gieo, so với danh sách tĩnh 100 công cụ, theo giá niêm yết).
- Limitation paper KHÔNG nói: chi phí vận hành hệ thống xếp hạng ở quy mô lớn; tác động của việc agent đọc lại kết quả đã lưu; chi phí thêm từ các lượt tìm kiếm liên tiếp.

## Metadata
- Năm: 2026
- Tác giả: Sam Partee, River Stevens, Thierry Damiba, Valerie Fanelle (Arcade.dev)
- Category arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2610.23707v1
- arXiv ID: 2610.23707v1
- Nhãn: [applied]
- Skill: tool-recommendation-multi-step-agents | Test: [SKILL VALID]
