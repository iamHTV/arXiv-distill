# [2608.30730v1] E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

## Giá trị cốt lõi (1 câu)

E-Commerce Bench là benchmark mã nguồn mở đầu tiên tích hợp đàm phán đa vòng với đối tác và sự kiện động vào hoạt động kinh doanh một năm (365 ngày), đánh giá 18 mô hình LLM trên 7 chiều và tìm ra hệ số 1,264 giữa mô hình tốt nhất và kém nhất — cho thấy không có mô hình nào thống trị mọi khía cạnh của vận hành kinh doanh tự trị.

## Problem

Prior work chưa giải quyết được đánh giá tác tử đại lý kinh doanh tự trị trên ngang dài (long-horizon). Các benchmark hiện có hoặc lệch khỏi động lực thị trường thực tế, hoặc dựa trên đối tác LLM thuần túy cho đàm phán đa vòng (giọng tiếng lấy mẫu gây nhiễu sampling noise, suy giảm tính uy tín và khả năng tái lập). Vending-Bench mô phỏng máy bán hàng tự động nhưng dữ liệu giả và phản hồi nhà cung cấp dựa trên prompt -> cực ngẫu nhiên. YC-Bench chạy năm khởi nghiệp déterministik nhưng không có nguồn hàng. MerchantBench và RetailBench có dữ liệu thực nhưng bỏ đàm phán và động lực đối kháng. Không có benchmark nào cùng lúc có: dữ liệu thực, đàm phán deterministik, sự kiện động, quản lý đa cửa hàng, và ngang dài một năm.

## Contribution

(i) E-Commerce Bench: benchmark mã nguồn mở đầu tiên kết hợp đàm phán đối tác deterministik, sự kiện động, và quản lý đa cửa hàng đồng thời trên ngang dài một năm (365 ngày).
(ii) Kinh tế deterministik trên cả hai bên thị trường: mô hình nhu cầu cố định điều khiển mua hàng và trả hàng của khách hàng, nhân thuyết đàm phán deterministik thiết lập mọi quyết định định giá,譲歩 và chấp nhận/từ chối, LLM chỉ dùng để diễn đạt lời thoại (verbalize).
(iii) 6,886 sản phẩm trong 60 danh mục, 576 nhà cung cấp (424 trung thành, 152 gian lận), dữ liệu lấy từ nền tảng thương mại điện tử thực (Taobao & Tmall).
(iv) 18 công cụ trong 7 nhóm, bối cảnh 128,000 token với sự đào thải bám nhóm (group-wise eviction) ở 120,000, không gian lưu trữ liên tục (persistent memory store) tối đa 20 mục.
(v) Đánh giá 18 mô hình frontier trên 7 chiều: tài sản cuối năm, chất lượng đàm phán, tránh gian lận, dòng tiền và khả năng thanh toán, hiệu quả vận hành, thực thi vận hành, học theo ngang dài.
(vi) Kết quả: GPT-5.6 Sol đạt ¥1,431,425 (14,3× vốn ¥100,000) nhưng xếp hạng 16/18 về tránh gian lận; Qwen3.8-Max-Preview dẫn nhóm mã nguồn mở với ¥416,252 (4,2×), xếp hạng 5 tổng thể; hệ số 1,264 giữa mô hình hàng đầu và cuối cùng; 10/90 lần chạychap ngân sách.

## Method

