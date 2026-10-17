# Skill: tagr-temporally-adaptive-recommendation
Source: 2608.24034v1
Type: framework

## Khi nào dùng skill này
- Xây dựng hệ thống gợi ý quảng cáo livestream (live-streaming advertising recommendation) trên nền tảng thương mại điện tử.
- Cần thích nghi với các quảng cáo livestream đang biến đổi liên tục (cảnh tượng livestream và sản phẩm được quảng bá thay đổi trong vài phút).
- Muốn cải thiện tỷ lệ vào phòng livestream (live-room entry), tỷ lệ nhấp vào giỏ hàng (shopping-cart click rates), và doanh thu (revenue).

## Tình huống KHÔNG nên dùng
- Hệ thống gợi ý quảng cáo tĩnh (static ads) không thay đổi theo thời gian.
- Không có dữ liệu về cảnh tượng livestream (live scene) và sản phẩm được quảng bá (promoted products).
- Không cần điều chỉnh theo thời gian (temporal adaptation).

## Input cần có
- Cảnh tượng livestream (live scene) và sản phẩm được quảng bá (promoted products) cho mỗi quảng cáo livestream.
- Lịch sử vào phòng livestream (live-room entry histories) của người dùng.
- Các chuỗi hành vi phụ (auxiliary behavior sequences) của người dùng.
- Bằng chứng ý định sau yêu cầu (post-request intent evidence) và giá trị kinh doanh (business value).
- Mô hình gợi ý generative (generative recommendation model).

## Các bước thực hiện
1. Mã hóa quảng cáo livestream (live-ad tokenization): định kỳ cập nhật SID của mỗi quảng cáo livestream đang hoạt động dựa trên cảnh tượng livestream hiện tại và sản phẩm được quảng bá, trong khi giữ vững từ vựng mã phân cấp (hierarchical token vocabulary) ổn định.
2. Mô hình hóa ý định người dùng (user intent modeling): mô hình hóa lịch sử vào phòng livestream ở nhiều cấp độ thời gian làm chuỗi ý định chính, lưu các chuỗi hành vi phụ làm các kênh đầu vào riêng biệt, và trọng số hóa dự đoán token tiếp theo bằng bằng chứng ý định sau yêu cầu và giá trị kinh doanh.
3. Căn chỉnh ưu tiên (preference alignment): định kỳ lấy mẫu các nhóm ứng viên tươi mới từ chính sách hiện tại và thực hiện các bản cập nhật ưu tiên phù hợp với hành vi và giá trị xen kẽ với giám sát NTP bảo trì.
4. Triển khai trên nền tảng thương mại điện tử livestreaming và đánh giá tỷ lệ vào phòng livestream, tỷ lệ nhấp vào giỏ hàng, và doanh thu.

## Output mong đợi
- Hệ thống gợi ý quảng cáo livestream cải thiện tỷ lệ vào phòng livestream (live-room entry) 8.5% và tỷ lệ nhấp vào giỏ hàng (shopping-cart click rates) 7.4%.
- Đạt sự tăng trưởng doanh thu (revenue lift) 16.1% so với cơ sở hạ tầng sản xuất (production baseline).

## Ví dụ áp dụng
- Xây dựng hệ thống gợi ý quảng cáo livestream cho một nền tảng thương mại điện tử: cập nhật định kỳ SID của mỗi quảng cáo livestream dựa trên cảnh tượng livestream và sản phẩm được quảng bá, mô hình hóa ý định người dùng ở nhiều cấp độ thời gian, và thực hiện các bản cập nhật ưu tiên xen kẽ với giám sát NTP bảo trì.

## Gotchas
- Đánh giá trên một nền tảng thương mại điện tử livestreaming duy nhất (Kuaishou), kết quả có thể không chuyển tiếp sang các nền tảng khác.
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).
- Cần chạy định kỳ (periodically) để cập nhật các mã định danh SID và mô hình ý định người dùng.
