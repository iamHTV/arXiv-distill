# [2608.08621] Business Arena: Benchmarking LLM Agents in a Realistic Marketplace

## Giá trị cốt lõi (1 câu)

Business Arena là môi trường kiểm soát nơi tác tử AI chạy một cửa hàng bán xuyên biên giới, mua từ nhà cung cấp và bán cho người mua theo ngang dài (long horizon), đánh giá 15 mô hình LLM frontier và tìm ra khoảng cách 9.0× trong trị giá ròng cuối cùng trung bình — cho thấy vận hành doanh nghiệp vẫn là thách thức lớn đối với tác tử LLM hiện tại.

## Problem

Prior work chưa giải quyết được đánh giá năng lực liên quan đến doanh nghiệp trong các benchmark tác tử hiện có. Các benchmark tác tử hiện tại tập trung vào tác vụ ngắn hạn, có thể xác minh (v patch code, điều hướng web, tuân thủ chính sách), trong khi vận hành doanh nghiệp thực tế yêu cầu suy luận trong điều kiện không certeza, cam kết vốn dưới sự không certeza, thích ứng với kết quả bị trễ trong thị trường thay đổi, và đáp lại nghĩa vụ quy định trước khi giao dịch theo quy định.

## Contribution

(i) Business Arena: môi trường kiểm soát nơi tác tử AI chạy cửa hàng bán xuyên biên giới, mua từ nhà cung cấp và bán cho người mua theo ngang dài, cơ sở dữ liệu nguồn từ dữ liệu cung cấp thực của Alibaba.com và điều kiện thị trường được quyenchính từ các nguồn uy tín.
(ii) Phân tích khả năng kinh doanh thành 4 năng lực: ra quyết định trong điều kiện không certeza, lập kế hoạch chiến lược dưới ràng buộc, cộng hưởng hiểu biết–hành động, hợp tác & cạnh tranh.
(iii) Chỉ số mức độ kỹ năng (skill-level metrics) tiết lộ những điểm mạnh/yếu ẩn sau kết quả tổng hợp; công cụ gán giá trị hành động (action-level attribution) truy vết giá trị/thua lỗ đã thực hiện về lại các hành động cụ thể tạo ra chúng.
(iv) Điều khiển cơ chế (mechanism ablation) thiết lập kết quả mạnh mẽ trongarena phản ánh trí thông minh kinh doanh thật chứ không phải lối tắt đặc thù của mô phỏng.
(v) Đánh giá 15 mô hình frontier: trị giá ròng cuối cùng trung bình dao động từ $20,856 đến $188,488 (khoảng cách 9.0×); 51% tất cả các lần chạy lỗ tiền; chỉ 4 mô hình bảo toàn vốn ban đầu trong mọi lần thử; chiến lược chuyên gia thiết kế mạnh nhất đạt $436,195, gấp hơn 2 lần trung bình mô hình tốt nhất.

## Method

Business Arena đặt một tác tử điều hành shop trong một thị trường gồm nhà cung cấp, người mua và đối thủ cạnh tranh. Tác tử chịu trách nhiệm vận hành doanh nghiệp đầu đến cuối và thích ứng theo thời gian. Một episode bắt đầu bằng giai đoạn thiết lập trước khi mở cửa: tác tử khai báo trọng tâm cửa hàng ban đầu (có thể sửa sau khi bằng chứng thị trường tích lũy), sau đó kiểm tra các cơ hội có sẵn và quyết định xem có mua kho hàng đầu tư hay giữ vốn cho việc nhập hàng sau. Kho hàng được chọn trong thiết lập sẵn sàng vào ngày 0, cho phép cửa hàng bắt đầu giao dịch mà không bị trễ vận chuyển không thể tránh được. Sau thiết lập, tác tử thoả mãn yêu cầu của các thị trường nó định vào và cấu hình các danh sách qua đó sản phẩm của nó được đưa ra bán.

