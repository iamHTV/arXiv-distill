# [2609.31704v1] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games

## Giá trị cốt lõi (1 câu)
Đánh giá độ mạnh phối hợp của nhóm agent LLM khi thông tin công khai bị hỏng: phải tách biệt lựa chọn gốc của agent, hành động công khai nhìn thấy, và kết quả thực thi — vì sự sụp đổ phối hợp có thể do biến đổi hành động máy tính (mechanical) chứ không phải do hành vi agent thay đổi.

## Problem
Prior work chưa giải quyết việc phân biệt giữa sự thay đổi trong lựa chọn của chính agent và hậu quả cơ học trực tiếp của việc biến đổi hành động công khai, khi đánh giá sự mạnh mẽ phối hợp đa agent trong môi trường thông tin công khai không tin cậy.

## Contribution
- Thiết lập trò chơi Stag Hunt lặp lại N người chơi với nhóm LLM đồng nhất, dưới sự hỏng thông tin công khai được kiểm soát bằng cách đảo ngược hành động theo chương trình (programmatic action inversion), tác động đồng thời đến transcript công khai và hành động dùng để thực thi.
- Quan sát ba mô hình chính trên lưới thí nghiệm spanning kích thước nhóm, ngưỡng phối hợp, mức hỏng, và bảy LLM: (1) lựa chọn Stag trước khi đảo (pre-flip) của agent trung thực giảm dần theo mức hỏng, nhưng sự sụp đổ thành công công khai chủ yếu là cơ học; (2) lựa chọn trung thực gắn liền với lịch sử công khai có sẵn tại thời điểm ra quyết định, đặc biệt khi hỏng cao; (3) ba benchmark báo cáo công khai kiểu ngưỡng cho tỷ lệ khớp hành động tương tự với agent LLM.
- Phân tách thành công trước khi đảo (pre-flip success), thành công công khai (public success), và lực lượng thực hiện (realised payoff) để đánh giá độ mạnh đa agent chính xác hơn.

## Method
Mỗi lượt chơi: mỗi agent i chọn hành động gốc rt_i ∈ {Stag, Hare}. Các agent nói theo thứ tự cố định và có thể căn cứ vào báo cáo công khai đã có trong transcript. Thiết lập thành công nếu ít nhất M hành động công khai là Stag. Cấu trúc trả giá thỏa mãn RS > HF ≥ HS > RF, với (RS, HS, RF, HF) = (4, 2, 0, 2). Một tập F agent được chỉ định là hỏng (corrupted) ngẫu nhiên, giữ nguyên suốt mô phỏng. Sau khi agent hỏng đưa ra quyết định gốc, mô phỏng đảo ngược hành động hiển thị trong transcript công khai (Stag → Hare, Hare → Stag) và sinh lý do mới phù hợp bằng một lệnh gọi LLM riêng. Các agent sau đó nhận báo cáo đã biến đổi không có chỉ báo về trạng thái hỏng. Cho phân tích, giữ cả hành động gốc và hành động công khai để tính thành công trước khi đảo (pre-flip success, áp ngưỡng vào hành động gốc) và thành công công khai (public success, áp ngưỡng vào hành động post-flip). Ba benchmark báo cáo công khai: naive aggregate (tỉ lệ Stag quan sát được), carryover updating (trôi qua trước đó với pseudo-count pooling), và outcome-alignment weighting (trọng số dựa trên sự phù hợp trước đó giữa báo cáo công khai và kết quả thực hiện). Đánh giá sự khớp mô tả giữa hành động gốc của agent và hành động được gợi ý bởi benchmark.

## KNOWLEDGE — Số liệu & khái niệm
- Lưới thí nghiệm: N ∈ {2, 3, 5}, M ∈ {1, …, N}, T ∈ {1, 2, 4}, F tùy N (N=2: F ∈ {0,1}; N=3: F ∈ {1,2}; N=5: F ∈ {1,2,3,4}).
- Bảy LLM: deepseek-v3.2-think, ernie-5.0-thinking-preview, glm-5, gpt-5-mini, gpt-5.2-2025-12-11, kimi-k2.5, llama-3.1-8b. Mỗi thử nghiệm sử dụng nhóm đồng nhất (các agent cùng một model).
- Trả giá: (RS, HS, RF, HF) = (4, 2, 0, 2).
- Cài đặt tiêu điểm N = 5, M = 3: thành công trước khi đảo ở 78% ở mức hỏng 80%, trong khi thành công công khai rơi xuống 12%.
- Thành công trước khi đảo giảm từ 0.972 ở 20% hỏng xuống 0.778 ở 80%; thành công công khai rơi từ 0.972 xuống 0.123.
- Ranh giới cơ học (mechanical boundary): 1 − M/N (40% cho N = 5, M = 3).
- Liên kết sequential: một đơn vị tăng tỉ lệ Stag công khai trước đó gắn với việc tăng 0.499 xác suất chọn Stag (95% CI [0.418, 0.580]); trong mô hình chung hệ số là 0.594 (95% CI [0.508, 0.679]).
- Tỷ lệ khớp benchmark trên 2.852 quan sát đủ điều kiện: naive 0.829, carryover 0.846, outcome-alignment-weighted 0.850.
- Llama-3.1-8b có tỷ lệ khớp thấp hơn (~0.62) trên cả ba quy tắc.
- Lực thực hiện: cài đặt trung thành hoàn toàn接 cận giá trị lý thuyết tối đa 4.0; dưới mức hỏng cao lực rơi xuống khoảng 2.0–2.4. Ở 60%: lực thực hiện 1.702 vs lực thực thi thành thật 3.218; ở 80%: 1.444 vs 3.032.
- Danh mục arXiv: cs.MA (multiagent systems), không phải cs.AI/cs.LG thuần.

