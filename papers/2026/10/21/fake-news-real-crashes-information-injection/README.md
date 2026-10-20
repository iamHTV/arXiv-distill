# [2610.26438v1] Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents

## Giá trị cốt lõi (1 câu)
Tấn công thông tin injection (information injection) vào LLM trading agents đạt ASR 62%, hơn gấp 4.5 lần so với prompt injection (14%); hai mẫu 30 từ đạt 100% trên tất cả 15 mã cổ phiếu, và chỉ defense phân cấp (star/hierarchical aggregation) giảm ASR xuống 9–10%.

## Problem
Prior work an toàn LLM tập trung vào control-plane (system prompt, role, tool routing, jailbreak), để data-plane — thông tin mà agent được xây dựng để hành động — không được phòng vệ. Một fabricated headline có thể đẩy nhiều agent cùng đọc cùng nguồn vào cùng giao dịch cùng lúc, gây thiệt hại tài chính thực.

## Contribution
1. Đưa ra thông tin injection (information injection) làm một đe dọa data-plane riêng biệt so với control-plane prompt injection, và xây dựng khung tấn công hệ thống cho nó.
2. Đo lường lớn quy mô: trên toàn bộ benchmark, thông tin injection gấp 4.5 lần hiệu quả hơn control injection, tổng quát qua các nhà cung cấp mô hình, và vẫn hiệu quả khi trộn vào nguồn tin thực mà không gắn nhãn.
3. Xây dựng benchmark 62 mẫu chéo năm vector (V1–V5) với bảy danh mục sự kiện, và chỉ ra tiêu chí phòng ngự: đánh giá nội dung tùy vào tư thế của agent và báo cáo ASR tại một tỷ lệ giả dương (FPR) cố định.

## Method
Khung tấn công hoạt động trên hai trục chính là vector (V1–V5: cách nội dung bị làm hỏng) và sự kiện (bảy danh mục: CA corporate action, GI governance/insider, RG regulatory/legal, EA earnings/analyst, MS market structure, MA macro/geopolitical, NA narrative/sentiment). Tham chiếu agent là một trader đơn lệnh (single-shot) trên GPT-4o-mini, nhận ảnh chụp thị trường (OHLCV, RSI, MACD, Bollinger, EMA, ATR, VWAP) và ngữ cảnh tin tức tự do, phát ra quyết định BUY/SELL/HOLD có cấu trúc. Nut tấn công: một công khai trên nền tảng như X (chỉ quyền đăng bài, không biết prompt/mô hình/trọng số agent, không thể sửa mã hay training data). ASR được tính bằng tỷ lệ quyết định thay đổi so với cơ sở良性 (temperature 0 vs 0.1, R=10 lặp). Benchmark gồm 62 mẫu (25 vector-grounded, 37 event-grounded), đánh giá trên 15 mã cổ phiếu Mỹ, khoảng 10.000 quyết định giao dịch. Ba topologie đa agent được kiểm tra: Linear (NewsAnalyst→RiskEvaluator→Trader), Star ({Fundamental, Technical, Sentiment} analyst→Aggregator→Trader), Debate (ba analyst độc lập, tranh luận hai vòng, trader hành động trên toàn bộ bản thảo tranh luận).

## KNOWLEDGE — Số liệu & khái niệm
- Thông tin injection (II) mean ASR: 62%; Control injection (CI) mean ASR: 14%; khoảng cách 4.5× (hoặc 3.8× theo cách thận trọng)
- Hai mẫu V1 fact-poisoning 30 từ ("CEO bị bắt giữ qua đêm", "CFO từ bỏ sau khi thừa nhận tăng doanh thu"): 100% ASR trên tất cả 15 tickers, phương sai 0
- ASR theo mã cổ phiếu: MSFT 34% (kháng cự nhất) đến AMZN 87% (khám-paturated nhất); 6 tên HOLD-baseline trung bình 68%, 5 tên BUY-baseline trung bình 48%
- Vector V4 (structured-signal poisoning, bảng chỉ số kỹ thuật giả mạo): 91% ASR đối với agent định HOLD, 12% đối với agent định BUY
- Vector V1 (fact poisoning): 69% HOLD, 100% BUY (một vector duy nhất mạnh trên cả hai cơ sở)
- Tin cậy bề mặt: xóa danh từ nguồn hoặc khung khẩn trương ("BREAKING") làm ASR sụt từ 100% xuống 0% mặc dù yêu cầu giả không đổi
- Danh mục sự kiện: RG (67%), GI (64%), CA (58%), MS (54%), EA (49%), MA (46%), NA (26%)
- Hướng ngả (steerability): 87% lượt lật thành công khớp với hướng tấn công (474/543)
- Entity grounding: áp dụng mẫu tùy cho mã s sang mã t khác không đổi → 7% ASR trung bình
- Tốc độ giới hạn feed: padding 12–240 headline bổ sung, ASR vẫn 100% ở tất cả 12 cấu hình
- Mô hình lớn hơn: GPT-4o làm V4/V5 xuống 0% nhưng V1 vẫn 93%; GPT-5 (reasoning) 45% mean ASR
- Chéo nhà cung cấp, trộn thực (blended): 46–72% trên 4 mô hình, 3 nhà cung cấp
- Tác động kinh tế: mỗi injection đẩy agent đầu tư $16K (khoảng 80% sức mua $20K) theo hướng attacker chọn
- Defense: Star pipeline (hội tụ phân cấp) giảm ASR xuống 9%; Linear 28%; Debate 74% (không hiệu quả); chỉ hierarchical aggregation giảm ASR đáng kể

