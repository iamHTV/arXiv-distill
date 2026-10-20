# [2610.16120v1] Scaling Multi-Agent Intelligence with Substrate-Centric Coordination

## Giá trị cốt lõi (1 câu)
ScaleMAS là một lớp hạ tầng (substrate) cho đa agent LLM: các agent tương tác qua kho dữ liệu tin nhắn liên kết chung bằng 3 thao tác (publish, search, visit), đọc được giới hạn k tin nhắn mỗi lần bất kể nhóm lớn, xếp hạng bằng liên kết trích dẫn, và continous scale lên đến 128 agent với chi phí suy luận thấp hơn các cơ chế phối hợp tập trung vào agent.

## Problem
Các hệ thống đa agent LLM hiện tại mở rộng kém: gánh nặng đọc tăng theo nhóm, thông tin hữu íc bị loãng bởi công việc chung chất lượng không xác định, và dễ gãy do agent lỗi. Các thiết kế tập trung vào agent (luồng công việc cố định, điều phối viên trung tâm, nhắn tin đều điffer) khiến việc đọc không giới hạn và một agent lỗi có thể làm hệ thống sập.

## Contribution
1. Xây dựng ScaleMAS: một lớp hạ tầng tác tử độc lập nhiệm vụ, nơi các agent không đồng bộ tương tác với kho dữ liệu tin nhắn liên kết qua 3 thao tác: publish (đăng tin nhắn với tùy chọn tham chiếu các tin nhắn trước đó), search (tìm theo nội dung, trả về tối đa k tin nhắn), visit (thăm tin nhắn theo địa chỉ).
2. Trọng số trích dẫn: tin nhắn bắt đầu tại trọng số 0, tăng một phần α hướng về 1 khi được tham chiếu, suy giảm γ mỗi bước; tìm kiếm xếp hạng bằng trọng số trích dẫn cộng với điểm liên kết lexical chuẩn hóa.
3. Đánh giá trên 4 nhiệm vụ tác tử (BrowseComp-Plus, FATE, SWE-bench Verified, Contradiction Audit) với 2 bộ xương (Qwen3.5-9B, Claude-5-Sonnet), so sánh với Multi-Agent Debate, DeLM, AOrchestra, và ReAct song song.

## Method
ScaleMAS gồm 3 phần: (1) kho dữ liệu tin nhắn, mỗi tin nhắn m = (u, a, r, R) ghi lại một công việc đã hoàn thành: tác vụ phụ u, manufak phẩm a, lý do ngắn r, và tập tham chiếu R đến công việc trước đó hoặc tài nguyên từ công cụ nhiệm vụ; mỗi tin nhắn nhận địa chỉ tiếp theo khi viết, không bao giờ được sửa hay xóa, tạo thành một đồ thị vô hướng chak về D; mỗi tin nhắn mang trọng số trích dẫn sm ∈ [0, 1). (2) Ba thao tác: publish(u,a,r,R) thêm tin nhắn và làm nó có thể đọc được bởi mọi agent; search(q) nhận mô tả văn bản tự do về những gì agent cần và trả về k tin nhắn xếp hạng cao nhất; visit(m1,…,mj) trả về các tin nhắn được chỉ định. (3) Các quy trình deterministik quyết định những gì được viết và những gì một lần đọc trả về. Các quy trình: publish chỉ chấp nhận tin nhắn nếu mọi tham chiếu trỏ đến sesu dụng tồn tại và lý do tên mọi tham chiếu và nói rõ nó đóng góp gì; trọng số mới bắt đầu s0 = 0, khi tin nhắn m được tham chiếu, sm ← sm + α(1−sm), và mỗi bước tất cả trọng số suy giảm sm ← γsm; tìm kiếm xếp hạng bằng score(q,m) = sm + Rel(q,m)/max Rel; mọi lần đọc thêm tối đa k tin nhắn có độ dài bị giới hạn vào ngữ cảnh, bất kể có bao nhiêu agent đang viết và D đã lớn đến đâu.

