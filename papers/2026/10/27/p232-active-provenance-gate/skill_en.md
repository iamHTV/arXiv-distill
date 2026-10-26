# Skill: Provenance Gate for Multi-Agent Synthesis Verification
Source: 2609.31422
Type: framework / evaluation-method

## When to use this skill
- An agent pipeline synthesizes summaries, messages, or decision reports from multiple sources or debating agents before sending them to customers or operators.
- Groundedness of the output matters more than fluency — customer support, data reports, debate synthesis.
- Do NOT use: creative output that needs no citations (ads, stories); or when you only have a single model and cannot split proposer/validator roles.

## Input required
- Debate transcript or the collected source set (KG/RAG documents, private traces).
- Two models: a cheap model as Proposer (drafts) and a strong reasoning model as Validator (audits) — never the same model for both roles.
- A PF (Provenance Fidelity) threshold, default 0.95; retry budget = 3.

## Steps
1. Freeze the corpus: merge all artifacts (transcript, deduplicated documents, private traces) into one closed corpus with stable addresses; the Proposer may only compress, expose conflict, and deduce logically — no information beyond the corpus.
2. Generate the synthesis: the Proposer (cheap model) drafts under consensus-oriented prompting with no "no-consensus" mode enabled, mimicking pressure to decide.
3. Audit sentence by sentence: the Validator (strong model) runs strict NLI (natural language inference) entailment per sentence against the corpus, returning JSON: verdict, provenance_fidelity = supported sentences / total sentences, list of unsupported sentences.
4. Apply the hard gate: PF >= 0.95 → publish the draft; PF < 0.95 → the FALLBACK NODE generates a correction hint from the failed sentences and the Proposer rewrites (at most 3 times); after 3 failures → hard exit.
5. Emit a Divergence Report on failure: JSON listing unresolved_claims plus inferred conflicting sources behind the deadlock, instead of publishing a fabricated compromise.

## Expected output
- Either a synthesis with PF >= 0.95 (every sentence traceable to the corpus), or a structured JSON Divergence Report an operator can act on immediately (knows which claims are disputed and which sources conflict).

## Example application
- A customer-support agent synthesizes the refund policy from 3 conflicting KB (knowledge base) documents: the draft says "refund within 30 days" but KB A says 14 days → gate fails → the email to the customer reads: "We could not reach a consistent term: source A says 14 days, source B says 30 days — our team will confirm within 24h" instead of a fabricated assertion.

## Gotchas
- Using the same model as Proposer and Validator: the ablation shows 85.6% of unsafe compromises get wrongly validated — always split roles and make the validator stronger.
- Soft prompting ("be honest") is not enough: a programmatic hard gate with an explicit PF number is required, otherwise models still fabricate fluently.
- Retrying more than 3 times: sessions failing after 2 hints enter oscillatory loops — extra retries burn compute without improving PF.
- Metric circularity: PF is computed by an LLM auditor, so verbosity and linguistic bias remain; if possible, validate a small sample with human annotators.
