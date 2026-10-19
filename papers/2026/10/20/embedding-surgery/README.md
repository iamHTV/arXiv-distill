# [2609.05110v1] Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval

## Giá trị cốt lõi (1 câu)
Embedding surgery là phương pháp nhẹ nhàng để sửa lỗi xếp hạng thích ứng trong truy xuất dense: áp dụng cập nhật cục bộ, tối thiểu vào embedding của các tài liệu đã truy xuất tại thời điểm truy vấn, hướng dẫn bởi phản hồi biên soạn, tương tác người dùng hoặc nhãn giả từ LLM, diễn giải qua bài toán tối ưu hóa凸 (bài toán tối ưu hàm bậc hai) ép buộc ràng buộc xếp hạng trong khi tối thiểu hoá sự thay đổi của biểu diễn tài liệu.

## Problem
Prior work chưa giải quyết vấn đề hệ thống truy xuất dense (dùng làm thành phần cốt lõi của máy tìm kiếm, nền tảng đềovas, ống dẫn RAG) bị cứng nhắc vì embedding tài liệu được tính toán ngoại tuyến và lưu trong chỉ mục tĩnh — khó thích ứng với phản hồi người dùng hoặc ý định tìm kiếm thay đổi; các phương pháp trước (fine-tuning encoder + lập chỉ mục lại) tốn kém và không kịp để sửa lỗi xếp hạng cụ thể theo từng truy vấn.