Trong mỗi ngày mô phỏng, tác tử có thể kiểm tra thị trường, điều chỉnh các Angebot, nhập hoặc bổ sung kho hàng, phân bổ chi phí quảng cáo, quản lý thanh khoản và đáp lại người mua và nhà cung cấp trước khi chọn cải thiện ngày. Sau đó arena tiến bộ phần còn lại của thị trường một cách độc lập: người mua đưa ra quyết định mua hàng, đối thủ cập nhật hoạt động của họ, hàng hóa tiến bộ, chi phí tài chính bị trừ, và các sự kiện hoặc tín hiệu thị trường mới có thể xuất hiện. Vì các quá trình này diễn ra độc lập với tác tử, các điều kiện nó đối mặt thay đổi trong suốt episode. Kết quả của ngày cập nhật trạng thái thế giới bền vững, mà tác tử có thể kiểm tra trước khi quyết định xem có mở rộng sản phẩm thành công, sửa giá, thay đổi trọng tâm, hoặc thanh lý kho hàng yếu hay không. Sau ngày cuối cùng, kho hàng còn lại đóng góp vào trị giá ròng cuối cùng với giá récup phần trăm (discounted salvage value).

Ba nguyên tắc chế độ arena: (i) bằng chứng không đầy đủ và ồn ào (incomplete and noisy evidence) — tác tử không thể quan sát trực tiếp điều kiện thị trường ẩn, nhưng có thể thu thập bằng chứng từ các tín hiệu công khai, đối thủ, đối tác và lịch sử vận hành của mình; (ii) hậu quả kinh tế bị trễ (delayed economic consequences) — chi phí hàng ngày cố định làm cho việc để vốn nhàn rằng tốn kém, trong khi phí giữ kho và giá récup giảm phạt việc triển khai thiếu cân nhắc vào sản phẩm không bán được; (iii) thị trường thay đổi (a changing market) — thị trường tiếp tục phát triển dù tác tử có hành động hay không; (iv) nghĩa vụ vận hành bền vững (persistent operational obligations) — tác tử phải thỏa mãn yêu cầu tuân thủ và vận hành trước khi có thể giao dịch theo pháp luật.

4 năng lực kinh doanh được đánh giá: (1) Ra quyết định trong điều kiện không certeza — trước khi người bán có thể quyết định mua gì hoặc bán ở đâu, nó phải hình thành quan điểm về những gì đang xảy ra trong thị trường; (2) Lập kế hoạch chiến lược dưới ràng buộc — sau khi hình thành quan điểm về thị trường, người bán phải chuyển nó thành kế hoạch vận hành: loại cửa hàng nào để xây dựng, cơ hội nào để theo đuổi, bao nhiêu vốn để triển khai, và bao nhiêu rộng để đa dạng hóa; (3) Cộng hưởng hiểu biết–hành động (Insight-to-Action Alignment) — kế hoạch kinh doanh khéo léo là không đủ; người bán phải làm đúng các chi tiết vận hành; (4) Hợp tác & Cạnh tranh — người bán không vận hành trong sự cô lập.

## KNOWLEDGE — Số liệu & khái niệm

