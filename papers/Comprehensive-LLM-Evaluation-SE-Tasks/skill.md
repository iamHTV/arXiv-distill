# Skill: LLM SE Efficiency Evaluation (Đánh giá Hiệu quả LLM cho Kỹ thuật Phần mềm)
Nguồn: 2602.07079
Loại: evaluation-method (phương pháp đánh giá)

## Khi nào dùng skill này
- Khi evaluate (đánh giá) LLMs cho software engineering tasks
- Khi compare (so sánh) models trên efficiency, không chỉ accuracy
- Khi identify (xác định) inefficiency patterns trong AI agents

## KHÔNG nên dùng khi
- Non-SE tasks
- Accuracy-only evaluation sufficient
- No tool call tracking available

## Input cần có
- LLM candidates cần evaluate
- SE tasks (bug fixing, feature dev, refactoring, etc.)
- Automated verification framework
- Cost tracking capability

## Các bước thực hiện

### Bước 1 — Define SE Tasks (định nghĩa tác vụ)
1. Bug fixing: fix code bugs
2. Feature development: implement new features
3. Code refactoring: improve code structure
4. Technical copywriting: write technical docs
5. Research synthesis: synthesize research findings
6. Output: 5 representative tasks

### Bước 2 — Evaluate Quality + Efficiency (đánh giá)
1. Run each model on each task
2. Measure: quality score, completion time, tool calls, cost
3. Output: performance matrix

### Bước 3 — Analyze Efficiency Variance (phân tích)
1. Compare models with same quality scores
2. Compute: speed variance, tool efficiency variance, cost variance
3. Identify: loop inefficiency, inference inefficiency
4. Output: efficiency analysis

### Step 4 — Select Best Model (chọn mô hình tốt nhất)
1. Rank by: quality × efficiency composite score
2. Consider: speed-quality tradeoff
3. Output: model recommendation

## Output mong đợi
- Model ranking by efficiency, not just accuracy
- Identification of inefficiency patterns
- Cost-effective model selection

## Ví dụ áp dụng
**Tình huống**: Choose LLM for code assistant deployment.

**Áp dụng**:
1. Evaluate GPT-5.1, Gemini-3, Deepseek on bug fixing
2. GPT-5.1: 18.8s, 3 tools. Gemini-3: 625s, 917 tools — same score
3. Choose GPT-5.1: 49× more efficient
4. Result: same quality, 49× lower cost

## Lưu ý quan trọng
1. **Efficiency > accuracy**: Same accuracy models có 49× efficiency difference
2. **More tools ≠ better**: No correlation between tool count và success
3. **Loop inefficiency**: Agent repeats tool sequences — needs stopping logic
4. **Inference inefficiency**: Model slow but correct — needs faster model
5. **OpenAI fastest**: Avg 54s, best speed-quality tradeoff