E-Commerce Bench hoạt động qua 4 lớp: (1) Lớp vòng tác tử (agent loop layer): điều khiển theo lượt (turn-based), quản lý bối cảnh, bộ nhớ liên tục. Mỗi lượt mô hình có thể gọi nhiều công cụ, chạy theo thứ tự. Một công cụ trừ nhảy ngày tốn phút mô phỏng (10 phút kiểm tra số dư, 60 phút mở cửa hàng). Ngày chạy 08:00–18:00 (600 phút), sau 18:00 nhảy sang 08:00 ngày hôm sau. Bối cảnh được đào thải khi vượt 120,000 token (mục tiêu giải phóng 60,000), nhóm công cụ cũ nhất bị loại trước. Bộ nhớ liên tục (persistent memory store) tối đa 20 mục, tác tử tự quản lý (tạo, cập nhật, cắt bớt). (2) Lớp công cụ (tool layer): 18 công cụ làm văn phòng sau của thương nhân, chia 7 nhóm, mỗi công cụ trừ nhảy ngày tốn phút mô phỏng. (3) Lớp môi trường (environment layer): động cơ bán hàng và kinh tế (sales and economy engine) bên cạnh động cơ đàm phán hai tầng (two-layer negotiation engine). (4) Lớp dữ liệu (data layer): lấy từ nền tảng thương mại điện tử thực.

Động cơ đàm phán: mỗi nhà cung cấp chia 2 tầng. Tầng 1 (nhân thuyết deterministik): mọi quyết định định giá,譲歩, chấp nhận/từ chối đến từ nhân thuyết deterministik chứ không phải mô hình. Tầng 2 (bọc renderer): LLM diễn đạt mỗi quyết định cam kết của nhân thuyết thành tin nhắn cửa hàng, chỉ lấy cảm xúc từ cue cảm xúc của nhân thuyết. Khoảng 1/4 nhà cung cấp là gian lận (fraudulent), chạy một trong 5 lớp lừa scripted. Giá không mang tín hiệu về gian lận theo thiết kế — bằng chứng決定 nằm trong lời thoại trước khi thành thệuc.

Mô hình nhu cầu: nhu cầu mỗi SKU mỗi ngày = nhu cầu cơ sở của danh mục × 6 nhân strips (phản ứng giá, cuối tuần uplift, khuyến mãi, mùa vụ theo tháng, sự kiện lịch hệ, danh tiếng cửa hàng) × 2 nhân công năng (danh mục, cửa hàng).

Đánh giá: điểm chính là tổng tài sản cuối năm (tài khoản ngân hàng + ví nền tảng + escrow chưa thanh toán), báo cáo dưới dạng hệ số so với vốn mở cửa ¥100,000. Chap ngân sách: 10 ngày liên tiếp số dư ngân hàng âm. 6 chiều đánh giá: (1) chất lượng đàm phán (CSE+): tỷ lệ khoảng đàm phán mà thỏa thuận đóng cửa thu được; (2) tránh gian lận (BadSpend%): tỷ lệ chi tiêu đơn hàng đã thanh toán vào tài khoản nhà cung cấp gian lận; (3) dòng tiền và khả năng thanh toán (drawdown trên đỉnh tổng tài sản); (4) hiệu quả vận hành (lợi nhuận trung bình trên mỗi lệnh gọi công cụ); (5) thực thi vận hành (lãi suất trả hàng có thể kiểm soát); (6) học theo ngang dài (AnchorRatio): mức quá trả trên mỗi lần đặt lại so với giá rẻ nhất đã từng giành được từ nhà cung cấp đó cho mặt hàng đó.

## KNOWLEDGE — Số liệu & khái niệm

