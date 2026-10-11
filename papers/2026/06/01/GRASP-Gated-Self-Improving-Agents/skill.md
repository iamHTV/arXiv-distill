# Skill: GRASP — Tự cải thiện Agent Có cổng Nhận thức Hồi quy
Nguồn: 2605.29668
Loại: workflow

## Khi nào dùng skill này
- Khi cần self-improve (tự cải thiện) LLM agents trong structured environments
- Khi accumulate guidance blindly causes regressions
- Khi procedural reliability matters

## KHÔNG nên dùng khi
- Open-ended action spaces
- No verifiable tasks
- No held-out probe available

## Input cần có
- Structured environment with verifiable tasks
- Failed trajectories from agent runs
- Held-out probe episodes
- Skill-writing LLM

## Các bước thực hiện

### Bước 1 — Classify Failures (phân loại lỗi)
1. After each batch, collect failed traces
2. Classify by mechanism-specific failure mode
3. Labels: "date_filter_omitted" not "wrong_answer"
4. Output: failure groups

### Bước 2 — Generate Proposals (tạo đề xuất)
1. Skill-writing model proposes ADD/MODIFY/REMOVE edits
2. Process from largest failure group to smallest
3. Include: failing traces, passing traces, active skills, other failure labels
4. Output: candidate skill edits

### Bước 3 — Validate with Regression Gate (xác minh)
1. Evaluate each candidate on held-out probe
2. Admit only if net improvement under hard regression budget
3. Check: no regression on previously passing examples
4. Output: validated skill edits

### Bước 4 — Update Library (cập nhật thư viện)
1. Apply accepted edits to skill library
2. Bounded library: ADD blocked at capacity unless paired REMOVE
3. Skills: trigger condition, behavioral rule, verification, contrastive example
4. Output: improved skill library

## Output mong đợi
- +48 points on structured tasks (MedAgentBench)
- No regression on previously correct tasks
- Transferable skills across models

## Ví dụ áp dụng
**Tình huống**: AI agent for clinical FHIR tasks. Current: 40.6% accuracy.

**Áp dụng**:
1. Classify: "date_filter_omitted", "wrong_endpoint", "missing_required_field"
2. Propose: skill for date filtering, skill for endpoint selection
3. Validate: test on held-out probe — date filter skill improves +30%, no regression
4. Admit date filter skill, reject others
5. Result: 40.6% → 88.8%

## Lưu ý quan trọng
1. **Validate before accepting**: Don't accumulate blindly. Test each skill
2. **Mechanism-specific labels**: Classify by failure mechanism, not outcome
3. **Hard regression budget**: No regression on previously correct tasks
4. **Frozen transfer**: Stronger model's skills help weaker models
5. **Bounded library**: Manage size with ADD/REMOVE pairing
