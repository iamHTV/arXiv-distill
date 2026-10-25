# Skill: cua-recovery-error-recovery

Source: 2610.27645
Type: framework

## Khi nào dùng skill này

- Xây dựng dữ liệu khôi phục lỗi cho agent máy tính trong quy trình dài hạn (tự động hóa máy tính để bàn, thao tác qua GUI và CLI).
- Muốn đánh giá xem agent có nhận biết và sửa lỗi của mình không sau khi một lỗi sớm đã ảnh hưởng đến quy trình.
- Có môi trường máy tính để bàn xác định (deterministic) và có thể ghi lại lịch sử tương tác (chụp màn hình, thao tác GUI, lệnh CLI).

## Tình huống KHÔNG nên dùng

- Nhiệm vụ đơn bước (nhập liệu đơn lần, truy xuất văn bản) — không có trạng thái tồn tại để hỏng, không cần khôi phục.
- Môi trường không xác định (có cập nhật tự động, thông báo ngẫu nhiên) — không thể tái lập trạng thái để chạy lại tiền tố.

## Input cần có

- Các lượtROLL thất bại của agent trên quy trình máy tính để bàn (ghi lại chụp màn hình, thao tác, lệnh CLI).
- Thực sự land ground truth (gold lineage) cho từng tác vụ — giá trị đúng ở mỗi bước.
- Bộ trình xác thực (verifier) để xác nhận xem tác vụ đã hoàn thành hay không.

## Các bước thực hiện

1. Chạy nhiều agent trên các quy trình dài hạn (ghép các tác vụ nguồn thành quy trình dài có sự phụ thuộc).
2. Dành cho từng lượtROLL thất bại, so sánh sự thực thi với gold lineage để xác định bước gốc (root-cause step), loại lỗi và bước đầu tiên lỗi trở nên rõ ràng.
3. Sửa các lỗi không liên quan trước bước gốc để gốc là lỗi duy nhất trong tiền tố.
4. Tạo trạng thái tiếp수át (takeover states) bằng cách chạy lại lượtROLL đến các độ sâu d ∈ {0, 5, 10, 15, 20, 25} sau gốc.
5. Người chú thích con người xác thực gốc, loại lỗi, ngưỡng lỗi, tiền tố đã sửa và trạng thái đã chạy lại (đối với bộ kiểm tra).
6. Đối với tập huấn luyện: để mô hình cơ sở tiếp수át từ mỗi trạng thái sai với gợi ý dần cụ thể (xác định bước sai → thêm bằng chứng xung đột → thêm dữ liệu bị ảnh hưởng); giữ lại chỉ bản tiếp tục được trình xác thực chấp nhận; loại bỏ gợi ý khỏi đầu vào huấn luyện.
7. Tinh chỉnh mô hình trên các quỹ đạo khôi phục đã xác thực (một epoch), không có gợi ý trong đầu vào.

## Output mong đợi

- Bộ kiểm tra: trạng thái sai có thể chạy lại, con người đã xác thực, dùng để đo EAR (tỷ lệ nhận biết lỗi), Rubric Score, Pass@3.
- Tập huấn luyện: quỹ đạo khôi phục đã xác thực, dùng để tinh chỉnh agent khôi phục lỗi.
- Agent tinh chỉnh nhận biết lỗi tốt hơn và khôi phục được nhiều tác vụ hơn.

## Ví dụ áp dụng

Agent tự động đặt hàng trên máy tính để bàn: agent chọn sản phẩm sai ở bước 3, lỗi không hiện ra ngay, chỉ bề mặt ở bước 43 khi agent báo hoàn thành nhưng giỏ hàng không đúng. Dùng CUA-Recovery: tạo trạng thái tiếp수át ở bước 3 (gốc), để agent mới tiếp수át và cố gắng sửa. Tinh chỉnh trên quỹ đạo khôi phục đã xác thực giúp agent nhận biết lỗi từ 19.9% lên 35.2% và hoàn thành tác vụ tốt hơn.

## Gotchas

- Hiệu suất từ trạng thái sạch không dự báo được khả năng khôi phục — agent mạnh từ sạch vẫn có thể không nhận ra lỗi được thừa kế.
- Nhận biết lỗi hiếm khi dẫn đến khôi phục (15.6% vs 12.2% tỷ lệ xác thực thành công) — agent thường xác định vấn đề nhưng để lại trạng thái bị ảnh hưởng không thay đổi.
- Môi trường phải xác định để có thể chạy lại tiền tố và xác định bước gốc chính xác.
- Chi phí thu con người xác thực các trạng thái sai cao.
