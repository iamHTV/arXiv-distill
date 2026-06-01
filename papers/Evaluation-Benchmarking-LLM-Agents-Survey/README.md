# [2507.21504] Đánh giá và Benchmarking LLM Agents: Khảo sát

## Vấn đề
LLM-based agents đã mở ra frontiers mới trong AI applications, nhưng evaluating (đánh giá) these agents remains complex và underdeveloped. Landscape of agent evaluation bị fragmented (phân mảnh). Enterprise-specific challenges (thách thức cụ thể doanh nghiệp) thường overlooked — role-based access, reliability guarantees, dynamic interactions, compliance.

## Đóng góp
1. **Two-dimensional taxonomy (phân loại hai chiều)**: (1) Evaluation Objectives — WHAT to evaluate: behavior, capabilities, reliability, safety. (2) Evaluation Process — HOW to evaluate: interaction modes, data, metrics, tooling
2. **Enterprise-specific challenges**: Role-based access, reliability guarantees, dynamic long-horizon interactions, compliance
3. **Future directions**: Holistic frameworks, realistic settings, automated evaluation, cost-bounded protocols

## Phương pháp (tóm tắt cốt lõi)
Survey taxonomy: Evaluation Objectives (4 categories): Agent Behavior (task completion, output quality), Agent Capabilities (tool use, planning, reasoning, memory, multi-agent), Reliability (consistency, robustness), Safety & Alignment (fairness, compliance, security). Evaluation Process (4 categories): Interaction Mode (static vs interactive), Evaluation Data (synthetic vs real-world), Metrics Computation (quantitative vs qualitative), Evaluation Tooling (instrumentation, leaderboards).

## Kết quả chính
- [SURVEY] — no new experiments, taxonomy + synthesis
- 4 evaluation objectives: behavior, capabilities, reliability, safety
- 4 evaluation process dimensions: interaction, data, metrics, tooling
- Enterprise challenges: role-based access, reliability, compliance
- 4 future directions: holistic, realistic, automated, cost-bounded

## Insight có thể áp dụng ngay
1. **Evaluate across multiple dimensions**: Don't just measure task success. Evaluate behavior, capabilities, reliability, safety simultaneously. Ví dụ: khi deploy AI agent, evaluate: task completion (behavior), tool use quality (capabilities), consistency (reliability), bias/fairness (safety).

2. **Enterprise challenges matter**: Role-based access, compliance, data security — often overlooked nhưng critical cho deployment. Ví dụ: khi deploy AI agent trong enterprise, ensure: role-based data access, audit trails, compliance logging, error handling.

3. **Automated evaluation reduces cost**: LLM-as-a-judge, Agent-as-a-judge — reduce human effort. Ví dụ: khi evaluate AI agent performance at scale, use LLM judge thay vì human review cho routine evaluations.

## Giả định & Hạn chế
**Điều kiện để survey work:**
- Comprehensive literature review
- Taxonomy must capture key dimensions

**Hạn chế paper thừa nhận:**
- Fragmented landscape — may miss some evaluation approaches
- Enterprise challenges underexplored in current research

**Hạn chế paper KHÔNG nói:**
- Survey scope may miss emerging evaluation methods
- Taxonomy may not capture all nuances
- No empirical comparison of evaluation methods
- Enterprise challenges described but not solved

## Metadata
- Năm: 2025
- Tác giả: Mahmoud Mohammadi, Yipeng Li, Jane Lo, Wendy Yip
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2507.21504
- Citation count: [EXTRACTION FAILED]
