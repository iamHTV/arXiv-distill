# 2610.26199 TaQFormer: Phân phối dữ liệu Transformer cho phân bổ phiếu giảm giá đa phương pháp điều trị

## Problem
Phân bổ phiếu giảm giá (coupon allocation — phân bổ phiếu giảm giá) trên sàn thương mại điện tử có nhiều danh mục dịch vụ: cần chọn một vectơ giảm giá theo từng danh mục, tính đến cả tác động trực tiếp và sự dịch chuyển nhu cầu giữa các danh mục. Mô hình uplift (mô hình tăng hiệu lực — ước lượng tác động tăng thêm của một can thiệp so với điều khiển) cần ước lượng phản hồi của vectơ điều trị toàn phần. Ba thách thức: (1) mô hình phản hồi tiêu điểm đối với điều trị có cấu trúc (vectơ M chiều), (2) kết hợp nhật ký quan sát (OBS) lớn nhưng thiên vị chính sách với dữ liệu thử nghiệm ngẫu nhiên (RCT) nhỏ hơn, (3) xác thực mô hình uplift dựa trên Transformer trong production.

## Contribution
- TaQFormer: Transformer điều trị làm truy vấn (treatment-as-query Transformer) — mỗi tọa độ điều trị được biểu diễn bằng một truy vấn token, cho phép cross-attention (các tráo chéo — cơ chế chú ý giữa hai dãy) ước lượng phản hồi cho vectơ điều trị đầy đủ.
- Hai giai đoạn huấn luyện: OBS pretraining (huấn luyện trước trên dữ liệu quan sát) học mô hình kết quả chung, sau đó LoRA fine-tuning (tinh chỉnh hạng thấp — điều chỉnh hiệu quả tham số) trên dữ liệu RCT với cổng hợp nhất yêu cầu cụ thể (request-specific fusion gate).
- Xác thực production: médric uplift ngoại tuyến, phục vụ song song điều trị (treatment-parallel serving), giám sát độ trễ, và kiểm tra A/B trực tuyến 14 ngày. Tacillent: cùng tỷ lệ phụ giá thu (subsidy cost rate), TaQFormer tăng giá trị kinh doanh trên mỗi người dùng 1,26% so với baseline production, vượt trội hơn cả baseline production và mô hình chỉ RCT, đồng thời đáp ứng ngân sách độ trễ. Đã được triển khai cho toàn bộ lưu lượng sàn và hoạt động ở quy mô đầy đủ từ tháng 10/2026.

## Method
Bài toán: phân bổ giảm giá cho M danh mục dịch vụ thay thế cùng lúc. Mỗi điều trị là một vectơ M chiều của độ giảm giá theo danh mục: a = (a₁, ..., a_M). Hành động khả thi a ∈ A thỏa mãn quy tắc kinh doanh: danh mục giá cao hơn nhận giảm giá nghiêm ngặt nhỏ hơn danh mục giá thấp hơn (a₁ < · · · < a_M). Mục tiêu nhân quả: hiệu ứng trị giá trung bình có điều kiện τ(x; a, a₀) = E[Y(a) − Y(a₀) | X = x].

Kiến trúc TaQFormer:
- Đường yêu cầu độc lập với điều trị: feature tokenizer chuyển ngữ cảnh thành N token ngữ nghĩa, stack Encoder Block mã hóa thành biểu diễn yêu cầu H(x) ∈ R^{N×d}.
- Đường điều trị phụ thuộc vào điều trị: mỗi chiều giảm giá là một treatment token, T(a) ∈ R^{M×d}. Treatment tokens làm truy vấn, dùng cross-attention để truy xuất thông tin liên quan từ H(x). Một mạng đọc phi tuyến (nonlinear readout) kết hợp các decoded treatment representations để dự đoán xác suất hoàn thành ˆy(x, a).
- Cross-attention điều trị nhận thức: L khối Treatment Decoder Block, mỗi khối có cross-attention sublayer và feed-forward sublayer. Z⁽⁰⁾ = T(a). Tại khối ℓ, các decoded treatment states là truy vấn, H(x) là khóa và giá trị. Cuối cùng, một MLP hai tầng GELU đọc tất cả M tọa độ đã giải mã để tạo phản hồi tiêu điểm.

Huấn luyện hai giai đoạn:
- Giai đoạn I (OBS pretraining): toàn bộ model được huấn luyện một époque trên dữ liệu OBS với mục tiêu cross-entropy nhị phân chính (primary BCE) cùng giám sát phụ.
- Giai đoạn II (RCT randomized fine-tune): giữ toàn bộ model OBS-trained làm đường tham chiếu đóng băng (frozen reference route) và xây dựng đường RCT riêng. Tokenizer và L − L_a Encoder Block đầu tạo prefix dùng chung. L_a Encoder Block cuối được đánh giá hai lần: một lần với trọng số đóng băng gốc tạo H_obs(x), một lần với cập nhật LoRA tạo H_rct(x). LoRA: W′ = W + (η/r)AB, A và B là ma trận trainable hạng r. Cổng hợp nhất theo từng instance (instance-wise gated fusion): MLP nhỏ g nhận các tóm tắt stop-gradient của bộ nhớ đã điều chỉnh, treatment token RCT, hai logits nhánh, và hiệu tuyệt đối của chúng; α(x,a) = σ(g(...)); logit cuối s(x,a) = α·s_obs + (1−α)·s_rct.

