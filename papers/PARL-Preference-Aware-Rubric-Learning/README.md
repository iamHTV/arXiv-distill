# [2605.31545v1] PARL: Học Tiêu chí Có Sở thích cho Đánh giá Cá nhân hóa

## Vấn đề
LLMs evolve từ general-purpose assistants sang user-centric agents — personalization (cá nhân hóa) become central. Nhưng evaluation of personalized alignment (đánh giá căn chỉnh cá nhân hóa) là critical bottleneck. Existing evaluation methods — automatic metrics, LLM-as-a-judge — fail to capture subjective, user-specific preferences embedded trong long-term interaction histories.

## Đóng góp
1. **Personalized Evaluation as Learning paradigm (paradigm đánh giá cá nhân hóa như học tập)**: Formulate personalized evaluation as learning problem, không phải static judgment. 3 principles: Representativeness, User-Consistency, Discriminativeness
2. **PARL framework**: Preference-Aware Rubric Learning — learns evaluation rubrics từ raw user histories. Self-validation mechanism cho consistency. Discriminative RL objective contrasts user-authored vs model outputs
3. **Results**: High-fidelity rubrics, reliable identification of user-aligned responses, generalize across users/tasks

## Phương pháp (tóm tắt cốt lõi)
PARL: (1) Rubric Induction: learn multi-dimensional evaluation rubrics từ raw user histories — not static prompts; (2) Self-Validation: ensure rubrics consistent with user preferences; (3) Discriminative RL: contrast user-authored responses vs model outputs — capture user-specific decision boundaries. Reference-free: no fixed references needed. Decouples evaluation from generation.

## Kết quả chính
- GT user-level accuracy: PARL achieves highest across 3 personalized text generation tasks
- Discriminative power: clear margin between authentic user responses và AI outputs
- Hand-crafted static prompts inadequate — GT accuracy can be lower than generic baselines
- PARL-0 (without Discriminative Margin Product): no discriminative capability — overly permissive rubrics
- PARL-A và PARL-B: robust discriminative power, high-fidelity rubrics
- Generalizes across users và tasks

## Insight có thể áp dụng ngay
1. **Personalized evaluation cần learning, không phải static judgment**: Dùng user history để learn evaluation criteria. Không rely trên hand-crafted prompts. Ví dụ: khi evaluate AI-generated content cho specific user, learn từ user's past preferences — what they liked, disliked, style preferences.

2. **Discriminative objective là key**: Contrast user-authored vs model outputs. Captures user-specific decision boundaries. Ví dụ: khi train personalized AI assistant, use discriminative RL to distinguish user's authentic style from AI-generated模仿.

3. **Reference-free evaluation**: No fixed references needed. Rubrics learned from user behavior. Ví dụ: khi evaluate personalized email drafts, don't compare to template — learn what this specific user considers good email từ their history.

## Giả định & Hạn chế
**Điều kiện để method work:**
- User behavioral history available
- Sufficient history quality và quantity
- Personalized text generation tasks

**Hạn chế paper thừa nhận:**
- Cold-start scenarios: sparse history → struggle to induce detailed rubrics
- Static preferences assumed — no temporal evolution modeling
- Focused on text generation — multimodal extensions open
- GT user-level accuracy chưa reach 1.0 — inconsistent users still challenging

**Hạn chế paper KHÔNG nói:**
- Privacy concerns with user history data
- Computational cost of rubric learning per user
- Scalability to millions of users
- Cross-domain transferability
- User preference drift over time

## Metadata
- Năm: 2026
- Tác giả: Yilun Qiu, Xiaoyan Zhao, Yang Zhang, et al.
- Category: cs.CL
- Link PDF: https://arxiv.org/pdf/2605.31545v1
- Citation count: [EXTRACTION FAILED]