## KNOWLEDGE — Số liệu & khái niệm
- 4 nhiệm vụ: BrowseComp-Plus (tìm kiếm thi sâu), FATE (chứng minh định lý Lean 4), SWE-bench Verified (giải quyết vấn đề GitHub thực), Contradiction Audit (xác định mâu thuẫn trong tài liệu phần mềm, do tác giả xây dựng)
- 2 bộ xương: Qwen3.5-9B, Claude-5-Sonnet
- 4 cơ chế so sánh: Parallel ReAct (không giao tiếp), Multi-Agent Debate (MAD, nhắn tin đều đè), DeLM (blackboard-style, ngữ cảnh chung), AOrchestra (điều phối viên trung tâm)
- Kết quả Qwen3.5-9B: BrowseComp-Plus 38.1% (1 agent) → 65.3% (16 agent); FATE-M 24.0% → 56.0%; Contradiction Audit x4 4.1% → 29.4%; SWE-bench Verified ổn định sau 8 agent
- Claude-5-Sonnet: Contradiction Audit x8 10.6% (1 agent) → 57.5% (8 agent)
- Hiệu quả chi phí suy luận: BrowseComp-Plus ~20M token/ví dụ, 8 ScaleMAS agent đạt 60.0% vs 16 DeLM agent đạt 26.0%; SWE-bench Verified 4 ScaleMAS agent đạt 80.0% với 15.3M token vs 8 ReAct agent 28.3M token
- Claude BrowseComp-Plus ~3.5M token/ví dụ: 8 ScaleMAS 79.8% vs 8 MAD 73.0% vs 4 ReAct 72.0%
- MAD tokens/tăng từ 5.6M (2 agent) lên 48.5M (16 agent) nhưng accuracy đứng yên 28–32%
- Scale lên 128 agent (Qwen3.5-9B): FATE-M ScaleMAS ổn định dưới 60% ở N=16, MAD đạt đỉnh ở N=32 rồi giảm, DeLM thấp hơn ở N=128 so với N=8; Contradiction Audit x4 ScaleMAS đạt 50.9% ở N=128, DeLM/MAD chưa qua 7%
- Sức kháng lại sự cố: 1 agent lỗi vĩnh viễn, ScaleMAS với 7 agent khỏe đạt 19.4% (giống 7 agent khỏe đơn lẻ), DeLM sụt dưới 1%; p=0.8 dropout: 8 ScaleMAS agent giải quyết 22.0% FATE-M vs 2.0% với 1 agent; AOrchestra mất hơn nửa điểm số ở p=0.2 (mất điều phối viên)
- Khử trọng số trích dẫn: N=8, BrowseComp-Plus 60.0%→40.8%, Contradiction Audit x4 23.1%→9.7%; FATE-M N=8: 49.0% vs 42.0%, BM25 đọc gấp đôi token (5.7M vs 2.7M)
- Kho dữ liệu riêng (phân vùng theo tác giả): giảm độ chính xác 8.3 điểm BrowseComp-Plus, 8.4 SWE-bench Verified
- Không kho dữ liệu (ReAct độc lập): Contradiction Audit 8.1% vs 6.6% (ScaleMAS)
- Trích dẫn từ đồng nghiệp: tin nhắn trên chuỗi bằng chứng của câu trả lời đúng tăng từ 29% (quintile ít trích nhất) lên 85% (quintile trích nhiều nhất); tin nhắn tên tài liệu bằng chứng vàng nhận gấp 2 lần trích dẫn so với tài liệu khác
- Đáp án đúng được lắp ráp qua các agent: tỷ lệ đáp án đúng có chuỗi bằng chứng chứa tin nhắn của agent khác tên tài liệu vàng mà agent nộp chưa từng mở: từ 9% (2 agent) lên 24% (8 agent)

