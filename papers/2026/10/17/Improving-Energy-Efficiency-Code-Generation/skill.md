# Skill: energy-efficient-llm-code-prompting
Source: 2610.02571v1
Type: framework

## Khi nào dùng skill này
- Sinh code bằng LLM cho production và muốn giảm năng lượng thực thi (execution energy) của code được tạo ra.
- Cần đánh giá hiệu quả năng lượng của code do LLM tạo ra, không chỉ tính chính xác hàm số (functional correctness).
- Có thể đo năng lượng thực thi của chương trình Python hoặc C++.

## Tình huống KHÔNG nên dùng
- Đầu ra không phải code có thể chạy và đo năng lượng (ví dụ: văn bản, dữ liệu cấu trúc).
- Không có công cụ đo năng lượng thực thi cho Python/C++.
- Áp dụng cho ngôn ngữ lập trình ngoài Python và C++ (thử nghiệm chỉ giới hạn ở hai ngôn ngữ này).

## Input cần có
- Tập bài toán lập trình có thể giải (ví dụ: từ EffiBench hay LeetCode).
- Bộ test case để kiểm tra tính chính xác hàm số của code đã sinh.
- Công cụ đo năng lượng thực thi cho chương trình Python/C++.
- Truy cập API của ít nhất một LLM để sinh code.

## Các bước thực hiện
1. Chọn tập bài toán lập trình có test case chuẩn để kiểm tra tính chính xác hàm số.
2. Xây dựng prompt cơ bản (baseline prompt) để sinh code cho từng bài toán.
3. Thiết kế 21 chiến lược nhắc nhở (prompting strategies) khác nhau, bao gồm prompt cơ bản làm tham chiếu.
4. Chạy giai đoạn phân tích ban đầu (initial analysis): đánh giá trên tập con phân tầng (stratified subset) với 110 bài toán, 10 bài từ mỗi nhóm thuật toán, dùng 3 mô hình, chỉ Python.
5. Lọc giữ lại bài toán mà tất cả chiến lược nhắc nhở (bao gồm baseline) tạo ra giải pháp đúng hàm số trên mọi mô hình được đánh giá.
6. Chọn 8 chiến lược nhắc nhở giảm năng lượng nhất quán nhất từ giai đoạn 1.
7. Chạy giai đoạn đánh giá mở rộng (extended evaluation): 8 chiến lược được chọn + baseline trên toàn bộ tập đánh giá, cả Python lẫn C++, trên 10 mô hình.
8. Đo năng lượng thực thi (execution energy) chi tiết cho từng chương trình đã sinh.
9. So sánh năng lượng thực thi của từng chiến lược nhắc nhở với baseline; chọn chiến lược giảm năng lượng nhất quán qua các mô hình và ngôn ngữ.

## Output mong đợi
- Danh sách chiến lược nhắc nhở giảm năng lượng thực thi của code do LLM tạo ra (tới 25% cho Python, 17% cho C++).
- Hiểu rõ hiệu quả của từng chiến lược nhắc nhở thay đổi theo mô hình và ngôn ngữ lập trình.

## Ví dụ áp dụng
- Sinh code Python cho tính toán phân bổ doanh thu (revenue apportionment): dùng Prompt 21 (−49% năng lượng so với baseline trong giai đoạn ban đầu) thay vì prompt đơn giản, đo năng lượng thực thi trên tập test chuẩn, chọn chiến lược giảm năng lượng nhất quán qua các mô hình.

## Gotchas
- Chiến lược nhắc nhở yêu cầu nhiều token hơn, tăng chi phí suy luận (inference energy) — hiệu quả tổng thể cần tính cả năng lượng suy luận và năng lượng thực thi.
- Hiệu quả không nhất quán theo mô hình, ngôn ngữ, chiến lược — một số strategi giảm năng lượng, một số tăng năng lượng so với baseline.
- Thử nghiệm chỉ giới hạn ở Python và C++; không bao gồm các ngôn ngữ khác.
- Tập dữ liệu đánh giá có phân phối độ khó không cân bằng (nhiều bài Medium hơn).
