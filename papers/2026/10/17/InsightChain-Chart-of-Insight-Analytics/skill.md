# Skill: insightchain-four-stage-visualization
Source: 2609.06438v1
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống trực quan hóa dữ liệu do LLM điều khiển cho khám phá insight mở-ended (open-ended insight discovery).
- Dữ liệu là bảng dữ liệu đơn (tabular dataset) mà không có câu hỏi phân tích hay ý định trực quan hóa đã định sẵn.
- Cần đánh giá cả quỹ đạo phân tích trung gian và trực quan hóa cuối cùng, không chỉ số liệu đầu ra cuối cùng.

## Tình huống KHÔNG nên dùng
- Truy vấn trực quan hóa có ý định rõ ràng sẵn có (user-specified intent).
- Không cần đánh giá quy trình phân tích trung gian.
- Không có sandbox để thực thi mã Python an toàn.

## Input cần có
- Bảng dữ liệu đơn (tabular dataset) D với tên cột, kiểu dữ liệu, thống kê tóm tắt, và mẫu năm dòng.
- Mô hình LLM có thể sinh mã Python (DSPy chain-of-thought module).
- Executor chạy trong hộp cát (sandboxed executor) để thực thi mã Python.
- LLM-as-judge để đánh giá năm chiều chất lượng (EXPLORATION BREADTH, FOCUS RELEVANCE, HYPOTHESIS RIGOR, INSIGHT COMMUNICATION, VISUAL QUALITY).

## Các bước thực hiện
1. Xây dựng ống dẫn bốn giai đoạn (Explore–Focus–Test–Present) mô phỏng quy trình phân tích của chuyên gia.
2. Tại mỗi giai đoạn, dự báo viên sinh ra đầu ra có cấu trúc chứa chương trình Python có thể thực thi.
3. Thực thi chương trình Python trong executor chạy trong hộp cát với ngân sách thử lại B = 2; nếu có lỗi, gửi dấu vết lỗi lại cho dự báo viên để tái tạo (vòng tự sửa lỗi — self-correcting execution loop).
4. Thu thập bản ghi của mỗi giai đoạn đã hoàn thành vào ngữ cảnh chạy C<t, điều kiện các giai đoạn dưới vào các đầu ra và dấu vết thực thi trước đó.
5. Đánh giá bằng Insight Progression Metric (IPM): tổng wd · ϕd(c) với năm chiều (EXPLORATION BREADTH 0.20, FOCUS RELEVANCE 0.25, HYPOTHESIS RIGOR 0.20, INSIGHT COMMUNICATION 0.25, VISUAL QUALITY 0.10), ϕd ∈ [1, 10] là điểm do LLM-as-judge.
6. Tối ưu hóa prompt từng giai đoạn bằng VG-COPRO: vòng lặp ngoài COPRO cho tối ưu hóa từng dự báo viên, vòng lặp bên trong lấy OPRO là đề xuất viên, với ba sửa đổi: phê bình chẩn đoán theo từng chiều, mục tiêu để một miền ngoài (LODO), và tín hiệu biên dịch nhận thức thị giác.

## Output mong đợi
- ống dẫn trực quan hóa cải thiện hiệu quả so với các bước tham chiếu đơn thành mẫu (Single-shot 4-prompt và LIDA) trên cả hai mô hình tác vụ (Gemini 3 Flash, GPT-4.1).
- VG-COPRO cải thiện IPM trong cả cài đặt trong miền (in-domain) và ngoài miền (cross-domain): Gemini 3 Flash IPM 7.24 → 8.56 (+1.31); GPT-4.1 IPM 7.90 → 8.54 (+1.16).

## Ví dụ áp dụng
- Hệ thống phân tích dữ liệu bán hàng: cho một bảng dữ liệu giao dịch, ống dẫn khám phá phân phối bán hàng (Explore), tập trung vào giả thuyết về sản phẩm bán chạy nhất (Focus), kiểm tra giả thuyết bằng kiểm tra thống kê (Test), và truyền đạt phát hiện trong một biểu đồ cuối cùng (Present).

## Gotchas
- Độ chính xác cấu trúc (construct validity) của IPM: đánh giá đầy đủ năm chiều bởi con người chỉ giới hạn ở thử nghiệm người dùng 100 chain.
- 91.9% bảng dữ liệu từ các nguồn công khai thực tế, với bộ dự phòng mẫu tự động nhỏ cho các miền bị thiếu biểu thị.
- Các phương pháp APO hiện có không sinh ra lợi ích nhất quán; chỉ VG-COPRO cải thiện hiệu quả nhất quán.