- 18 mô hình được đánh giá (8 độc quyền, 10 mã nguồn mở), 5 tập sự mỗi mô hình, 90 sự kiện tổng cộng.
- Hệ số 1,264 tách GPT-5.6 Sol ở trên cùng từ Qwen3.5-Plus ở dưới cùng.
- GPT-5.6 Sol: ¥1,431,425 tài sản cuối năm (14,3× vốn ¥100,000), xếp hạng 16/18 về tránh gian lận, kém Fable5 về hiệu quả vận hành.
- Qwen3.8-Max-Preview: ¥416,252 (4,2×), dẫn nhóm mã nguồn mở, xếp hạng 5 tổng thể, học mạnh nhất theo ngang dài (m सौ매n progressively bargain down prices across repeated orders).
- 10/90 sự kiện chap ngân sách, 6 trong số đó dưới mô hình độc quyền.
- GPT-5.5, Claude Opus 4.6, Gemini 3.1 Pro, Qwen3.5-Plus phụ trách tất cả 10 sự kiện chap ngân sách.
- Claude Opus 4.7 giữ được phần lớn nhất của khoảng đàm phán (0.811), dẫn cả đàm phán và tránh gian lận từ nhóm giữa về lợi nhuận.
- Kimi K2.6 giữ ít nhất (0.596).
- 6,886 sản phẩm trong 60 danh mục, 576 nhà cung cấp (424 trung thành, 152 gian lận).
- 12 loại cửa hàng, tối đa 4 cửa hàng giao dịch đồng thời, một loại cửa hàng mỗi lần.
- Mở cửa hàng tốn ¥500 và ¥60–130/ngày để vận hành.
- Bối cảnh 128,000 token, đào thải bắt đầu ở 120,000, mục tiêu giải phóng 60,000.
- Bộ nhớ liên tục tối đa 20 mục (tiêu đề + nội dung).
- 3 tài khoản thanh toán hoãn định: tài khoản ngân hàng (chi phí ngay), escrow (do thu nhập bán hàng sau khi giao hàng, trừ hoa hồng nền tảng), ví nền tảng (t mature sau 9 ngày, chỉ lấy ra qua tác vụ rõ ràng).
- Chap ngân sách: 10 ngày liên tiếp số dư ngân hàng âm dừng sự kiện.
- Khoảng 1/4 nhà cung cấp gian lận, chạy 1 trong 5 lớp lừa scripted (2 lớp lừa trước khi thành thệuc, 3 lớp lừa sau khi thành thệuc).
- Giá không mang tín hiệu về gian lận theo thiết kế.

## INSIGHT — Cơ chế & tại sao

[Hệ số 1,264 giữa mô hình tốt nhất và kém nhất] cho thấy không có mô hình nào thống trị mọi khía cạnh của vận hành kinh doanh tự trị — môi trường là deterministik cho dù chuỗi hành động, nên khoảng cách này thuộc về tác tử chứ không phải do nhu cầu được lấy mẫu lại. Điều này nghĩa là hoạt động kinh doanh tự trị là một môi trường đánh giá phân biệt mạnh, nơi các mô hình có thể khác nhau rất nhiều trong khả năng kết hợp vốn, định giá, phục vụ khách hàng và đáp ứng nghĩa vụ vận hành.

[Không có mô hình nào ocupar vị trí hàng đầu trên mọi chiều] (GPT-5.6 Sol dẫn về lợi nhuận nhưng xếp 16/18 về tránh gian lận; Claude Opus 4.7 dẫn về đàm phán và tránh gian lận nhưng nằm ở giữa về lợi nhuận). Điều này nghĩa là một điểm số tổng hợp (tài sản cuối năm) không đủ để hiểu thực sự tác tử mạnh hay yếu ở đâu — cần chẩn đoán đa chiều.

[Determinism trên cả hai bên thị trường] (mô hình nhu cầu cố định + nhân thuyết đàm phán deterministik) đảm bảo sự khác biệt trong kết quả hoàn toàn thuộc về chính sách tác tử chứ không phải do may răn. Điều này nghĩa là benchmark có thể tái lập chính xác — hai sự kiện thực hiện cùng chuỗi hành động sẽ kết thúc năm với cùng số tiền.

[Học theo ngang dài (AnchorRatio) cho thấy 16/18 mô hình không có dấu hiệu rõ ràng về giảm giá mua trên các lần đặt lại] qua 8,647 lần mua lại cùng mặt hàng từ cùng nhà cung cấp trung thành. Điều này nghĩa là khả năng biến kinh nghiệm trước thành quyết định tốt hơn trên ngang dài là một thiếu hụt quan trọng của các mô hình hiện tại.

[Giá không mang tín hiệu về gian lận theo thiết kế] — bằng chứng quyết định nằm trong lời thoại trước khi thành thệuc, không mẫu mã cố định nào có thể xây dựng nó. Điều này nghĩa là tác tử phải đọc hiểu bối cảnh câu chuyện chứ không chỉ dựa trên giá để phát hiện gian lận.

