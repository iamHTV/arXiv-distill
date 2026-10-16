# Skill: rag-scientific-code-understanding
Source: 2609.12190v1
Type: framework

## Khi nào dùng skill này
- Xây hệ thống tra cứu/hiểu mã code nội bộ (codebase) cho doanh nghiệp hoặc cá nhân.
- Muốn dùng mô hình nhỏ chạy local thay vì mô hình lớn lưu trữ trên đám mây (bảo mật dữ liệu, giảm chi phí).
- Có codebase cần tra cứu và hiểu (ví dụ mã khoa học, mã doanh nghiệp).

## Tình huống KHÔNG nên dùng
- Không có codebase để tra cứu.
- Cần code agent tất phép (sửa file, chạy test, xác thực đầu ra) chứ không chỉ tra cứu.

## Input cần có
- Codebase cần hiểu và tra cứu (ví dụ code C++, Python, v.v.).
- Hệ thống embedding và vector store để lưu trữ ngữ cảnh mã code.
- Mô hình LLM nhỏ có thể chạy local.

## Các bước thực hiện
1. Xây dựng vector store chuyên biệt cho codebase: parsing mã code, xây dựng structural graph, tạo giải thích thực thể bằng LLM, và embedding (giai đoạn offline ingestion).
2. Khi người dùng hỏi, hệ thống truy xuất ngữ cảnh liên quan từ vector store và cho mô hình nhỏ trả lời (giai đoạn online answering).
3. Dùng mô hình nhỏ (ví dụ 9B) cho giai đoạn trả lời, không cần mô hình lớn lưu trữ trên đám mây.
4. Đánh giá câu trả lời bằng một mô hình lớn hơn làm judge (thẩm phán độc lập).

## Output mong đợi
- Mô hình nhỏ (9B) đạt average score 0.795 trên benchmark 100 câu hỏi, vượt qua mô hình lớn hơn.
- Hệ thống chạy local, bảo mật dữ liệu, miễn phí (không phải trả phí API đám mây).

## Ví dụ áp dụng
Solopreneur có mã code nội bộ cho công cụ phân tích dữ liệu: xây dựng vector store chuyên biệt cho mã code này, dùng mô hình nhỏ (9B) chạy local để trả lời câu hỏi về mã code (ví dụ "hàm này làm gì", "tại sao lỗi ở đây"). Giúp bảo mật mã code và giảm chi phí so với dùng Claude Code hoặc Codex trên đám mây.

## Gotchas
- Hệ thống chỉ dựa trên semantic explanation của codebase, không phải all-round code agent (không sửa file, chạy test, hoặc tự xác thực đầu ra).
- Cần xây dựng vector store chuyên biệt cho mỗi codebase, không thể dùng chung cho nhiều codebase khác nhau.
- Cần một mô hình lớn làm judge để đánh giá câu trả lời, có thể tăng chi phí đánh giá.
