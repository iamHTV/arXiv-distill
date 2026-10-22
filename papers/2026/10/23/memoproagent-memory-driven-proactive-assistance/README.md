# 2610.22671 MemoProAgent: Trợ giúp chủ động dựa trên bộ nhớ

## Problem
Trợ giúp chủ động (proactive assistance — trợ giúp mà không cần người dùng hỏi trước) yêu cầu trợ lý quyết định khi nào nên nói và nói gì. Trong mô hình phản ứng (reactive paradigm), bộ nhớ chỉ cung cấp nội dung trả lời cho câu hỏi của người dùng. Trong mô hình chủ động, bộ nhớ cũng phải quyết định khi nào có can thiệp đáng làm — bằng chứng cần thiết phải được khai thác từ một bộ nhớ cá nhân dài hạn (~618K token trung bình), không được giao sẵn. Các hệ thống hiện tại đều kém (tối đa 15% chính xác) vì chúng không thể phân biệt nội dung đúng và thời điểm đúng.

## Contribution
- MemoProBench: tiêu chí đánh giá (benchmark) cho trợ giúp chủ động dựa trên bộ nhớ (memory-driven proactive assistance — MPA), kết hợp video egocentric (video ghi từ góc nhìn người dùng) với bộ nhớ cá nhân kéo dài một năm, đầy nhiễu gây vías (distractor-rich), có cửa sổ kích hoạt (trigger window — khoảng thời gian mà việc can thiệp là đáng làm) do con người xác minh, và giao thức đánh giá nội dung và thời điểm cùng lúc.
- MemoProAgent: thắt lõi (harness — khung bọc) plug-and-play không thay đổi trọng số mô hình, tổ chức bộ nhớ thành đồ thị (graph) các ký sự (episodic) và ngữ nghĩa (semantic), có cổng lọc (gate) duy trì chỉ bằng chứng xứng đáng bị ngắt lời (worth interrupting for), plus giai đoạn RL nhẹ (lightweight RL) giảm tiro sớm và lặp lại (early and repeated firing).
- Kết quả: nâng độ chính xác nghiêm ngặt (strict accuracy — Perfect) từ dưới 10% lên 37.5% trên Qwen3.8-27B và 38% trên GPT-5.3-Chat không cần huấn luyện; RL hậu huấn luyện đạt 42.4%.

## Method
MemoProBench định nghĩa tác vụ: trợ lý quan sát luồng video egocentric V = (v1, v2, ...), có bộ nhớ dài hạn M, không nhận câu hỏi nào, tại mỗi thời điểm t phát ra r_t = π(M, V_{t-n:t}) ∈ {∅} ∪ A, trong đó ∅ là im lặng, A là không gian các can thiệp ngôn ngữ tự nhiên. Một can thiệp đúng nếu nổ trong cửa sổ kích hoạt và nội dung trung thành với bộ nhớ liên quan. Đánh giá chính là Perfect (chính xác nghiêm ngặt): nổ đúng một lần, trong cửa sổ, nội dung tốt, không có tiro sớm, chậm hay lặp lại.

MemoProAgent harness: tại mỗi điểm ra quyết định, trình sinh (generator) theo vòng lặp tác nhân hai vòng (observe → retrieve → reason → answer). Bộ nhớ được tổ chức thành đồ thị hai lớp: lớp ký sự (object-keyed episodic memories) và lớp ngữ nghĩa (semantic facts). Cổng lọc (gate) là một cuộc gọi LLM duy nhất đọc các ứng viên bằng chứng so với đối tượng đang quan sát, lọc những gì không xứng đáng ngắt lời, giữ những gì xứng đáng, tinh chỉnh thành một đoạn bằng chứng duy nhất (hoặc không trả về gì). Giai đoạn RL hậu huấn luyện dùng GRPO (học tăng cường chính sách theo nhóm — group relative policy optimization) với phần thưởng có thể kiểm chứng từ chú thích benchmark: +1 cho im lặng đúng và can thiệp đúng thời điểm có nội dung tốt, −1 ngược lại.

