# Skill: niocis-typed-decision-routing-layer

Source: 2610.25985v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần giảm chi phí suy luận cho AI agent gọi công cụ bằng cách thay thế phần lớn cuộc gọi LLM mỗi hop bằng một readout rẻ.
- Khi có nhật ký thực thi agent lịch sử và muốn xây dựng lớp định tuyến chọn next-hop từ không gian tùy chọn được điều chế bởi trạng thái hiện tại.
- Khi cần hệ thống hai tầng: readout rẻ xử lý quyết định kiểm soát, LLM chỉ được gọi khi không chắc chắn.

## Tình huống KHÔNG nên dùng
- Khi không có nhật ký thực thi agent lịch sử.
- Khi không gian hành động mở vô hạn (không thể liệt kê các tùy chọn đã khai báo).
- Khi quyết định không lặp lại (mỗi trạng thái chỉ xảy ra một lần).

## Input cần có
- Nhật ký thực thi agent (các tập thực thi có nhãn hành động, loại bước advance/retry/back, vector ngữ cảnh).
- Danh mục hành động hữu hạn (ví dụ 154 tên công cụ).
- Mô hình backbone nhỏ (ví dụ Laya/ModernBERT-large) hoặc MLP trên các đặc điểm quan sát được.
- Tài nguyên GPU để huấn luyện readout và suy luận batch-1.
- Ngưỡng tin cậy τ để accept/escalate (ví dụ 0.55/0.75/0.9).

## Các bước thực hiện
1. Thu thập nhật ký thực thi agent: ghi lại mỗi bước với nhãn hành động, loại bước (advance/retry/back), vector ngữ cảnh.
2. Đúc nhật ký thành đồ thị hành động loop-collapsed: gộp các bước thử lại ngay (retry) làm bước đã kéo dài thời gian, ghi lại các bước quay lại (back) làm cạnh phục hồi, tạo thành đồ thị có hướng các chuyển tiếp tiến qua (E+) và cạnh phục hồi (E−).
3. Xây dựng không gian tùy chọn được điều chế bởi nút: tại mỗi nút v, không gian tùy chọn A(v) = các cạnh đi ra của v (cộng stop).
4. Huấn luyện readout: hành vi-cloning (cross-entropy) trên các tuple (trạng thái, mục tiêu, ngữ cảnh, next-hop) sao chép từ chuyển tiếp đã đăng nhập; dùng CE hoặc CE+Brier, 5 hạt giống huấn luyện.
5. Triển khai accept/escalate: đọc phân phối từ forward pass duy nhất; nếu max phân phối ≥ τ thì chấp nhận, ngược lại chuyển tới LLM.
6. Thiết lập vòng tự tiến hóa có cổng: mỗi tập thực thi thật trở thành dữ liệu huấn luyện, bản cập nhật chỉ được chấp nhận nếu hiệu năng đánh giá giữ nguyên ngoài δ = 0.005, ngược lại hoàn tác.
7. Đo lường route-level: độ sống nghiêm ngắt (mỗi quyết định trong tập phải khớp) và khoảng cách nhầm lẫn (chi phí tích lũy của các bước nhầm lẫn).

## Output mong đợi
- Lớp định tuyến typed-decision thay thế phần lớn cuộc gọi LLM mỗi hop.
- Báo cáo đánh giá: độ khớp top-1, độ chính xác trong không gian đã khai báo, độ trễ, tỷ lệ cuộc gọi LLM/quyết định.
- Quyết định triển khai: triển khai readout, điều chỉnh ngưỡng τ, hoặc giữ LLM cho mọi hop.

## Ví dụ áp dụng
Một đội agentes bảo mật hoạt động (SOC) gọi công cụ hàng nghìn lần mỗi ngày, mỗi lần LLM suy nghĩ 2.2 giây. Họ thu thập nhật ký thực thi, gộp thành đồ thị hành động, huấn luyện một readout nhỏ chọn hành động tiếp theo từ không gian tùy chọn của trạng thái hiện tại. Kết quả: readout đạt 32.8% khớp với đội (35.6% trong không gian đã khai báo) trong 10 ms so với 2.2 giây mỗi hop LLM; chỉ gọi LLM khi độ tin cậy thấp.

## Gotchas
- Không để từ tiếng Anh không giải thích: typed-decision (quyết định typed), node-conditioned option space (không gian tùy chọn được điều chế bởi nút), loop-collapsed action graph (đồ thị hành động gộp vòng), forward transitions (chuyển tiếp tiến qua), recovery back-edges (cạnh phục hồi quay lại), typed-decision router (bộ định tuyến quyết định typed), feature-MLP readout (đầu đọc MLP đặc điểm), behavior cloning (h moist hành vi cloning), accept/escalate gate (cổng chấp nhận/leo thang), calibration (đo lường chuẩn bị), ECE-15 (lỗi chuẩn bị 15 thùng), AURC (diện tích dưới đường cong rủi pok-lý thr coverage), masked-renormalized (đã che và chuẩn hóa lại), declared option space (không gian tùy chọn đã khai báo), in-space accuracy (độ chính xác trong không gian đã khai báo), strict survival (độ sống nghiêm ngắt), wrong-hop gap (khoảng cách nhầm lẫn bước), gated self-evolution (tự tiến hóa có cổng), rollback (hoàn tác), δ tolerance (ngưỡng dung sai delta), branch factor (nhánh nhánh nhân tử), zero-shot typed choice (lựa chọn typed không gói labels), hidden-state probe (đầu vào trạng thái ẩn), edge-ID readout (đầu đọc mã định danh cạnh), class-space readout (đầu đọc không gian lớp), LLM calls per decision (cuộc gọi LLM mỗi quyết định), inference cost (chi phí suy luận), loop mass (khối lượng vòng), node vocabulary saturation (bão hòa từ vựng nút), transition pair discovery (khám phá cặp chuyển tiếp), capability family (nhóm khả năng), cross-family mass (khối lượng chéo nhóm).
- Không có dữ liệu chi phí token/tiền thực tế (chỉ đoán độ trễ và cuộc gọi LLM/quyết định).
- Tham chiếu là chính sách đội thực sự, không phải trình lập kế hoạch oracle; độ chính xác tuyệt đối thấp (32.8%) vì nhiệm vụ khó.
- Không so sánh trực tiếp với các hệ thống định tuyến mô hình/công cụ hiện có ngoài MIMO Pro V2.6 stand-in.
- Không đánh giá trên các tác vụ không phải bảo mật hoạt động.