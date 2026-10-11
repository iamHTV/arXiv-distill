# [2604.00073] Terminal Agents Đủ cho Tự động hóa Doanh nghiệp

## Vấn đề
Growing interest trong building agents tương tác với digital platforms để execute enterprise tasks. Approaches explored: tool-augmented agents (MCP — Model Context Protocol) và web agents (GUI — giao diện đồ hoạ). Nhưng unclear whether complex agentic systems are necessary given cost và operational overhead. Đơn giản hơn có đủ không?

## Đóng góp
1. **Terminal agents = sufficient**: Coding agent với terminal + filesystem có thể solve enterprise tasks bằng cách interact trực tiếp với platform APIs
2. **Match/outperform complex architectures**: Terminal agents match hoặc outperform MCP-based agents và web agents
3. **Lower cost, less overhead**: Simple programmatic interfaces + strong foundation models = sufficient cho enterprise automation

## Phương pháp (tóm tắt cốt lõi)
Compare 3 paradigms: (1) Web agents (Playwright MCP — browser interaction); (2) Tool-augmented agents (platform-specific MCP servers); (3) Terminal agents (terminal + filesystem, interact directly với APIs). Platforms: ServiceNow, GitLab, ERPNext. Models: Claude Sonnet 4.6, Claude Opus 4.6, GPT-5.4 Thinking, Gemini 3.1 Pro. Metric: success rate (SR). 729 tasks total.

## Kết quả chính
- Terminal agents match/outperform complex architectures
- ServiceNow: terminal agents competitive với web agents
- GitLab: terminal agents competitive
- ERPNext: terminal agents competitive
- Lower cost than web agents
- Avoids brittleness (sự giòn) của GUI interaction
- Avoids expressivity constraints (hạn chế khả năng diễn đạt) của predefined tool schemas

## Insight có thể áp dụng ngay
1. **Expose stable programmable interfaces**: Khi build enterprise platforms, expose stable APIs thay vì thêm abstraction layers. Terminal agents + APIs > complex agent stacks. Ví dụ: khi deploy enterprise automation, invest vào stable APIs thay vì fancy agent frameworks.

2. **Simple > complex cho enterprise**: Coding agent + terminal + filesystem đủ cho most enterprise tasks. Don't over-engineer. Ví dụ: khi automate IT support, simple terminal agent calling APIs > complex MCP-based agent.

3. **Strong foundation models là key**: Terminal agents work vì foundation models đủ mạnh. Invest vào model quality thay vì agent complexity. Ví dụ: khi choose automation approach, spend budget on better LLM thay vì complex agent architecture.

## Giả định & Hạn chế
**Điều kiện để method work:**
- Platforms expose APIs
- Strong foundation models available
- Sandboxed terminal environment

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn chế paper KHÔNG nói:**
- ServiceNow/GitLab/ERPNext specific — may not generalize
- API quality dependency — poor APIs = poor terminal agents
- Long-horizon coordination across platforms not tested
- Human oversight integration not addressed
- Security implications of terminal access

## Metadata
- Năm: 2026
- Tác giả: Patrice Bechard, Orlando Marquez Ayala, et al. (ServiceNow)
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2604.00073
- Citation count: [EXTRACTION FAILED]
