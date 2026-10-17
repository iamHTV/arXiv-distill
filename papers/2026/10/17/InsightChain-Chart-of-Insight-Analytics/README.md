# [2609.06438v1] InsightChain: Optimized Chain-of-Insight Analytics for LLM-driven Data Visualization

## Problem
- Các phương pháp hiện đại trong trực quan hóa dữ liệu do LLM điều khiển thường khung hình tạo trực quan hóa như một ánh xạ một bước từ truy vấn của người dùng đến hình hoặc mã, bỏ qua quá trình suy luận phân tích lặp đi lặp lại của các chuyên gia phân tích. Prior work chưa giải quyết được việc đánh giá trực quan hóa phức tạp — một bảng có thể hỗ trợ nhiều hướng phân tích hợp lệ, không có cái nhìn tham chiếu duy nhất, trong khi số liệu đầu ra cuối cùng không thể xác định xem các giả thuyết trung gian có được begründ trên bằng chứng đã thực thi hay không.

## Contribution
- InsightChain — ống dẫn trực quan hóa nhắc nhở (visualization prompting pipeline) bốn giai đoạn (Explore–Focus–Test–Present) mô phỏng quy trình phân tích của chuyên gia, cùng với VG-COPRO, một phương pháp tối ưu hóa nhắc nhở tự động (automatic prompt optimization — APO) được điều chỉnh để cùng tối ưu hóa các ống dẫn thực thi (executable pipelines) nhiều giai đoạn.
- Insight Progression Metric (IPM) — một thước rubric kết hợp bốn chiều dựa trên văn bản với một chiều dựa trên thị giác (vision-based dimension) để đánh giá cả quỹ đạo phân tích trung gian và trực quan hóa cuối cùng.
- Đánh giá IPM thông qua thử nghiệm người dùng (human pilot) 100 chain và đánh giá dựa trên agent (agent-based evaluation) 300 chain trải rộng trên tất cả mười miền.

## Method (tóm tắt cốt lõi)
- Đặt bài: Cho một bảng dữ liệu đơn D không có câu hỏi phân tích hay ý định trực quan hóa đã định sẵn, hệ thống phải xác định một hướng phân tích đáng giá, kiểm tra giả thuyết kết quả thông qua phân tích thực thi, và truyền đạt phát hiện được hỗ trợ trong một trực quan hóa. Đầu ra là một dấu vết suy luận và thực thi đa giai đoạn cùng với một hình cuối cùng.
- ống dẫn bốn giai đoạn S = (t1, t2, t3, t4) tương ứng với Explore, Focus, Test, Present. Tại mỗi giai đoạn t, một dự báo viên (predictor) πt, được thực hiện như một module chuỗi suy nghĩ (chain-of-thought module) với chữ ký kiểu (typed signature), sinh ra đầu ra có cấu trúc ot = πt(xt; θt), trong đó xt biểu thị ngữ cảnh đầu vào và θt biểu thị prompt riêng cho giai đoạn.
- Mỗi đầu ra ot chứa một chương trình Python có thể thực thi pyt, được thực thi bởi một executor chạy trong hộp cát (sandboxed executor) với ngân sách thử lại (retry budget) B = 2. Nếu có lỗi, dấu vết lỗi được gửi lại cho dự báo viên, hướng dẫn tái tạo ot và tạo nên một vòng tự sửa lỗi (self-correcting execution loop).
- Các giai đoạn dưới điều kiện trên các đầu ra trước và dấu vết thực thi. Bản ghi của mỗi giai đoạn đã hoàn thành được thu thập vào ngữ cảnh chạy C<t = (o1, e1, ..., ot−1, et−1).
- IPM(c) = tổng wd · ϕd(c) với D = {EXPLORATION BREADTH, FOCUS RELEVANCE, HYPOTHESIS RIGOR, INSIGHT COMMUNICATION, VISUAL QUALITY}, ϕd ∈ [1, 10] là điểm đánh giá do LLM-as-judge, và w = (0.20, 0.25, 0.20, 0.25, 0.10).
- VG-COPRO: được xây dựng trên vòng lặp ngoài COPRO cho tối ưu hóa từng dự báo viên (per-predictor), với vòng lặp bên trong lấy OPRO là đề xuất viên (proposer), có ba sửa đổi: phê bình chẩn đoán theo từng chiều (per-dimension diagnostic critique), mục tiêu để một miền ngoài (leave-one-domain-out — LODO), và tín hiệu biên dịch nhận thức thị giác (vision-aware compile signal).

