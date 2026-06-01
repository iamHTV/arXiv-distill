# Skill: Skill Availability & Presentation Granularity cho LLM Agents
Nguồn: 2605.31408v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi design (thiết kế) skill documents cho LLM agents
- Khi quyết định presentation format (định dạng trình bày) cho procedural knowledge
- Khi evaluate (đánh giá) effectiveness (hiệu quả) của skill documentation

## KHÔNG nên dùng khi
- Agents không dùng skill documents
- Task không cần procedural knowledge
- Chỉ cần 1 model — không cần cross-model comparison

## Input cần có
- Task set cần evaluate
- Skill documents ở different abstraction levels
- Model configurations (ít nhất 2 models)
- Evaluation metric: pass rate, task success

## Các bước thực hiện

### Bước 1 — Define Skill Conditions (định nghĩa điều kiện kỹ năng)
1. No skill (baseline)
2. High-abstraction: principles, guidelines
3. Medium-abstraction: structured steps
4. Low-abstraction: detailed checklists
5. With/without worked examples

### Bước 2 — Run Controlled Experiment (chạy thí nghiệm có kiểm soát)
1. Same tasks across all conditions
2. Multiple trials per condition (5+ recommended)
3. Multiple models (2+ recommended)
4. Record: pass rate, task success per cell

### Bước 3 — Analyze Skill Availability Effect (phân tích hiệu ứng)
1. Compare: any skill vs no skill
2. Expected: +18-36 pp improvement
3. This is LARGEST signal — prioritize having skills

### Bước 4 — Analyze Presentation Effect (phân tích hiệu ứng trình bày)
1. Compare: low vs high abstraction
2. Expected: small, uncertain effects (CIs cross zero)
3. Compare: with vs without worked examples
4. Expected: small positive effect (+0.7-1.3 pp)

### Bước 5 — Draw Design Implications (rút ra hàm ý thiết kế)
1. Priority 1: HAVE skill documents (biggest impact)
2. Priority 2: Choose convenient format (presentation doesn't matter much)
3. Priority 3: Add worked examples when convenient (small positive)

## Output mong đợi
- Skill availability effect size per model
- Presentation granularity effect size (small, uncertain)
- Design recommendations: prioritize content over format

## Ví dụ áp dụng
**Tình huống**: Design skill documents cho AI coding assistant. Budget limited — need to prioritize.

**Áp dụng**:
1. Priority 1: Write skill documents for common tasks (biggest impact: +26-36 pp)
2. Format: use natural format — don't invest in converting to checklists
3. Add 1-2 worked examples per skill (small positive: +1-2 pp)
4. Don't over-optimize presentation — effects uncertain, model-dependent

## Lưu ý quan trọng
1. **Skill availability >> presentation**: Having skills matters most. Don't skip skills because format isn't perfect
2. **Presentation effects uncertain**: Low vs high abstraction CIs cross zero. Don't invest heavily in format optimization
3. **Model-dependent**: DeepSeek with thinking mode may be constrained by low-level instructions. Test on your model
4. **Worked examples are optional**: Small positive effect. Include when convenient
5. **30 tasks subset**: Results specific to this subset. Validate on your tasks
6. **Don't over-specify**: Detailed checklists may constrain model's own planning. Balance guidance with flexibility
