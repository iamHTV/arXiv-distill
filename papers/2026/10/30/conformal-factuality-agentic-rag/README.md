# [2610.34872] Adaptive Retrieval, Selective Answers: Evaluating Conformal Factuality in Agentic RAG

## Giá trị cốt lõi (1 câu)

Khi triển khai RAG agent, nên áp dụng lọc chuẩn (conformal filtering) sau khi agent tạo câu trả lời — chỉ giữ các claim nguyên tử có độ liên quan vượt ngưỡng đánh giá từ tập định chuẩn — để đạt tỷ lệ đầy đủ hỗ trợ 89–95% với mức mục tiêu 95%, đồng thời báo cáo cùng lúc tỷ lệ câu trả lời không rỗng (17–60%) để thấy rõ sự đánh đổi độ tin cậy–thông tin.

## Problem

RAG (retrieval-augmented generation — tăng sinh truy xuất) điều chỉnh phản hồi của mô hình ngôn ngữ dựa trên tài liệu bên ngoài, nhưng việc lấy bằng chứng không đảm bảo mọi claim được tạo ra là sự thật hoặc có bằng chứng. Công việc trước đã nghiên cứu tính đúng sự thật cấp claim chuẩn (tính đúng sự thật cấp claim chuẩn) trong RAG đơn giai đoạn và RAG đa nhảy, nhưng chưa đánh giá trong agentic RAG (RAG tác tử), nơi một ngôn ngữ-mô hình chính sách (language-model policy) thích ứng đưa ra các truy vấn theo dõi hoặc chấm dứt lấy bằng chứng trước khi sinh phản hồi. Trong agentic RAG, việc lấy bằng chứng dùng để tạo và chấm điểm các claim thay đổi tùy theo câu hỏi và bằng chứng quan sát được cho đến thời điểm đó, còn giai đoạn lọc chuẩn sau sinh vẫn giữ nguyên ý nghĩa khái niệm.

## Contribution

1. Công thức rõ ràng quy trình lấy bằng chứng tác tử (adaptive retrieval trajectory) dưới dạng chuỗi các quyết định chính sách lấy bằng chứng phụ thuộc vào bằng chứng, và đánh giá sáu cấu hình mô hình–tập dữ liệu với toàn bộ mức mục tiêu và giá trị chuẩn không lọc.
2. Giữ nguyên công thức chấm điểm liên quan dựa trên truy xuất và lọc chuẩn sau sinh, mở rộng đánh giá từ RAG đơn giai đoạn và đa nhảy sang RAG tác tử.
3. Cho thấy việc tăng mức mục tiêu conformal tạo ra cùng sự cải thiện được quan sát ở mức hỗ trợ cấp phản hồi khi việc lấy bằng chứng do tác tử điều hướng, và mô tả sự đánh đổi độ tin cậy–thông tin (reliability–informativeness trade-off) khi tính đúng sự thật chuẩn được áp dụng sau khi tác tử chấm dứt.

## Method

Quy trình lấy bằng chứng tác tử được định thức hóa như sau: cho câu hỏi x và kho tài liệu K, các hoạt động lấy bằng chứng được đánh chỉ mục bởi t. Truy vấn ban đầu là câu hỏi gốc q(1) = x. Với một bộ lấy bằng chứng top-k có ngưỡng độ tương đồng θ, chuỗi tài liệu ban đầu là D1 = Unique(Retrieve(K, q(1); k, θ)). Sau t lần lấy bằng chứng, viết Qt = (q(1), ..., q(t)) và Dt chứa các đoạn văn bản riêng biệt đã tích lũy theo thứ tự lấy bằng chứng. Trạng thái quyết định là Ht = (x, Ψ(Dt), Qt, t, B − t), ở đó πω là chính sách của tác tử, B là ngân sách hoạt động lấy bằng chứng, Q là không gian truy vấn theo dõi, và Ψ(Dt) là kết quả bằng chứng bị giới hạn được cung cấp cho chính sách. Nếu at = Retrieve(q(t+1)) được chấp nhận, thì Et+1 = Retrieve(K, q(t+1); k, θ), Dt+1 = Dt ⊕ New(Et+1, Dt), trong đó New loại bỏ các trùng lặp đã có trong Dt và ⊕ thêm các đoạn văn bản chưa từng thấy. Thứ tự quan trọng vì nó có thể ảnh hưởng đến kết quả bằng chứng có sẵn cho quyết định chính sách tiếp theo. Số lần lấy bằng chứng khi quy trình chấm dứt là τ(x), với 1 ≤ τ(x) ≤ B. Sau khi tác tử chấm dứt, mô hình sinh phản hồi và trình phân tích claim trích xuất các phát biểu nguyên tử: ŷ = G(x, Dπ(x)), C(x) = g(ŷ) = {c1, ..., cp(x)}. Số lượng claim trích xuất p(x) thay đổi qua các câu hỏi. Chỉ số hỗ trợ sự thật của mỗi claim thuộc {S, I, U, N}, trong đó chỉ S tính là được hỗ trợ. Ghi A(c) ∈ {0, 1} là chỉ số hỗ trợ này. Điểm liên quan của tác tử được biểu diễn bằng Ragent(c; x) = max(0, max d∈Dπ(x) sret(d) sim(c, d)). Sự tương đồng sim(c, d) đo lường sự can thiệp ngữ nghĩa giữa claim và đoạn văn bản. Điểm liên quan được đánh giá sau sinh: mục tiêu chuẩn không kiểm soát khi tác tử truy xuất chấm dứt. Tập được giữ theo ngưỡng là Fλ(C(x)) = {c ∈ C(x) : eR(c) ≥ λ}. Một phản hồi được hỗ trợ đầy đủ ở ngưỡng λ khi mọi claim được giữ được hỗ trợ: Bi(λ) = I[∀cij ∈ Fλ(Ci), Aij = 1]. Điểm không-thích-thích hợp cho chuẩn tất cả-claim-được-hỗ trợ là Vi = max j:Aij=0 rij, max ∅ = −∞. Các điểm chuẩn bị được sắp xếp V(1) ≤ ... ≤ V(n), ngưỡng thống kê thứ tự chuẩn chia-thử là  λα = V(kα) nếu kα ≤ n, và +∞ nếu kα = n + 1, với kα = ⌈(n + 1)(1 − α)⌉. Năm mức mục tiêu đánh giá 1 − α ∈ {0.80, 0.85, 0.90, 0.925, 0.95} tương ứng, với n = 30, với kα ∈ {25, 27, 28, 29, 30}.

