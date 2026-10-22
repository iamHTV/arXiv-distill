# Skill: Kiến trúc treatment-as-query cho mô hình uplift đa điều trị (TaQFormer)
Source: 2610.26199
Type: framework

## Khi nào dùng skill này
- Cần ước lượng tác động nhân quả (uplift) cho quyết định can thiệp có cấu trúc (ví dụ phân bổ giảm giá đa danh mục, khuyến mãi).
- Có dữ liệu quan sát lớn (OBS) và dữ liệu thử nghiệm ngẫu nhiên nhỏ hơn (RCT).
- KHÔNG dùng khi không có dữ liệu RCT hoặc không cần ước lượng tác động nhân quả.

## Input cần có
- Ngữ cảnh yêu cầu (context) với các tính năng có sẵn ở thời điểm quyết định.
- Vectơ điều trị M chiều (mỗi chiều là một mức giảm giá cho một danh mục).
- Dữ liệu OBS (nhật ký quan sát lớn) và dữ liệu RCT (thử nghiệm ngẫu nhiên nhỏ hơn).
- Mục tiêu phụ giá thu (subsidy cost rate) mục tiêu.

## Các bước thực hiện
1. Xây dựng đường yêu cầu độc lập với điều trị: tokenizer chuyển ngữ cảnh thành N token ngữ nghĩa, Encoder Block stack mã hóa thành biểu diễn yêu cầu H(x).
2. Xây dựng đường điều trị phụ thuộc: mỗi chiều giảm giá là một treatment token, dùng cross-attention để truy xuất thông tin liên quan từ H(x).
3. Huấn luyện giai đoạn I: toàn bộ model trên dữ liệu OBS một'époque với mục tiêu cross-entropy nhị phân chính.
4. Huấn luyện giai đoạn II: giữ toàn bộ model OBS-trained làm đường tham chiếu đóng băng, xây dựng đường RCT riêng với LoRA (hạng r = 16, scaling η = 16) trên L_a = 2 khối Encoder cuối.
5. Thêm cổng hợp nhất theo từng instance: MLP nhỏ trộn hai nhánh logits (OBS đóng băng và RCT đã điều chỉnh) dựa trên tóm tắt stop-gradient của bộ nhớ, treatment token, hai logits, và hiệu tuyệt đối.
6. Tối ưu phục vụ: encoder chạy một lần cho một lô yêu cầu, tất cả các cặp yêu cầu–điều trị được flatten thành một giải mã batch.

## Output mong đợi
- Qini cải thiện từ 0,1612 (baseline PEPNet) lên 0,2697, AUC từ 0,6776 lên 0,7393, PCOC từ 1,3737 xuống 1,0012.
- Giá trị kinh supérieur trên mỗi người dùng +1,26% trong kiểm tra A/B 14 ngày, tỷ lệ phụ giá thu gần như không đổi (~20,4%).
- Độ trễ P99 21 ms tại 500 QPS, xếp điểm tất cả 33 điều trị khả thi.

## Ví dụ áp dụng
- Hệ thống phân bổ phiếu giảm giá cho 2 danh mục dịch vụ (ví dụ xe hơi và giao hàng): mỗi mức giảm giá là một treatment token, cross-attention ước lượng xác suất hoàn thành dưới vectơ giảm giá toàn phần, cổng hợp nhất điều chỉnh dự đoán từ dữ liệu OBS bằng dữ liệu RCT.

## Gotchas
- Tính toán chuyên ngành bị giấu kín vì bảo mật — chỉ có thay đổi tương đối.
- Chỉ đánh giá trên M = 2 danh mục; mở rộng lên nhiều hơn 7 danh mục sẽ cần đánh giá lại khả năng bao phủ và hiệu quả phục vụ.
- Cổng hợp nhất là một MLP bổ sung, cần tính vào chi phí mô hình.