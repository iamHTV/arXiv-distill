# Skill: self-evolving-multi-agent-translation
Source: 2609.38660v2
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống dịch phụ đề dài (long-form subtitle translation) bằng multi-agent.
- Cần duy trì thuật ngữ và phong cách đồng bộ qua nhiều tập phim.
- Có dữ liệu phụ đề và transcript của các tập phim để huấn luyện.

## Tình huống KHÔNG nên dùng
- Dịch câu đơn (sentence-level translation) không cần ngữ cảnh dài.
- Không có dữ liệu phụ đề để train.
- Không cần duy trì thuật ngữ đồng bộ qua nhiều tập.

## Input cần có
- Tập hợp các tập phim và phụ đề tương ứng.
- Bộ dữ liệu phụ đề đã được dịch (parallel subtitles).
- Mô hình LLM để dịch và đánh giá.
- Công cụ gọi công cụ (tool-calling modules) cho xác thực thuật ngữ và kiểm tra ràng buộc phụ đề.

## Các bước thực hiện
1. Xây dựng bộ nhớ cấp series (series-level memory) bền vững từ các tập phim và phụ đề đã dịch.
2. Xây dựng hệ thống đa agent với dynamic graph router và Mixture-of-Agents translation layer.
3. Thêm các công cụ (tool-calling modules) để xác thực thuật ngữ (terminology verification), xác thực ràng buộc phụ đề (subtitle constraint validation), và truy xuất ngữ cảnh (contextual retrieval).
4. Thêm judge-refiner loop để đánh giá từng bản dịch ứng viên và truyền lại phê bình văn bản để tinh chỉnh hướng dẫn agent và chính sách định tuyến.
5. Đánh giá trên tập dữ liệu phụ đề dài (long-form subtitle translation).

## Output mong đợi
- Hệ thống dịch phụ đề dài với độ chính xác cao (MQM score cao).
- Giảm mức phạt (average penalty) so với hệ thống agent mạnh nhất cạnh tranh.
- Điểm tổng hợp tổng thể (overall score) cao trong đánh giá bằng con người.

## Ví dụ áp dụng
- Xây dựng hệ thống dịch phụ đề dài cho phim hoặc phim truyền hình. Dùng hệ thống đa agent với dynamic graph router và Mixture-of-Agents translation layer để dịch từng câu, đồng thời duy trì thuật ngữ và phong cách qua nhiều tập.

## Gotchas
- Đánh giá trên 14 thể loại (genres), 2–198 tập phim mỗi series, 15 vùng miền (locales).
- Không có thông tin chi tiết về thời gian đào tạo và chi phí tính toán.
