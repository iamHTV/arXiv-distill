# Skill: leafskill-retrieve-bind-select (lớp grounding cấp lá cho tác tử đệ quy)

Source: 2610.32412v1
Type: framework / workflow

## Khi nào dùng skill này

- Tác tử LLM đệ quy gọi mô hình chủ lớn quá nhiều lần chỉ để dịch tác vụ lá thành lệnh thực thi.
- Cần tái sử dụng kinh nghiệm tác vụ/hành động mà không lấy quá quyền lập kế hoạch đệ quy của mô hình chủ.
- Môi trường có danh sách hành động chấp nhận được (admissible action set) rời rạc.

Tình huống KHÔNG nên dùng:
- Hành động liên tục hoặc không có giao diện hành động rời rạc.
- Không có lịch sử quỹ đạo để xây dựng thư viện kỹ năng.

## Input cần có

- Thư viện kỹ năng (skill library): các cặp tác vụ chuẩn/mẫu hành động được trích xuất từ quỹ đạo mô hình chủ.
- Truy xuất ngữ nghĩa (semantic retriever): ví dụ BGE-small-en-v1.5.
- Trình gắn kết dựa trên trạng thái (state-bound binder): tạo mẫu loại bằng thực thể từ yêu cầu hiện tại.
- Trình chọn nhẹ (lightweight selector): ví dụ Qwen3-1.7B với LoRA, chọn một ứng viên hoặc từ chối.
- Tập hành động chấp nhận được At của môi trường tại mỗi bước.
- Mô hình chủ (host) và lập kế hoạch đệ quy (recursive planner) giữ nguyên.

## Các bước thực hiện

1. Xây dựng thư viện kỹ năng ngoại tuyến: chuyển quỹ đạo của mô hình chủ thành các cặp tác vụ chuẩn/mẫu hành động (canonical task–action template), mỗi cặp là một kỹ năng.
2. Tại mỗi tác vụ lá đủ điều kiện (adapter eligibility), gọi LeafSkill: truy xuất ngữ nghĩa top-k mẫu liên quan trên ngưỡng γ.
3. Gắn kết dựa trên trạng thái: tạo mẫu loại bằng thực thể từ yêu cầu hiện tại, chỉ giữ lệnh khớp chính xác một hành động trong At, hợp nhất các cặp trùng lặp thành tập ứng viên Ct.
4. Chọn lựa cục bộ: gán mã định dạng cục bộ yêu cầu cho ứng viên, tráo đổi, trình chọn chọn một mã hoặc ⊥ (từ chối).
5. Giải quyết mã định dạng được chọn qua bản đồ cục bộ yêu cầu, kiểm tra lại đối với At trước khi thực thi.
6. Nếu không có ứng viên, gắn kết thất bại, hoặc trình chọn từ chối: trả ⊥, quyền điều khiển quay lại mô hình chủ mà không thay đổi trạng thái.

## Output mong đợi

- Giảm token mô hình chủ (23.1% Robotouille, 41.3% ALFWorld trên các tác vụ được giải quyết chung).
- Giảm lệnh gọi mô hình chủ (22.54% Robotouille, 41.75% ALFWorld).
- Thành công cao hơn hoặc bằng mô hình chủ đơn thuần (8 điểm trên Robotouille C).
- Khi thư viện tăng trưởng (không cần huấn luyện lại), mức giảm token sâu hơn (18.3% → 25.6%).

## Ví dụ áp dụng

Tác tử nấu ăn Robotouille: lập kế hoạch đệ quy đã tạo tác vụ lá "grab the onion". Thay vì gọi Qwen3.5-27B để dịch thành lệnh, LeafSkill truy xuất mẫu "pick_up(·, ·)", gắn kết thành "pick up onion1 from board1" (khớp với At), trình chọn chọn hoặc từ chối. Nếu chọn, thực thi lệnh và trả phản hồi cho môi trường; nếu từ chối, trả về Qwen3.5-27B. Kết quả: giảm 23.1% token chủ so với gọi chủ mỗi lần.

## Gotchas

- Giả định các tác vụ lá xuất hiện lặp lại và có thể tham số hóa; nếu tác vụ lá độc lập mỗi lần, thư viện không hữu ích.
- Cần bộ biến đổi môi trường (environment adapter) và trình gắn kết tương ứng cho mỗi ngữ pháp hành động mới.
- Chi phí phụ của trình chọn (6.900–9.952 token/tập sự) được báo cáo riêng biệt vì trình chọn và chủ có trình phân mã khác nhau.
- Từ chối (abstention) trả quyền về host, không thực thi hành động nào — cần host xử lý trường hợp này.
- Thư viện có thể tăng trưởng tại thời điểm đọc nhưng chỉ với kỹ năng tương thích (cùng ngữ pháp hành động và ô typed slot).
