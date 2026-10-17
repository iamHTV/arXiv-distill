# [2609.24928v2] Trajectory-Aware Benchmark Subset Selection for Cost-Efficient Software Engineering Agent Regression Testing

## Problem
- Các tác nhân tự lý phần mềm (autonomous software engineering agents — SWE-agents) ngày càng có khả năng sửa lỗi chương trình, gỡ lỗi hệ thống phần mềm, và tạo và chạy thử nghiệm. Trong khi đánh giá SWE-agents đòi hỏi chạy các benchmark lớn trên nhiều tác vụ phần mềm thực tế, mỗi bản cập nhật agent có thể đòi hỏi chạy lại toàn bộ benchmark để phát hiện hồi quy (regression) và sự cải tiến, với chi phí hàng trăm triệu token LLM mỗi lần, làm cho việc đánh giá trở thành một apt-get (bottleneck) trong quá trình phát triển. Một giải pháp là chỉ đánh giá một tập con (subset) của các instance benchmark. Tuy nhiên, các cách tiếp cận đơn giản, như lấy mẫu ngẫu nhiên (random sampling) hoặc lấy mẫu phân tầng (stratified random sampling) dựa trên kết quả thành công/thất bại quá khứ, rủi ro tạo ra các subset có sai số cao (high variance) và không đại diện (unrepresentative).

## Contribtuion
- Một phương pháp lựa chọn subset nhận thức về quỹ đạo (trajectory-aware subset selection) thay thế lấy mẫu ngẫu nhiên bằng lựa chọn định mức (deterministic selection) dựa trên nhúng quỹ đạo (trajectory embeddings). Chúng tôi đầu tiên nhóm các instance test set theo kết quả test (test outcome) trong một lần chạy test đầy đủ (recent full test run) để giữ nguyên tỷ lệ thành công/thất bại quá khứ (historical pass/fail rate), sau đó chọn subset bằng không gian nhúng (embedding space) của quỹ đạo (trajectory).
- Đánh giá hệ thống 76 cấu hình lựa chọn subset, bao gồm lấy mẫu ngẫu nhiên (random sampling), lựa chọn dựa trên nhúng (embedding-based selection), lựa chọn dựa trên phân nhóm (clustering-based selection), và chiến lược ngắn gọn sau đó lấy mẫu (hybrid shortlist-then-subsample strategies), trên ba kịch bản hồi quy (regression scenarios): chạy lại cùng cấu hình (same-configuration reruns), thay đổi mô hình và cấu hình (model and configuration changes), và thay đổi khung agent (agent framework changes).
- Phương pháp nhận thức về quỹ đạo (trajectory-aware method) tốt nhất là phương pháp chọn các instance benchmark gần trọng tâm (centroid) nhất của mỗi nhóm kết quả (outcome group) trong không gian nhúng (embedding space). Nó đạt sai số ước tính (estimation error) thấp nhất trong tất cả các phương pháp chúng tôi đánh giá, trong đó sai số là khoảng cách giữa tỷ lệ giải quyết (resolve rate) được đo trên subset và tỷ lệ giải quyết của toàn bộ benchmark.

## Method (tóm tắt cốt lõi)
- Quy trình đầu đến cuối (end-to-end pipeline) cho phương pháp lựa chọn subset kiểm thử hồi quy (regression test selection) của SWE-agent.
- Bước 1: Phân tích các quỹ đạo thô (raw trajectories) thành định dạng chuẩn hóa (standardized format), vì các khung agent khác nhau ghi lại dữ liệu quỹ đạo theo cách không tương thích.
- Bước 2: Lọc sạch (sanitize) các quỹ đạo đã phân tích để loại bỏ các tín hiệu kết quả (outcome signals) rõ ràng, vì các mã thông báo (tokens) như passed hoặc exit code 0 sẽ rò rỉ (leak) kết quả thành công hoặc thất bại, khiến các nhúng (embeddings) nhóm theo kết quả thay vì theo hành vi.
- Bước 3: Truyền các quỹ đạo đã lọc sạch vào một mô hình nhúng (embedding model) để tạo ra các biểu diễn số (numerical representations).
- Bước 4: Dựa trên các nhúng (embeddings) của các quỹ đạo trong lần chạy hồi quy đầy đủ (full regression run) gần nhất, chọn một tập con nhỏ (small subset) các instance.
- Bước 5: Trong các lần chạy sau, chỉ đánh giá tập con đã chọn và dùng tỷ lệ giải quyết (resolve rate) của tập con để ước tính tỷ lệ giải quyết của toàn bộ suite.

## Key Findings
- 5 tác giả từ Đại học Queen's (Queen's University, Canada) và Đại học Concordia (Concordia University, Canada), category arXiv: cs.SE.
- 76 cấu hình lựa chọn subset được đánh giá trên ba kịch bản hồi quy.
- Phương pháp nhận thức về quỹ đạo (trajectory-aware method) tốt nhất: chọn các instance benchmark gần trọng tâm (centroid) nhất của mỗi nhóm kết quả (outcome group) trong không gian nhúng (embedding space).
- Khi đánh giá một phiên bản agent cụ thể trên một tập con chỉ 5% hoặc 10% của các instance test, phương pháp này giảm sai số ước tính trung bình (average estimation error) 3–11% và sai số trường hợp tồi tệ nhất (worst-case error), sai số lớn nhất giữa tỷ lệ giải quyết của subset và tỷ lệ giải quyết của toàn bộ benchmark trên bất kỳ lần chạy đơn lẻ nào, 4–11% so với vòng quay điển hình (typical draw) và 38–46% so với vòng quay thứ 95 (95th-percentile draw) của strong baseline mạnh nhất.
- Kết quả cho thấy một subset nhận thức về quỹ đạo (trajectory-aware subset) 10% giữ sai số ước tính trung vị (median estimation error) dưới 5% trong khi cắt giảm chi phí token (token cost) khoảng 90%.
- Consistency Stratification (Consist-Strat) là strong baseline mạnh nhất, đạt median RMSE thấp nhất trong tất cả các dataset và kích thước subset. Nó giảm median RMSE so với Random 51% trong Single-setup, 31–32% trong Multi-model, và 40–42% trong Multi-agent.

## Actionable Insights
1. Dùng nhóm kết quả quá khứ (outcome grouping) để phân tầng các instance trước khi lấy mẫu subset. Áp dụng: khi chọn mẫu subset để đánh giá agent regression, hãy nhóm instance theo kết quả test trong lần chạy đầy đủ gần nhất trước khi lấy mẫu.
2. Dùng embedding của quỹ đạo (trajectory embedding) để chọn mẫu gần trọng tâm (centroid) của mỗi nhóm kết quả. Áp dụng: thay vì lấy mẫu ngẫu nhiên, hãy dùng trajectory embedding để chọn các instance gần trọng tâm nhất của mỗi nhóm kết quả.

## Assumptions & Limitations
- Đánh giá trên các benchmark code-repair được xây dựng từ các issue GitHub, kết quả có thể không chuyển tiếp sang các benchmark agent trong các miền khác.
- Mỗi cấu hình chỉ chạy một lần.
- Vẫn cần chạy full regression run để có historical outcomes.

## Metadata
- Năm: 2026, tác giả: Mahmoud Ayyad, Zehao Wang, Jiho Shin, Ying Zou, Bram Adams (Đại học Queen's, Đại học Concordia), category arXiv: cs.SE, link PDF: https://arxiv.org/pdf/2609.24928v2
