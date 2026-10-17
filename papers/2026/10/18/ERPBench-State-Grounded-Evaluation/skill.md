# Skill: Đánh giá State-Grounded cho Computer-Use Agent trong Phần mềm Doanh nghiệp

Source: 2609.17885v2
Type: evaluation-method

## Khi nào dùng skill này
- Bạn xây dựng computer-use agent (CUA) để tương tác với phần mềm doanh nghiệp (ERP, CRM) và cần đánh giá độ tin cậy thực sự.
- Bạn muốn đảm bảo agent không chỉ nhìn thấy thông báo thành công trên màn hình mà thực sự ghi giá trị chính xác vào cơ sở dữ liệu.
- Bạn cần harness có cổng phê duyệt con người cho hành động rủi ro trước khi triển khai sản xuất.

## Tình huống KHÔNG nên dùng
- Ứng dụng đơn giản không tương tác với phần mềm doanh nghiệp phức tạp.
- Bạn không có cơ sở dữ liệu test để kiểm tra giá trị trường sau khi agent chạy.

## Input cần có
- Hệ thống phần mềm doanh nghiệp test (ERPNext hoặc tương đương) chạy trong Docker.
- Bộ tác vụ YAML chỉ định prompt, start URL, giá trị trường dự định, cấu hình chấm điểm.
- Cơ sở dữ liệu test với dữ liệu mẫu (fixture) được seed qua API.
- Harness chạy agent từ chụp màn hình và mô phỏng chuột/bàn phím.

## Các bước thực hiện
1. Xây dựng bộ tác vụ đánh giá với ba tier độ phức tạp: T1 (đơn bản ghi), T2 (phối hợp nhiều trường), T3 (luồng làm việc nhiều màn hình liên kết).
2. Mỗi tác vụ được chấm điểm bởi ba chấm điểm viên: Database grader (kiểm tra giá trị trường trong DB), Stage grader (Navigation, Interaction, Commit, Database), Log grader (số lần hành động, thời gian, chi phí token).
3. Thiết lập harness chạy ở hai chế độ: Triển khai (dành hành động commit/irreversible lên phê duyệt con người) và Đánh giá (auto-approver).
4. Chạy mỗi tác vụ nhiều lượt độc lập, chấm điểm mỗi lần chạy so với giá trị ground-truth trong database.
5. Nhận diện mode lỗi theo từng giai đoạn để định vị nơi agent thất bại.

## Output mong đợi
- Một hệ thống đánh giá CUA có thể đo độ tin cậy doanh nghiệp thực sự.
- Biết được agent thất bại ở giai đoạn nào (điều hướng, nhập giá trị, lưu, hoặc cơ sở dữ liệu).
- Harness có cổng phê duyệt con người cho hành động rủi ro.
- Báo cáo tỷ lệ thành công theo tier và theo giai đoạn.

## Ví dụ áp dụng
Bạn xây dựng agent tự động tạo hóa đơn trong phần mềm kế toán doanh nghiệp. Thay vì chỉ kiểm tra xem agent có nhấn nút "Lưu" hay không, bạn kiểm tra giá trị trường "số tiền" trong cơ sở dữ liệu sau khi agent chạy. Nếu agent nhấn lưu nhưng giá trị trong DB sai, bạn đánh giá là thất bại. Các hành động xóa bản ghi hoặc gửi hóa đơn phải được con người phê duyệt trước khi thực thi.

## Gotchas
- Hiệu suất GUI tổng thể mạnh không dự báo được độ tin cậy doanh nghiệp.
- Agent có thể điều hướng đến màn hình đúng và nhấn lưu, nhưng giá trị trong cơ sở dữ liệu vẫn sai (silent failure).
- Mô hình mở (open-weight) sụt sớt mạnh trên tier phức tạp hơn (T2, T3), đạt 0–3% so với 34% trên T1.