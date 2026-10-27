# 2610.32415v1 Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge

## Giá trị cốt lõi (1 câu)
ANT-OR, một khung đa agent (multi-agent framework) cho việc gán nhãn dữ liệu tự động, cải thiện độ chính xác agreement@≥2 4.5 điểm so với baseline mạnh nhất và đạt sự phù hợp cao nhất với phân phối nhãn của các annotator người (do Fleiss' κ đo lường) trong phạm vi 2 điểm — nhờ distillation quy tắc quyết định tương phản (contrastive decision rules) từ phản hồi tích cực và tiêu cực.

## Problem
Prior work (các nghiên cứu trước) về gán nhãn bằng LLM đã phát triển nhanh, nhưng các tiêu chí đánh giá hiện tại vẫn không phù hợp với thực hành thực tế. Việc gán nhãn thực tế thường liên quan đến hướng dẫn tác vụ dài, chi tiết, và các annotator khác nhau có thể tạo ra những phán đoán khác nhau nhưng đều hợp lý, đặc biệt là trên các trường hợp ranh giới (boundary cases), nơi các dataset có một nhãn đơn (single-labeled) không phản ánh sự bất đồng (disagreement). Khoảng cách này cũng hạn chế các hệ thống gán nhãn đơn agent và dựa trên quy trình (workflow-based) hiện có, thường thiếu khả năng thích ứng với các hướng dẫn phức tạp, phát triển liên tục. Các tiêu chí đánh giá LLM annotation hiện có thường thiếu các tài liệu hướng dẫn được dùng trong các tác vụ thực tế và chỉ cung cấp một nhãn tiêu chuẩn đơn (single gold-standard label) cho mỗi mẫu. Nhiều tác vụ gán nhãn thực tế được điều khiển bởi các tài liệu hướng dẫn chi tiết, có thể vốn mập mờ hoặc mở cho sự diễn giải. Do đó, sự bất đồng giữa các annotator có thể phản ánh các giải thích thay thế hợp lý chứ không phải là lỗi gán nhãn. Các tiêu chí đánh giá có một nhãn đơn (single-label benchmarks) do đó sụt kết quả (collapse) sự bất xác (uncertainty) này và không thể xác định xem các annotator LLM có đạt được sự nhất quán tương đương con người hay không.

## Contribution
1. Xác định hai chök ngắt (bottleneck) quan trọng đối với gán nhãn tự động đáng tin cậy: các tiêu chí đánh giá không đầy đủ không thể phản ánh sự bất đồng giữa các annotator (inter-annotator disagreement) và sự phức tạp từ các hướng dẫn gán nhãn chi tiết, cùng với hạn chế của các agent gán nhãn hiện tại, đặc biệt là những thiết kế đơn agent hoặc đa agent tĩnh (static multi-agent designs).
2. Xây dựng và phát hành ANT-A (Aggregated N-annotator Task Annotations), một tiêu chí đánh giá đa annotator (multi-annotator benchmark) gồm 7 dataset với hướng dẫn chi tiết và 5 nhận xét độc lập của con người mỗi mẫu, cho phép đánh giá nhận thức về phân phối (distribution-aware evaluation), sử dụng Fleiss' κ (hệ số Fleiss) để đánh giá mức độ sự gán nhãn của model phù hợp với phân phối gán nhãn của con người.
3. Đề xuất ANT-OR (automated ANnotation framework Through multi-agent Optimization with agent-level contRastive knowledge), một khung đa agent thích ứng có thể biến thành công (collective prediction successes) và thất bại (failures) thành kiến thức quyết định có cấu trúc (structured decision knowledge) có thể tái sử dụng, cho phép cộng tác mạnh mẽ hơn trên các tác vụ gán nhãn phức tạp với ranh giới quyết định tinh tế (nuanced decision boundaries).
4. Thí nghiệm rộng trên tiêu chí đánh giá đề xuất cho thấy ANT-OR cải thiện đáng kể hiệu suất gán nhãn trên các tác vụ đa dạng, vượt qua baseline mạnh nhất 4.5 điểm về độ chính xác và đạt mức độ phù hợp cao nhất với phân phối gán nhãn của các annotator con người theo Fleiss' κ trong khoảng 2 điểm trung bình.
5. ANT-A bao gồm 7 dataset crosses các domain (y tế, thương mại điện tử, tổng quát) và modality (văn bản, vision-language), 1.500 mẫu mỗi dataset, 5 annotator độc lập mỗi mẫu.

## Method
Pipeline (dòng xử lý) của ANT-OR có các bước chính:
1. Chuẩn bị dataset (Dataset Preparation): thu thập các mẫu truy vấn liên quan đến domain từ các nguồn dữ liệu internet công khai cho mỗi dataset, ẩn danh thông tin có thể nhận dạng, lọc bỏ các bản sao chính xác và instance chất lượng thấp để có 1.500 mẫu với sự kết hợp giữa các trường hợp rõ ràng (clear-cut) và trường hợp ranh giới (boundary cases).
2. Thiết kế tài liệu hướng dẫn (Guideline Document Design): lấy các hướng dẫn gán nhãn từ yêu cầu thực tế và tinh chỉnh bằng cách làm rõ các định nghĩa mập mờ, thêm các quy tắc quyết định cho các trường hợp ranh giới, và điều chỉnh cho phù hợp với phân phối dữ liệu. Các tài liệu kết quả quy định các ranh giới quyết định chi tiết và các quy tắc xử lý trường hợp cực đoan.
3. Quá trình gán nhãn của con người (Human Annotation Process): tất cả các gán nhãn được thực hiện bởi các annotator chuyên nghiệp từ một nhà cung cấp gán nhãn nội bộ, sử dụng một nhóm 10 annotator, và mỗi mẫu được gán nhãn độc lập bởi 5 người. Giao thức ba giai đoạn (three-phase protocol) với tổng chi phí gán nhãn USD $4078: Phase 1 (pre-annotation — gán nhãn một tập con nhỏ khoảng 50 mẫu bởi tất cả 10 annotator), Phase 2 (rule clarification — làm rõ quy tắc dựa trên câu hỏi và điểm confusing của annotator), Phase 3 (batch annotation — mỗi mẫu được gán nhãn bởi 5 annotator được chọn từ nhóm 10).
4. Khung ANT-OR (ANT-OR Framework):
   - Contrastive Knowledge Mining (khai phá kiến thức tương phản): mỗi agent được trang bị một cơ sở kiến thức có cấu trúc gồm các mẫu đã xác thực và các kích thước phân biệt (discriminative dimensions), cho phép agent tích luỹ liên tục cả các ví dụ gán nhãn cụ thể và kiến thức quyết định qua các vòng tối ưu hóa. Xây dựng contrastive sample pool (Hồ mẫu tương phản) với mẫu dương (s+) và mẫu âm (s−). Khi agent đưa ra dự đoán sai ˆy− trên truy vấn q, xây dựng mẫu lỗi s−, sau đó lấy hai mẫu đúng tương tự về mặt ngữ nghĩa s+1, s+2 để tạo thành contrastive tuple và một LLM được nhắc để tóm tắt kích thước phân biệt (discriminative dimension) d từ các trường hợp gây nhầm lẫn. Mỗi kích thước phân biệt được gán một số hỗ trợ (support count) ghi lại số lần nó đã được tham gia vào sự hợp nhất (fusion). Giữ lại chỉ các kích thước có số hỗ trợ không dưới 2.
   - Knowledge-Augmented Reasoning (suy luận bổ trợ kiến thức): kiến trúc annotator–verifier (hệ thống phân cấp) với ba annotator độc lập tạo ra nhãn và lý luận bằng các prompt được tối ưu hóa riêng biệt, và một verifier sau đó so sánh các lý luận của họ để xác định nhãn cuối cùng. Truy xuất mẫu có ý thức về chất lượng (quality-aware sample retrieval) với điểm số Score(q, si) = sim(E(q), E(si)) · wi. Tiêm coupling mẫu-kích thước (dimension–sample coupled injection): chọn top-K mẫu có điểm số cao nhất và các kích thước phân biệt liên quan đến chúng. ANT-OR tiêm cả thứ cấp mẫu (instance-level) và cấp quy tắc (rule-level) vào prompts.
   - Attribution-Guided Optimization (tối ưu hóa hướng dẫn bởi gán lỗi): ANT-OR thực hiện tối ưu hóa prompt ở cấp agent. Đầu tiên gán lỗi (attribute) mỗi lỗi cho các agent chịu trách nhiệm, sau đó tinh chỉnh prompt của chúng. Sau khi cập nhật prompts, đánh giá lại hệ thống đa agent trên batch hiện tại và chỉ giữ lại các prompt đã cập nhật nếu hiệu suất batch-level cải thiện; nếu không, quay lại (rollback) các prompt trước đó để đảm bảo cập nhật mạnh mẽ (robust updates).
   - Mở rộng cơ sở kiến thức lặp đi lặp lại (iterative knowledge base expansion): tối ưu hóa diễn ra trên nhiều kỳ (epochs) qua một chu kỳ lặp của đánh giá, cập nhật cơ sở kiến thức, và tinh chỉnh prompt. Sau mỗi kỳ, các kết quả dự đoán đã xác thực được thêm vào các hồ mẫu tương phản (contrastive sample pools), mở rộng cơ sở kiến thức có sẵn cho việc truy xuất và khai phá tương phản trong các kỳ tiếp theo.

## KNOWLEDGE — Số liệu & khái niệm
- Agreement@≥2 (thỏa thuận ≥2): một gán nhãn được coi là đúng nếu nó khớp với ít nhất hai trong năm annotator con người.
- Fleiss' κ (hệ số Fleiss κ): đo lường sự nhất quán giữa các annotator (inter-annotator consistency).
- Contrastive decision rules (quy tắc quyết định tương phản): các quy tắc quyết định được distillation từ các mẫu tương phản (dương và âm).
- Discriminative dimension (kích thước phân biệt): một đơn vị văn bản có cấu trúc chứa các tiêu chí quyết định theo thể loại được distillation từ các trường hợp tương phản và các tình huống áp dụng mà các tiêu chí này được mong đợi hướng dẫn các quyết định gán nhãn.
- Contrastive sample pool (hồ mẫu tương phản): hồ mẫu dương và âm đã xác thực cho mỗi agent.
- Contrastive tuple (bộ tương phản): (s+1, s+2, s−) dùng để khai phá kích thước phân biệt.
- Support count (số hỗ trợ): số lần một kích thước phân biệt đã tham gia vào sự hợp nhất, dùng để ước lượng số lượng mẫu huấn luyện có lỗi suy luận chia sẻ các mẫu phán 판단 tương tự.
- Annotator–Verifier Architecture (kiến trúc annotator–verifier): ba annotator độc lập tạo nhãn và lý luận, một verifier so sánh lý luận để xác định nhãn cuối cùng.
- Quality-Aware Sample Retrieval (truy xuất mẫu có ý thức về chất lượng): điểm số truy xuất kết hợp độ tương đồng ngữ nghĩa và điểm số chất lượng lịch sử.
- Dimension–Sample Coupled Injection (tiêm coupling kích thước–mẫu): tiêm cả mẫu cấp instance và quy tắc cấp rule vào prompts.
- 7 dataset: Disease Privacy Assessment, Billing Scenario Classification, E-commerce Medical Entity Extraction, Social Text Classification, Image Attribution Recognition, Image Classification, Image Text Relevance.
- 1.500 mẫu mỗi dataset, 5 annotator độc lập mỗi mẫu.
- Fleiss' κ trung bình của con người: 63.60 (trên các dataset).
- ANT-OR: agreement@≥2 trung bình 71.75%, Fleiss' κ trung bình 61.37.
- ANT-OR cải thiện 4.5 điểm so với baseline mạnh nhất (SPO tại 67.08%).
- ANT-OR đạt Fleiss' κ trong 2 điểm so với sự đồng nhất giữa các annotator con người.
- Chi phí tối ưu hóa: $101.43 (ANT-OR) vs $65.94 (SPO), cải thiện độ chính xác 4.7 điểm (71.75% vs 67.08%).
- ANT-OR tổng quát tốt hơn SPO trung bình 3.7 phần trăm điểm trên tập test (SPO overfit dữ liệu huấn luyện).
- 3 LLM-based annotators + 1 verifier, temperature = 0.1.
- 200 mẫu huấn luyện mỗi tác vụ, batch size 20, 3 lần lặp mỗi batch qua 6 kỳ (epochs).
- Đánh giá trên 1000 mẫu test; 300 mẫu còn lại không dùng.

## INSIGHT — Cơ chế & tại sao
- [Single-label benchmarks collapse uncertainty] xảy ra VÌ các annotation thực tế có hướng dẫn chi tiết có thể mập mờ, và sự bất đồng giữa annotator có thể phản ánh các giải thích thay thế hợp lý chứ không phải lỗi gán nhãn. Nghĩa là các tiêu chí đánh giá chỉ dùng một nhãn đơn không thể xác định xem LLM annotator có đạt được sự nhất quán tương đương con người hay không.
- [Static agent systems lack adaptability] xảy ra VÌ các hệ thống gán nhãn đơn agent hoặc đa agent tĩnh thường phụ thuộc vào prompt được làm bằng tay (hand-crafted) và quy trình tĩnh, thất bại trên các tác vụ phức tạp với hướng dẫn chi tiết và các trường hợp ranh giới. Nghĩa là cần hệ thống có thể thích ứng với hướng dẫn phức tạp, phát triển liên tục.
- [Contrastive knowledge drives improvement] xảy ra VÌ việc khai phá kích thước phân biệt từ các mẫu tương phân (dương và âm) cung cấp các tín hiệu tối ưu hóa phong phú hơn các mẫu lỗi đơn thuần. Nghĩa là cấu trúc kiến thức quyết định (structured decision knowledge) là THEN THEN (thì thì) then chốt (key driver) cho cải thiện.

## IDEA — Áp dụng được gì
1. Áp dụng ANT-A Benchmark vào việc đánh giá hệ thống gán nhãn LLM của doanh nghiệp: thu thập 5 nhãn độc lập từ các annotator con người cho mỗi mẫu, sử dụng Fleiss' κ để đánh giá mức độ sự gán nhãn của model phù hợp với phân phối gán nhãn của con người. Bước đầu: xây dựng một tập dữ liệu gán nhãn nhỏ với hướng dẫn chi tiết và 5 annotator độc lập cho mỗi mẫu.
2. Áp dụng kiến trúc annotator–verifier vào hệ thống gán nhãn đa agent: ba annotator độc lập tạo nhãn và lý luận bằng các prompt được tối ưu hóa riêng biệt, sau đó một verifier so sánh các lý luận để xác định nhãn cuối cùng. Bước đầu: triển khai hệ thống 3 annotator + 1 verifier với các prompt khác nhau cho mỗi annotator.
3. Áp dụng khai phá kiến thức tương phản (contrastive knowledge mining): khi agent đưa ra dự đoán sai, lấy hai mẫu đúng tương tự về mặt ngữ nghĩa để tạo contrastive tuple, sau đó dùng LLM để tóm tắt kích thước phân biệt (discriminative dimension) từ các trường hợp gây nhầm lẫn. Bước đầu: thiết lập cơ sở lưu trữ các mẫu đúng và sai, sau mỗi dự đoán sai trích xuất kích thước phân biệt và lưu vào knowledge base.

## WISDOM — Nguyên tắc tổng quát
- Nguyên tắc: Gán nhãn bằng LLM nên được đánh giá theo sự phù hợp với phân phối phán đoán của con người (distribution-aware evaluation), không chỉ so sánh với một nhãn vàng đơn lẻ — sự bất đồng giữa annotator trên các trường hợp ranh giới phản ánh sự mập mờ thực tế, không phải là lỗi cần loại bỏ.
- Khi nào dùng: Khi xây dựng hệ thống gán nhãn dữ liệu tự động cho các tác vụ có hướng dẫn chi tiết và nhiều trường hợp ranh giới (phân loại văn bản, trích xuất thực thể y tế, phân loại hình ảnh...).
- Khi nào KHÔNG dùng: Khi tác vụ gán nhãn có một đáp án rõ ràng, không mập mờ (như phân loại spam/không spam với quy tắc rõ ràng) — không cần hệ thống đa agent phức tạp.

## Assumptions & Limitations
- Điều kiện phải đúng: Cần có các annotator con người chuyên nghiệp để tạo các nhãn tham chiếu và hướng dẫn tác vụ chi tiết.
- Limitation paper thừa nhận: Benchmark vẫn chỉ đại diện cho một tập con của các thiết lập gán nhãn thực tế; có thể mở rộng để bao gồm nhiều tác vụ hơn như gán nhãn tài liệu dài (long-document annotation), phán đoán mở (open-ended judgment), và các quy trình chuyên gia chuyên sâu hơn. Chi phí tối ưu hóa cao hơn do thiết kế đa agent và lặp đi lặp lại.
- Limitation paper KHÔNG nói: Không nói rõ làm thế nào để tự động tạo hướng dẫn tác vụ chi tiết mà không cần can thiệp con người.

## Metadata
- Năm: 2026
- Tác giả: Xiaopeng Ke, Zhixin Wang, Xuebo Liu, Xinyu Ma, Xing Zheng, Bowen Song, Weiqiang Wang, Min Zhang
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.32415v1
- Classification: [applied]