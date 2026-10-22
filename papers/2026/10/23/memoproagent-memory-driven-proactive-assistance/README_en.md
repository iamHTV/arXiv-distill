# 2610.22671 MemoProAgent: Memory-Driven Proactive Assistance

## Problem
Proactive assistance (assistance without waiting for an explicit user query) requires the assistant to decide both when to speak and what to say. In the reactive paradigm, memory only supplies content to answer a user query. In the proactive paradigm, memory must also decide whether and when to intervene — the justifying evidence must be mined from a long-horizon personal memory (~618K tokens on average), not handed to the system. Current systems all perform poorly (at most 15% Perfect) because they cannot separate correct content from correct timing.

## Contribution
- MemoProBench: a benchmark for memory-driven proactive assistance (MPA), pairing egocentric video (video from the user's perspective) with year-long, distractor-rich personal memories, human-verified trigger windows (the interval in which an intervention is warranted), and a protocol that scores content and timing jointly.
- MemoProAgent: a plug-and-play harness that changes no model weights, organizing memory into a graph of episodic and semantic memories, with a gate that passes only evidence worth interrupting for, plus a lightweight RL post-training stage that curbs early and repeated firing.
- Results: lifts strict accuracy (Perfect) from below 10% to 37.5% on Qwen3.8-27B and 38% on GPT-5.3-Chat without training; RL post-training reaches 42.4%.

## Method
MemoProBench defines the task: the assistant observes an egocentric video stream V = (v1, v2, ...), has access to long-term memory M, receives no explicit query, and at each timestep t emits r_t = π(M, V_{t-n:t}) ∈ {∅} ∪ A, where ∅ is silence and A is the space of natural-language interventions. An intervention is correct if it fires within its trigger window and its content is faithful to the relevant memory. The primary metric is Perfect (strict accuracy): fire exactly once, in-window, with good content, no early/late/over-trigger.

MemoProAgent harness: at each decision step, the generator follows a two-round agentic loop (observe → retrieve → reason → answer). Memory is organized as a two-layer graph: object-keyed episodic memories and semantic facts. The gate is a single LLM call that reads candidate memories against the observed object, filters out those not worth intervening on, keeps the worthy ones, and refines them into a single clear piece of evidence (or abstains). The RL post-training uses GRPO (group relative policy optimization) with a verifiable binary reward from benchmark annotations: +1 for correct silence and correct timed good reminder, −1 otherwise.

## KNOWLEDGE — Data & Concepts
- MemoProBench has 1,804 data pairs (904 train, 100 dev, 800 eval), each an egocentric video clip from Ego4D plus a ~1-year personal history (~618K tokens, target evidence only ~0.19%).
- All baselines perform poorly (at most 15% Perfect), including frontier models given summarized or retrieval-augmented memory.
- Oracle evidence + timing given: GPT-5.3-Chat reaches 96%; oracle + timing chosen by model: drops to 38%; retrieved evidence + timing given: drops to 15.3%. Content and timing are independently necessary; missing either is catastrophic.
- MemoProAgent harness (no training): Qwen3.8-27B from below 10% to 37.5% (windowed), 33.3% (streaming); GPT-5.3-Chat reaches 38%. RL post-training: Qwen3.8-27B up to 42.4% (windowed), 40.6% (streaming).
- The gate reduces 13.3 points (37.3→24.0); cuts false-trigger rate on negative clips (clips where nothing warrants intervention) from 77.3%/84.0% (RAG) to 15.3% (windowed/streaming).
- Generalization: transferred zero-shot to 100 Epic-Kitchens samples, harness lifts Perfect from at most 11.0 to 41.0 (windowed) and 37.0 (streaming).

## INSIGHT — Mechanism & Why
[Simply dumping long-term memory into context does not help] happens BECAUSE target evidence is only ~0.19% of memory, buried in distractor-rich history, and models dumping everything into context fire almost everywhere (99.9% over-trigger). This means [memory needs structure and a gate to deliver only evidence worth intervening on at the right time, not just more content].
[The gate asks whether memory justifies intervening, not whether it is relevant] happens BECAUSE many retrieved memories, though real, are not a good reason to remind (object may merely co-occur with a past mention, or its open loop may already be resolved). This means [deeper RAG (larger k) increases Hit but causes disproportionate over-triggering, collapsing Perfect — filtering matters more than retrieving more].

## IDEA — Actionable Applications
1. Apply MemoProAgent harness to AI wearable / smart glasses assistant: first step is to organize user history into an episodic-semantic memory graph, add a gate (single LLM call) before feeding evidence to the generator, only remind when evidence is worth interrupting for.
2. Apply binary-reward RL post-training to a proactive assistant generator: first step is to define the reward from trigger-window annotations, use GRPO to curb early and repeated firing.

## WISDOM — General Principle
Principle: In proactive assistance, memory decides both content and timing; missing either is catastrophic, so the solution must filter evidence (deliver only when worth interrupting) rather than just provide more memory. Use when: the assistant needs to intervene proactively without a user query, and has a long, noisy user history. Do NOT use when: the assistant only reacts to explicit queries, or there is no user history data.

## Assumptions & Limitations
- Long-term memories in MemoProBench are synthesized and text-based (rendered caption streams), not real multimodal histories.
- Evaluates task performance, not latency (end-to-end latency depends on hardware, infrastructure, network).
- Each clip contains a single trigger window; multiple triggers per stream not covered.
- Code and evaluation set will be released upon publication.

## Metadata
- Year 2026; authors: Shenglai Zeng, Xiao Yang, Tiffany Ma, Xinyuan Zhang, Nanshu Wang, Deren Lei, Kai Sun, Xilun Chen, Tammy Stark, Xianhui Zhu, Yuetai Li, Rulin Shao, Tianxin Wei, Rakesh Wanga, Anuj Kumar, Jiliang Tang, Wen-tau Yih, Xin Luna Dong (Michigan State University, Meta Reality Labs, Meta Superintelligence Labs, Meta, University of Washington, UIUC); category: cs.CL; PDF: https://arxiv.org/pdf/2610.22671v2; code: https://github.com/facebookresearch/Memo-Pro-Agent; data: https://huggingface.co/datasets/facebook/MemProBench; citation count: [NO DATA — paper 2026-10-21]