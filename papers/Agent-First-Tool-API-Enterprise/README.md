# [2605.10555] Agent-First Tool API: Paradigm Giao diện Ngữ nghĩa cho Hệ thống AI Agent Doanh nghiệp

## Vấn đề
AI agents transition từ research prototypes sang enterprise production systems, nhưng tool interfaces vẫn rooted trong human-oriented CRUD paradigms (paradigm CRUD hướng con người). 5 architectural mismatches (sai lệch kiến trúc): exact-identifier dependence (phụ thuộc định danh chính xác), rendering-oriented responses (phản hồi hướng hiển thị), single-shot interaction assumptions (giả định tương tác một lần), user-equivalent authorization (ủy quyền tương đương người dùng), opaque error semantics (ngữ nghĩa lỗi mờ đục).

## Đóng góp
1. **Six-Verb Semantic Protocol (giao thức ngữ nghĩa sáu động từ)**: Decompose tool interactions thành search, resolve, preview, execute, verify, recover
2. **Normalized Tool Contract (NTC — hợp đồng công cụ chuẩn hóa)**: Structured decision-support metadata — confidence scores, evidence chains, suggested next actions
3. **Dual-layer governance (quy trị hai tầng)**: Static capability policies + dynamic risk escalation

## Phương pháp (tóm tắt cốt lõi)
Agent-First Tool API: (1) Six-Verb Protocol: search (tìm) → resolve (phân giải) → preview (xem trước) → execute (thực thi) → verify (xác minh) → recover (phục hồi); (2) NTC: mỗi tool response chứa structured metadata — confidence, evidence, next actions; (3) Governance: static policies (what tools can do) + dynamic risk (real-time escalation). Validated trên production SaaS: 85 tools, 6 business domains.

## Kết quả chính
- 88% end-to-end task success rate vs 64% CRUD baselines (+37.5%)
- 72.7% reduction in human interventions
- 5.8x improvement in autonomous error recovery
- 85 registered tools across 6 business domains
- Production multi-tenant SaaS platform validated

## Insight có thể áp dụng ngay
1. **Six-Verb Protocol cho tool interactions**: Khi design APIs cho AI agents, use structured protocol: search → resolve → preview → execute → verify → recover. Ví dụ: khi build AI assistant that calls APIs, structure mỗi interaction theo 6 verbs — agents biết exactly what to expect.

2. **NTC: structured metadata trong responses**: Tool responses phải contain confidence scores, evidence chains, suggested next actions. Ví dụ: khi API returns data, include: confidence: 0.85, evidence: [source1, source2], next_actions: ["verify_with_user", "execute"].

3. **Dual-layer governance**: Static policies (what tools can do) + dynamic risk (real-time escalation). Ví dụ: khi deploy AI agent trong enterprise, define static policies (agent can read but not write financial data) + dynamic risk (if agent tries to delete >10 records → escalate to human).

## Giả định & Hạn chế
**Điều kiện để paradigm work:**
- Enterprise APIs can be adapted to Agent-First protocol
- Production SaaS platform available
- Tool registration system

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- Migration cost từ CRUD sang Agent-First
- Tool developer adoption challenges
- Performance overhead của six-verb protocol
- Legacy system compatibility

## Metadata
- Năm: 2026
- Tác giả: Kai Pan
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.10555
- Citation count: [EXTRACTION FAILED]