## KNOWLEDGE — Số liệu & khái niệm

- Sáu cấu hình mô hình–tập dữ liệu: GPT-6 Luna và Llama 3.1 8B trên HotpotQA, Natural Questions (NQ), và TriviaQA.
- Mỗi cấu hình dùng 60 câu hỏi cố định, 100 phân đoạn chia–thử 30/30 đã gieo hạt, năm mức mục tiêu chuẩn (80, 85, 90, 92.5, 95%), và giá trị chuẩn không lọc làm cơ sở so sánh.
- Bộ lấy bằng chứng: sentence-transformer embeddings (all-MiniLM-L6-v2), chỉ mục FAISS, top-k = 10 tài liệu mỗi lần lấy bằng chứng, ngưỡng độ tương đồng θ = 0.3, lấy bằng chứng ban đầu được bật, tối đa ba hoạt động lấy bằng chứng và ba quyết định chính sách.
- Tại mức mục tiêu 95%, tỷ lệ phản hồi không rỗng trải qua 17.23% (GPT-6 Luna, NQ) đến 60.17% (Llama 3.1 8B, TriviaQA); tỷ lệ giữ claim trải qua 10.72% đến 43.16%; tỷ lệ hỗ trợ đầy đủ trong các đầu ra không rỗng trải qua 89.14% đến 95.56%; tỷ lệ claim được hỗ trợ trong các claim được giữ trải qua 90.16% đến 97.72%.
- Việc tăng mức mục tiêu chuẩn đi kèm với tỷ lệ hỗ trợ đầy đủ quan sát được cao hơn và tỷ lệ sẵn sàng câu trả lời thấp hơn.
- NQ đạt cobertura thấp hơn nhiều so với TriviaQA tại các mục tiêu nghiêm ngặt.
- Lọc chuẩn được áp dụng sau sinh, sau khi tác tử đã chấm dứt và sinh phản hồi; nó không kiểm soát khi tác tử truy xuất chấm dứt.

## INSIGHT — Cơ chế & tại sao

[Tỷ lệ hỗ trợ đầy đủ tăng khi mục tiêu chuẩn được nâng] xảy ra VÌ [ngưỡng liên quan cao hơn loại bỏ nhiều claim không được hỗ trợ hơn, để lại phần nhỏ hơn các phản hồi nhưng phần lớn chúng được hỗ trợ đầy đủ]. Điều này nghĩa là [có sự đánh đổi rõ ràng giữa độ tin cậy và khả năng cung cấp thông tin: ngưỡng cao hơn tăng độ tin cậy nhưng làm giảm khả năng trả lời].

[Mức đánh đổi phụ thuộc mạnh vào tổ hợp mô hình/tập dữ liệu] xảy ra VÌ [NQ đạt cobertura thấp hơn nhiều so với TriviaQA tại các mục tiêu nghiêm ngặt, cho thấy chi phí chọn lọc của một mục tiêu cho trước không đồng nhất trên các thiết lập]. Điều này nghĩa là [không nên giảm đánh giá xuống một con số tin cậy duy nhất; khả năng trả lời câu trả lời và tỷ lệ giữ claim cần đi kèm với tỷ lệ hỗ trợ đầy đủ cấp phản hồi trong báo cáo triển khai].

[Lọc chuẩn sau sinh không kiểm soát khi tác tử chấm dứt truy xuất] xảy ra VÌ [ngưỡng chuẩn chỉ được áp dụng trên các claim sau khi phản hồi đã được tạo, trong khi thời điểm dừng của tác tử được quyết định bởi chính sách truy xuất thích ứng]. Điều này nghĩa là [cân nhắc độ tin cậy–thông tin xảy ra ở cấp claim sau khi thực thể đã được thu thập, không tại thời điểm lấy bằng chứng].

