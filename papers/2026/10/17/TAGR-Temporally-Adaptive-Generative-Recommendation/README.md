# [2608.24034v1] TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising

## Problem
- Quảng cáo livestreaming (live-streaming advertising) đã trở thành một kênh quan trọng để tạo tiền thu nhập (monetization) trên các nền tảng video ngắn (short-video) và thương mại điện tử (e-commerce). Các mô hình gợi ý phân sinh (generative recommenders) hiện đại chủ yếu được thiết kế cho các vùng mặt mục hu/domain tương đối ổn định (stationary item domains) và do đó không thích nghi (adapt) tốt tại ba cấp độ: mã định danh ngữ nghĩa tĩnh (static semantic IDs/SID) không thể đại diện cho các mục tiêu quảng cáo livestream đang biến đổi (evolving live-ad targets), mô hình hóa hành vi người dùng ở đơn_scale (single-scale user behavior modeling) không thể tin cậy nắm bắt ý định của người dùng đang thay đổi nhanh (rapidly changing intent), và tối ưu hóa ưu tiên (preference optimization) khó cân bằng giữa phản hồi hiện trường mới (fresh on-policy feedback) và độ ổn định của việc đào tạo (training stability).

## Contribtuion
- TAGR (Temporally Adaptive Generative Recommendation) — một khung làm việc gợi ý phân sinh (generative recommendation framework) thực hiện điều chỉnh theo thời gian (temporal adaptation) ở ba cấp độ: mã hóa quảng cáo livestream (live-ad tokenization), mô hình hóa ý định của người dùng (user intent modeling), và căn chỉnh ưu tiên (preference alignment).
- LSID (Live Semantic-Collaborative ID) — định kỳ cập nhật (periodically updates) mã định danh SID của mỗi quảng cáo livestream đang hoạt động (active live ad) dựa trên cảnh tượng livestream hiện tại và các sản phẩm được quảng bá (promoted products), trong khi vẫn giữ vững từ vựng mã phân cấp (hierarchical token vocabulary) ổn định cho việc tạo tự hồi quy (autoregressive generation).
- IAG (Intent-Aware Generation) — mô hình hóa lịch sử vào phòng livestream (live-room entry histories) ở nhiều cấp độ thời gian (multiple temporal granularities) làm chuỗi ý định chính (primary intent sequence), bảo lưu các chuỗi hành vi phụ (auxiliary behavior sequences) dưới dạng các kênh đầu vào riêng biệt (separate input channels), và trọng số hóa dự đoán token tiếp theo (next-token prediction/NTP) bằng bằng chứng ý định sau yêu cầu (post-request intent evidence) và giá trị kinh doanh (business value).
- IOPO (Intermittent On-Policy Preference Optimization) — định kỳ lấy mẫu các nhóm ứng viên (candidate groups) tươi mới từ chính sách hiện tại (current policy) và thực hiện các bản cập nhật ưu tiên phù hợp với hành vi và giá trị (behavior- and value-aligned preference updates) xen kẽ (interleaved) với giám sát NTP bảo trì (supervised NTP maintenance) để bảo lưu phân phối hành vi đã học (learned behavior distribution).

