# [2601.11044] AgencyBench: Benchmarking Tác nhân Tự động trong Ngữ cảnh Thực tế 1M-Token

## Vấn đề
LLM-based autonomous agents có multifaceted capabilities (khả năng đa diện) contributing substantially đến economic production. Nhưng existing benchmarks focus trên single agentic capability — fail to capture long-horizon real-world scenarios (kịch bản thực tế dài hạn). Reliance trên human-in-the-loop feedback tạo scalability bottleneck (nút thắt cổ chai khả năng mở rộng).

## Đóng góp
1. **AgencyBench**: Comprehensive benchmark từ daily AI usage. 6 core agentic capabilities, 32 real-world scenarios, 138 tasks với specific queries, deliverables, rubrics
2. **Long-horizon tasks**: Average 90 tool calls, 1M tokens, hours of execution time per task
3. **Automated evaluation**: User simulation agent cho iterative feedback + Docker sandbox cho visual/functional rubric-based assessment

## Phương pháp (tóm tắt cốt lõi)
AgencyBench: derive từ daily AI usage. 6 capabilities: tool use, planning, reasoning, memory, self-correction, multi-step execution. 32 scenarios, 138 tasks. Automated: user simulation agent provides feedback, Docker sandbox evaluates rubrics. Evaluate closed-source vs open-source models.

## Kết quả chính
- Closed-source models significantly outperform open-source: 48.4% vs 32.1%
- Significant disparities trong resource efficiency, feedback-driven self-correction, tool-use preferences
- Proprietary models best trong native ecosystems (Claude via Claude-Agent-SDK)
- Open-source models have distinct performance peaks cho specific frameworks
- Average 90 tool calls, 1M tokens per task

## Insight có thể áp dụng ngay
1. **Closed-source > open-source cho agents**: 48.4% vs 32.1% gap. Invest vào best closed-source models cho agent tasks. Ví dụ: when deploying AI agent, choose Claude/GPT over open-source cho better success rate.

2. **Native ecosystem advantage**: Proprietary models perform best trong native SDKs. Ví dụ: when using Claude, use Claude-Agent-SDK. When using GPT, use OpenAI Agents SDK. Don't mix model + foreign framework.

3. **Long-horizon tasks cần 1M tokens**: Real-world agent tasks average 90 tool calls, 1M tokens. Budget accordingly. Ví dụ: when planning agent deployment, budget for 1M tokens per complex task — not 10K.

## Giả định & Hạn chế
**Điều kiện để benchmark work:**
- 32 real-world scenarios representative
- User simulation agent accurate
- Docker sandbox reliable

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- 32 scenarios may not cover all use cases
- Cost of running 1M-token tasks
- Model versions change rapidly
- Framework-specific optimization bias

## Metadata
- Năm: 2026
- Tác giả: Keyu Li, Junhao Shi, Yang Xiao, et al.
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2601.11044
- Citation count: [EXTRACTION FAILED]
