# Skill: Terminal Agent cho Enterprise Automation
Nguồn: 2604.00073
Loại: workflow

## Khi nào dùng skill này
- Khi build (xây dựng) enterprise automation agents
- Khi evaluate (đánh giá) agent architectures cho enterprise tasks
- Khi muốn simplify (đơn giản hóa) agent stack

## KHÔNG nên dùng khi
- Platforms không expose APIs
- GUI-only environments (không có terminal access)
- Tasks cần visual understanding

## Input cần có
- Enterprise platform với APIs
- Strong foundation model (Claude, GPT-5, Gemini)
- Sandboxed terminal environment
- Task descriptions

## Các bước thực hiện

### Bước 1 — Setup Terminal Environment (thiết lập môi trường terminal)
1. Sandboxed terminal với filesystem access
2. API credentials cho target platforms
3. Strong foundation model as backbone
4. Output: terminal agent environment

### Bước 2 — Implement Agent (triển khai tác nhân)
1. Coding agent that writes/runs code
2. Interacts directly with platform APIs
3. No GUI interaction needed
4. No predefined tool schemas needed

### Bước 3 — Execute Tasks (thực thi tác vụ)
1. Agent receives natural language task description
2. Discovers APIs dynamically
3. Writes code to complete task
4. Output: task completion

### Bước 4 — Evaluate (đánh giá)
1. Compare: terminal vs web vs MCP agents
2. Metric: success rate, cost
3. Expected: terminal agents competitive or better
4. Output: architecture recommendation

## Output mong đợi
- Competitive success rate with complex architectures
- Lower cost than web agents
- Simpler implementation
- Dynamic API discovery

## Ví dụ áp dụng
**Tình huống**: Enterprise wants to automate IT support tasks.

**Áp dụng**:
1. Setup: terminal agent with ServiceNow API access
2. Task: "Create incident ticket for server outage"
3. Agent: discovers ServiceNow API, writes code, creates ticket
4. Result: task completed, lower cost than web agent scraping GUI

## Lưu ý quan trọng
1. **APIs > GUI**: Expose stable APIs. Terminal agents + APIs > complex stacks
2. **Simple > complex**: Don't over-engineer. Terminal + filesystem enough
3. **Model quality matters**: Invest in better LLM, not complex architecture
4. **Dynamic discovery**: Terminal agents discover APIs on-the-fly
5. **Lower cost**: Terminal agents cheaper than web agents
6. **Platform-specific**: Results on ServiceNow/GitLab/ERPNext. Test on your platforms
