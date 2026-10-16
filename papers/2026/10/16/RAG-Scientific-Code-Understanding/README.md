# [2609.12190v1] Retrieval-Augmented Generation for Scientific Code Understanding

## Problem
Các mô hình LLM đã trở thành trung tâm của các coding assistant hiện đại, nhưng các hệ thống tối tân như Claude Code hoặc Codex dựa trên các mô hình lớn, lưu trữ trên đám mây với chi phí tính toán lớn và ảnh hưởng đến bảo mật dữ liệu (data privacy).

## Contribution
- Điều tra xem có thể xây dựng một coding agent hoàn toàn local (chạy cục sở) xung quanh các mô hình open-source nhỏ bằng cách chuyển tải gánh nặng tính toán từ inference (suy luận) ra ngoài.
- Phát triển hệ thống RAG (Retrieval-Augmented Generation) hiểu mã khoa học, tách biệt nghiêm ngäst giai đoạn offline ingestion (phân tích, xây dựng đồ thị cấu trúc, giải thích thực thể bằng LLM, nhúng) khỏi giai đoạn online answering (trả lời trực tuyến) nhẹ nhàng.
- Đánh giá trên benchmark 100 câu hỏi spanning eleven categories (mười một danh mục) trên codebase khoa học IPPL viết bằng C++.
- Các câu trả lời được chấm điểm bởi một frontier model độc lập làm judge (thẩm phán).

## Method (tóm cốt lõi)
Hệ thống RAG cho scientific code understanding tách biệt giai đoạn ingestion đắt giá (offline) khỏi giai đoạn trả lời trực tuyến (online) nhẹ nhàng. Giai đoạn ingestion bao gồm parsing, xây dựng structural graph (đồ thị cấu trúc), giải thích thực thể bằng LLM, và embedding. Giai đoạn online trả lời dựa trên vector store đã chuẩn bị sẵn.

## Key Findings
- Across seven answering models, model family và retrieval quality quan trọng hơn parameter count (số tham số).
- Mô hình 9B đạt average score cao nhất (0.795), vượt qua cả các mô hình lớn hơn trong cùng pipeline và cùng các mô hình được nhúng trong kiến trúc retrieval của Claude Code.
- Kết quả cho thấy việc front-loading (tải trước) hiểu mã code vào một vector store có thể tái sử dụng, chuyên biệt cho codebase, cho phép các mô hình nhỏ local đưa ra câu trả lời có nền tảng (grounded) và đặc thù repository.

## Actionable Insights
- Không nhất thiết phải dùng mô hình lớn, lưu trữ trên đám mây cho coding assistant: mô hình nhỏ (9B) có thể đạt kết quả cao hơn nếu có retrieval context tốt. Áp dụng: solopreneur xây coding assistant nội bộ nên dùng mô hình nhỏ chạy local với RAG vector store đã chuẩn bị sẵn, giúp bảo mật dữ liệu và giảm chi phí.
- Tách biệt giai đoạn ingestion đắt giá khỏi giai đoạn trả lời trực tuyến: chuẩn bị vector store một lần, sau đó trả lời nhanh và rẻ. Áp dụng: khi xây hệ thống tra cứu mã code nội bộ, hãy xây dựng vector store chuyên biệt cho codebase một lần, sau đó để các mô hình nhỏ trả lời.

## Assumptions & Limitations
- Điều kiện: có codebase khoa học và dữ liệu để xây dựng vector store; không áp dụng nếu không có codebase.
- Paper thừa nhận: hệ thống dựa trên semantic explanation của codebase chứ không phải all-round code agent (không chỉnh sửa file, chạy test, hoặc xác thực lặp đi lặp lại đầu ra của riêng nó).
- Limitation paper không nói: chưa đánh giá trên nhiều codebase khác ngoài IPPL, chưa test chi phí thực tế của ingestion stage.

## Metadata
- Năm: 2026
- Tác giả: Aaron Nobile, Andreas Adelmann, Mohsen Sadr (ETH Zürich, Paul Scherrer Institute, MIT)
- Category arXiv: cs.AI, cs.SE
- Link PDF: https://arxiv.org/pdf/2609.12190
