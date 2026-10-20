# Skill: Local Contract-Conditioned Privacy Enforcement (send-time wrapper for agent actions)
Source: 2610.18007v1
Type: framework / workflow

## When to use this skill
- Your agent sends external messages (email, Slack, CRM updates) after reading private context (mailbox, Notion, user PII).
- You need to reduce privacy leakage AND remote enforcement cost (checker/repair LLM tokens) at the same time.
- You worry about strategic requesters (asking for exact values, raw records, source evidence, "all details" while keeping a legitimate-looking task).
- Do NOT use: actions with no private context (no enforcement needed); deployments that cannot accept fail-closed blocking; low-sensitivity content (MG-only is enough, maybe no checker at all).

## Inputs needed
- A wrappable send boundary: access to where the agent calls the sending tool + ability to block sends + exact-draft-only allowlisting.
- Annotated sensitive items or a policy item list per task type (or must_generalize rules by data type: name/phone/address/salary/health...).
- A local on-prem rewriter (e.g. Gemma 4B quantized via Ollama, temp 0.0, 12k context) — any trusted local editor.
- A Boolean PrivacyChecker (remote or local) + a mechanism to return feedback verbatim to the rewriter.
- Baseline metrics: remote tokens + checker calls + item/secret-level leakage + UsableRate (keep the utility judge separate from the enforcement path).

## Steps
1. Install a send-time wrapper: capture recipient fields + subject + body before delivery; build a normalized email signature; allow sending only the exact draft that passed the enforcement path; a mismatched resend triggers re-inspection (the agent cannot decide whether its own output is checked).
2. Generate an information-release contract from the user instruction + original draft, separating 4 concerns: (a) must_preserve + required_slots (benign task slots to keep), (b) must_generalize + privacy-risk rules (abstract sensitive/confidential/source-specific/reconstructive details), (c) information_shape + safe_output_shape (keep the requested structure: status update, bullet list, next step, high-level range), (d) must_not_add (no hallucinated replacement facts, new values, new commitments, private-source references, unsupported attachments) + safe-substitution guidance (abstract instead of delete when deletion makes the email useless). The contract is a deployable rewrite policy, not an oracle label.
3. Local rewrite: the Gemma-class executor takes original subject/body + contract (+ checker feedback when repairing) -> rewritten subject/body + change summary; minimal edits: preserve communicative purpose, generalize sensitive details, avoid unsupported facts, keep professional tone.
4. Final gate: PrivacyChecker Boolean pass/fail on the rewritten draft; pass -> send the exact checked draft; fail -> verbatim feedback -> local repair (budget: 3 rounds); budget exhausted -> BLOCK (fail closed).
5. Risk-adaptive routing: MG (Gemma-only, no checker) only for low-risk sends when mu*DeltaR_remote > lambda*DeltaL (saved remote cost outweighs expected privacy loss); high-risk or attack-suspected sends -> MG+C (full).
6. Monitor: CostAmp = RemoteTokens(attack)/RemoteTokens(normal) (target <=1.02x); checker-call amplification; item-level + secret-level leakage (exact/paraphrased/reconstructive); UsableRate on the benign task shell; slot retention + semantic drift. Expected: normal leakage ~11.4% -> ~4.0%; attack 28.2% -> 18.8%; remote tokens -17.6% (normal) / -36.6% (attack).

## Expected output
- A fail-closed enforcement pipeline; leakage cut 64.7% (normal) with utility IMPROVED (UsableRate 85.2% -> 92.6%); CostAmp near 1.0x under strategic attack (vs 1.32x baseline); remote token billing -17.6-36.6%; local ~1.1-1.2M Gemma tokens per task set as a separate deployment cost.

## Example application
- A solopreneur's reply agent with access to an order database + user addresses/phones. Wrapper contract: must_preserve order status + delivery date (generalize into a range), must_generalize customer phone/address to "on file", must_not_add new discount commitments. When a customer asks "send exact invoice numbers raw": baseline drafts leak 28.2% -> wrapper 18.8%, average checker calls 1.79 -> 1.02, remote bill -36.6%.

## Gotchas
- Gemma-only is NOT enough for high-risk sends: residual reconstructive leakage (disease names removed but respiratory-monitoring cues remain -> recipient can infer) — the checker is mandatory for sensitive sends.
- Contract failures: wrong task type inference, omitted required slot, over-generalization, preserved unsafe detail -> monitor slot retention (target >=0.97) and drift (<=~0.05).
- A generic "remove private information" prompt is 36-54% weaker in relative terms — do not skip contract fields (required_slots + information_shape especially: removing them -> -27.2% / -52.1% vs -36.3% / -54.1%).
- Checker/feedback loop: feedback must go verbatim to the LOCAL executor, never back to the remote action LLM (that is MB — costing 1.32x under attack).
- Leakage evaluator from the same model family as the checker -> self-preference bias risk; spot-check with humans.
- Extending to Slack/calendar/CRM requires action-specific information-shape constraints — do not copy the email contract as-is.

## Dry run test
- Hypothetical case (support agent, ~50 similar tasks): baseline MB: normal leak 11.4%, usable 85.2%, 8.7M remote tokens, attack leak 28.2%, CostAmp 1.32x, calls 1.69x. Running the skill steps 1-6 (wrapper + 4-field contract + local Gemma + checker with 3-round fail-closed budget): normal 4.0% leak, usable 92.6%, 7.2M tokens (-17.6%); attack 18.8% leak, CostAmp 1.02x, calls 1.02, safe-shell usability 100%, rounds 0.04. Offline replay ablation confirms the contract matters: generic 7.38/32.21 -> contract 4.70/14.77 (-36.3% / -54.1%). Output: fail-closed pipeline with simultaneous privacy + cost + utility gains -> meaningful -> [SKILL VALID].
