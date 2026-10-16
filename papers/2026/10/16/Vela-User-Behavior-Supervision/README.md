# [2610.14709v1] Vela: User Behavior as Supervision Sparks LLM Intelligence

## Problem
Các mô hình LLM hiện tại được huấn luyện trên văn bản tĩnh (static text) hoặc dữ liệu tổng hợp (synthetic data), không thể ghi lại cách hành vi người dùng thay đổi theo thời gian. Tuy nhiên, các ứng dụng thực tế (trợ lý cá nhân, hệ thống khuyến nghị và quảng cáo) đòi hỏi user dimension of LLM intelligence (khía cạnh người dùng của trí tuệ LLM): khả năng suy luận sở thích, ý định, và hành vi tương lai của một người từ hàng tuần đến hàng năm dữ liệu hành vi.

## Contribution
- Đề xuất paradigm user behavior as supervision (hành vi người dùng làm tín hiệu 감독): tín hiệu huấn luyện cho LLM đến từ hành vi thực tế của người dùng trên các nền tảng nội dung.
- Giới thiệu Vela: framework vận hành hóa paradigm này bằng cách chuyển đổi real user behavior data thành trainable tasks và trajectories.
- Từ 100,000 anonymized behavior records của user, Vela sinh 100,000 tasks qua 91 real-world task templates.
- Difficulty-based filtering và trajectory acceptance criteria cùng l retain (giữ lại) các task phù hợp.

## Method (tóm cốt lõi)
Vela lấy 100,000 anonymized behavior records của người dùng, chia thành visible histories (lịch sử可见) và hidden futures (tương lai ẩn). Mỗi bản ghi hành vi được tổ chức thành 6 danh mục: Views, Searches, Purchases, Posts, Follows, Dislikes. Vela sinh tasks và trajectories từ các bản ghi này, áp dụng difficulty-based filtering và trajectory acceptance criteria. Sau đó fine-tune LLM trên các tasks này.

## Key Findings
- Từ 100,000 anonymized behavior records → 100,000 tasks qua 91 real-world task templates.
- Vela-35B-A3B cải thiện so với base model bởi 11.5 points trên VelaBench và lên đến 11.2 points trên user-related OOD benchmarks.
- Average improvement trên general OOD benchmarks: 4 points.
- Reinforcement learning after fine-tuning vượt quá RL từ base model bởi 7.7 points trên cả VelaBench và ProfileSummary.
- VelaBench: 982 held-out evaluation tasks từ cùng 91 task templates.
- User-related OOD benchmarks: PurchaseIntent, ProfileSummary, PersonaBench, AdRecommendation.
- General OOD benchmarks: AIME 2026, GPQA-Diamond, IFBench, CL-bench, CL-bench Life.

## Actionable Insights
- Dùng real user behavior làm tín hiệu huấn luyện (supervision) thay vì chỉ dùng văn bản tĩnh hoặc dữ liệu tổng hợp. Áp dụng: solopreneur có dữ liệu hành vi người dùng (lịch sử xem, tìm kiếm, mua hàng) nên chuyển đổi thành tasks để fine-tune LLM, giúp LLM hiểu hơn về sở thích và ý định người dùng.
- Dùng difficulty-based filtering và trajectory acceptance criteria để lọc các task chất lượng cao. Áp dụng: khi sinh dữ liệu huấn luyện từ hành vi người dùng, hãy lọc theo độ khó và tiêu chí chấp nhận trajectory để đảm bảo chất lượng.

## Assumptions & Limitations
- Điều kiện: cần có dữ liệu hành vi người dùng thật (anonymized behavior records); không áp dụng nếu không có dữ liệu hành vi.
- Paper thừa nhận: evaluation trên các benchmark cụ thể (VelaBench, PurchaseIntent, etc.); có thể khác trên các tác vụ khác.
- Limitation paper không nói: chưa đánh giá trên nhiều domen ngoài khuyến nghị và trợ lý cá nhân, chưa test chi phí huấn luyện thực tế.

## Metadata
- Năm: 2026
- Tác giả: AllSpark Team
- Category arXiv: cs.AI
- Link PDF: https://arxiv.org/pdf/2610.14709
- Code: https://github.com/AllSpark-Research/Vela