- 15 mô hình frontier được đánh giá (khương tài: GPT 5.6 Sol, GPT-5.5, Claude Fable 5, Opus 4.6 và 4.8, Gemini 3.1 Pro và 3.5 Flash, Qwen 3.7 Max; mã nguồn mở: GLM 5.2, Kimi K2.6 và K3, DeepSeek V4 Pro, MiniMax M2.5 và M3, Qwen-3.8-Max-Preview).
- Trị giá ròng cuối cùng trung bình: $188,488 (Gemini 3.1 Pro) đến $20,856 (MiniMax M2.5), khoảng cách 9.0×.
- 51% tất cả các lần chạy lỗ tiền so với vốn ban đầu $80,000.
- Chỉ 4 mô hình bảo toàn vốn ban đầu trong mọi lần thử.
- Chiến lược chuyên gia thiết kế mạnh nhất: $436,195, gấp hơn 2 lần trung bình mô hình tốt nhất.
- ICC = 0.944 (trung bình 10 lần chạy đáng tin cậy), ρ = 0.898 (thứ hạng được bảo toàn trong tập con 5 lần chạy khác nhau), 98.7% cùng nhóm dẫn đầu.
- Vận dụng vốn (capital utilization): Gemini 3.1 Pro 199%, GPT-5.6 Sol 167%, Fable 5 150%; Qwen 3.7 Max chỉ 22.3% (ít đầu tư).
- Lợi nhuận đơn hàng (order margin): Gemini 3.1 Pro 52.0% (Premium House); GPT-5.6 Sol và Opus 4.6 >93% sell-through (Volume Wholesalers); MiniMax M2.5 12.1% margin, <40% sell-through (Stranded Shop).
- Dịch vụ khách hàng: Opus 4.8 chuyển đổi 84%, Fable 5 81%, Qwen 3.8 74%, Gemini 3.1 Pro 57%.
- Tuân thủ (compliance): Fable 5 và GPT-5.5 không có vi phạm bị phạt; MiniMax M2.5 trung bình 22.7 vi phạm và $51,750 tiền phạt; DeepSeek V4 Pro 17.4 vi phạm và $39,650.
- Điều khiển cơ chế (mechanism ablation): Dự án danh mục (dự án dựa trên nhu cầu) +$63.6k vs mua sỉ mù quáng -$14.6k; Sự kiện thị trường (kiểm tra bằng chứng) +$6.6k vs bỏ qua sự kiện -$17.3k; Định giá (giá toàn bộ chi phí) +$50.3k vs định giá gần chi phí -$58.1k; Thuế quan (định tuyến nhận thức thuế quan) +$25.9k vs Focus Mỹ mù thuế quan -$3.7k; Dịch vụ khách hàng (trả lời dựa trên bằng chứng) +$5.6k vs trả lời chung chung 0.
- Hơn 60 công cụ trải quanh chuỗi kinh doanh, hỗ trợ lập luận nhiều bước và hành động riêng lẻ, gọi MCP kiểu, API sau cùng và không gian làm việc bền vững.

## INSIGHT — Cơ chế & tại sao

[Khoảng cách 9.0× giữa mô hình tốt nhất và kém nhất] cho thấy hoạt động doanh nghiệp vẫn là thách thức lớn đối với tác tử LLM hiện tại — sự khác biệt không chỉ là độ sâu suy luận mà là khả năng kết hợp vốn, định giá sản phẩm, phục vụ khách hàng và đáp ứng nghĩa vụ vận hành. Điều này nghĩa là benchmark doanh nghiệp có thể phân biệt các mô hình nơi benchmark ngắn hạn không thể.

[51% các lần chạy lỗ tiền] cho thấy việc bảo toàn vốn một cách liên tục quan trọng hơn việc bù đắp những lần lỗi thường xuyên bằng một vài lần chạy xuất sắc. Điều này nghĩa là một tác tử hữu ích thương mại phải bảo toàn vốn ổn định chứ không chỉ đạt được lợi nhuận cao ở một số lần.

[Chiến lược chuyên gia đạt gấp hơn 2 lần mô hình tốt nhất] cho thấy còn có khoảng lớn (headroom) để cải thiện — tác tử LLM hiện tại vẫn chưa khai thác hết cơ hội có sẵn trong thị trường. Điều này nghĩa là có không gian lớn cho việc cải thiện tác tử qua dữ liệu huấn luyện tốt hơn và RL.

[Phân tích mức độ kỹ năng (skill-level analysis) tiết lộ các kiểu vận hành nhận ra được]: từ người bán tập trung vào biên độ lợi (margin-focused premium sellers) đến người bán xoáy vòng cao (high-turnover wholesalers) và chuyên viên chăm sóc khách hàng (customer-service specialists). Điều này nghĩa là một điểm số cuối cùng duy nhất có thể che giấu những điểm mạnh/yếu quan trọng — cần chẩn đoán cấp độ kỹ năng để hiểu thực sự tác tử mạnh hay yếu ở đâu.

[Gán giá trị hành động (action-level attribution)] truy vết giá trị/thua lỗ đã thực hiện về lại các hành động cụ thể tạo ra chúng. Điều này nghĩa là thay vì chỉ quan sát một mô hình earns nhiều hơn, chúng ta có thể nhận ra sự khác biệt hành hoạt thức sau khoảng cách và đo tầm quan trọng kinh tế của nó — cung cấp cơ sở tự nhiên cho gán giá trị học khích cường hóa (RL) ở cấp độ hành động kinh doanh riêng lẻ.

## IDEA — Áp dụng được gì

