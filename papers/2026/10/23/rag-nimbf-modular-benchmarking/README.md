# 2610.27816 RAG-NIMBF: Khung benchmark phi xâm lấn, mô-đun cho phân tích cấu hình RAG tự động

## Problem
Các thực hành viên RAG (Retrieval-Augmented Generation — sinh tăng cường bằng truy xuất) phải đối mặt với không gian cấu hình rất rộng (chia đoạn, nhúng, truy xuất, xếp lại, thiết kế nhắc, mô hình sinh) nhưng thiếu hướng dẫn về cách các thành phần tương tác. Các khung đánh giá hiện có chủ yếu chấm điểm một chuỗi pipeline đã cho thay vì xem cấu hình bản thân là đối tượng nghiên cứu.

## Contribution
- RAG-NIMBF: khung benchmark phi xâm lấn, mô-đun, gắn vào các pipeline RAG hiện có như một lớp đánh giá không xâm lấn (không sửa đổi nội bộ mô hình hay bộ truy xuất). Đánh giá không gian cấu hình thông qua kiểm soát thuần khiết (ablation) với theo dõi thí nghiệm cuốiสุด (end-to-end experiment tracking).
- Đánh giá lai (hybrid evaluation): kết hợp điểm chất lượng câu trả lời dựa trên LLM (RAGAS), đo độ chính xác truy xuất, và chỉ số thời gian chạy.
- Xác thực trên nhiều mô hình sinh trên tập dữ liệu SQuAD (100 câu hỏi). Khám phá các tương tác không rõ ràng: MMR tăng nDCG@5 lên +4 đến +11 điểm phần trăm so với tìm kiếm tương tự truyền thống; hướng dẫn nhắc chi tiết tăng độ trung thành (faithfulness) +10 đến +13 điểm trên các mô hình giỏi và mô hình suy lý (Qwen3.5-think, GPT-4o-mini, Qwen3.6-27B), nhưng không đáng kể trên máy tạo 20B.
- Mô hình cục bộ Qwen3.6-27B khớp GPT-4o-mini ở độ trung thành trung bình 0.89; mô hình tham chiếu ranh giới (frontier) không chiếm ưu thế trên các mô hình liên quan đến RAG.

## Method
Khung có sáu giai đoạn độc lập: cấu hình, nạp dữ liệu, chia đoạn, truy xuất, sinh, đánh giá. Một quy định khai báo (declarative specification) xác định phạm vi tham số cho mọi thành phần; khung tạo tích phân Cartes và đánh giá mọi tổ hợp. Các thành phần trung gian (đoạn, chỉ mục vector, ngữ cảnh truy xuất) được lưu trữ để tái sử dụng. Tất cả tham số và chỉ số được ghi vào MLflow.

Ba nguyên lý cốt lõi:
1. Tích hợp phi xâm lấn (non-invasive integration): đóng gói các thành phần RAG hiện có mà không sửa đổi nội bộ; kết nối với Ollama và các điểm cuối tương thích OpenAI (vLLM, TGI) qua định tuyến nhà cung cấp (provider routing), chỉ cần chuỗi nhận diện mô hình và dữ liệu truy cập.
2. Khám phá cấu hình có hệ thống: tích phân Cartes thay vì tìm kiếm dựa trên thiết kế thay thế (surrogate-based search), để các hiệu ứng tương tác giữa các giai đoạn pipeline còn có thể quan sát được.
3. Đánh giá lai: mỗi lần chạy được đánh giá bằng sự kết hợp các chỉ số chất lượng câu trả lời, truy xuất, sinh, và thời gian chạy.

Không gian cấu hình quét: 6 mô hình sinh × 2 chiến lược chia đoạn × 2 kích thước đoạn × 2 mức chồng lấp × 2 phương pháp truy xuất × 2 mẫu nhắc = 192 cấu hình (nhưng nghiên cứu thực nghiệm sử dụng một tập hợp nhỏ hơn có chủ ý).

Các mô hình sinh: Qwen3-32B-AWQ (32B, cục bộ), GPT-OSS-20B (20B, DGK Spark), Qwen3.5-35B-A3B (35B MoE, cluster GPU), Qwen3.6-27B-NVFP4 (27B dense, trạm làm việc), GPT-4o-mini (API), DeepSeek-V4-Pro (862B, API). Critic: Qwen3.5-397B-A17B (397B MoE, 17B active, non-thinking, dùng cho RAGAS).

Các chỉ số đánh giá:
- Lớp RAGAS: Faithfulness (tỷ lệ khẳng định trong câu trả lời được bế rõ bởi ngữ cảnh truy xuất).
- Lớp truy xuất (IR): Context recall, Semantic sim., Hit@k, Recall@k, nDCG@k.
- Lớp NLG: BERTScore-F1, METEOR, ROUGE-L, BLEU.
- Lớp thời gian chạy: TTFT (time-to-first-token), TPS (tokens-per-second).

