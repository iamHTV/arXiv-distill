# [2510.21618] DeepAgent: Tác nhân Suy luận Tổng hợp với Bộ công cụ Mở rộng

## Vấn đề
Large reasoning models có strong problem-solving abilities, nhưng real-world tasks thường cần external tools và long-horizon interactions (tương tác tầm xa). Existing agent frameworks typically follow predefined workflows (luồng công việc định sẵn), limiting autonomous và global task completion. Prior work chưa có end-to-end deep reasoning agent với autonomous thinking, tool discovery, action execution trong single coherent reasoning process.

## Đóng góp
1. **DeepAgent**: End-to-end deep reasoning agent — autonomous thinking, tool discovery, action execution trong single reasoning process
2. **Autonomous memory folding**: Compresses past interactions thành structured episodic, working, tool memories — reduces error accumulation while preserving critical information
3. **ToolPO**: End-to-end RL strategy cho tool use — LLM-simulated APIs, tool-call advantage attribution cho fine-grained credit assignment

## Phương pháp (tóm tắt cốt lõi)
DeepAgent: (1) Autonomous thinking — agent reasons through problem; (2) Tool discovery — finds appropriate tools dynamically; (3) Action execution — executes actions in single coherent process. Memory folding: agent triggers <fold_thought> token at logical points → auxiliary LLM compresses history into 3 memories: episodic (key events), working (current state), tool (tool interactions). ToolPO: RL training với LLM-simulated APIs, tool-call advantage attribution assigns credit to tool invocation tokens.

## Kết quả chính
- TMDB: 89.0% vs best baseline 55.0% (+34 pp)
- Spotify: 75.4% vs 52.6% (+22.8 pp)
- ToolBench (open-set): 64.0% vs 54.0% (+10 pp)
- ToolHop: 40.6% vs 29.0% (+11.6 pp)
- GAIA: 53.3 vs 42.5 (best baseline) (+10.8)
- ALFWorld: 91.8% vs 84.3% (+7.5 pp)
- ToolPO improvements: ToolBench +6.0%, Spotify +5.2%
- End-to-end reasoning > workflow-based methods

## Insight có thể áp dụng ngay
1. **End-to-end reasoning > predefined workflows**: Khi build AI agents, don't constrain với rigid workflows. Let agent reason autonomously. Ví dụ: customer service agent → don't script conversation flow. Let agent reason through problem dynamically.

2. **Memory folding cho long-horizon tasks**: Compress past interactions into structured memories. Reduces error accumulation. Ví dụ: khi AI agent xử lý long project, periodically fold memories: episodic (what happened), working (current state), tool (what tools used).

3. **ToolPO cho better tool use**: Train agent với tool-call advantage attribution. Better alignment giữa tool calls và end-task success. Ví dụ: when training AI assistant with tools, use RL to align tool usage with task completion, not just tool call accuracy.

## Giả định & Hạn chế
**Điều kiện để method work:**
- LLM-simulated APIs available cho training
- Auxiliary LLM cho memory folding
- 8 benchmarks tested

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED: limitation section]

**Hạn chế paper KHÔNG nói:**
- Memory folding quality depends on auxiliary LLM
- ToolPO training compute requirements
- Real-world API simulation fidelity
- Scalability to very large toolsets
- Error handling when tools fail

## Metadata
- Năm: 2025
- Tác giả: Xiaoxi Li, Wenxiang Jiao, Jiarui Jin, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2510.21618
- Citation count: [EXTRACTION FAILED]