## INSIGHT — Cơ chế & tại sao
[Thông tin injection mạnh hơn prompt injection gấp 4.5×] VÌ [payload hướng dẫn không thể覆盖 mục tiêu cố định mà trading policy theo đuổi, nhưng thông tin đối phó chính là nội dung mà policy được xây dựng để hành động, nên nó đi qua policy mà không vi phạm bất kỳ quy tắc nào của nó]. Điều này nghĩa là [benchmark an toàn control-plane không làm an toàn một agent được triển khai làm trader].
[Mẫu fact poisoning đạt 100% ASR] VÌ [yêu cầu giả mang các dấu hiệu Credibility bề mặt (danh từ nguồn, khung khẩn trương) mà agent phản ứng thay vì bằng chứng có thể xác minh]. Điều này nghĩa là [agent xác thực thực thể mà yêu cầu đề cập đến nhưng không xác thực yêu cầu đó].
[Thành công phụ thuộc vào tư thế của agent] VÌ [bảng chỉ số kỹ thuật giả mạo dễ tạo ra một quyết định khi agent định không giao dịch (HOLD), nhưng không thể mâu thuẫn một BUY mà chỉ số thời gian thực của agent đã minh chứng]. Điều này nghĩa là [tấn công viên chọn vector phù hợp với tư thế agent: V4 để tạo ra quyết định mới, V1 để đảo ngược một quyết định mua đã định].
[Phân cấp hoạt động, tranh luậnPeer không hoạt động] VÌ [giai đoạn tổng hợp/risk-review trong topology Star chéo kiểm tra yêu cầu giả định với các đánh giá độc lập của các analyst khác và chỉ số thời gian thực trong ngữ cảnh, trong khi tranh luận hai vòng tạo ra sự đồng thuận giả mạo xung quanh nội dung bị inject]. Điều này nghĩa là [phức tạp kiến trúc chỉ bảo vệ khi họp là phân cấp và chéo kiểm tra; tranh luận đối xứng mang lại ít nhiều sự bảo vệ].

## IDEA — Áp dụng được gì
1. Áp dụng [topology Star/hierarchical aggregation] vào [bảo vệ LLM agent ra quyết định rủi ro cao]: bước đầu là triển khai ba analyst độc lập (cơ bản, kỹ thuật, cảm xúc) + một bộ tổng hợp chéo kiểm tra yêu cầu trước khi trader thực hành, thay vì để một agent đơn xử lý tất cả.
2. Áp dụng [entity grounding] vào [phát hiện nội dung bị làm hỏng]: bước đầu là cấu hình agent để xác thực thực thể mà yêu cầu đề cập đến (mã cổ phiếu, công ty) và từ chối hành động nếu yêu cầu nhắm vào thực thể khác.
3. Áp dụng [action-conditioned gating] vào [giới hạn thiệt hại từ một tấn công đơn lẻ]: bước đầu là đặt ngưỡng chứng minh cao hơn khi khối lượng vị thế thay đổi lớn, sao cho một mục đơn chưa được chứng thực không thể thay đổi danh mục hơn một phần trăm cố định.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Nội dung mà agent được xây dựng để hành động trên đó (data-plane) là bề mặt tấn công lớn hơn so với hướng dẫn hệ thống (control-plane). Áp dụng khi: đánh giá bảo mật cho LLM agent trong lĩnh vực rủi ro cao (tài chính, y tế, pháp lý, vận hành). Không áp dụng khi: chỉ cần benchmark prompt injection cơ bản.
2. Nguyên tắc: Phân cấp với tổng hợp chéo kiểm tra (hierarchical aggregation) là defense duy nhất được đo lường giảm ASR đáng kể; mô hình lớn hơn chỉ giúp một phần. Áp dụng khi: thiết kế kiến trúc agent giao dịch hay quyết định tài chính. Không áp dụng khi:争论 đối xứng (peer debate) được coi là đủ.

## Assumptions & Limitations
- Điều kiện phải đúng: agent đọc nguồn tin công khai không xác thực, agent có chính sách giao dịch cố định (trend-following), attacker chỉ có quyền đăng bài công khai.
- Limitation paper thừa nhận: thí nghiệm online chỉ trong một kịch bản cụ thể; agent tham chiếu đơn giản (130 dòng Python, GPT-4o-mini); không có broker hoặc vốn thực; không có dữ liệu về số lượng agent tự động tham gia trong sự cố crash AP năm 2013.
- Limitation paper KHÔNG nói: chi phí inference thực tế của defense phân cấp so với agent đơn; thời gian trễ thêm từ các bước tổng hợp/chéo kiểm tra; không đánh giá trên các tác vụ không phải giao dịch tài chính (y tế, pháp lý, v.v.).

## Metadata
- Năm: 2026
- Tác giả: Mengxiao Wang, Nitesh Saxena (Texas A&M University)
- Category arXiv: cs.CR
- Link PDF: https://arxiv.org/pdf/2610.26438
- arXiv ID: 2610.26438v1
- Nhãn: [applied]
- Citation count: [không tìm được]