Áp dụng [Business Arena] vào việc đánh giá tác tử kinh doanh cho solopreneur VN: thay vì chỉ kiểm tra xem tác tử có thể trả lời câu hỏi hay không, hãy tạo một môi trường mô phỏng nơi tác tử phải chạy một doanh nghiệp thực tế (nhập hàng, định giá, phục vụ khách hàng, tuân thủ quy định) và đo kết quả tài chính cuối cùng.

Áp dụng [chỉ số mức độ kỹ năng (skill-level metrics)] vào việc chẩn đoán tác tử của riêng bạn: thay vì chỉ theo dõi một số liệu tổng hợp, hãy đo lường vận dụng vốn, hiệu suất bán hàng, tuân thủ và dịch vụ khách hàng riêng rẽ để biết tác tử mạnh hoặc yếu ở đâu.

Áp dụng [gán giá trị hành động (action-level attribution)] vào việc cải thiện tác tử: truy vết từng quyết định về lại kết quả tài chính của nó để biết quyết định nào nên được khuyến khích và quyết định nào cần được sửa — tạo cơ sở cho dữ liệu huấn luyện và học khích cường hóa trong tương lai.

## WISDOM — Nguyên tắc tổng quát

Nguyên tắc: Đánh giá tác tử doanh nghiệp qua kết quả tài chính cuối cùng kết hợp với phân tích cấp độ kỹ năng và gán giá trị hành động là hiệu quả hơn chỉ dùng một điểm số tổng hợp, bởi vì kết quả tương tự có thể đến từ các lựa chọn vận hành khác nhau và giá trị của các lựa chọn đó phụ thuộc vào cơ hội có sẵn trong thị trường.

Khi nào dùng: Khi cần đánh giá tác tử AI cho vận hành doanh nghiệp, thương mại điện tử hoặc bất kỳ ứng dụng nào liên quan đến ra quyết định trong điều kiện không certeza với hậu quả bị trễ.

Khi nào KHÔNG dùng: Khi tác tử chỉ cần thực hiện các tác vụ ngắn hạn, có thể xác minh (ví dụ: v patch code, điều hướng web) mà không cần quản lý vốn dài hạn hoặc thích ứng với thị trường thay đổi.

Ví dụ áp dụng ngoài domain gốc: Xây dựng benchmark cho tác tử tài chính cá nhân (personal finance agent) — tác tử phải quản lý ngân sách, đầu tư, tiết kiệm và trả nợ theo thời gian, với kết quả được đo bằng trị giá ròng tài sản cuối cùng và phân tích cấp độ kỹ năng cho từng quyết định tài chính.

## Assumptions & Limitations

- Điều kiện đúng: Có dữ liệu thương mại thực hoặc có thể mô phỏng được; tác tử có thể sử dụng hơn 60 công cụ trải quanh chuỗi kinh doanh; môi trường mô phỏng có thể chạy độc lập với tác tử.
- Limitation paper thừa nhận: Arena tập trung vào ra quyết định kinh doanh đầu đến cuối và do đó trừu tượng hóa các hệ thống vận hành bên ngoài sau các công cụ có cấu trúc; đánh giá xem tác tử chọn làm gì, chứ không phải xem nó có thể cập nhật cửa hàng trực tiếp, đưa ra đề nghị qua các nền tảng bên thứ ba, hoặc quản lý cuộc trò chuyện khách hàng qua hộp thư và GUI thực sự. Arena hiện tại cũng giới hạn ở thương mại B2B xuyên biên giới, trong khi doanh nghiệp trải qua nhiều kịch bản và ngành công nghiệp khác nhau.
- Limitation paper KHÔNG nói: Không có đánh giá trên các mô hình nhỏ hơn (dưới 7B tham số); không có đánh giá chi phí chạy arena (chi phí tính toán, thời gian mỗi episode); không có đánh giá độ ổn định khi điều kiện thị trường thay đổi mạnh hơn mức đã mô phỏng.

## Metadata

- Năm: 2026
- Tác giả: Yijun Pan, Yukun Lian, Kunyu Shi, Junbo Li, Hongwei Xue, Sicong Xie, Guannan Zhang, Xiaoying Xing
- Thể loại arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2608.08621
- Số lượt trích dẫn: chưa có thông tin