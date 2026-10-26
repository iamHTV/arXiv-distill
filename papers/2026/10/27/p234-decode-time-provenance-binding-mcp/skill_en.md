# Skill: Decode-Time Provenance Binding for Tool-Using Agents
Source: 2610.31974
Type: framework / defense-implementation

## When to use this skill
- An agent pipeline calls tools via MCP (Model Context Protocol) or equivalent, where some tools "decode" content (OCR, metadata extractors, Base64/zip parsers, web scrapers, image analyzers) and the pipeline has side-effecting critical sinks (send email, write files, payment APIs, export secrets).
- Multi-agent settings: workers relay outputs before acting, so labels must survive handoffs.
- Do NOT use: chat-only agents with no sinks; or third-party closed agent frameworks where you cannot inject tool-call middleware.

## Input required
- The agent's tool list, split into D (decode tools — those reversing a concealment transform: OCR, stego/metadata extractors, Base64 decoders, file parsers) and C (critical tools — side-effecting sinks).
- An MCP layer (or middleware proxy) you control, holding the signing key k (the key never leaves the layer).
- An in-memory ledger: a binding store (ID -> signed record) plus a per-context taint set.
- An audited trusted-promotion policy for legitimately decoded values (e.g. an OCR'd invoice that may be used).

## Steps
1. Register allow-lists at tool registration: assign every tool to D or C (short, reviewed lists — never classify at runtime). A missing decoder in D leaks; an over-broad one false-blocks.
2. MintBinding at tool return (inside the tool handler): binding l = (payload p, tool t, label tau, provenance pi, dependency IDs delta, signature sigma); tau = Untrusted if t in D or any input is Untrusted (contagious); delta is resolved by the LAYER from handles it issued (never from agent claims); sigma = HMAC_k(canonical(l)); if tau = Untrusted, add the ID to the context taint set; return only an opaque handle id(l) to the agent — the agent never sees the key or edits the ledger.
3. Carry bindings with tool results across every hop: inter-agent messages are also mediated through the layer, which re-binds them to their source and propagates taint to the destination context.
4. EnforceCritical before every call in C: resolve handles via the ledger into a dependency closure S; BLOCK if sigma fails HMAC recomputation (forged/stripped), if tau = Untrusted appears in S, if a dependency is unresolved in the ledger, or if taint(context) minus promoted(context) is non-empty; ALLOW if clean. Never read agent-presented labels — only the lineage the layer recorded.
5. Audited trusted promotion: when a legitimately decoded value must drive a critical action (e.g. an OCR'd invoice number), explicitly re-label that specific value Trusted under human/policy authorization, logging the clearance alongside the original binding.

## Expected output
- Critical calls execute only when the transitive lineage (data + context) is fully Trusted, bindings verify against the HMAC, and any promotion is logged; everything else is blocked — 0% attack success on an adaptive payload bank (per paper: 100% undefended -> 0%), 0 false blocks with promotion, overhead ~17 us per call (0.16% of a decode round-trip).

## Example application
- A support agent reads an image of a customer's credit card: OCR is a tool in D -> the card number is minted Untrusted; the agent drafts a confirmation email (critical send_email in C): EnforceCritical sees the Untrusted lineage and blocks; a human approves via a promotion UI (logged) -> the card value becomes Trusted -> send_email allowed. An attacker embedding an instruction in a signature logo decodes it, it relays to the orchestrator, and the critical call is blocked even if the agent attaches a forged Trusted label.

## Gotchas
- Contain is not detect: you do NOT detect that an image carries a payload — the payload still decodes into the agent's context and can skew summary prose; the defense only blocks it from reaching sinks. If you also need safe summaries, add separate taint/output checks (paper leaves this to future work).
- An agent paraphrasing an instruction into free text on an unmediated channel (personal Slack DM, notes) escapes taint recording — ensure ALL inter-agent communication flows through mediated layer channels.
- Cross-host/cross-domain relays: a shared-key HMAC needs a secured channel, or switch to public-key signatures (algorithms unchanged).
- An over-broad D causes false blocks (paper: 67% legitimate-task completion without promotion) — the promotion path is mandatory for deployment, not optional.
- High PSNR/SSIM does not prove a carrier looks innocent — but it is irrelevant: the defense blocks whether or not the carrier is visible (containment is independent of carrier quality).
