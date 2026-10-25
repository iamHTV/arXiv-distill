# Skill: arctic-swe-rl-baseline

Source: 2610.24914
Type: framework

## Khi nào dùng skill này

- Trước khi đánh giá thuật toán hoặc dữ liệu mới cho đào tạo RL agent dài hạn, cần thiết lập cơ sở mạnh mẽ và tái lập được.
- Muốn dùng overfit trên nhóm tác vụ nhỏ làm kiểm tra định kỳ để phơi bày lỗi hạ tầng mà phần thưởng sớm che lấp.
- Có hạ tầng hỗ trợ RL bất đồng bộ (nhiều engine suy luận, bộ nhớ đệm KV, cân bằng tải).

## Tình huống KHÔNG nên dùng

- Nhiệm vụ ít tương tác dài hạn (đáp luận đơn lần, phân loại văn bản).
- Nhóm nhỏ hơn 8 GPU (chi phí mô-hệ thống co-design chưa được kiểm chứng).

## Input cần có

- Nhóm tác vụ nhỏ (100-200) mà mô hình có thể giải quyết ít nhất một lần trên bốn lần thử.
- Hạ tầng RL bất đồng bộ: ít nhất 2 GPU đào tạo, nhiều engine suy luận vLLM.
- Định dạng tin nhắn có cấu trúc (khối lý luận, gói gọi côngockey, thẻ).

## Các bước thực hiện

1. Lọc nhóm tác vụ nhỏ: chọn các tác vụ mà mô hình vượt qua ít nhất một lần trên bốn lần thử.
2. Đào tạo trên nhóm nhỏ trong nhiều epochs, theo dõi entropy token và KL không khớp giữa lượtROLL và trình huấn luyện — nếu không thể ghi nhớ nhóm nhỏ, công thức chưa ổn định.
3. Áp dụng gated reward: yêu cầu nộp rõ ràng, gán phần thưởng bằng 0 cho định dạng sai, gọi công cụ không hợp lệ, hết lượt hoặc ngân sách token.
4. Áp dụng kiểm tra định dạng thó: xác thực đầu ra token thô (khối lý luận, gói gọi, thẻ bên trong) chứ không chỉ gọi đã được trình phân tích chuyển đổi.
5. Căn chỉnh đào tạo và suy luận số: giữ FP32 cho trạng thái tuần tự, số học cổng, và Alog.
6. Vô hiệu hóa tất cả bộ nhớ đệm khi làm mới trọng số và tải lại trước lịch sử đã giữ.
7. Phân phối mỗi nhóm đến engine ít tải nhất, giới hạn chuỗi tồn tại, cắt bớc tác vụ đã thành thạo và thất bại lặp lại.
8. Lọc dữ liệu: dùng Pipeline 1 (cổng fail-to-pass qua thực thi) rồi Pipeline 2 (LLM judge kiểm tra đồng ý giữa vấn đề, bài kiểm tra, bản vá vàng).

## Output mong đợi

- Cơ sở RL ổn định, có thể overfit nhóm tác vụ nhỏ đến >90% phần thưởng.
- Phần thưởng không sụp đổ sau nhiều epochs.
- Cơ sở cho việc so sánh thuật toán và dữ liệu mới.

## Ví dụ áp dụng

Đào tạo agent viết code trên 160 tác vụ SWE: lọc 160 tác vụ mà Qwen3.5-4B giải quyết được ít nhất 1/4 lần, chạy overfit nhiều epochs. Nếu phần thưởng sụp đổ sau epoch 11 (như Prime-RL ban đầu), áp dụng gated reward và kiểm tra định dạng thó → phần thưởng ổn định tại 74.5%+ và đạt 62.0% trên SWE-bench Verified.

## Gotchas

- Phần thưởng sớm che lỗi hạ tầng: đánh giá chỉ vài epochs đầu là không đủ.
- Bất đồng bộ làm cho tốc độ engine suy luận và trình huấn luyện ảnh hưởng đến động lực đào tạo, không chỉ tốc độ.
- 4B có thể quên tác vụ đã thành thạo khi chúng bị loại khỏi đào tạo (giới hạn dung lượng).
- Môi trường sandbox cần cô lập (tách .git, từ chối lưu lượng ra ngoài) để tránh đánh giá gian lận.