[Tập claim rỗng được xem là được hỗ trợ đầy đủ theo quy ước] xảy ra VÌ [yêu cầu tất cả-claim-được-hỗ trợ được thỏa mãn một cách trống rỗng khi không có claim nào được giữ]. Điều này nghĩa là [tỷ lệ hỗ trợ đầy đủ cấp phản hồi bao gồm các trường hợp trống rỗng, nên cần báo cáo cả tỷ lệ phản hồi không rỗng để tránh hiểu nhầm].

## IDEA — Áp dụng được gì

1. Áp dụng lọc chuẩn sau sinh cho RAG agent: sau khi agent tạo câu trả lời, phân tích thành các claim nguyên tử, tính điểm liên quan cho mỗi claim dựa trên tài liệu đã lấy, chỉ giữ các claim vượt ngưỡng conformal đánh giá từ tập định chuẩn. Cho ai: hệ thống RAG agent cần đảm bảo sự đúng sự thật của từng claim. Bước đầu: triển khai bộ phân tích claim và bộ chấm điểm liên quan dựa trên truy xuất.

2. Áp dụng báo cáo song song độ tin cậy và khả năng câu trả lời: khi triển khai RAG agent, báo cáo cùng lúc tỷ lệ phản hồi đầy đủ được hỗ trợ FS(λ) và tỷ lệ phản hồi không rỗng NE(λ), không chỉ báo một con số tin cậy. Cho ai: đội đánh giá và Triển khai RAG. Bước đầu: thêm hai chỉ số FS(λ) và NE(λ) vào bảng đánh giá của hệ thống.

3. Áp dụng mục tiêu conformal tuỳ theo tập dữ liệu: vì chi phí chọn lọc khác nhau trên các tập dữ liệu (NQ mất cobertura nhiều hơn TriviaQA tại các mục tiêu nghiêm ngặt), điều chỉnh mục tiêu conformal theo từng tập dữ liệu thay vì dùng một ngưỡng đồng nhất. Cho ai: hệ thống RAG được triển khai trên nhiều tập dữ liệu hoặc miền khác nhau. Bước đầu: chạy sweep mục tiêu conformal trên tập đánh giá nhỏ trước khi chọn ngưỡng sản xuất.

## WISDOM — Nguyên tắc tổng quát

- Nguyên tắc: Lọc claim sau sinh tạo ra sự đánh đổi độ tin cậy–thông tin: ngưỡng cao hơn tăng độ tin cậy nhưng giảm khả năng trả lời; cần báo cáo cùng lúc cả hai chỉ số thay vì chỉ một con số. Áp dụng khi xây dựng hệ thống RAG agent cần đảm bảo sự đúng sự thật của từng claim. Không áp dụng khi cần trả lời mọi câu hỏi bất kể sự hỗ trợ bằng chứng.

## Assumptions & Limitations

- Điều kiện phải đúng: có tập định chuẩn và tập thử riêng biệt, có khả năng phân tích câu trả lời thành claim nguyên tử, có hệ thống chấm điểm liên quan dựa trên truy xuất.
- Limitation paper thừa nhận: đánh giá dựa trên các tập con được kiểm soát của 60 câu hỏi từ mỗi của ba tiêu chuẩn Hỏi–Đáp (HotpotQA, Natural Questions, và TriviaQA); kích thước mẫu tương đối nhỏ có thể hạn chế sự tổng quát hóa của kết quả đến các tập câu hỏi lớn hơn và đa dạng hơn; quy trình lấy bằng chứng tác tử bị giới hạn tối đa ba hoạt động lấy bằng chứng và ba quyết định chính sách, để lại các tác động của các quỹ đạo lấy bằng chứng dài hơn và các chính sách tác tử thay thế chưa được khám phá; furthermore, các thí nghiệm chỉ xem xét hai ngôn ngữ-mô hình, GPT-6 Luna và Llama 3.1 8B. Mở rộng đánh giá sang các họ ngôn ngữ-mô hình khác, chẳng hạn Qwen và DeepSeek, sẽ giúp thiết lập tính mạnh mẽ và tổng quát hóa của sự cải thiện tính đúng sự thật chuẩn được quan sát trên các kiến trúc ngôn ngữ-mô hình khác nhau.
- Limitation paper KHÔNG nói: hiệu quả trên các tác tử RAG lớn hơn, chi phí vận hành của lọc chuẩn trên quy mô lớn, và khả năng mở rộng sang các môi trường thực tế bên ngoài ba tập Hỏi–Đáp được đánh giá.

## Metadata

- Năm: 2026
- Tác giả: Muhammad Aimal Rehman, Chi-Kuang Yeh (Georgia State University)
- Category arXiv: cs.CL
- Link PDF: https://arxiv.org/pdf/2610.34872v1
- Citation count: [không tìm được]