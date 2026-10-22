# Skill: Giao thức đánh giá gắn chú ý bằng chứng cho câu hỏi-đáp tài liệu cục bộ
Source: 2609.28007
Type: workflow

## Khi nào dùng skill này
- Triển khai hệ thống câu hỏi-đáp tài liệu cục bộ bằng ngôn ngữ không phải tiếng Anh với hạn chế phần cứng.
- Cần tách biệt lỗi truy xuất khỏi lỗi suy luận mô hình.
- KHÔNG dùng khi xử lý trên đám mây hoặc khi không có tài liệu lĩnh vực bằng ngôn ngữ mục tiêu để đánh giá.

## Input cần có
- Tài liệu lĩnh vực bằng ngôn ngữ mục tiêu (PDF, báo cáo).
- Tập câu hỏi đánh giá với bằng chứng hỗ trợ được ghi lại cho mỗi câu hỏi.
- Các mô hình LLM ứng viên (7B–8B, định lượng 4-bit).
- Hệ thống truy xuất (từ điển ký tự TF-IDF, BM25, dense, hybrid).
- Phần cứng cục bộ (GPU với VRAM hạn chế).

## Các bước thực hiện
1. Chuyển đổi tài liệu sang văn bản giữ bố cục, chia đoạn, xây dựng chỉ mục truy xuất.
2. Xây dựng tập câu hỏi đánh giá chia thành các dải khả năng (dễ, trung bình, khó, khinh bác), mỗi câu ghi câu trả lời mong đợi, bằng chứng hỗ trợ, và quy tắc chấm điểm.
3. Chạy truy xuất một lần cho mỗi câu hỏi, giữ ngữ cảnh lấy được cố định trên tất cả các mô hình.
4. Đánh giá từng mô hình bằng quy tắc chấm điểm theo loại câu trả lời (số, thực thể, từ khóa, đúng/sai, chọn nhiều, ngày, khinh bác).
5. Đo nhớ lại bằng chứng (evidence recall) độc lập so với chấm điểm câu trả lời — câu hỏi được đếm là đã nhớ lại chỉ khi tất cả con số nguồn được ghi lại xuất hiện trong ngữ cảnh truy xuất.
6. Gán lỗi cho mô hình hay cho hệ thống truy xuất dựa trên kết quả nhớ lại bằng chứng.
7. So sánh các cấu hình truy xuất bằng kiểm định McNemar đôi chính xác và khoảng tin cậy Wilson 95%.

## Output mong đợi
- Độ chính xác end-to-end, độ chính xác theo dải khả năng, điểm số khinh bác, nhớ lại bằng chứng, độ trễ.
- Phân biệt lỗi truy xuất và lỗi suy luận mô hình.

## Ví dụ áp dụng
- Hệ thống câu hỏi-đáp tài liệu công nghiệp bằng tiếng Turkce: ghi bằng chứng cho mỗi câu hỏi, đo nhớ lại bằng chứng, phát hiện truy xuất là ràng buộc buộc (57% nhớ lại trên báo cáo chính), chọn mô hình dựa trên kết quả thực nghiệm (Trendyol 75% chính xác nhưng chậm 14 lần Qwen2.5).

## Gotchas
- Sự điều chỉnh ngôn ngữ đơn lẻ không đảm bảo hiệu năng tài liệu-grounded (Qwen2.5 đa ngôn ngữ vượt qua các mô hình điều chỉnh Turkce).
- Truy xuất có thể là ràng buộc buộc đối với một số tài liệu (57% nhớ lại báo cáo chính) nhưng không phải tất cả (91% báo cáo thứ cấp).
- Không cấu hình truy xuất nào vượt trội đáng kể so với gốc từ điển ký tự TF-IDF (tất cả p > 0.05).