# [2609.38660v2] Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation

## Problem
Dịch phụ đề dài (long-form subtitle translation) khó hơn machine translation thường: một episode có hàng trăm câu cuyo ý nghĩa phụ thuộc vào ngữ pháp dài hạn (long-range discourse) và ngữ cảnh văn hóa trải suốt toàn bộ episode hay cả 시리즈, đồng thời chất lượng dịch đòi hỏi duy trì thuật ngữ và phong cách nhất quán. Các phương pháp hiện tại còn hạn chế: single-LLM hoạt động ở mức câu, không giữ ngữ cảnh dài hạn.

## Contribution
- Giới thiệu SMART: hệ multi-agent tự-tiến hóa (self-evolving) dịch phụ đề dài, với memory cấp series, dynamic router + Mixture-of-Agents, judge-refiner cập nhật prompt không cần retrain.
- Đánh giá trên 15 hướng Subtitle Arena, 14 thể loại, 15 locale; thắng tất cả 15 hướng, giảm average penalty 6.9% so với hệ agent mạnh nhất.
- SMART giảm mean Overall penalty từ 0.41 xuống 0.37 (giảm 10.0% tương đối), lowest Overall score.

## Method (tóm cốt lõi)
SMART chia nội dung thành overlapping windows (cửa sổ chồng lấp) kích thước 5, 10, 20 với 50% overlap. Dùng memory cấp series để tích luỹ thuật ngữ và phong cách qua các episode. Dynamic router chọn agent phù hợp cho mỗi đoạn. Judge-refiner (thẩm phán - tinh chỉnh) cập nhật prompt dựa trên phản hồi mà không cần retrain mô hình. First 30% nội dung dùng cho test-time training (huấn luyện tại thời điểm kiểm tra), remaining 70% dùng cho held-out inference (suy luận giữ riêng).

## Key Findings
- Thắng tất cả 15 hướng Subtitle Arena, giảm average penalty 6.9% so với strongest competing agent system.
- Overall MQM penalty: 1.11 (SMART) vs 1.20 (TransAgent), giảm tương đối 6.9%.
- Mean Overall penalty: 0.37 (SMART) vs 0.41 (TransAgent), giảm 10.0% tương đối.
- Mean Accuracy penalty giảm từ 0.63 xuống 0.57, giảm khoảng 9.5%.
- Sử dụng Claude Sonnet 4.6 làm default backbone, nhưng vẫn vượt trội so với các hệ agent dùng mô hình lớn hơn.

## Actionable Insights
- Dùng multi-agent với judge-refiner để cập nhật prompt liên tục mà không retrain: phù hợp cho dịch nội dung dài cần nhất quán thuật ngữ (ví dụ dịch phim, video Khoa học). Áp dụng: solopreneur làm dịch nội dung đa kênh nên xây hệ thống agent chấm điểm và tinh chỉnh prompt tự động sau mỗi đoạn dịch.
- Tích luỹ memory cấp series (ngữ cảnh séries) giúp duy trì thuật ngữ và phong cách nhất quán qua nhiều episode. Áp dụng: khi dịch chuỗi video, lưu lại glossary (từ điển thuật ngữ) và phong cách từ các tập trước để dùng cho tập sau.

## Assumptions & Limitations
- Điều kiện: nội dung dài có cấu trúc'épisode/series' để có ngữ cảnh dài hạn; không áp dụng cho dịch câu đơn lẻ.
- Paper thừa nhận: default backbone là Claude Sonnet 4.6, chưa đánh giá trên mô hình open-source lớn.
- Limitation paper không nói: chưa test trên ngôn ngữ ít tài nguyên (low-resource language), chưa đánh giá chi phí inference thực tế.

## Metadata
- Năm: 2026
- Tác giả: Haibo Jin, Xinjie Li, Najmeh Sadoughi, Yang Liu, Yibo Wang, Zhu Liu, Yuzong Liu (UIUC, Amazon)
- Category arXiv: cs.AI, cs.CL
- Link PDF: https://arxiv.org/pdf/2609.38660
