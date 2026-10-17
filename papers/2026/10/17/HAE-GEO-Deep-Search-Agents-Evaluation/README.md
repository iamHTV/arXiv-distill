# [2609.06027v2] Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning

## Problem
- Trợ thủ tìm kiếm tăng cường bằng LLM (search-augmented LLM agents) ngày càng được dùng để ra quyết định tiêu dùng, khiến chúng dễ bị nhiễm độc bởi Tối ưu hóa Máy tạo Sinh (Generative Engine Optimization — GEO). Prior work chưa giải quyết được việc theo dõi toàn bộ quỹ đạo từ sự tiếp xúc đến khôi phục (full trajectory from exposure to recovery) — các đánh giá hiện tại chỉ đo nội dung bị thao tác có được truy xuất hay được tán thành hay không, không theo dõi agent có xác minh bằng chứng nghi ngờ, sửa đổi claim đã nhận, hoặc khôi phục trước khi đưa ra khuyến nghị cuối cùng hay không.

## Contribution
- HAE-GEO — benchmark theo dõi toàn bộ quỹ đạo từ tiếp xúc đến khôi phục dưới sự nhiễm độc Web ngày càng thuyết phục. Agent tương tác qua giao diện Search–Scrape đa lượt (multi-turn) trên ba cấp tấn công (L1 khẳng định trực tiếp, L2 giả bộ ngữ cảnh, L3 tăng cường bằng chứng).
- Corpus kiểm soát 72,039 trang sạch và 770 trang bị nhiễm độc mỗi cấp trải qua 8 danh mục sản phẩm và 154 thương hiệu.
- Đánh giá kết hợp các thước đo hành vi deterministik (deterministic behavioral measures) với sáu chiều thước rubric ngữ nghĩa (semantic rubric dimensions).

## Method (tóm tắt cốt lõi)
- Thiết kế quỹ đạo-trạng thái (trajectory-state design): kiểm soát cách bằng chứng bị nhiễm độc được trình bày và ghi lại cách agent phản hồi sau khi bằng chứng vào ngữ cảnh.
- Ba cấp nhiễm độc: L1 Nhiễm độc trực tiếp (khẳng định không được hỗ trợ), L2 giả bộ ngữ cảnh (được nhúng trong ngữ cảnh tự nhiên), L3 nhiễm độc tăng cường bằng chứng (chuỗi chứng thực).
- Năm trạng thái hành vi có thể quan sát: Tiếp xúc (E), Nhận tư (A), Nhận kết quả xác minh (V), Khôi phục (R), tán thành (Y).
- Sáu chiều thước rubric ngữ nghĩa: M1 Xử lý rủi ro thương hiệu giả, M2 Nhận thức bằng chứng nhiễm độc, M3 Khôi phục sau khi nhận tư, M4 Chất lượng bằng chứng & Độc lập, M5 Đánh giá độ tin cậy, M6 Tiện ích hợp pháp dưới tấn công.
- Giao thức LLM-as-Judge chia hai (Split LLM-as-Judge Protocol): Attack-aware Poison Judge (điểm M1–M3) và Attack-label-blind Quality Judge (điểm M4–M6), mỗi điểm trong {0,1,2}.

## Key Findings
- 10 agent được đánh giá, tác giả từ Đại học Zhejiang và Ant Group, category arXiv: cs.CR.
- Nhận thức bằng chứng suy giảm dưới bẫy chứng thực (corroboration trap, L3).
- Tìm kiếm do agent (agentic search) cải thiện khả năng kháng cự cuối cùng mà không cải thiện nhận thức bằng chứng hay tiện ích.
- Defense prompting tăng xác minh, nhưng hiếm khi chuyển đổi xác minh thành khôi phục.
- Kimi-K3: DEF FR 10,9%, 24,2%, 18,8% trên L1–L3 (mạnh nhất trong bảng).
- GPT-5.6-sol: L1 FR không đổi, L2 FR 47,6%→49,2%; GLM-4.7-Flash stays above 46% at all three levels.
- Defense thêm 1,82 lệnh gọi công cụ mỗi truy vấn trung bình, tăng tiêu thụ token 24,5% theo macro-average.

## Actionable Insights
1. Xác minh độc lập (independent verification) là chìa khóa chống lại nhiễm độc GEO — agent cần xác minh sự độc lập và nguồn gốc của bằng chứng schien dẫn trước khi chấp nhận. Áp dụng: thêm bước xác minh độc lập trước khi agent đưa ra khuyến nghị sản phẩm, dùng nguồn không phải từ trang đã bị nhiễm độc.
2. Defense prompting tăng xác minh nhưng hiếm khi chuyển đổi thành khôi phục (recovery). Áp dụng: không chỉ khuyến khích agent xác minh, mà yêu cầu agent rút lui (retract) và thay đổi khuyến nghị khi phát hiện bằng chứng mâu thuẫn.

## Assumptions & Limitations
- Bộ dữ liệu kiểm soát 72.039 trang sạch và 770 trang bị nhiễm độc mỗi cấp có thể không phản ánh web thực tế hoàn toàn.
- M3 chỉ áp dụng khi prior adoption có thể quan sát được.
- Không nói rõ: hiệu quả trên các thương hiệu và danh mục sản phẩm ngoài 154 thương hiệu, 8 danh mục đã đánh giá.

## Metadata
- Năm: 2026, tác giả: Zhongan Bi (Đại học Zhejiang), Qiwen Wang, Jianrong Jiang, Jigang Ding, Wenwen Xiong, Changhua Meng, Xuanang Gao, Kepeng Lin, Changjiang Jiang, Yi’ang Chen, Huan Yao, Wei Wang, Zhenyu Ma, Wenhui Dong (Ant Group), category arXiv: cs.CR, link PDF: https://arxiv.org/pdf/2609.06027v2