## INSIGHT — Cơ chế & tại sao
[Sự sụp đổ thành công công khai chủ yếu là cơ học, không phải hành vi] VÌ [hành động bị đảo ngược trực tiếp thay đổi cả transcript công khai lẫn hành động dùng để tính toán thành công và lực thực hiện]. Điều này nghĩa là [phải tách lựa chọn gốc, hành động công khai, và kết quả thực thi khi đánh giá độ mạnh đa agent; giảm mạnh trên transcript công khai không nhất định nghĩa agent đã thay đổi hành vi].
[Lựa chọn trung thành gắn liền với lịch sử công khai, đặc biệt khi hỏng cao] VÌ [agent căn cứ vào thông tin công khai nhìn thấy tại thời điểm ra quyết định, không phải lịch sử hành động gốc ẩn]. Điều này nghĩa là [agent nhạy với transcript công khai nhìn thấy; thiết kế hệ thống trong suốt (transparency) cần thiết khi thông tin có thể bị hỏng].
[Ba benchmark báo cáo công khai có tỷ lệ khớp tương tự agent LLM] VÌ [quyết định LLM tuân theo dạng ngưỡng cắt-off dựa trên ước tính tỉ lệ Stag công khai]. Điều này nghĩa là [có thể dùng benchmark đơn giản để mô tả quyết định phối hợp của LLM, thay vì giả định agent giữ niềm tin phức tạp bên trong].

## IDEA — Áp dụng được gì
Áp dụng nguyên tắc tách lựa chọn gốc / hành động công khai / kết quả thực thi vào hệ thống multi-agent doanh nghiệp: bước đầu là ghi lại cả hành động gốc trước khi biến đổi và hành động công khai để phân tích riêng rễ rễ của sự cố phối hợp.
Dùng benchmark ngưỡng công khai đơn giản (naive aggregate) để theo dõi quyết định phối hợp của agent: bước đầu là tính tỉ lệ báo cáo Stag công khai và so sánh với ngưỡng q* (mức tỉ lệ Stag cần thiết để chọn Stag là tối ưu).

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Đánh giá độ mạnh phối hợp đa agent phải tách biệt lựa chọn gốc của agent, hành động công khai nhìn thấy, và kết quả thực thi — sự suy giảm có thể là cơ học chứ không phải hành vi, nên không kết luận sai về sự đa View (behavioral tipping point) từ mức sụp đổ trên transcript công khai.

## Assumptions & Limitations
- Điều kiện đúng: trò chơi phối hợp Stag Hunt, thông tin công khai có thể bị biến đổi theo chương trình, nhóm agent đồng nhất, thứ tự nói cố định.
- Limitation paper thừa nhận: nhóm đồng nhất, báo cáo nhị phân có cấu trúc, thứ tự nói cố định, khoảng tương tác ngắn; lưới thí nghiệm không cân bằng, không có điều kiện zero-corruption khớp cho mọi cài đặt; thành công trước khi đảo không phải 반 Durchschnitt no-corruption; benchmark trung bình là quy tắc mô tả chưa sửa theo mức hỏng; phân tích quan sát không xác định nhân-viết (causal mediation).
- Limitation paper KHÔNG nói: chi phí vận hành hệ thống ghi nhật ký hai lớp hành động tại quy mô lớn; tác động lên độ trễ khi duy trì transcript gốc và công khai song song; tính ổn định qua nhiều lần chơi dài hơn.

## Metadata
- Năm: 2026
- Tác giả: Xuanyi Liu, Niall Dalton, Hairi Amin, Xiyuan Yin, Lydia Lim (University College London)
- Category arXiv: cs.MA
- Link PDF: https://arxiv.org/pdf/2609.31704v1
- arXiv ID: 2609.31704v1
- Nhãn: [applied]
- Skill: be-careful-who-you-trust | Test: [SKILL VALID]