## KNOWLEDGE — Số liệu & khái niệm
- MemoProBench có 1.804 cặp dữ liệu (904 train, 100 dev, 800 eval), mỗi cặp là clip video egocentric từ Ego4D + lịch sử cá nhân khoảng một năm (~618K token, bằng chứng mục tiêu chỉ ~0.19%).
- Tất cả các baseline đều kém (tối đa 15% Perfect), bao gồm các mô hìnhendoza (frontier models) cho tóm tắt hoặc RAG tăng cường bộ nhớ.
- Oracle evidence + timing given: GPT-5.3-Chat đạt 96%; oracle + timing do model chọn: giảm xuống 38%; retrieved evidence + timing given: xuống 15.3%. Nội dung và thời điểm độc lập cần thiết, thiếu một là thảm họa.
- MemoProAgent harness (không huấn luyện): Qwen3.8-27B từ dưới 10% lên 37.5% (windowed), 33.3% (streaming); GPT-5.3-Chat đạt 38%. RL post-training: Qwen3.8-27B lên 42.4% (windowed), 40.6% (streaming).
- Cổng lọc (gate) giảm 13.3 điểm (37.3→24.0); giảm tỷ lệ tiro sai trên clip âm (negative clips — không có gì đáng nhắc nhở) từ 77.3%/84.0% (RAG) xuống 15.3% (windowed/streaming).
- Generalization: chuyển không điều chỉnh sang Epic-Kitchens, harness nâng Perfect từ tối đa 11.0 lên 41.0 (windowed) và 37.0 (streaming).

## INSIGHT — Cơ chế & tại sao
[Bộ nhớ dài hạn không giúp nếu chỉ ném toàn bộ vào ngữ cảnh] xảy ra VÌ bằng chứng mục tiêu chỉ ~0.19% bộ nhớ, bị chôn sâu trong nhiễu gây vías, và các mô hình ném toàn bộ vào ngữ cảnh hay tiro khắp nơi (99.9% over-trigger — tiro quá nhiều). Điều này nghĩa là [cần cấu trúc bộ nhớ và cổng lọc để chỉ đưa bằng chứng xứng đáng vào lúc xứng đáng, không phải cung cấp thêm nội dung].
[Cổng lọc (gate)問 việc xứng đáng ngắt lời chứ không phải liên quan] xảy ra VÌ nhiều ký sự được truy xuất, dù thực, không phải lý do tốt để nhắc nhở (đối tượng chỉ đồng xuất hiện, hoặc open loop đã được giải quyết). Điều này nghĩa là [việc lấy thêm bằng chứng (RAG sâu hơn k) làm tăng Hit nhưng gây over-trigger tỉ lệ cao hơn, khiến Perfect sụt đổ — cần lọc chứ không phải lấy nhiều hơn].

## IDEA — Áp dụng được gì
1. Áp dụng MemoProAgent harness vào trợ lý AI wearable / AI kính thông minh: bước đầu là tổ chức lịch sử người dùng thành đồ thị ký sự–ngữ nghĩa, thêm cổng lọc (một cuộc gọi LLM) trước khi đưa bằng chứng vào trình sinh, chỉ nhắc nhở khi bằng chứng xứng đáng.
2. Áp dụng RL hậu huấn luyện với phần thưởng nhị phân (im lặng đúng / can thiệp đúng) vào trình sinh trợ lý chủ động: bước đầu là định nghĩa phần thưởng từ chú thích trigger window, dùng GRPO để curb tiro sớm và lặp lại.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Trong trợ giúp chủ động, bộ nhớ quyết định cả nội dung lẫn thời điểm; thiếu một trong hai là thảm họa, nên giải pháp phải lọc bằng chứng (chỉ đưa khi xứng đáng) chứ không chỉ cung cấp thêm bộ nhớ. Khi nào dùng: khi hệ thống cần can thiệp chủ động mà không có truy vấn từ người dùng, và có bộ nhớ dài hạn giàu nhiễu. Khi nào KHÔNG: khi trợ lý chỉ phản ứng theo truy vấn rõ ràng (reactive) hoặc không có dữ liệu lịch sử người dùng.

## Assumptions & Limitations
- Bộ nhớ dài hạn trong MemoProBench được tổng hợp (synthesized) và dựa trên văn bản (dòng chú thích), không phải lịch sử đa phương thức thực tế.
- Đánh giá hiệu suất tác vụ chứ không phải độ trễ (latency).
- Mỗi clip chỉ chứa một cửa sổ kích hoạt, chưa bao gồm nhiều trigger trong một luồng.
- Mã và tập đánh giá sẽ được công bố sau khi xuất bản.

## Metadata
- Năm 2026; tác giả: Shenglai Zeng, Xiao Yang, Tiffany Ma, Xinyuan Zhang, Nanshu Wang, Deren Lei, Kai Sun, Xilun Chen, Tammy Stark, Xianhui Zhu, Yuetai Li, Rulin Shao, Tianxin Wei, Rakesh Wanga, Anuj Kumar, Jiliang Tang, Wen-tau Yih, Xin Luna Dong (Michigan State University, Meta Reality Labs, Meta Superintelligence Labs, Meta, University of Washington, UIUC); category: cs.CL; PDF: https://arxiv.org/pdf/2610.22671v2; code: https://github.com/facebookresearch/Memo-Pro-Agent; data: https://huggingface.co/datasets/facebook/MemProBench; citation count: [NO DATA — paper 2026-10-21]