## Method (tóm tắt cốt lõi)
- Mô hình gợi ý quảng cáo livestream (live-streaming advertising recommendations) trong một tình huống phục vụ công nghiệp (industrial serving scenario). Đối với mỗi yêu cầu của người dùng tại thời điểm t, hệ quan sát ngữ cảnh người dùng C_u(t) bao gồm hồ sơ người dùng (user profile), hành vi sử dụng trong quá khứ (historical behaviors), và các mục tiêu quảng cáo đang xuất hiện (emerged targets).
- LSID: mã hóa quảng cáo livestream (live-ad tokenization). Định kỳ cập nhật SID của mỗi quảng cáo livestream đang hoạt động dựa trên cảnh tượng livestream hiện tại và các sản phẩm được quảng bá, trong khi giữ vững từ vựng mã phân cấp (hierarchical token vocabulary) ổn định cho việc tạo tự hồi quy (autoregressive generation).
- IAG: mô hình hóa ý định của người dùng (user intent modeling). Mô hình hóa lịch sử vào phòng livestream ở nhiều cấp độ thời gian làm chuỗi ý định chính, bảo lưu các chuỗi hành vi phụ làm các kênh đầu vào riêng biệt, và trọng số hóa dự đoán token tiếp theo bằng bằng chứng ý định sau yêu cầu và giá trị kinh doanh.
- IOPO: căn chỉnh ưu tiên (preference alignment). Định kỳ lấy mẫu các nhóm ứng viên tươi mới từ chính sách hiện tại và thực hiện các bản cập nhật ưu tiên phù hợp với hành vi và giá trị xen kẽ với giám sát NTP bảo trì để bảo lưu phân phối hành vi đã học.

## Key Findings
- 10 tác giả từ Kuaishou Technology và Đại học Tsinghua (Tsinghua University), category arXiv: cs.IR.
- Triển khai trên một nền tảng thương mại điện tử livestreaming quy mô lớn (large-scale e-commerce live-stream advertising platform).
- TAGR cải thiện tỷ lệ vào phòng livestream (live-room entry) 8.5% và tỷ lệ nhấp vào giỏ hàng (shopping-cart click rates) 7.4%, đồng thời đạt sự tăng trưởng doanh thu (revenue lift) 16.1% trong cài đặt quảng cáo livestream thương mại điện tử so với cơ sở hạ tầng sản xuất (production baseline).
- Các kết quả chứng minh hiệu quả và khả năng triển khai công nghiệp (industrial viability) của việc gợi ý generative thích nghi theo thời gian (temporally adaptive generative recommendation) cho quảng cáo livestream.

## Actionable Insights
1. Điều chỉnh theo thời gian (temporal adaptation) ở ba cấp độ (mã hóa quảng cáo livestream, mô hình hóa ý định người dùng, và căn chỉnh ưu tiên) cải thiện đáng kể hiệu quả của hệ thống gợi ý quảng cáo livestream. Áp dụng: khi xây dựng hệ thống gợi ý quảng cáo livestream, hãy cập nhật định kỳ các mã định danh SID của quảng cáo livestream dựa trên cảnh tượng livestream và sản phẩm được quảng bá.
2. Mô hình hóa ý định người dùng có ý thức (Intent-Aware Generation) mô tả lịch sử vào phòng livestream ở nhiều cấp độ thời gian làm chuỗi ý định chính, lưu các chuỗi hành vi phụ làm các kênh đầu vào riêng biệt, và trọng số hóa dự đoán token tiếp theo bằng bằng chứng ý định sau yêu cầu và giá trị kinh doanh. Áp dụng: khi xây dựng hệ thống gợi ý livestream, hãy mô hình hóa ý định người dùng ở nhiều cấp độ thời gian và sử dụng bằng chứng ý định sau yêu cầu để trọng số hóa dự đoán token tiếp theo.

## Assumptions & Limitations
- Đánh giá trên một nền tảng thương mại điện tử livestreaming thực tế (real-world e-commerce live-stream advertising platform).
- Chỉ đánh giá trên một nền tảng duy nhất (Kuaishou).
- Không có thông tin chi tiết về thời gian đào tạo (training time) và chi phí tính toán (computational cost).

## Metadata
- Năm: 2026, tác giả: Wencai Ye, Guangyi Liu, Chaoyi Wang, Wenbin Luo, Shengyu Wang, Mingjie Sun, Peng Wang, Quanming Yao, Wenjin Wu, Peng Jiang (Kuaishou Technology, Đại học Tsinghua), category arXiv: cs.IR, link PDF: https://arxiv.org/pdf/2608.24034v1
