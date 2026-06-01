# [2507.08616] AgentsNet: Phối hợp và Suy luận Cộng tác trong Multi-Agent LLMs

## Vấn đề
LLMs organized trong multi-agent systems có powerful problem-solving capabilities. Nhưng unclear whether these systems có thể leverage topology (cấu trúc mạng) effectively. Existing benchmarks chỉ cover 2-5 agents — không test scalability (khả năng mở rộng). Cần benchmark đo lường coordination, self-organization, communication trong larger networks.

## Đóng góp
1. **AgentsNet benchmark**: Đo lường ability của multi-agent systems để collaboratively form strategies, self-organize, communicate given network topology
2. **Classical distributed systems problems**: Coloring, Consensus, Leader Election, Matching, Vertex Cover — adapted cho LLM agents
3. **Scalable**: Practically unlimited size — tests up to 100 agents

## Phương pháp (tóm tắt cốt lõi)
AgentsNet: inspired từ distributed systems và graph theory. 5 tasks: Coloring (assign colors, no adjacent same), Consensus (agree on value), Leader Election (choose leader), Matching (pair nodes), Vertex Cover (minimum cover set). Homogeneous networks: agents must agree on basic protocols first. Evaluate frontier LLMs trên different network sizes.

## Kết quả chính
- Claude 3.7 Sonnet: 0.70 AgentsNet score (best)
- Claude 3.5 Haiku: 0.26
- GPT-4.1 mini: 0.45
- Frontier LLMs strong on small networks, fall off at scale
- Consensus easiest (1.00 for Claude 3.7), Vertex Cover hardest (0.40)
- Scaling challenge: performance drops khi network size increases

## Insight có thể áp dụng ngay
1. **Topology matters cho multi-agent**: Khi build multi-agent systems, consider network structure. Agents must agree on protocols first. Ví dụ: khi deploy multi-agent customer service, agents phải agree on communication protocol trước khi collaborate.

2. **Consensus is easiest, coordination is hard**: Models excel at agreeing on values nhưng struggle với complex coordination. Ví dụ: multi-agent pricing — agents dễ agree on market price nhưng khó coordinate competitive strategy.

3. **Scaling challenge**: Strong on small networks, weak at scale. Start small, expand gradually. Ví dụ: khi deploy multi-agent system, start với 5-10 agents, test coordination, then scale.

## Giả định & Hạn chế
**Điều kiện để benchmark work:**
- Homogeneous agents (same model)
- Network topology defined
- Classical distributed systems problems adapted

**Hạn chế paper thừa nhận:**
- [EXTRACTION FAILED]

**Hạn paper KHÔNG nói:**
- Homogeneous agents only — heterogeneous not tested
- Classical problems may not capture real-world coordination
- Communication costs not modeled
- Real-world multi-agent tasks more complex

## Metadata
- Năm: 2025
- Tác giả: Florian Grötschla, Luis Müller, Jan Tönshoff, Mikhail Galkin, Bryan Perozzi
- Category: cs.AI
- Link PDF: https://arxiv.org/pdf/2507.08616
- Citation count: [EXTRACTION FAILED]