Phục vụ song song điều trị (treatment-parallel serving): tại thời điểm phục vụ, encoder chạy một lần và tạo H(X) cho một lô yêu cầu. Bảng điều trị khả thi được lưu như một tensor hằng số. Tất cả các cặp yêu cầu–điều trị được flatten thành một giải mã batch và reshape đầu ra thành ma trận phản hồi kích thước B × |A|. Giảm tính toán trên mỗi yêu cầu từ |A|(C_enc + C_dec) xuống C_enc + |A|C_dec.

## KNOWLEDGE — Số liệu & khái niệm
- M = 2 danh mục dịch vụ, |A| = 33 điều trị hợp lệ (không tính điều trị tham chiếu). Encoder kích thước d = 64, 4 khối Transformer, 4 đầu chú ý, chiều feed-forward 4d. Treatment decoder L = 2 khối.
- Offline (theo cùng tuần RCT đã giữ lại): PEPNet baseline Qini = 0,1612, AUC = 0,6776, PCOC = 1,3737. TaQFormer: Qini = 0,2697, AUC = 0,7393, PCOC = 1,0012.
- Giao thẳng kiểm tra A/B trực tuyến 14 ngày: PEPNet = 100,00, RCT-only = 101,08 (*), Two-stage TaQFormer = 101,26 (*†). Tỷ lệ phụ giá thu gần như giống nhau: 20,43%, 20,45%, 20,42%. Tất cả so sánh 쌍 có ý nghĩa (p < 0,05).
- Độ trễ P99 = 21 ms trong kiểm tra tải 500 QPS, xếp điểm tất cả 33 điều trị khả thi.
- Two-stage pipeline cải thiện Qini và AUC 0,0033 so với fine-tuning toàn bộ tham số truyền thống, đồng thời đưa PCOC gần với 1 (1,0114 → 1,0027).
- Mô hình được triển khai cho toàn bộ lưu lượng sàn và hoạt động ở quy mô đầy đủ từ tháng 10/2026.

## INSIGHT — Cơ chế & tại sao
[Mỗi tọa độ giảm giá có token điều trị riêng] xảy ra VÌ điều trị có cùng giảm giá cho một danh mục nào đó chia sẻ tham số nhúng, trong khi mỗi tọa độ còn có bảng nhúng riêng để mô hình vẫn biết từng giảm giá thuộc danh mục nào. Điều này nghĩa là [các điều trị liên quan chia sẻ thông tin nhưng vẫn giữ được định danh danh mục, khác với baseline PEPNet hợp nhất nhúng tọa độ thành một vectơ trước khi dự đoán].
[Cổng hợp nhất kết hợp hai nhánh logits dưới giám sát RCT] xảy ra VÌ hai đường (OBS đóng băng và RCT đã điều chỉnh) có phân phối huấn luyện khác nhau và có thể tạo sai số dự đoán khác nhau trên mỗi cặp yêu cầu–điều trị. Điều này nghĩa là [cổng học cách trộn theo từng instance thay vì dùng trọng số cố định, giữ lại thông tin dự đoán hữu ích từ OBS trong khi thích ứng với RCT].

## IDEA — Áp dụng được gì
1. Áp dụng treatment-as-query vào hệ thống gợi ý giảm giá/khuyến mãi đa danh mục: bước đầu là đại diện mỗi chiều giảm giá bằng một truy vấn token, dùng cross-attention để ước lượng phản hồi dưới vectơ điều trị toàn phần.
2. Áp dụng huấn luyện hai giai đoạn OBS→RCT với cổng hợp nhất: bước đầu là huấn luyện trước trên dữ liệu quan sát lớn, sau đó tinh chỉnh LoRA trên dữ liệu RCT nhỏ hơn với một cổng trộn logits theo từng yêu cầu.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Trong mô hình uplift công nghiệp, dữ liệu quan sát lớn cung cấp thông tin dự đoán chung nhưng dữ liệu RCT nhỏ cung cấp điều chỉnh không thiên vị; kết hợp hai nguồn qua cổng hợp nhất theo từng instance tốt hơn chọn một nguồn duy nhất. Khi nào dùng: khi có dữ liệu quan sát lớn và dữ liệu RCT nhỏ hơn cho quyết định can thiệp có cấu trúc (giảm giá, khuyến mãi). Khi nào KHÔNG: khi không có dữ liệu RCT hoặc không cần ước lượng tác động nhân quả.

## Assumptions & Limitations
- Kế hoạch mở rộng phân bổ phiếu giảm giá chung lên nhiều hơn 7 danh mục dịch vụ — sẽ cần đánh giá thêm khả năng bao phủ điều trị, lựa chọn hành động ứng viên, và hiệu quả phục vụ khi không gian hành động khả thi tăng.
- Tính toán chuyên ngành và giá trị tuyệt đối bị giấu kín vì bảo mật.
- Chỉ đánh giá trên một sàn thương mại điện tử cụ thể với M = 2 danh mục.

## Metadata
- Năm 2026; tác giả: Jiahong Li, Zhifan Jiang, Jixing Xu, Zeqin Yang, Jingqi Ma, Jun Wu, Yu Xiang, Enzheng Hua, Fei Wang, Enyun Yu, Jiecheng Guo (tất cả Didi Chuxing, Bắc Kinh, Trung Quốc); category: cs.LG; PDF: https://arxiv.org/pdf/2610.26199v1; citation count: [NO DATA — paper 2026-10-19]