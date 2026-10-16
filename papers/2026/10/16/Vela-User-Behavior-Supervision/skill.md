# Skill: vela-user-behavior-as-supervision
Source: 2610.14709v1
Type: framework

## Khi nào dùng skill này
- Huấn luyện LLM để hiểu sở thích và ý định người dùng từ dữ liệu hành vi thật.
- Có dữ liệu hành vi người dùng (lịch sử xem, tìm kiếm, mua hàng, đăng bài, theo dõi, ẩn bài).
- Muốn cải thiện khả năng personalization và user-facing của LLM.

## Tình huống KHÔNG nên dùng
- Không có dữ liệu hành vi người dùng thật.
- Chỉ cần LLM trả lời từ kiến thức chung, không cần hiểu hành vi người dùng cụ thể.

## Input cần có
- Dữ liệu hành vi người dùng đã ẩn danh (anonymized behavior records): Views, Searches, Purchases, Posts, Follows, Dislikes.
- Hệ thống fine-tune LLM có thể chạy trên các tasks sinh ra.
- Tiêu chí lọc task (difficulty-based filtering, trajectory acceptance criteria).

## Các bước thực hiện
1. Thu thập anonymized behavior records của người dùng (lịch sử xem, tìm kiếm, mua hàng, v.v.).
2. Chia mỗi bản ghi thành visible histories (lịch sử可见) và hidden futures (tương lai ẩn).
3. Chuyển đổi từng bản ghi thành trainable tasks và trajectories qua 91 real-world task templates (hoặc tự định nghĩa template tương ứng).
4. Áp dụng difficulty-based filtering và trajectory acceptance criteria để lọc task chất lượng cao.
5. Fine-tune LLM trên các tasks đã lọc; sau đó dùng RL (reinforcement learning) để cải thiện thêm.

## Output mong đợi
- Cải thiện performance trên các tác vụ liên quan đến người dùng: +11.5 points trên VelaBench, lên đến +11.2 points trên user-related OOD benchmarks.
- RL sau fine-tuning vượt quá RL từ base model bởi 7.7 points.

## Ví dụ áp dụng
Solopreneur có hệ thống xem phim trực tuyến: thu thập lịch sử xem phim, tìm kiếm, và đánh giá của người dùng. Chuyển đổi thành tasks fine-tune LLM để LLM hiểu sở thích phim của từng người và đề xuất phim chính xác hơn. Dùng difficulty-based filtering để chỉ lấy các task có nhãn hành vi rõ ràng.

## Gotchas
- Cần đủ dữ liệu hành vi người dùng (100,000 records trong paper) để có hiệu quả.
- Cần thiết kế task templates phù hợp với domen của bạn (91 templates trong paper là cho nội dung chung).
- RL sau fine-tuning giúp cải thiện thêm nhưng cần tài nguyên tính toán hơn.
