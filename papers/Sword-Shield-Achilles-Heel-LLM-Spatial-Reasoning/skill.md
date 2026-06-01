# Skill: LLM Spatial Representation Bias — Kiếm, Khiên, Gót chân
Nguồn: 2605.31404v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi design (thiết kế) spatial representations (biểu diễn không gian) cho LLM-based navigation/reasoning systems
- Khi evaluate (đánh giá) linguistic inductive bias (thiên kiến cảm ứng ngôn ngữ) của LLMs
- Khi optimize (tối ưu hóa) text-based spatial representations

## KHÔNG nên dùng khi
- Multimodal systems (images + text) — chỉ text-based
- Non-spatial reasoning tasks
- Real-world noisy environments (chỉ synthetic tested)

## Input cần có
- Spatial reasoning task với topology, geometry, semantics
- Multiple representation formats (text, graph, structured)
- Multiple compression levels
- Model configs ở different scales

## Các bước thực hiện

### Bước 1 — Test Topological Integrity (kiểm tra tính toàn vẹn topo)
1. Represent spatial info với accurate topology
2. Simplify/remove connections → test degradation
3. Expected: topology is sturdy shield — dominates geometry
4. Preserve topology as first-class constraint

### Bước 2 — Test Linguistic Format (kiểm tra định dạng ngôn ngữ)
1. Vary format: natural text, structured, graph notation
2. Vary compression: detailed → compressed
3. Expected: double-edged sword — depends on model size, task
4. Calibrate format to model capacity

### Bước 3 — Test Semantic Correctness (kiểm tra tính đúng đắn ngữ nghĩa)
1. Inject semantic ambiguity: "warehouse A" = multiple locations?
2. Test: incorrect semantic cues derail planning
3. Expected: Achilles' heel — systematic planning failure
4. Ensure semantic disambiguation is mandatory

### Bước 4 — Apply Engineering Guidance (áp dụng hướng dẫn kỹ thuật)
1. Preserve topological integrity — don't simplify connections
2. Calibrate compression to model capacity:
   - Small models → detailed representations
   - Large models → more compression OK
3. Ensure semantic correctness — disambiguate all references
4. Select format task-aware — no single representation fits all

## Output mong đợi
- Identification of which representation factors affect LLM planning
- Engineering guidelines cho text-based spatial representations
- Model-specific recommendations

## Ví dụ áp dụng
**Tình huống**: Build AI route planner cho logistics company. LLM-based.

**Áp dụng**:
1. Topology: preserve accurate road connections — don't simplify
2. Compression: edge deployment (small model) → detailed. Cloud (large) → compressed
3. Semantics: ensure "warehouse A" always = same location. Disambiguate
4. Format: test multiple formats, pick best per model/task
5. Result: robust planning with fewer failures

## Lưu ý quan trọng
1. **Topology > geometry**: Preserve connections over distances. Topological integrity is most important
2. **Semantic correctness is MANDATORY**: Incorrect semantics derails planning systematically. Not optional
3. **Compression calibration**: Smaller models need less compression. Match to capacity
4. **No single representation**: Different tasks/models need different formats. Task-aware selection
5. **Synthetic limitation**: Results from synthetic environments. Validate on real-world
6. **Double-edged sword**: Linguistic format helps OR hurts depending on context. Test carefully
