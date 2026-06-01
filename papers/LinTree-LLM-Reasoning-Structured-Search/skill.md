# Skill: LinTree — Cấu trúc hóa Search History cho LLM Reasoning
Nguồn: 2605.31492v1
Loại: prompt-pattern (khuôn mẫu prompt)

## Khi nào dùng skill này
- Khi design (thiết kế) reasoning prompts cho LLM trên tree-structured problems (bài toán có cấu trúc cây)
- Khi LLM backtrack (quay lui) hoặc explore alternatives (khám phá thay thế) trong reasoning
- Khi cần improve (cải thiện) search efficiency (hiệu quả tìm kiếm) của LLM reasoning

## KHÔNG nên dùng khi
- Task không có tree structure (linear tasks)
- Model quá yếu để utilize structured traces
- Trace length overhead quá lớn so với context window

## Input cần có
- Reasoning task với tree-structured search space
- LLM capable enough để process structured traces
- Format specification (đặc tả định dạng) cho parent pointers

## Các bước thực hiện

### Bước 1 — Define Reasoning Step Format (định dạng bước suy luận)
1. Mỗi reasoning step cần:
   - Step ID (unique)
   - Parent ID (step nào nó branched from)
   - Action/decision content
   - Status (active/abandoned/success)
2. Format: "Step 3 (parent: Step 1): Trying alternative approach X → [status]"

### Bước 2 — Generate Structured Traces (tạo dấu vết có cấu trúc)
1. Khi LLM reason, append parent pointer vào mỗi step
2. Khi backtrack: explicitly state "Abandoning Step 3, returning to Step 1"
3. Khi explore alternative: "From Step 1, trying Step 4 (different from Step 3)"
4. Maintain tree structure visible trong trace

### Bước 3 — Extract Plan from Structured Trace (trích xuất kế hoạch)
1. Follow success path từ root đến solution
2. Parent pointers enable (cho phép) easy path extraction
3. Identify (xác định) which branches succeeded vs failed
4. Output: final solution với reasoning path

### Bước 4 — Optimize Search Efficiency (tối ưu hiệu quả)
1. Parent pointers giúp model avoid revisiting failed branches
2. Model có thể learn từ failures trên other branches
3. Structured history enables better state tracking
4. Result: fewer search expansions, higher solve rate

## Output mong đợi
- Improved solve rate trên tree-structured reasoning tasks
- Fewer search expansions (hiệu quả hơn)
- Clear reasoning path từ root đến solution
- Better plan extraction từ traces

## Ví dụ áp dụng
**Tình huống**: AI assistant giúp debug complex code. Multiple possible causes, cần explore systematically.

**Áp dụng**:
1. Step 1 (parent: root): Checking memory allocation → looks fine
2. Step 2 (parent: Step 1): Checking null pointer → found issue at line 45
3. Step 3 (parent: root): Checking concurrency → no race condition
4. Step 4 (parent: Step 2): Fixing null pointer at line 45 → SUCCESS
5. Structured trace: root → Step 2 → Step 4 (success path extracted)

## Lưu ý quan trọng
1. **Minimal change, big impact**: Chỉ thêm parent pointer field → cải thiện performance. Không cần complex restructuring
2. **Flat traces lose structure**: Sequential "Step 1, Step 2, Step 3" KHÔNG đủ. Phải show branching
3. **Parent pointers enable plan extraction**: Dễ dàng trace back từ solution đến root
4. **Context window overhead**: Parent pointers add tokens. Balance structure vs length
5. **Not for linear tasks**: Nếu task không có branching → parent pointers overhead without benefit
6. **Model must be capable**: Weak models không utilize structured traces → ensure model size sufficient
