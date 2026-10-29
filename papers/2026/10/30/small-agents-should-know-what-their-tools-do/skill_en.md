# Skill: effect-typed-tool-agent-training (train tool-calling agents with effect declarations)

Source: 2610.35981v1
Type: framework / workflow

## When to use this skill

- You are building a small open language model (≤4B parameters) that calls external tools (API, email, calendar, orders) and want it to call fewer tools and act more safely.
- You want the agent to know what each call does to the world (delete, send, modify, read-only) instead of only checking call syntax.
- You have public tool-calling training data (Nemotron-Agentic, Hermes, ToolACE…) and want to avoid refusal templates teaching the agent not to call tools.

Do NOT use this skill when:
- The agent only retrieves read-only information and has no state-changing actions.
- The agent is a large frontier model (>70B) that already calls tools reliably; no token optimization needed.

## Input needed

- List of tools the agent will call, each with: name, description, parameters, effect type (pure/read/write/destructive), idempotence flag, and footprint (resources read/written).
- System prompt with the 5 policies: confirm before irreversible actions; never repeat non-idempotent writes; read current state before modifying; ask when required information is missing; do not call tools when none is needed.
- Tool-calling training data (can combine EffectWorld data and public data filtered for refusal templates).
- Small backbone model (e.g. Qwen3-4B, Qwen3-1.7B, Phi-4-mini, Falcon3-3B) and a LoRA training environment.

## Steps to execute

1. Declare effects for each tool: assign effect type (pure, read, write, destructive), idempotence flag, and read/write footprint. Write the declaration into the tool schema, in MCP (Model Context Protocol — standard for connecting agents to tools) annotation style.
2. Write the system prompt with the 5 effect policies: confirm before destructive actions; never repeat non-idempotent writes; read before writing; ask when information is missing; do not call when no tool fits.
3. Prepare training data: generate gold traces (optimal call sequences) and naive traces (correct but wasteful) from task generators; use the trace optimizer to remove unnecessary calls (redundant reads, dead calls, batching, scheduling).
4. Filter public data: remove turns with templated refusal phrases (e.g. "I don't have access to a tool that can do that"); cap first-turn no-call examples at 5% per source.
5. Train a LoRA adapter (low-rank adapter) on the backbone model using SFT (supervised fine-tuning) on the filtered data, two epochs.
6. Evaluate the agent on real tasks: count task success, unconfirmed destructive calls, output tokens, and number of calls.

## Expected output

- The agent calls fewer tools (about one-third of the output tokens versus the base model).
- High task success (99% in distribution, 81% on the hard split, 83% on unseen domains like online shopping).
- No unconfirmed destructive calls (effect-safe trace).
- The agent does not call tools when the request is irrelevant (irrelevance detection).

## Example application

A solopreneur builds an online order-processing agent: the agent needs to find products, add to cart, place an order (irreversible), and cancel orders. Apply the skill: declare "place order" as destructive, idempotent=false; "get product" as pure; "add to cart" as write, idempotent=false. The system prompt requires confirmation before placing an order, reading the cart before changing it, and not calling any tool when the user only asks for price. Train a LoRA on EffectWorld data plus public data filtered for refusals. Result: the agent places orders only after user confirmation, does not repeat orders, and reduces output by 2/3 compared to unoptimized.

## Gotchas

- Refusal templates in public data can teach the agent not to call tools, dropping BFCL non-live accuracy from 88.0 to 31.4 — filter them before training.
- Negative examples do not substitute for positives: unlikelihood, NPO, DPO on negatives do not beat the SFT control on any held-out split; they mainly change how readily the model calls.
- Confirmation-before-destructive does not transfer well to unseen tools: on the commerce split, adapters make 24–37 unconfirmed destructive calls versus 7 for the base model.
- EffectWorld is small (9 task kinds, one training domain); results may differ on agents larger than 4B parameters or real data outside simulation.
- The replay verifier checks by replaying recorded traces, not by proving for all possible states.