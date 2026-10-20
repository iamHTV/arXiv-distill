# [2610.25356v1] CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts

## Giá trị cốt lõi (1 câu)
Một cờ vua transformer 210M tham số có thể điều khiển phong cách chơi bằng mô tả văn bản tự do (free-text style prompt), với style adherence tăng rõ rệt sau DPO (queens traded early 53%→67%, queenside castling 97.3%→99.7%) mà không làm suy yếu sức mạnh không có prompt (1792 vs 1797 Elo).

## Problem
Prior work kiểm soát mô hình cờ vua qua rating hoặc danh tính cầu thủ, không chấp nhận yêu cầu mở dạng "castle queenside and storm the enemy king with your pawns". Các mô hình hiện có không cho phép người dùng định hướng phong cách chơi bằng văn bản tự nhiên thoải mái.

## Contribution
1. Mô hình cờ vua đầu tiên (đến tri thức tác giả) chơi theo mô tả phong cách tự do bằng văn bản tự nhiên, thay vì rating, danh tính cầu thủ hoặc prompt mẫu.
2. Pipeline toàn bộ mở và tái sản xuất: trọng số, tập dữ liệu (bao gồm nhãn giáo viên dùng để huấn luyện labeler và mô hình phong cách), công thức hoàn chỉnh với prompt và cấu hình, mã suy luận và demo chơi được công khai.
3. Tập dữ liệu mới không tồn tại trước đây: corpus 1.07B ván cờ lọc từ kho 7.95B ván Lichess; ván trực tuyến của top 100 FIDE; 5 mô tả phong cách cho mỗi trong 30.1M ván bên; nhãn giáo viên và tập蒸馏 phía sau labeler.

## Method
CHSM8-PT được pretrain trên 1.07B ván cờ Lichess đã lọc (theo rating, thời gian kiểm soát, chất lượng ván), dùng factorized move representation và legal-move masking, không dùng search, đạt 1837 Elo đối với Stockfish giới hạn sức mạnh. Sau đó labels 30.1M ván bên bằng mô tả phong cách tự nhiên: Gemma-4-31B mô tả phong cách chơi của 3M ván bên, Gemma-3-1B được蒸馏 từ 2.4M mô tả không mâu thuẫn với nhãn ván bên gán nhãn phần còn lại, mỗi ván bên được chọn nhận 5 mô tả. SFT gắn một text encoder đóng băng thông qua gated cross-attention. DPO dùng cùng những nước đi dưới mô tả không khớp làm mẫu bị từ chối. Sau DPO, style adherence tăng trên mọi prompt được thử. Lựa chọn thiết kế ở mọi giai đoạn được đưa ra bởi vòng lặp tìm kiếm tự động có ngân sách cố định trên các kiến thức và training recipe tiêu chuẩn. Hệ thống hoàn toàn mở nguồn và có thể tái sản xuất.

## KNOWLEDGE — Số liệu & khái niệm
- Kiến trúc: 210M tham số, decoder theo recipe Llama, text conditioning qua Flamingo-style gated cross-attention
- Corpus pretraining: 1.07B ván cờ lọc từ 7.95B ván Lichess (lọc theo rating, time control, game quality); 49.1% ván kết thúc 1-0, 44.7% 0-1
- Sức mạnh: 1837 Elo đối với Stockfish giới hạn sức mạnh; thắng mọi mô hình công khai tương tự (không preference tuning, rewards hoặc search), từ 23M đến 2.8B tham số, bao gồm một mô hình có 13 lần nhiều tham số
- Huấn luyện: Gemma-4-31B mô tả phong cách 3M ván bên; Gemma-3-1B蒸馏 từ 2.4M mô tả sạch gán nhãn 30.1M ván bên × 5 mô tả; SFT 27.1M sides × 5 mô tả; DPO 0.56M ván (2% corpus), 20 phút trên 1 GPU, 4.366 bước batch 128
- Style adherence sau DPO (2,000 ván/prompt): queens traded early 53%→66.5%, pawn moves .290→.319, queenside castling 97.3%→99.7%
- Sức mạnh không prompt: SFT 1792 Elo, DPO 20-min 1797 Elo, DPO full pass 1812 Elo (trong khoảng sai số)
- Alignment tax: SFT mất ~45 Elo không prompt (1792 vs 1837 pretrain)
- DPO recipe chính: label pairs, β=0.5, NLL 1.0, KL 1.0, body LR 2×10⁻⁷, conditioning LR 10⁻⁴, pinned no-text term
- Attack gap (Elo dưới prompt tấn công − Elo không prompt): DPO 20-min −150, DPO full pass −155, SFT −40
- Chi phí mỗi ván: SFT ~36 layer applications/vị trí (K=5), DPO ~18 (K=2); SFT 2.400 ván/giây, DPO 3.750 ván/giây
- Vòng lặp tìm kiếm tự động: ~70 chạy DPO ngắn (10-20 phút/GPU), screened với 100 ván/prompt, từ vòng 6 dùng 300 ván không prompt, 300 ván attack prompt, 150 ván mỗi prompt khác; 20 chạy hứa hận nhất đánh giá lại 1.000 ván/prompt

