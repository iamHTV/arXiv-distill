# [2605.29668] GRASP: Bộ đề xuất Kỹ năng Có cổng Nhận thức Hồi quy cho LLM Agents Tự cải thiện

## Vấn đề
LLM agents fail trong operational ways (cách vận hành), không phải conversational ways. Reliability depends trên procedural knowledge (tri thức quy trình) của môi trường. Prior self-improvement methods accumulate natural-language guidance mà không check rằng mỗi item mới preserves (duy trì) behavior đúng trước đó — note fix một trajectory có thể silently regress (hồi quy im lặng) trajectory khác.

## Đóng góp
1. **GRASP**: Gated Regression-Aware Skill Proposer — treats agent improvement như edits to bounded skill library, admitting each candidate only if net improvement trên balanced held-out probe under hard regression budget
2. **Failure-Driven Skill Proposal**: Classify failures by mechanism, generate grouped proposals
3. **Frozen libraries transfer**: Skills from stronger model improve weaker executors — asymmetry no baseline reproduces

## Phương pháp (tóm tắt cốt lõi)
GRASP: (1) After each batch, classify failing traces by mechanism-specific failure mode; (2) Skill-writing model proposes ADD/MODIFY/REMOVE edits for most frequent modes; (3) Each candidate evaluated trên held-out probe — admit only if net improvement under hard regression budget; (4) Skills = structured behavioral instructions: trigger condition, behavioral rule, verification step, contrastive example; (5) Library bounded — ADD blocked at capacity unless paired REMOVE frees slot.

## Kết quả chính
- MedAgentBench: gpt-oss-120b from 40.6% to 88.8% (+48.2 points)
- Exceeds strongest baseline by 21.0 points
- Improves every model by 17.2 to 40.3 points
- Gains from: comparative proposal generation, acceptance gate, hard regression budget
- Frozen libraries transfer: stronger → weaker improves, reverse doesn't
- Skill writing alone without validation = no better than no skills

## Insight có thể áp dụng ngay
1. **Validate before accepting skills**: Don't accumulate guidance blindly. Test each skill trên held-out probe trước khi admit. Ví dụ: when AI agent learns new skill, validate trên previous tasks — nếu regress → reject.

2. **Failure-driven proposals**: Classify failures by mechanism, not outcome. Ví dụ: "date_filter_omitted" not "wrong_answer" — mechanism-specific labels point to corrective actions.

3. **Frozen library transfer**: Skills from stronger model improve weaker ones. Ví dụ: develop skills on GPT-5, deploy on GPT-4.1 — weaker model benefits from stronger model's skills.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Structured environments with verifiable tasks
- FHIR/state-based evaluation
- Held-out probe available

**Hạn chế paper thừa nhận:**
- Benchmark-specific, not clinical correctness
- Validation cost dominant (440 agent calls per batch)
- English-language FHIR only
- Skills need clinician review for clinical deployment

**Hạn paper KHÔNG nói:**
- Open-ended action spaces don't benefit
- Probe size trade-off
- Skill library size management

## Metadata
- Năm: 2026
- Tác giả: Johannes Moll, Jean-Philippe Corbeil, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2605.29668
- GitHub: https://github.com/jomoll/GRASP
- Citation count: [EXTRACTION FAILED]
