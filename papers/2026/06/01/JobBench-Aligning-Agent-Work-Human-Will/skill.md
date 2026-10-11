# Skill: Delegation Readiness Assessment (Đánh giá Sẵn sàng Delegation)
Nguồn: 2605.26329v1
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi evaluate (đánh giá) AI readiness cho workplace automation (tự động hóa nơi làm việc)
- Khi prioritize (ưu tiên) tasks để automate dựa trên worker delegation desire (mong muốn delegation của workers)
- Khi design (thiết kế) AI agent evaluation framework (khung đánh giá tác nhân AI)

## KHÔNG nên dùng khi
- Chỉ cần economic cost-benefit analysis (phân tích lợi ích chi phí)
- Tasks không phải knowledge work (công việc tri thức)
- Không có access (truy cập) đến worker feedback

## Input cần có
- Worker survey data: delegation desire ratings per work duty
- Task descriptions với heterogeneous reference materials
- Evaluation rubrics: fact-anchored binary criteria
- AI models/agents cần evaluate

## Các bước thực hiện

### Bước 1 — Survey Worker Delegation Desire (khảo sát mong muốn delegation)
1. Survey workers trong target occupations
2. Rate mỗi work duty: delegation desire (1-5 scale)
3. Identify (xác định) tasks workers WANT delegated AND spend most time on
4. Prioritize tasks với: high delegation desire + high time spent
5. Output: prioritized task list

### Bước 2 — Build Heterogeneous Workspaces (xây dựng không gian làm việc đa dạng)
1. Với mỗi prioritized task, collect reference materials:
   - Multiple data sources (CSVs, documents, reports)
   - Conflicting information (thông tin mâu thuẫn)
   - Cluttered formats (định dạng lộn xộn)
2. Package task = workspace với all reference files
3. Include (bao gồm) noise — irrelevant files, outdated data
4. Output: task workspace packages

### Bước 3 — Design Fact-Anchored Rubric Chains (thiết kế chuỗi tiêu chí)
1. Define rubric chain per task:
   - Step 1: Sources located? (binary)
   - Step 2: Data reconciled? (binary)
   - Step 3: Analysis sound? (binary)
   - Step 4: Conclusion supported? (binary)
2. Average 35+ binary criteria per task
3. Award credit ONLY when EVERY step holds
4. Output: rubric chains per task

### Step 4 — Evaluate AI Agents (đánh giá tác nhân AI)
1. Deploy AI agents on task workspaces
2. Record: outputs, tool calls, runtime, trajectory
3. Grade bằng rubric chains
4. Compare across models/scaffolds
5. Output: agent performance scores

### Bước 5 — Analyze Gaps & Act (phân tích khoảng cách & hành động)
1. Identify tasks where agents score highest → delegate first
2. Identify tasks where agents score lowest → keep human, improve agent
3. Compare: agent capability vs worker delegation desire
4. Prioritize automation theo: high delegation desire + high agent capability
5. Output: delegation roadmap

## Output mong đợi
- Worker delegation desire rankings per occupation
- Agent performance scores per task
- Delegation readiness matrix: tasks ranked by desire × capability
- Prioritized automation roadmap

## Ví dụ áp dụng
**Tình huống**: Company muốn automate knowledge work. 50 workers trong 10 occupations. Muốn biết tasks nào delegate cho AI trước.

**Áp dụng**:
1. Survey: workers rate delegation desire cho 200 work duties
2. Top desire: data reconciliation (4.8/5), report generation (4.5/5), fact-checking (4.7/5)
3. Build workspaces: mỗi task với heterogeneous reference files
4. Evaluate: AI agent scores 45% trên data reconciliation, 60% trên report generation
5. Delegate: report generation trước (high desire + decent capability). Data reconciliation cần improvement (high desire nhưng low capability)

## Lưu ý quan trọng
1. **Worker desire ≠ economic value**: Tasks economically valuable nhất có thể không phải tasks workers MUỐN delegate. Survey workers, không chỉ economists
2. **Heterogeneous workspaces là key**: Real work có cluttered, conflicting data. Clean inputs không represent real capability
3. **Rubric chains prevent gaming**: Binary criteria per step → agents can't fake quality. EVERY step must hold
4. **Current agents weak**: Even strongest (Claude Opus 4.7) chỉ 45.9%. Don't overestimate AI capability
5. **GDPVal saturation misleading**: GDPVal 83% ≠ real capability. JobBench 38.9% = more realistic
6. **U.S.-centric limitation**: Survey data U.S. only. Worker preferences có thể khác ở other countries