## IDEA — Áp dụng được gì

Áp dụng [E-Commerce Bench] vào việc đánh giá tác tử thương mại cho solopreneur VN: thay vì chỉ kiểm tra xem tác tử có thể trả lời câu hỏi hay không, hãy tạo môi trường mô phỏng nơi tác tử phải chạy một cửa hàng bán hàng trên năm (nhập hàng, đàm phán giá, định giá, giao hàng, xử lý trả hàng, quản lý dòng tiền) và đo tài sản cuối năm.

Áp dụng [chẩn đoán đa chiều (multi-dimensional analysis)] vào việc đánh giá tác tử của riêng bạn: thay vì chỉ theo dõi một chỉ số tổng hợp, hãy đánh giá riêng rẽ trên 7 chiều (lợi nhuận, đàm phán, tránh gian lận, dòng tiền, hiệu quả, thực thi, học tập) để biết tác tử mạnh hay yếu ở đâu.

Áp dụng [deterministic evaluation] vào việc kiểm thử tác tử: đảm bảo môi trường đánh giá là deterministik cho cùng chuỗi hành động, để sự khác biệt trong kết quả hoàn toàn thuộc về chính sách tác tử chứ không phải do may răn.

## WISDOM — Nguyên tắc tổng quát

Nguyên tắc: Đánh giá tác tử kinh doanh tự trị qua điểm tài sản cuối năm kết hợp với chẩn đoán đa chiều (không chỉ một số tổng hợp) là hiệu quả hơn, bởi vì các mô hình có thể mạnh trên một chiều nhưng yếu trên chiều khác, và một điểm số duy nhất có thể che giấu điểm yếu quan trọng.

Khi nào dùng: Khi cần đánh giá tác tử AI cho vận hành thương mại, bán lẻ hoặc bất kỳ ứng dụng nào liên quan đến ra quyết định liên tiếp trên ngang dài với hậu quả tài chính.

Khi nào KHÔNG dùng: Khi tác tử chỉ cần thực hiện các tác vụ ngắn hạn, có thể xác minh, không cần quản lý vốn dài hạn hoặc thích ứng với sự kiện động.

Ví dụ áp dụng ngoài domain gốc: Xây dựng benchmark cho tác tử quản lý đầu tư tự động — tác tử phải quản lý danh mục cổ phiếu, trái phiếu, tiền gửi trong một năm, với kết quả được đo bằng tổng tài sản cuối năm và phân tích đa chiều (rủi ro, hiệu quả, khả năng học từ kinh nghiệm).

## Assumptions & Limitations

- Điều kiện đúng: Có dữ liệu thương mại thực hoặc có thể tổng hợp từ nhật ký phân tích; tác tử có thể sử dụng 18 công cụ trong 7 nhóm; môi trường mô phỏng có thể chạy deterministik.
- Limitation paper thừa nhận: Không có limitations section rõ rệt (paper kết thúc tại Conclusion rồi sang References); 5 sự kiện là mẫu nhỏ nên mọi trung bình trong bảng đều in với độ lệch chuẩn; không đánh giá tác tử trên các mô hình nhỏ hơn; không đánh giá chi phí chạy benchmark.
- Limitation paper KHÔNG nói: Không có Limitations section rõ rệt trong paper; không đánh giá độ ổn định khi sự kiện thị trường thay đổi mạnh hơn mức đã mô phỏng; không đánh giá trên các ngôn ngữ ngoài tiếng Trung (dữ liệu từ Taobao & Tmall).

## Metadata

- Năm: 2026
- Tác giả: Wei Fan, Xinjie Shen, Xudong Guo, Jianhong Tu, Yang Su, Yinger Zhang, Lianghao Deng, Fengyu Wang, Baohua Dong, Yangqiu Song, Dayiheng Liu
- Thể loại arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2608.30730v1
- Số lượt trích dẫn: chưa có thông tin