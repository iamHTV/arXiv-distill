# Skill: self-evolving-multi-agent-translation
Source: 2609.38660v2
Type: workflow

## Khi nào dùng skill này
- Dịch nội dung dài (phụ đề phim, video khoa học, tài liệu đa trang) cần duy trì thuật ngữ và phong cách nhất quán.
- Có nhiều épisode/tiếp theo trong cùng một series để tích luỹ ngữ cảnh.
- Muốn cập nhật prompt dịch liên tục mà không retrain mô hình.

## Tình huống KHÔNG nên dùng
- Dịch câu đơn lẻ hoặc đoạn văn ngắn không có ngữ cảnh dài hạn.
- Không có nhiều nội dung liên quan trong cùng một series để tích luỹ memory.

## Input cần có
- Nội dung nguồn cần dịch (phụ đề, video, tài liệu).
- Danh sách các locale (ngôn ngữ đích) cần dịch.
- Hệ thống judge-refiner có thể chấm điểm chất lượng dịch và gợi ý chỉnh sửa prompt.
- Glossary (từ điển thuật ngữ) và phong cách từ các épisode trước (nếu có).

## Các bước thực hiện
1. Chia nội dung dài thành overlapping windows kích thước 5, 10, 20 câu với 50% overlap.
2. Dùng multi-agent (SMART) với dynamic router chọn agent dịch phù hợp cho từng đoạn.
3. Sau mỗi đoạn dịch, judge-refiner chấm điểm và cập nhật prompt dịch dựa trên lỗi phát hiện (không retrain).
4. Tích luỹ memory cấp series: lưu thuật ngữ, phong cách đã dịch vào glossary dùng cho các đoạn sau.
30% nội dung đầu dùng để test-time training (điều chỉnh prompt), 70% nội dung còn lại dùng để đánh giá đánh giá held-out.
5. Lặp lại cho các episode tiếp theo, dùng glossary và prompt đã được tinh chỉnh từ các tập trước.

## Output mong đợi
- Giảm average penalty 6.9% so với hệ agent mạnh nhất trên Subtitle Arena.
- Duy trì thuật ngữ và phong cách nhất quán qua nhiều épisode.

## Ví dụ áp dụng
Solopreneur dịch chuỗi video hướng dẫn phần mềm sang 15 ngôn ngữ. Dùng SMART để dịch từng đoạn, sau mỗi đoạn judge-refiner chấm điểm và chỉnh sửa prompt dịch. Lưu thuật ngữ phần mềm vào glossary dùng cho tất cả video trong series. Chất lượng dịch duy trì nhất quán, không cần retrain mô hình khi sang series mới.

## Gotchas
- Chỉ hiệu quả khi có nhiều nội dung liên quan trong cùng một series (để tích luỹ memory).
- Không hiệu quả cho dịch câu đơn lẻ, đoạn văn ngắn.
- Default backbone Claude Sonnet 4.6, chưa biết hiệu quả trên mô hình khác.
