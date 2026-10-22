# Skill: Harness bộ nhớ gated cho trợ giúp chủ động (MemoProAgent)
Source: 2610.22671
Type: framework

## Khi nào dùng skill này
- Trợ lý AI cần can thiệp chủ động (proactive) mà không có truy vấn từ người dùng (ví dụ AI kính thông minh, wearable assistant).
- Có bộ nhớ dài hạn của người dùng giàu nhiễu, cần quyết định khi nào và nói gì.
- KHÔNG dùng cho trợ lý chỉ phản ứng theo truy vấn rõ ràng, hoặc khi không có dữ liệu lịch sử người dùng.

## Input cần có
- Lịch sử sự kiện người dùng (ký sự episodic +사실 ngữ nghĩa semantic).
- Luồng quan sát hiện tại (video egocentric hoặc ngữ cảnh hiện tại).
- Trình sinh ngôn ngữ (generator) có thể gọi tool retrieval.
- Giao thức đánh giá trigger window (khi nào nên nhắc nhở).

## Các bước thực hiện
1. Xây dựng đồ thị bộ nhớ hai lớp: lớp ký sự (object-keyed episodic memories) và lớp ngữ nghĩa (semantic facts), mỗi ký sự có cờ open-loop (ý định chưa giải quyết).
2. Tại mỗi điểm ra quyết định, chạy vòng lặp tác nhân: observe (nhận diện đối tượng đang quan sát) → retrieve (embed-match đến seed entities, pull one-hop episodic/semantic facts, Personalized PageRank trên đồ thị) → gate (một cuộc gọi LLM duy nhất lọc bằng chứng xứng đáng ngắt lời, tinh chỉnh thành một đoạn duy nhất hoặc abstain) → reason → answer (nói nhắc nhở hoặc im lặng).
3. Chỉ đưa <evidence> vào trình sinh khi cổng lọc xác nhận xứng đáng can thiệp; nếu không, để trống để im lặng là hành vi mặc định.
4. (Tùy chọn) Hậu huấn luyện trình sinh bằng GRPO với phần thưởng nhị phân: +1 im lặng đúng hoặc can thiệp đúng thời điểm với nội dung tốt, −1 ngược lại; mask token bằng chứng khi tính loss.

## Output mong đợi
- Độ chính xác nghiêm ngặt (Perfect) từ dưới 10% lên 37.5% (Qwen3.8-27B) / 38% (GPT-5.3-Chat) không cần huấn luyện; RL lên 42.4%.
- Giảm tỷ lệ tiro sai trên clip âm từ 77.3%/84.0% (RAG) xuống 15.3%.

## Ví dụ áp dụng
- Trợ lý AI kính thông minh quan sát người dùng đi qua cửa hàng tạp hóa: đồ thị bộ nhớ nhớ người dùng đã hết nước ngân laatste hôm qua, cổng lọc xác nhận xứng đáng nhắc nhở khi thấy người dùng đi lại cửa hàng, trình sinh đưa ra "Bạn nên mua thêm nước ngân" đúng lúc, không tiro sớm hay lặp lại.

## Gotchas
- Bộ nhớ tổng hợp (synthesized) trong benchmark, không phải lịch sử đa phương thức thực tế — cần thích ứng khi triển khai production.
- Không đánh giá độ trễ, chỉ đánh giá hiệu suất tác vụ.
- Mỗi clip chỉ một cửa sổ kích hoạt; nhiều trigger trong một luồng chưa được xử lý.
- Cổng lọc là một cuộc gọi LLM bổ sung, cần tính vào chi phí và độ trễ.