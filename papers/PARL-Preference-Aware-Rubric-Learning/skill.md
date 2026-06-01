# Skill: PARL — Đánh giá Cá nhân hóa qua Học Tiêu chí
Nguồn: 2605.31545v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi evaluate (đánh giá) personalized LLM outputs
- Khi cần learn evaluation criteria từ user history
- Khi static prompts không capture user preferences

## KHÔNG nên dùng khi
- No user behavioral history available
- Cold-start users với sparse history
- Non-personalized evaluation tasks

## Input cần có
- User behavioral history (past interactions, preferences)
- Personalized text generation outputs cần evaluate
- User-authored reference texts (ground truth)

## Các bước thực hiện

### Bước 1 — Collect User History (thu thập lịch sử)
1. Gather user's past interactions, preferences, feedback
2. Include: liked/disliked content, style preferences, decision patterns
3. Ensure sufficient quality và quantity

### Bước 2 — Induce Evaluation Rubrics (tạo tiêu chí đánh giá)
1. Learn multi-dimensional rubrics từ user history
2. Not static prompts — learned criteria
3. Self-validation: ensure rubrics consistent with preferences
4. Output: user-specific evaluation rubrics

### Bước 3 — Apply Discriminative RL (áp dụng RL phân biệt)
1. Contrast user-authored responses vs model outputs
2. Capture user-specific decision boundaries
3. Ensure rubrics distinguish authentic vs AI outputs
4. Output: discriminative rubrics

### Step 4 — Evaluate với Learned Rubrics (đánh giá với tiêu chí đã học)
1. Apply learned rubrics to new personalized outputs
2. Score: user-level accuracy, discriminative margin
3. Identify user-aligned responses
4. Output: personalized evaluation scores

## Output mong đợi
- User-specific evaluation rubrics
- High-fidelity personalized evaluation
- Clear discriminative margin between user and AI outputs
- Generalization across users/tasks

## Ví dụ áp dụng
**Tình huống**: Evaluate AI-generated emails for specific user.

**Áp dụng**:
1. User history: past emails, tone preferences, structure patterns
2. Induce rubrics: "prefers concise openings", "uses formal tone", "includes specific data"
3. Discriminative: contrast user's real emails vs AI-generated
4. Evaluate new AI emails against learned rubrics
5. Result: high-fidelity evaluation aligned with user preferences

## Lưu ý quan trọng
1. **Learning > static prompts**: Hand-crafted prompts inadequate. Learn from user history
2. **Discriminative objective essential**: Without it, rubrics overly permissive
3. **Cold-start limitation**: Sparse history → poor rubrics. Need sufficient data
4. **Static preferences assumed**: User preferences may change over time
5. **Reference-free**: No fixed references needed — rubrics from behavior
6. **Privacy concerns**: User history data sensitive. Handle carefully