## INSIGHT — Cơ chế & tại sao
[DPO cải thiện style adherence mà không làm suy yếu sức mạnh không prompt] VÌ [DPO dùng cùng những nước đi dưới mô tả khớp và không khớp, nên chỉ văn bản giải thích sự khác biệt, không cần sampling hay reward model]. Điều này nghĩa là [có thể điều khiển hành vi mô hình qua văn bản tự nhiên mà khôngtrade-off quá lớn về sức mạnh cơ bản].
[Vòng lặp tìm kiếm tự động có ngân sách cố định tìm ra cấu hình DPO tốt hơn hand-tuning] VÌ [mỗi cấu hình được chạy cố định thời gian, chấm điểm trên tập validation cố định, vòng kế hoạch từ kết quả trước]. Điều này nghĩa is [tự động hóa thiết kế 실험 giảm sai sót con người và tìm ra cấu hình tốt hơn nhanh hơn].
[Style-move DPO giảm tổn thất sức mạnh dưới prompt tấn công] VÌ [chỉ dùng DPO trên 10–50% nước đi nơi log-likelihood của reference phụ thuộc nhiều nhất vào nhãn, KL/NLL anchor phần còn lại]. Điều này nghĩa is [cân nhã style adherence với sức mạnh bằng cách tập trung préférence vào những nước đi quan trọng].
[Full pass DPO không cải thiện hơn chạy 20 phút] VÌ [style adherence饱和 trong phần đầu corpus, validation pair accuracy vẫn tăng nhưng không chuyển thành chơi tốt hơn]. Điều này nghĩa is [dùng nhiều dữ liệu DPO hơn không phải luôn tốt hơn; dừng sớm có thể hiệu quả hơn].

## IDEA — Áp dụng được gì
1. Áp dụng [DPO với label-swap pairs] vào [điều khiển hành vi LLM agent qua natural language]: bước đầu là chuẩn bị cặp dữ liệu (cùng output, mô tả khớp vs không khớp), chạy DPO để agent tuân theo hướng dẫn style mà không cần reward model.
2. Áp dụng [vòng lặp tìm kiếm tự động có ngân sách cố định] vào [tối ưu hóa prompt hoặc cấu hình agent]: bước đầu là thiết lập hàng đợi các cấu hình, mỗi chạy cố định thời gian, chấm điểm trên tập validation, tự động lên kế hoạch vòng tiếp theo từ kết quả.
3. Áp dụng [distill teacher lớn sang student nhỏ để gán nhãn dữ liệu] vào [xây dựng tập dữ liệu huấn luyện cho agent]: bước đầu là dùng mô hình lớn (Gemma-4-31B) để gán nhãn một tập nhỏ, sau đó蒸馏 vào mô hình nhỏ (Gemma-3-1B) để gán nhãn toàn bộ corpus lớn.

## WISDOM — Nguyên tắc tổng quát
1. Nguyên tắc: Điều khiển hành vi mô hình qua văn bản tự nhiên có thể đạt được bằng DPO mà không cần reward model, miễn là dùng cặp dữ liệu (cùng output, điều kiện khác nhau). Áp dụng khi: cần điều khiển style/behavior của agent qua text instructions. Không áp dụng khi: tác vụ không có sự phân biệt rõ ràng giữa output tốt và xấu.
2. Nguyên tắc: Thiết kế thử nghiệm tự động với ngân sách cố định thường vượt quá tinh chỉnh thủ công. Áp dụng khi: tối ưu hóa hyperparameter hoặc cấu trúc agent. Không áp dụng khi: không có tập validation hoặc metric rõ ràng để đánh giá.

## Assumptions & Limitations
- Điều kiện phải đúng: có corpus ván cờ lớn có chất lượng, có mô hình lớn để tạo mô tả phong cách, có tài nguyên GPU để pretrain và fine-tune.
- Limitation paper thừa nhận: alignment tax (SFT mất ~45 Elo không prompt); không có điều kiện chơi yếu/mạnh (mỗi mô hình được mô tả rated ≥ 2200); player prompts hiệu ứng nhỏ (khoảng 1 điểm move match); adherence đo trên một vài prompt với metric viết tay, không phải validated judgment of style; không dùng search nên sức mạnh kém hơn hệ thống có search.
- Limitation paper KHÔNG nói: không đánh giá trên tác vụ không phải cờ vua; không có so sánh với các phương pháp điều khiển hành vi LLM khác (ví dụ: prompting đơn thuần, classifier-free guidance); không có chi phí_real inference so với các mô hình lớn hơn.

## Metadata
- Năm: 2026
- Tác giả: Ilia Badanin
- Category arXiv: cs.LG
- Link PDF: https://arxiv.org/pdf/2610.25356
- arXiv ID: 2610.25356v1
- Nhãn: [applied]
- Citation count: [không tìm được]