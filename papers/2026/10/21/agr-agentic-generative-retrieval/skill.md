# Skill: Tool-augmented generation — fetch feature theo nhu cầu khi sinh
Source: 2610.26831 (AGR)
Type: framework

## Khi nào dùng skill này
- Hệ thống retrieval (truy xuất) / recommendation sinh ID, nhưng quality (chất lượng) phụ thuộc feature ngoài (user history, freshness) mà nhồi vào input thì quá đắt.
- Cần agent (tác nhân) tự quyết định mỗi bước có fetch data không, fetch gì.
- KHÔNG dùng khi feature ít, cố định, và cost (chi phí) không thành vấn đề → injection tĩnh đơn giản hơn.

## Input cần có
- Item corpus với hierarchical Semantic ID (SID — định danh ngữ nghĩa phân cấp) đã học (residual quantization).
- Tập tool: mỗi tool = function f(query, user, context) trả về giá trị rời rạc (categorical features, behavioral sequence summary, query/user features).
- Log chất lượng để tính information gain (lợi ích thông tin) mỗi fetch.

## Các bước thực hiện
1. Mở rộng vocabulary: V = S ∪ T ∪ O — thêm tool token và observation token; mỗi tool token kích hoạt function call, kết quả thành observation token.
2. Xây training trajectory: dọc theo SID hierarchy, đánh dấu fetch mỗi feature khi nó có applicability (tính áp dụng) và information gain dương (ví dụ giảm ΔPPL).
3. Pretrain model trên SID generation (không tool) đến hội tụ.
4. Fine-tune tool-augmented: model học khi nào emit tool token, feature nào, và observation ảnh hưởng token tiếp theo thế nào.
5. Inference: decoding từng beam, model emit tool token khi cần → gọi tool → tiếp tục decoding với observation token.

## Output mong đợi
- Model sinh SID kèm fetch feature on-demand: Recall/MRR cao hơn baseline tĩnh, serving cost (chi phí phục vụ) thấp hơn nhiều so với nhồi toàn bộ feature (AGR: −42.9% serving, −81.8% training time so direct encoding).

## Ví dụ áp dụng
- Gợi ý video ngắn: model sinh SID item; khi prefix cho thấy user mới (cold), emit tool token fetch "freshness + trending" feature thay vì gửi toàn bộ history 400 token → Recall@50 ngang (0.3237 vs 0.3241) mà serving còn 4.76 vs 8.33 GPUs/1K requests.

## Gotchas
- Trajectory supervision bằng rules sẽ chặn trần hiệu năng — cân nhắc agentic RL với sparse rewards.
- Xây trajectory trên golden SID prefix gây exposure bias (thiên kiến phơi nhiễm) — model chưa học phục hồi khi prefix sai.
- Kiểm tra serving budget: tool calls ~2× cost so no-feature baseline — phải nằm trong latency (độ trễ) budget (AGR: 35ms).
