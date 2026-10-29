# Skill: conformal-filtering-agentic-rag (lọc chuẩn cho RAG tác tử)

Source: 2610.34872v1
Type: framework / workflow

## Khi nào dùng skill này

- Hệ thống RAG agent cần đảm bảo sự đúng sự thật của từng claim trong câu trả lời.
- Cần báo cáo cùng lúc độ tin cậy và khả năng trả lời, không chỉ một con số.
- Có khả năng phân tích câu trả lời thành các claim nguyên tử và tính điểm liên quan dựa trên tài liệu đã lấy.

Tình huống KHÔNG nên dùng:
- Cần trả lời mọi câu hỏi bất kể sự hỗ trợ bằng chứng.
- Không có tập định chuẩn để đánh giá ngưỡng conformal.

## Input cần có

- Tập định chuẩn và tập thử riêng biệt (60 câu hỏi, 100 phân đoạn chia–thử 30/30).
- Trình phân tích claim nguyên tử (atomic claim decomposer).
- Bộ chấm điểm liên quan dựa trên truy xuất (retrieval-based relevance scorer).
- Ngưỡng độ tương đồng (θ = 0.3), top-k = 10, tối đa 3 lần lấy bằng chứng và 3 quyết định chính sách.
- Năm mức mục tiêu conformal (80, 85, 90, 92.5, 95%) để chọn ngưỡng sản xuất.

## Các bước thực hiện

1. Sau khi tác tử RAG tạo câu trả lời, phân tích thành các claim nguyên tử (atomic claims).
2. Tính điểm liên quan cho mỗi claim dựa trên tài liệu đã lấy bằng công thức Ragent(c; x) = max(0, max d∈Dπ(x) sret(d) sim(c, d)).
3. Xác định ngưỡng conformal λα từ tập định chuẩn bằng thống kê thứ tự chuẩn chia-thử: λα = V(kα) với kα = ⌈(n + 1)(1 − α)⌉.
4. Giữ chỉ các claim có điểm liên quan ≥ λα: Fλ(C(x)) = {c ∈ C(x) : eR(c) ≥ λ}.
5. Tạo câu trả lời cuối từ các claim được giữ; nếu không có claim nào được giữ, câu trả lời rỗng (được xem là được hỗ trợ đầy đủ theo quy ước).
6. Báo cáo cùng lúc tỷ lệ phản hồi đầy đủ được hỗ trợ FS(λ) và tỷ lệ phản hồi không rỗng NE(λ).

## Output mong đợi

- Tỷ lệ phản hồi đầy đủ được hỗ trợ 89–95% tại mức mục tiêu 95%.
- Tỷ lệ phản hồi không rỗng 17–60% tại mức mục tiêu 95% (phụ thuộc vào mô hình/tập dữ liệu).
- Tỷ lệ giữ claim 10–43%, tỷ lệ claim được hỗ trợ 90–98%.
- Sự đánh đổi rõ ràng giữa độ tin cậy và khả năng trả lời.

## Ví dụ áp dụng

Hệ thống RAG agent trả lời câu hỏi về kiến thức tổng quát (TriviaQA): agent lấy bằng chứng thích ứng (tối đa 3 lần lấy bằng chứng), sau đó sinh câu trả lời. Áp dụng skill: phân tích câu trả lời thành các claim, tính điểm liên quan dựa trên tài liệu đã lấy, chỉ giữ claim vượt ngưỡng conformal 95%. Kết quả: câu trả lời chỉ chứa các claim có bằng chứng hỗ trợ, tỷ lệ đầy đủ hỗ trợ 95%, nhưng chỉ 60% câu trả lời không rỗng (còn lại bị lọc trống). Báo cáo cùng hai chỉ số này để người dùng thấy được sự đánh đổi.

## Gotchas

- Mục tiêu conformal cao hơn tăng độ tin cậy nhưng giảm khả năng trả lời; không nên dùng một ngưỡng đồng nhất cho tất cả tập dữ liệu.
- Tập claim rỗng được xem là được hỗ trợ đầy đủ theo quy ước — cần báo cáo tỷ lệ phản hồi không rỗng để tránh hiểu nhầm.
- Lọc chuẩn được áp dụng sau sinh, không kiểm soát khi tác tử chấm dứt truy xuất.
- Kích thước mẫu nhỏ (60 câu hỏi/tập dữ liệu) có thể hạn chế sự tổng quát hóa.
- Chỉ đánh giá trên hai mô hình (GPT-6 Luna, Llama 3.1 8B) và ba tập Hỏi–Đáp.