## Contribution
- Giới thiệu embedding surgery, sáng kiến sửa lỗi xếp hạng thích ứng qua cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn.
- Diễn giải embedding surgery như bài toán tối ưu hóa凸 (bài toán tối ưu hàm bậc hai): ép buộc ràng buộc xếp hạng (từ tín hiệu phản hồi) trong khi tối thiểu hoá sự thay đổi của biểu diễn tài liệu ảnh hưởng; đối với một ràng buộc pairwise đơn lẻ, giải pháp tối ưu có dạng chius (closed-form); đối với lô ràng buộc, bài toán tối ưu hàm bậc hai tương ứng được giải quyết hiệu quả bằng các công cụ tối ưu hóa chuẩn.
- Khung thống nhất hợp nhất embedding surgery với phản hồi biên soạn, dựa trên nhấp chuột và suy ra từ LLM trong ống dẫn truy xuất dense.
- Đánh giá rộng trên 4 mô hình truy xuất dense (Contriever, TAS-B, E5 đa ngôn ngữ, Snowflake-Arctic Embed) và 7 benchmark IR (TREC DL 2019/2020, DL-Hard, TREC Robust '04, TREC CAsT 2019, MS MARCO, QSharedRel).
- Phân tích quy mô lớn trên 56k truy vấn trên cấu trúc chỉ mục ANN (IVF, HNSW), chứng tỏ cập nhật vẫn cục bộ, bảo toàn hiệu quả truy xuất và có thể áp dụng an toàn, hiệu quả qua việc ghi đè chép lại tại chỗ (in-place overwriting), không cần lập chỉ mục lại tốn kém.

## Method
Truy xuất dense là khuôn quy IR dựa trên vector, trong đó truy vấn và tài liệu được mã hóa độc lập vào không gian hidden dùng chung qua kiến trúc bi-encoder; encoders được huấn luyện cùng nhau với học cách đối lập (contrastive learning), độ tương đồng giữa các embedding thường tính bằng tích vô hướng hay cosine similarity. Để mở rộng, embedding tài liệu được tính toán trước ngoại tuyến và lập chỉ mục dùng hệ thống tìm xấp x cận nhất láng giềng (ANN) như FAISS, Falcon, ScaNN, HNSW, MRNG. Điểm liên kết điểm số liên quan tính như ⟨q, di⟩. K- tài liệu có điểm số cao nhất, ký hiệu π = [d1, d2, ..., dk], được trả về làm tập kết quả. Mục tiêu của embedding surgery là áp dụng các sửa đổi nhỏ, cục bộ vào các embedding tài liệu để xếp hạng kết quả tốt hơn phản ánh tín hiệu phản hồi, đồng thời bảo toàn cấu trúc tổng thể của không gian nhúng. Với một truy vấn q có embedding q và một danh sách xếp hạng đã truy xuất π = [d1, ..., dk], mỗi tài liệu di đại diện bởi embedding di, giả định có quyền truy cập tín hiệu phản hồi R quy định các sửa đổi mong muốn cho xếp hạng. Mỗi phần tử của R là một ưu tiên cặp (dr, dn), cả dr và dn thuộc tập đã truy xuất π, chỉ ra rằng dr nên được xếp hạng trên dn cho truy vấn q. Embedding surgery tìm các cập nhật Δdi vào các embedding của các tài liệu đã truy xuất để ép buộc các ràng buộc này trong khi tối thiểu hoá sự phân rạc tổng thể của không gian nhúng. Bài toán tối ưu hóa được hình thức hóa như sau: tối thiểu hoá tổng ∥Δdi∥2^2 qua i=1..k, dự phó với ràng buộc ⟨q, dr + Δdr⟩ ≥ ⟨q, dn + Δdn⟩ + ε, ∀(dr, dn) ∈ R. Ở đây: Δdi là hiệu chỉnh áp dụng vào embedding gốc di; ∥·∥2 là chuẩn L2, phạt các độ lệch lớn từ các vector gốc; ε > 0 xác định biên cách biệt giữa điểm số liên quan cho truy vấn q của tài liệu dr và dn. Hàm mục tiêu khuyến khích di chuyển tối thiểu trong không gian nhúng, đảm bảo các vector đã điều chỉnh vẫn gần các vị trí gốc. Đồng thời, các ràng buộc bảo đảm xếp hạng kết quả nhất quán với phản hồi. Bởi bài toán tối ưu hóa là凸 và hàm bậc hai, nó thừa nhận cực tiểu lớn duy nhất toàn cục và có thể giải quyết hiệu quả bằng các bộ giải chuẩn như CVXPY. Các embedding đã sửa đổi sau đó được tính là d'i = di + Δdi. Nhiều biến thể, tùy vào embeddings nào của mỗi cặp được phép thay đổi: đối xứng (mặc định, cả hai đều điều chỉnh — hiệu chỉnh cân bằng, tối thiểu hoá tổng di chuyển đồng thời thỏa mãn ràng buộc phản hồi); hạ thấp (embedding của tài liệu liên quan hơn cố định Δdr = 0, chỉ đổi embedding ít liên quan hơn — hạ thấp tài liệu ít liên quan hơn trong xếp hạng, để embedding tài liệu liên quan không đổi); nâng cao (embedding của tài liệu ít liên quan hơn cố định Δdn = 0, chỉ đổi embedding liên quan hơn — nâng cao tài liệu liên quan hơn lên trên trong xếp hạng). Nguồn phản hồi: (i) phán xét biên soạn từ chuyên gia đánh giá (chất lượng cao, dùng làm oracle); (ii) tín hiệu tương tác người dùng (nhấp chuột, thời gian tồn tại), mô phỏng qua mô hình phản 사실을 (counterfactual click models) khi thiếu nhật ký truy vấn thật; (iii) giám sát phụ từ LLM (xấp xỉ phán đoán liên quan, giúp nhận lỗi xếp hạng). Các mô hình tương tác người dùng: Perfect (P — nhấp định danh vào tài liệu liên quan, xác suất nhấp tăng tuyến tính theo mức độ liên quan 0→1), Noisy (N — chủ yếu nhấp vào tài liệu liên quan nhưng có thể nhấp vào tài liệu không liên quan với xác suất 0.2), Near-Random (R — sở thích yếu cho nội dung liên quan, nhấp vào tài liệu không liên quan với xác suất 0.4 và tài liệu liên quan cao nhất với 0.6). Xác suất nhấp cuối cùng pc(q, d, i) = p̂r(q, d) · p̂e(i), với k′ = 20 và p̂e(i) = 1 với mọi vị trí (loại bỏ sai số vị trí), nên pc phụ thuộc chỉ thành phần dựa trên liên quan p̂r. Nhấp vào tài liệu dr tại cấp i > 1 được diễn giải như ưuentiq so với tài liệu dn tại cấp i−1. Cặp (dr, dn) kết quả được thêm vào R, kích hoạt cập nhật embedding surgery.

## KNOWLEDGE — Số liệu & khái niệm
- Dense retrieval: truy xuất dựa trên vector, truy vấn và tài liệu mã hóa vào không gian hidden dùng chung qua bi-encoder.
- ANN (Approximate Nearest Neighbor): tìm xấp x cận nearest neighbor — hệ thống chỉ mục như FAISS, Falcon, ScaNN, HNSW, MRNG.
- Embedding surgery: cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn để sửa lỗi xếp hạng.
- Bài toán tối ưu hóa凸 (convex optimization, bài toán tối ưu hàm bậc hai): ép buộc ràng buộc xếp hạng, tối thiểu hoá sự thay đổi embedding.
- Kendall Tau distance (KD): đếm số cặp bất đồng giữa hai hoán vị, đo số ràng buộc thứ tự cặp cần giải quyết để sắp xếp xếp hạng mô hình với mục tiêu.
- Swap Accuracy: tỷ lệ phần trăm cặp tài liệu được xếp thứ tự chính xác sau khi phẫu thuật.
- nDCG@k (Normalized Discounted Cumulative Gain): đo chất lượng top-k tài liệu đã truy xuất, tính cả mức độ liên quan theo cấp bậc và vị trí xếp hạng.
- RR/MRR (Reciprocal Rank / Mean Reciprocal Rank): dùng cho tập dữ liệu có một mục liên quan duy nhất mỗi truy vấn (MS MARCO Dev, QSharedRel).
- 4 mô hình: Contriever, TAS-B, E5 (multilingual), Snowflake-Arctic Embed (tất cả dùng ở chế độ zero-shot, không tinh chỉnh thêm theo tác vụ).
- 7 benchmark: TREC DL 2019 (43 truy vấn), DL 2020 (54 truy vấn), DL-Hard (tập tough subset của DL '19 và DL '20), TREC Robust '04 (249 truy vấn, zero-shot out-of-domain vì các mô hình tinh chỉnh trên MS MARCO), TREC CAsT 2019 (20 phiên trò chuyện tìm kiếm đối thoại, khoảng 10 lượt mỗi phiên), QSharedRel (346 truy vấn từ MS MARCO Dev, các cặp truy vấn ít nhất chia một đoạn liên quan; 169 truy vấn tiêu điểm áp dụng embedding surgery, sau đó đánh giá hiệu ứng lên các truy vấn liên quan tương ứng), MS MARCO Dev (khoảng 56k truy vấn được phán xét, dùng để phân tích cập nhật embedding quy mô lớn và tác động lên không gian latent và chỉ mục ANN).
- 3 nguồn phản hồi: biên soạn (phán xét chuyên gia, chất lượng cao), tương tác người dùng (mô phỏng qua mô hình phản사실: Perfect, Noisy, Near-Random), LLM-derived (BGE, Qwen rerankers làm nhãn giả).
- Kết quả chính: cải thiện nhất quán, lên đến +60.64% cải thiện tương đối nDCG@10 (TAS-B trên DL-Hard dưới phản hồi biên soạn).
- Phương pháp đối xứng (symmetric) hiệu quả nhất trên hầu hết tập dữ liệu, trừ Robust '04 (khoảng bằng với demotion).
- Contriever, phản hồi biên soạn: nDCG@10 từ 0.674→0.845 (DL '19), 0.672→0.878 (DL '20), 0.377→0.591 (DL-Hard), 0.466→0.687 (Robust '04).
- Click-based, người dùng hoàn hảo (P) sau 1.000 lần nhấp: 0.702, 0.700, 0.454, 0.486 cho DL '19, DL '20, DL-Hard, Robust '04.
- Mạnh mẽ dưới phản hồi nhôound (noisy); Near-random (R) cho lợi ích hạn chế nhưng không làm kém hiệu quả truy xuất gốc (trừ Goes giảm nhỏ, không có ý nghĩa thống kê, trên Robust '04).
- LLM-based: BGE tạo reranking, lợi ích ổn định, nhỏ nhất +3.59% (Snowflake, DL '19), lớn nhất +24.56% (E5, Robust '04).
- Hiệu chỉnh xếp hạng lan truyền đến các truy vấn ngữ nghĩa liên quan (QSharedRel).
- Bổ sung phương pháp thích ứng truy vấn như CoRocchio, sinh thêm điểm gain trong khi mạnh mẽ hơn trước phản hồi nhôound.
- Phân tích quy mô lớn: 56k truy vấn trên cấu trúc chỉ mục ANN (IVF, HNSW), cập nhật vẫn cục bộ, bảo toàn hiệu quả truy xuất, áp dụng an toàn và hiệu quả qua ghi đè chép lại tại chỗ (in-place overwriting), không cần lập chỉ mục lại tốn kém.
- Chi phí tính toán thấp; bài toán tối ưu hóa giải quyết bằng thư viện cvxpy trên một lõi CPU đơn (AMD Rome 7742, 2.25 GHz).
- Mã nguồn: https://github.com/maddalena-amendola/Embedding-Surgery
- Danh mục arXiv: cs.IR
- Chấp nhận tại ACM CIKM 2026

## INSIGHT — Cơ chế & tại sao
[Trực xuất dense bị cứng nhắc sau khi huấn luyện] VÌ [embedding tài liệu được tính toán trước ngoại tuyến và lưu trong chỉ mục tĩnh, khó tích hợp phản hồi người dùng hoặc thích ứng với ý định tìm kiếm thay đổi]. Điều này nghĩa là [cần phương pháp cập nhật nhẹ nhàng tại thời điểm truy vấn mà không retraining hay re-indexing].
[Phẫu thuật embedding sửa lỗi xếp hạng hiệu quả] VÌ [diễn giải như bài toán tối ưu hóa凸 (bài toán tối ưu hàm bậc hai) ép buộc ràng buộc xếp hạng trong khi tối thiểu hoá sự thay đổi của biểu diễn tài liệu ảnh hưởng]. Điều này nghĩa là [cập nhật cục bộ và tối thiểu giữ cấu trúc tổng thể của không gian nhúng].
[Phương pháp đối xứng hiệu quả nhất] VÌ [cả hai embedding đều được điều chỉnh, tạo hiệu chỉnh cân bằng tối thiểu tổng di chuyển đồng thời thỏa mãn ràng buộc phản hồi]. Điều này nghĩa là [cả hai hướng (thúc mạnh câu liên quan hơn và hạ thấp câu ít liên quan hơn) cùng côngiare tốt hơn chỉ thay đổi một phía].

## IDEA — Áp dụng được gì
Áp dụng embedding surgery vào hệ thống tìm kiếm dense doanh nghiệp: bước đầu là xác định các lỗi xếp hạng qua phản hồi biên soạn hoặc tương tác người dùng, rồi áp dụng cập nhật cục bộ vào embedding của tài liệu đã truy xuất tại thời điểm truy vấn.
Kết hợp embedding surgery với CoRocchio (thích ứng truy vấn): bước đầu là áp dụng cả hai — surgery chỉnh sửa embedding tài liệu, CoRocchio chỉnh sửa embedding truy vấn — để đạt thêm điểm gain.

## WISDOM — Nguyên tắc tổng quát
Nguyên tắc: Sửa lỗi xếp hạng dense retrieval bằng cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn (không retraining/re-indexing); hiệu chỉnh có thể lan truyền đến truy vấn ngữ nghĩa liên quan và bổ sung các phương pháp thích ứng truy vấn như CoRocchio.

## Assumptions & Limitations
- Điều kiện đúng: hệ thống truy xuất dense, có quyền truy cập tín hiệu phản hồi (biên soạn/tương tác người dùng/LLM), truy vấn cụ thể cần sửa lỗi xếp hạng.
- Limitation paper thừa nhận: sử dụng LLM làm đánh giá cần được tiếp cận với sự thận trọng (nhãn do LLM tạo ra có điểm yếu hệ thống, hạn chế khả năng thay thế hoàn toàn đánh giá liên quan của con người); phản hồi gần ngẫu nhiên (Near-Random) cho lợi ích hạn chế và có thể làm kém hiệu quả truy xuất gốc trên một số tập (Robust '04, giảm nhỏ không có ý nghĩa thống kê).
- Limitation paper KHÔNG nói: chi phí vận hành giải quyết bài toán tối ưu hóa cho mỗi truy vấn tại quy mô lớn hàng ngày; tính ổn định của cập nhật embedding qua nhiều lần áp dụng liên tiếp; tác động lên độ trễ truy vấn khi chạy chirurg embedding tại thời điểm truy vấn.

## Metadata
- Năm: 2026
- Tác giả: Maddalena Amendola (IIT-CNR, Pisa, Ý), Antonio Mallia (Seltz, San Francisco, Mỹ), Raffaele Perego (ISTI-CNR, Pisa, Ý)
- Category arXiv: cs.IR
- Link PDF: https://arxiv.org/pdf/2609.05110v1
- arXiv ID: 2609.05110v1
- Nhãn: [applied]
- Skill: embedding-surgery | Test: [SKILL VALID]
