# Skill: Gated memory harness for proactive assistance (MemoProAgent)
Source: 2610.22671
Type: framework

## When to use this skill
- AI assistant needs to intervene proactively without a user query (e.g. smart glasses, wearable assistant).
- Has a long, noisy user history and needs to decide when and what to say.
- Do NOT use for assistants that only react to explicit queries, or when no user history data exists.

## Input needed
- User event history (episodic memories + semantic facts).
- Current observation stream (egocentric video or current context).
- A language generator that can call retrieval tools.
- A trigger-window evaluation protocol (when a reminder is warranted).

## Steps
1. Build a two-layer memory graph: object-keyed episodic memories and semantic facts, each memory carrying an open-loop flag (unresolved intention, constraint, or issue).
2. At each decision step, run the agentic loop: observe (identify objects in focus) → retrieve (embed-match to seed entities, pull one-hop episodic/semantic facts, Personalized PageRank on the graph) → gate (single LLM call filtering evidence worth interrupting for, refining into one clear evidence or abstaining) → reason → answer (speak a grounded reminder or stay silent).
3. Only fill the <evidence> slot when the gate confirms intervention is warranted; otherwise leave it empty so silence is the default behavior.
4. (Optional) Post-train the generator with GRPO using a binary reward: +1 for correct silence or correctly timed good reminder, −1 otherwise; mask evidence tokens when computing loss.

## Expected output
- Strict accuracy (Perfect) from below 10% to 37.5% (Qwen3.8-27B) / 38% (GPT-5.3-Chat) without training; RL up to 42.4%.
- False-trigger rate on negative clips reduced from 77.3%/84.0% (RAG) to 15.3%.

## Example application
- Smart glasses assistant observes the user walking past a grocery store: the memory graph recalls the user finished sparkling water yesterday, the gate confirms it's worth reminding when the user is at the store, the generator says "You should restock sparkling water" at the right moment, without firing too early or repeatedly.

## Gotchas
- Benchmark memories are synthesized and text-based, not real multimodal histories — needs adaptation for production deployment.
- Evaluates task performance, not latency.
- Each clip contains a single trigger window; multiple triggers per stream not covered.
- The gate is an additional LLM call, adding cost and latency.