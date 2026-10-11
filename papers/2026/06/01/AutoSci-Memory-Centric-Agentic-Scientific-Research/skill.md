# Skill: AutoSci — Tự động hóa Nghiên cứu Khoa học với Bộ nhớ Lõi
Nguồn: 2605.31468v1
Loại: framework (khung phương pháp)

## Khi nào dùng skill này
- Khi automate (tự động hóa) scientific research lifecycle (vòng đời nghiên cứu khoa học)
- Khi cần persistent memory (bộ nhớ bền vững) across research projects
- Khi build (xây dựng) AI research assistant cho organization

## KHÔNG nên dùng khi
- Task đơn giản, không cần multi-stage lifecycle
- Không có structured data để build memory
- Creative/exploratory work không có clear workflow

## Input cần có
- Research domain (miền nghiên cứu) với literature corpus (kho văn liệu)
- Memory schema (lược đồ bộ nhớ): entities (thực thể), relationships (quan hệ)
- Five-stage workflow definition (định nghĩa quy trình 5 giai đoạn)
- Agent infrastructure (hạ tầng tác nhân): coding, reasoning capabilities
- Feedback channels (kênh phản hồi): user, experiments, reviews

## Các bước thực hiện

### Bước 1 — Setup SciMem (thiết lập bộ nhớ)
1. Define memory schema: Concept, Method, Paper, Idea, Experiment entities
2. Tách Long-Term Knowledge Memory (reusable across projects)
3. Tách Active Research Memory (current project state)
4. Setup memory growth rules: accumulate, consolidate, archive

### Bước 2 — Design SciFlow (thiết kế quy trình)
1. Define 5 stages: Literature → Ideation → Experiment → Writing → Rebuttal
2. Mỗi stage: harness-based skill contract (input, output, verification)
3. Define state transitions giữa stages
4. Setup context passing (truyền ngữ cảnh) giữa stages

### Bước 3 — Build SciDAG Operators (xây dựng toán tử)
1. Identify difficult skills cần augmentation (tăng cường)
2. Build DAG-shaped multi-agent operators:
   - Generate node: create content
   - Review node: evaluate quality
   - Router node: decide continue/retry/branch
3. Store as reusable templates per stage
4. Enable adaptive execution theo quality signals

### Bước 4 — Implement SciEvolve (triển khai tiến hóa)
1. Setup signal collection: user feedback, experiment results, external updates
2. Implement /dream: SciMem evolution (archive stale, consolidate related)
3. Implement /forge: SciFlow evolution (update skills based on feedback)
4. Implement /morph: SciDAG evolution (update templates based on patterns)
5. Version all changes cho auditability (khả năng kiểm toán)

### Bước 5 — Execute & Iterate (thực thi & lặp)
1. Run full lifecycle trên first project
2. Collect feedback signals
3. SciEvolve updates system
4. Run next project với improved system
5. Iterate: system improves over time

## Output mong đợi
- Reviewable paper-level artifacts từ end-to-end research
- Persistent memory growing across projects
- Self-improving research workflow
- Versioned evolution history

## Ví dụ áp dụng
**Tình huống**: Research lab muốn automate market research process.

**Áp dụng**:
1. SciMem: Long-term = industry knowledge, competitor data. Active = current research project
2. SciFlow: Market Understanding → Hypothesis → Testing → Report → Client Feedback
3. SciDAG: Report generation với generate → review → retry nếu quality low
4. SciEvolve: Client feedback → update report templates, refine hypotheses workflow
5. Result: AI assistant conducting market research end-to-end, improving over projects

## Lưu ý quan trọng
1. **Memory schema là foundation**: Define entities và relationships carefully. Bad schema → bad memory → bad research
2. **Five-stage lifecycle is flexible**: Có thể customize stages cho domain cụ thể. Không phải all research fits 5 stages
3. **SciDAG là optional**: Không phải all tasks cần DAG operators. Start simple, add complexity khi needed
4. **SciEvolve cần feedback**: Without feedback signals, system không improve. Setup feedback channels early
5. **Built on general-purpose agents**: Not science-specialized. May need domain-specific adaptations
6. **Evaluation gap**: No standard benchmarks cho full research systems. Rely on case studies
