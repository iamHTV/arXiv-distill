# [2602.11780] RELATE: Khung LLM Tăng cường bằng Học tăng cường cho Tạo Văn bản Quảng cáo

## Vấn đề
Các nghiên cứu trước chưa giải quyết được bài toán tạo quảng cáo text hiệu quả vì: hệ thống công nghiệp hiện tại theo paradigm (mô hình) hai giai đoạn — tạo candidate text trước, sau đó align (căn chỉnh) với performance metrics (chỉ số hiệu suất) như CTR (tỷ lệ nhấp chuột). Cách tách rời này dẫn đến misaligned optimization objectives (mục tiêu tối ưu lệch nhau), low funnel efficiency (hiệu suất phễu thấp), và không đạt global optimality (tối ưu toàn cục). Ngoài ra, text fatigue (mệt mỏi văn bản) — lặp lại cùng quảng cáo cho cùng user — làm giảm engagement (tương tác).

## Đóng góp
1. **End-to-end framework (khung đầu cuối)**: Thay vì hai giai đoạn tách rời, RELATE unify (thống nhất) generation (tạo) và objective alignment (căn chỉnh mục tiêu) trong một model duy nhất qua policy learning (học chính sách)
2. **Multi-dimensional reward (phần thưởng đa chiều)**: Joint model (mô hình kết hợp) quality reward (phần thưởng chất lượng), diversity reward (phần thưởng đa dạng), và CTCVR reward (phần thưởng tỷ lệ nhấp-chuyển đổi) với compliance constraints (ràng buộc tuân thủ)
3. **Granularity-aware credit assignment (phân bổ tín hiệu theo độ chi tiết)**: Giải quyết reward sparsity (thưa phần thưởng) và delayed feedback (phản hồi trễ) bằng cách gán reward ở token level (mức ký tự), không chỉ sentence level (mức câu)

## Phương pháp (tóm tắt cốt lõi)
RELATE xây dựng trên LLM, dùng GRPO (Group Relative Policy Optimization — tối ưu chính sách tương đối theo nhóm) để train. Reward gồm 3 phần: (1) Quality reward — structural quality (chất lượng cấu trúc: length, format) + semantic quality (chất lượng ngữ nghĩa: correctness — đúng đắn, relevance — liên quan, risk-control — kiểm soát rủi ro); (2) Diversity reward — chống text fatigue bằng cách reward quảng cáo khác biệt; (3) CTCVR reward — conversion-oriented metrics (chỉ số hướng chuyển đổi) trực tiếp từ online feedback. Credit assignment strategy (chiến lược phân bổ tín hiệu): diversity và semantic quality constraints được attribute (gán) ở token level, trong khi structural quality và CTCVR ở sentence level.

## Kết quả chính
- Online deployment (triển khai thực tế): +9.19% CTCVR so với production baseline (cơ sở sản xuất)
- Compliance (tuân thủ): cải thiện so với cả production system và SFT baseline (cơ sở fine-tune có giám sát)
- Diversity (đa dạng): đáng kể cao hơn baselines
- Ablation study (kiểm nghiệm thành phần): Model 1 (structural quality only) → Model 2 (+CTCVR) → Model 3 (+diversity) → Model 4 (+semantic quality) → RELATE (+credit assignment). Credit assignment cải thiện rõ rệt
- Human evaluation (đánh giá bởi người): RELATE vượt baselines trên fluency (mượt mà), relevance (liên quan), attractiveness (thu hút)

## Insight có thể áp dụng ngay
1. **Unify generation và optimization**: Thay vì tạo content rồi optimize riêng, hãy integrate business objectives trực tiếp vào quá trình tạo. Ví dụ: khi AI viết email marketing, không chỉ optimize cho open rate mà integrate conversion goal vào generation process — model sẽ tạo email hướng đến chuyển đổi, không chỉ mở.

2. **Multi-dimensional reward cho content**: Chỉ optimize một metric (như CTR) là không đủ. Cần joint reward: quality + diversity + business outcome. Ví dụ: KPI cho content team — không chỉ engagement rate mà còn brand consistency (chất lượng), content variety (đa dạng), và conversion (chuyển đổi).

3. **Credit assignment ở granularity phù hợp**: Gán reward ở level chi tiết phù hợp — semantic constraints ở token level, business metrics ở sentence level. Ví dụ: khi đánh giá AI viết quảng cáo, check grammar/relevance từng câu (token level), nhưng check conversion effectiveness ở toàn bộ quảng cáo (sentence level).

## Giả định & Hạn chế
**Điều kiện để phương pháp work:**
- Cần online feedback data (CTR, CTCVR logs) từ production system
- Cần compliance rules (quy tắc tuân thủ) rõ ràng để tạo risk-control reward
- Cần đủ scale (quy mô) — paper dùng large-scale industrial datasets từ Baidu

**Hạn chế paper thừa nhận:**
- Future work: explore richer reward designs (thiết kế phần thưởng phong phú hơn) như semantic diversity rewards
- Future work: more fine-grained credit assignment strategies (chiến lược phân bổ tín hiệu chi tiết hơn)

**Hạn chế paper KHÔNG nói:**
- Không discuss cold start problem (bài toán khởi đầu) — model cần đủ historical data để train
- Không address multi-platform (đa nền tảng) — chỉ test trên Baidu's platform
- Không compare cost-effectiveness (hiệu quả chi phí) của RL training vs simpler approaches
- Không discuss latency (độ trễ) — end-to-end RL có slower inference không?
- Dependency (phụ thuộc) vào quality of reward model — nếu reward model sai → policy sai

## Metadata
- Năm: 2026
- Tác giả: Jinfang Wang, Jiajie Liu, Jianwei Wu, Ziqin Luo, Zhen Chen, Chunlei Li, Biao Han, Tao Deng, Yi Li, Shuanglong Li, Lin Liu (Baidu Inc.)
- Category: cs.CL, cs.AI
- Link PDF: https://arxiv.org/pdf/2602.11780
- Citation count: [EXTRACTION FAILED]