## Key Findings
- 5 tác giả từ Huawei Technologies Co., Ltd., category arXiv: cs.CL.
- 285 bảng dữ liệu trải rộng qua 10 miền từ 7 nguồn công khai. Thử nghiệm theo quy tắc để năm miền ra ngoài (leave-five-domains-out): năm miền cung cấp 150 bảng dữ liệu cho biên dịch (train n=95, validation n=20, và trong miền kiểm tra n=35), trong khi năm miền khác cung cấp kiểm tra ngoài miền (cross-domain test set n=135).
- IPM đạt tương quan Spearman ρ = 0.88 với đánh giá con người trong thử nghiệm người dùng 100 chain.
- InsightChain liên tục vượt quá các bước tham chiếu đơn thành mẫu (Single-shot 4-prompt và LIDA) dưới hai mô hình tác vụ (Gemini 3 Flash và GPT-4.1).
- Các phương pháp APO hiện có không sinh ra lợi ích nhất quán; VG-COPRO cải thiện hiệu quả cả trong cài đặt trong miền (in-domain) và ngoài miền (cross-domain).
- Bảng 1: Gemini 3 Flash — InsightChain trước APO IPM 7.24 → VG-COPRO IPM 8.56 (+1.31); GPT-4.1 — 7.90 → 8.54 (+1.16). Single-shot 4-prompt IPM: Gemini 6.38 (−1.00), GPT-4.1 6.92 (−1.09); LIDA: Gemini 5.79 (−1.46), GPT-4.1 4.29 (−3.62).

## Actionable Insights
1. Thay vì ánh xạ một bước từ truy vấn đến biểu đồ, hãy dùng ống dẫn bốn giai đoạn (Explore–Focus–Test–Present) để mô phỏng quy trình phân tích của chuyên gia. Áp dụng: chia tác vụ trực quan hóa dữ liệu thành bốn giai đoạn riêng biệt, mỗi giai đoạn sinh mã Python được thực thi và kiểm tra trước khi tiến sang giai đoạn tiếp theo.
2. Dùng thước đo đa chiều (IPM) kết hợp đánh giá văn bản và thị giác để đánh giá ống dẫn trực quan hóa nhiều giai đoạn. Áp dụng: đánh giá cả quỹ đạo phân tích trung gian và kết quả trực quan cuối cùng, không chỉ số liệu đầu ra cuối cùng.

## Assumptions & Limitations
- Độ chính xác cấu trúc (construct validity) của IPM: đánh giá đầy đủ năm chiều bởi con người chỉ giới hạn ở thử nghiệm người dùng 100 chain; đánh giá mở rộng 300 chain dựa trên đánh giá lặp lại do agent thực hiện và kiểm tra của một chuyên gia trên ba tiêu chí nhị phân.
- 91.9% bảng dữ liệu từ các nguồn công khai thực tế, với bộ dự phòng mẫu tự động nhỏ cho các miền bị thiếu biểu thị và năng lượng.
- Mỗi cấu hình chỉ chạy với các mô hình cụ thể (Gemini 3 Flash, GPT-4.1).

## Metadata
- Năm: 2026, tác giả: Hanya Sun, Chen Zhang, Sheng Liang, Yongyue Zhang, Yong Liu (Huawei Technologies Co., Ltd.), category arXiv: cs.CL, link PDF: https://arxiv.org/pdf/2609.06438v1
