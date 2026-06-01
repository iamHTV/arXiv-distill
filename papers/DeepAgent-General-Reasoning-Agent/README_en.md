# [2510.21618] DeepAgent: A General Reasoning Agent with Scalable Toolsets

## Problem
Large reasoning models have strong problem-solving abilities, but real-world tasks often require external tools and long-horizon interactions. Existing agent frameworks typically follow predefined workflows, limiting autonomous and global task completion. Prior work has no end-to-end deep reasoning agent with autonomous thinking, tool discovery, and action execution in a single coherent reasoning process.

## Contribution
1. **DeepAgent**: End-to-end deep reasoning agent — autonomous thinking, tool discovery, action execution in single reasoning process.
2. **Autonomous memory folding**: Compresses past interactions into structured episodic, working, tool memories — reduces error accumulation while preserving critical information.
3. **ToolPO**: End-to-end RL strategy for tool use — LLM-simulated APIs, tool-call advantage attribution for fine-grained credit assignment.

## Method (core summary)
DeepAgent: (1) Autonomous thinking — agent reasons through problem; (2) Tool discovery — finds appropriate tools dynamically; (3) Action execution — executes actions in single coherent process. Memory folding: agent triggers <fold_thought> token at logical points → auxiliary LLM compresses history into 3 memories: episodic (key events), working (current state), tool (tool interactions). ToolPO: RL training with LLM-simulated APIs, tool-call advantage attribution assigns credit to tool invocation tokens.

## Key Findings
- TMDB: 89.0% vs best baseline 55.0% (+34 pp)
- Spotify: 75.4% vs 52.6% (+22.8 pp)
- ToolBench (open-set): 64.0% vs 54.0% (+10 pp)
- ToolHop: 40.6% vs 29.0% (+11.6 pp)
- GAIA: 53.3 vs 42.5 (best baseline) (+10.8)
- ALFWorld: 91.8% vs 84.3% (+7.5 pp)
- ToolPO improvements: ToolBench +6.0%, Spotify +5.2%
- End-to-end reasoning > workflow-based methods

## Actionable Insights
1. **End-to-end reasoning > predefined workflows**: When building AI agents, don't constrain with rigid workflows. Let agent reason autonomously. Example: customer service agent → don't script conversation flow. Let agent reason through problem dynamically.

2. **Memory folding for long-horizon tasks**: Compress past interactions into structured memories. Reduces error accumulation. Example: when AI agent handles long project, periodically fold memories: episodic (what happened), working (current state), tool (what tools used).

3. **ToolPO for better tool use**: Train agent with tool-call advantage attribution. Better alignment between tool calls and end-task success. Example: when training AI assistant with tools, use RL to align tool usage with task completion, not just tool call accuracy.

## Assumptions & Limitations
**Conditions for method to work:**
- LLM-simulated APIs available for training
- Auxiliary LLM for memory folding
- 8 benchmarks tested

**Limitations the paper acknowledges:**
- [EXTRACTION FAILED: limitation section]

**Limitations the paper does NOT mention:**
- Memory folding quality depends on auxiliary LLM
- ToolPO training compute requirements
- Real-world API simulation fidelity
- Scalability to very large toolsets
- Error handling when tools fail

## Metadata
- Year: 2025
- Authors: Xiaoxi Li, Wenxiang Jiao, Jiarui Jin, et al.
- Category: cs.AI
- PDF: https://arxiv.org/pdf/2510.21618
- Citation count: [EXTRACTION FAILED]
