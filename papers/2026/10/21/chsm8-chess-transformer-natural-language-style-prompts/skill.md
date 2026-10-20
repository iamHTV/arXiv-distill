# Skill: nlp-style-behavior-control-dpo

Source: 2610.25356v1
Type: framework / workflow

## Khi nào dùng skill này
- Khi cần điều khiển hành vi hoặc phong cách của một mô hình AI qua hướng dẫn văn bản tự nhiên (natural language instruction), thay vì chỉ điều khiển qua rating hoặc danh tính.
- Khi muốn cải thiện khả năng tuân theo phong cách (style adherence) của mô hình mà không cần xây dựng reward model phức tạp.
- Khi cần cân bằng giữa việc tuân theo hướng dẫn và duy trì sức mạnh cơ bản của mô hình.

## Tình huống KHÔNG nên dùng
- Khi tác vụ không có sự phân biệt rõ ràng giữa đầu ra tốt và xấu.
- Khi không có dữ liệu cặp (cùng đầu ra, điều kiện khác nhau) để huấn luyện DPO.
- Khi không có tài nguyên GPU để chạy fine-tune hoặc DPO.

## Input cần có
- Tập dữ liệu cặp: cùng đầu ra nhưng dưới hai điều kiện khác nhau (mô tả khớp vs mô tả không khớp).
- Mô hình SFT đã được huấn luyện trước (reference model).
- Tài nguyên GPU cho DPO (khuyến nghị ít nhất 1 GPU cho chạy ngắn, nhiều GPU cho chạy đầy đủ).
- Tập validation với các metric đánh giá style adherence và sức mạnh cơ bản.

## Các bước thực hiện
1. Chuẩn bị dữ liệu cặp (label-swap pairs): lấy cùng một ván cờ/output, gán mô tả khớp làm mẫu được chọn và mô tả không khớp làm mẫu bị từ chối.
2. Chạy SFT trước: gắn text encoder đóng băng vào mô hình qua gated cross-attention, huấn luyện trên dữ liệu có mô tả phong cách.
3. Chạy DPO: dùng cùng những nước đi/dầu ra dưới mô tả không khớp làm mẫu bị từ chối, với hàm loss DPO kết hợp NLL anchor và KL term.
4. Pin no-text term: giữ nguyên no-prompt policy không thay đổi thông qua cross-attention biases.
5. Tinh chỉnh hyperparameters: β, NLL weight, KL weight, learning rate cho body và conditioning layer.
6. Đánh giá trên tập validation: đo style adherence (theo các metric như tỷ lệ trades, pawn moves, castling) và sức mạnh không prompt (Elo hoặc metric tương đương).
7. Chạy vòng lặp tìm kiếm tự động: hàng đợi các cấu hình, mỗi chạy cố định thời gian, chấm điểm, lên kế hoạch vòng tiếp theo từ kết quả.

## Output mong đợi
- Một mô hình đã được điều khiển hành vi qua natural language, với style adherence cao và sức mạnh cơ bản giữ nguyên.
- Báo cáo đánh giá: style adherence metrics, sức mạnh không prompt, attack gap (tỷ lệ giảm sức mạnh dưới prompt rủi ro).

## Ví dụ áp dụng
Một công ty muốn xây dựng một LLM agent tư vấn bán hàng có thể thay đổi phong thái tiếp cận theo yêu cầu của khách (ví dụ: "hãy nhiệt tình và nhanh chóng", "hãy trầm lặng và chuyên nghiệp"). Họ thu thập các cặp conversación (cùng câu trả lời, nhưng một được mô tả là nhiệt tình, một khác là trầm lặng), chạy DPO để agent tuân theo phong cách yêu cầu mà không cần reward model.

## Gotchas
- Không để từ tiếng Anh không giải thích: factorized move representation (biểu diễn nước đi phân tích), legal-move masking (che nước đi hợp pháp), gated cross-attention (chéo quan tâm có cổng), label-swap pairs (cặp hoán đổi nhãn), NLL (negative log-likelihood — xác suất âm logarithm), KL term (hосле khai số Kullback-Leibler), alignment tax (thuế căn chỉnh — mất mát sức mạnh khi căn chỉnh style), attack gap (khoảng cách tấn công — giảm sức mạnh dưới prompt tấn công), distilled (đã蒸馏), gated cross-attention (chéo quan tâm có cổng), pinned no-text term (công cụ không văn bản cố định), body learning rate (tốc độ học phần thân), conditioning learning rate (tốc độ học phần điều chỉnh), wall-clock budget (ngân sách thời gian thực), validation set (tập kiểm chứng), style adherence (tuân theo phong cách), no-prompt strength (sức mạnh không có prompt).
- DPO cần dữ liệu cặp chất lượng: nếu NLL weight quá yếu, mô hình tìm lối tắt (làm conditioning gây hại) và Elo giảm 50-145 điểm.
- Phải pin no-text term, nếu không no-prompt policy sẽ bị thay đổi qua cross-attention biases.
- Full pass DPO không phải luôn tốt hơn chạy ngắn: style adherence饱和 sớm, nhiều dữ liệu hơn không cải thiện chơi.
- Screening với ít ván (100) có thể dẫn đến kết quả sai lệch (ví dụ: đánh giá −66 nhưng thực tế −165 tại 1.000 ván).
- Style adherence chỉ đáng tin cậy khi có metric xác thực, không chỉ metric viết tay.