## KNOWLEDGE — Số liệu & khái niệm
- MMR tăng nDCG@5 từ +4 đến +11 điểm phần trăm (lớn nhất GPT-4o-mini +11pp: 0.68→0.79, Qwen3.5-think +10pp: 0.70→0.80, nhỏ nhất GPT-OSS-20B +4pp).
- Nhắc chi tiết (Detailed template) tăng faithfulness +10 đến +13pp trên các mô hình đám mây/lớn và mô hình suy lý (Qwen3.5-think +13pp, GPT-4o-mini +11pp, Qwen3.6-27B +10pp); Qwen3-32B +7pp; GPT-OSS-20B +1pp.
- Điểm faithfulness trung bình: GPT-4o-mini 0.89, Qwen3.6-27B 0.89, Qwen3.5-think 0.88, Qwen3-32B 0.83, GPT-OSS-20B 0.77. Cấu hình đơn lẻ tốt nhất đạt 0.96 (GPT-4o-mini).
- Chất lượng truy xuất toàn cầu: nDCG@5 = 0.75, Hit@5 = 0.86, Recall@5 = 0.69.
- Qwen3.6-27B-NVFP4 dẫn lưu lượng tuần tự cục bộ (127.5 TPS).
- 192 cấu hình trong không gian quét đầy đủ.

## INSIGHT — Cơ chế & tại sao
[MMR cân bằng mức độ liên quan và sự đa dạng] xảy ra VÌ MMR giảm sự dư thừa trong tập được truy xuất, cho thấy bằng chứng rộng hơn. Điều này nghĩa là [các máy tạo nhỏ hơn hưởng lợi từ sự kết hợp bằng chứng rộng hơn MMR cung cấp, trong khi các máy tạo mạnh hơn đã căn cứ tốt trên đoạn tương tự nhất và bị phân loãng bởi ngữ cảnh bổ sung].
[Nhắc chi tiết tăng faithfulness] xảy ra VÌ hướng dẫn nhắc cụ thể yêu cầu câu trả lời đầy đủ với lý luận chứng minh, giúp câu trả lời gắn bó chặt chẽ hơn với bằng chứng đã truy xuất. Điều này nghĩa là [lợi thế faithfulness bị trade-off với METEOR (giảm 10-22pp với nhắc chi tiết) vì câu trả lời dựa trên bằng chứng khác về hình thức bề mặt so với tham chiếu ngắn của SQuAD, dù vẫn về mặt ngữ nghĩa].

## IDEA — Áp dụng được gì
1. Áp dụng RAG-NIMBF vào hệ thống RAG sản xuất hiện có: bước đầu là gắn khung làm lớp đánh giá không xâm lấn, định nghĩa phạm vi tham số cho các thành phần (kích thước đoạn, chiến lược truy xuất, mẫu nhắc, mô hình sinh), chạy tích phân Cartes và theo dõi kết quả trong MLflow.
2. Áp dụng nguyên tắc đánh giá lai (đa chỉ số): bước đầu là theo dõi cùng lúc faithfulness, nDCG@5, và thời gian chạy để tránh tối ưu hóa một chỉ số đơn lẻ gây sai lệch (ví dụ tối ưu METEOR alone sẽ sai lệch favorece câu trả lời chưa đủ chi tiết).

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Trong cấu hình RAG, không có chỉ số đơn lẻ nào đủ; chất lượng câu trả lời, độ chính xác truy xuất, và thời gian chạy có thể di chuyển theo các hướng khác nhau, nên đánh giá phải dùng nhiều chỉ số cùng lúc. Khi nào dùng: khi cần đánh giá hệ thống cấu hình RAG một cách có hệ thống trên phần cứng tiêu dùng. Khi nào KHÔNG: khi chỉ cần chấm điểm một pipeline đã cho mà không muốn quét không gian cấu hình.

## Assumptions & Limitations
- Chỉ đánh giá trên tập SQuAD (câu hỏi trích xuất ngắn, chủ yếu một đoạn) — kết quả có thể không chuyển giao sang tài liệu dài, đa bước, tiếng ồn, hoặc tập doanh nghiệp.
- Các đánh giá chất lượng đều tự động, do đó tương đối với critic RAGAS.
- Các mẫu nhắc được viết một lần và áp dụng đồng nhất.
- Reranking, HyDE, và so sánh mô hình nhúng bị bỏ qua; top-k và tham số λ của MMR được giữ cố định.

## Metadata
- Năm 2026; tác giả: Niclas Hart, Nicolas Weeger (Ansbach University of Applied Sciences); category: cs.SE; PDF: https://arxiv.org/pdf/2610.27816v1; code: https://github.com/aiengineeringblueprints/RAG-NIMBF; citation count: [NO DATA — paper 2026-10-20]