## INSIGHT — Cơ chế & tại sao
[ScaleMAS mở rộng tốt hơn các cơ chế tập trung vào agent] VÌ [mỗi lần đọc trả về tối đa k tin nhắn, được xếp hạng bởi liên kết trích dẫn và mức liên kết lexical, nên lượng đọc của agent không tăng theo kích thước nhóm; tin nhắn tồn tại sau khi tác giả rời đi, nên nhóm tiếp tục chạy khi agent cá nhân lỗi]. Điều này nghĩa là [phối hợp nên được thiết kế vào chất đồ thị mà agent chia sẻ thay vì dây dritto vào chính các agent].
[Trọng số trích dẫn tự động điều phối kho dữ liệu] VÌ [trọng số chỉ tích lũy khi người khác xây dựng trên một tin nhắn, do tìm kiếm bật lên những gì nhóm thực sự đã dựa vào, và tín hiệu được tăng cường khi kho dữ liệu lớn]. Điều này nghĩa là [chất lượng được kiếm mérite thông qua sử dụng lại, không phải do thẩm phán tập trung].
[Đáp án đúng được lắp ráp qua các agent] VÌ [các agent ngày càng trả lời bằng cách kết hợp bằng chứng mà người khác đã tìm, và nhiều đáp án đúng hơn dựa trên nó khi nhóm lớn]. Điều này nghĩa là [sự phân công lao động hiện ra mặc dù không agent nào được giao tiểu nhiệm vụ nào].
[Một agent lỗi không làm hỏng nhóm] VÌ [ScaleMAS không giao công việc cho agent và không yêu cầu agent hoàn thành bất kỳ việc gì; agent lỗi đơn giản không xuất bản gì, còn agent khỏe tiếp tục tìm và xây dựng trên tin nhắn của nhau]. Điều này nghĩa là [thành viên linh hoạt thay đổi — thành viên mới đọc kho dữ liệu và bắt kịp bằng tìm kiếm, thành viên rời đi không mang theo gì].

## IDEA — Áp dụng được gì
1. Áp dụng [substrate-centric coordination] vào [xây dựng hệ thống đa agent LLM mở rộng]: bước đầu là thiết lập kho dữ liệu tin nhắn liên kết chung, các agent chỉ tương tác qua publish/search/visit, mỗi lần đọc giới hạn k tin nhắn.
2. Áp dụng [trọng số trích dẫn từ peer] vào [xếp hạng thông tin chung mà không cần thẩm phán tập trung]: bước đầu là theo dõi tin nhắn nào được các agent khác trích dẫn và dùng số lần trích dẫn làm tín hiệu chất lượng cho tìm kiếm.
3. Áp dụng [sức kháng lại sự cố agent] vào [thiết kế hệ thống agent liên tục hoạt động]: bước đầu là để tin nhắn tồn tại sau khi tác giả rời đi, không giao công việc cố định cho agent, nên agent mới có thể gia nhập và agent rời đi không làm gián đoạn.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Phối hợp đa agent nên được thiết kế vào chất đồ thị chung (shared datastore, search-bounded reads, persistent messages) thay vì dây dritto vào logic của các agent. Áp dụng khi: xây dựng hệ thống đa agent cần mở rộng theo số agent. Không áp dụng khi: tác vụ đơn giản chỉ cần 1–2 agent.
2. Nguyên tắc: Tín hiệu chất lượng có thể được kiếm merits qua việc sử dụng lại (citation/reuse) thay vì đánh giá tập trung. Áp dụng khi: cần xếp hạng thông tin chung trong hệ thống mở lớn. Không áp dụng khi: không có cơ chế theo dõi việc sử dụng lại thông tin.

## Assumptions & Limitations
- Điều kiện phải đúng: agent có thể chạy không đồng bộ, có kho dữ liệu chung có thể truy xuất, có công cụ tìm kiếm (BM25 hoặc tương đương) để xếp hạng tin nhắn.
- Limitation paper thừa nhận: ScaleMAS là harness-agnostic (chạy trên ReAct loop tiêu chuẩn), không đánh giá trên các tác vụ ngoài 4 benchmark đã chọn; SWE-bench Verified ổn định sau 8 agent (giới hạn của khả năng LLM).
- Limitation paper KHÔNG nói: không có chi phí thiết lập và duy trì kho dữ liệu chung trong thực tế; không đánh giá độ trễ của tìm kiếm khi kho dữ liệu rất lớn; không so sánh trực tiếp với các hệ thống phối hợp agent hiện có trên sản xuất.

## Metadata
- Năm: 2026
- Tác giả: Zhenting Qi, Zhuokai Zhao, Rulin Shao, Kerem Oktar, Zhiyuan Yao, Himabindu Lakkaraju, Wen-tau Yih, Ansong Ni, Bhargavi Paranjape, Yilun Du (FAIR at Meta, Meta AI, Harvard, Kempner Institute)
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.16120
- arXiv ID: 2610.16120v1
- Nhãn: [applied]
- Citation count: [không tìm được]