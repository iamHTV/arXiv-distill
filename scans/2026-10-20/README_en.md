# arXiv distill report — 2026-10-20

Summary of 20 papers distilled today (#175–#194), selected from arXiv scan and the continuation queue. Each paper went through the full distill process (6 steps, bilingual, skill check) and was committed+push to GitHub.

## Overview
- Total papers distilled: **20**
- All are [applied] — real experiments, real datasets, concrete benchmarks.

## 20 papers today

### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)
- What it does: Shows a small SLM (fine-tuned on real data) can be more stable than the larger teacher model used to distill it, because the teacher is non-deterministic (agrees with itself only 72.7% of the time) and acts as a noisy annotator, not ground truth. The approach develops behavior in prompt space on a frontier model, then distills into an SLM using real production data.
- What we learn: Don't treat a large model's output as absolute truth; collect real feedback from production and distill into a smaller, cheaper model.
- How to apply: Instead of letting one big AI proofread its own writing, collect customer content that was actually rated highly and use it to train a smaller, cheaper internal model.

### [2] Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs (arXiv 2610.23707v1)
- What it does: Argues completeness@10 matters more than recall@10 for multi-step agents — missing one tool in a chain causes task failure; each extra lookup re-sends the whole conversation, so lookup frequency determines whether recommendation is cheaper than a static tool list (threshold ~0.63 lookups per tool call).
- What we learn: When building multi-step agents, ensure the agent finds ALL needed tools, not just the best tool per step.
- How to apply: When using an agent for multi-step tasks (e.g., check Shopee price → compare → place order), verify the agent has all tools needed for the full chain, not just each step.

### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
- What it does: TRACER reduces indirect prompt injection via RAG (retrieval-augmented generation — find documents, then generate answer) from 65.5% down to 6.1% while keeping 78–82% clean accuracy, using evidence-gated rewards + ATRC trace alignment; multi-channel training (RAG + tools) achieves average ASR 13.9% best at 3B.
- What we learn: When using RAG to retrieve documents, add an evidence check before trusting retrieved content, especially with hidden instructions from outside.
- How to apply: When AI extracts info from customer documents to write a report, have AI quote the source passage and you verify the quote before sending, avoiding hidden instructions in the document tricking the AI.

### [4] Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games (arXiv 2609.31704v1)
- What it does: Coordination collapse in multi-agent games under corrupted communication is mainly mechanical (actions reversed change transcript and execution), not agent behavior; separate original choice / public action / actual execution when evaluating multi-agent strength.
- What we learn: When evaluating a multi-agent system, consider both public actions and actual execution results, not just the transcript.
- How to apply: When using multiple agents together (e.g., one writes, one edits), check the final result sent to the customer, not just the agents saying they are done.

### [5] Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning (arXiv 2609.14896v1)
- What it does: MODA uses role conditioning in shared policy (each mode = competing MARL agent) + prompt-conditioned quality gate to increase SBERT diversity +265% and +75.9% over DivPO, while maintaining/increasing general capability +10.3%.
- What we learn: Adding multiple viewpoints/personas when generating content increases diversity without reducing overall quality.
- How to apply: When using AI to generate multiple captions or headlines, ask AI to write from different angles (customer view, sales view, expert view) for more diverse options.

### [6] Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions (arXiv 2610.22138v1)
- What it does: One opposing agent causes belief collapse 44.8% (three agents 60.5%); hidden contamination (51.6% private documents vs 19.7% public agreement) is 2.6x what the transcript reveals; knowledge does not predict strength; contamination stabilizes at round 4, intervene early.
- What we learn: In multi-agent discussion, hidden errors spread far more than transcripts show, so intervene early before errors stabilize.
- How to apply: When using multiple agents to discuss business decisions, intervene early if discussion goes wrong, don't wait until conclusion stabilizes (then it's too late).

### [7] When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning (arXiv 2610.04686v1)
- What it does: Debate helps when there are surface-level correct proposals (recoverable headroom) AND correct answers can be recognized when voting misses them (LVD evidence verification); neither alone is enough; committees selected via coverage (AC-Greedy/SC-Greedy) generate more additional correct proposals than top-score.
- What we learn: Multi-agent debate works only when combined with generating multiple proposals AND verifying answers, not just counting votes.
- How to apply: When using multiple AIs to brainstorm a decision, ask them to produce several different solutions, then verify each, rather than just counting how many AIs agree.

### [8] Candidate supply and answer selection shape the value of LLM judging in multi-agent systems (arXiv 2608.25937v2)
- What it does: Correct answer is often in the candidate pool but the system still reports it wrong (generate–keep gap 13–14 pp); judge trustworthiness is not fixed; combining vote frequency + judge ranking raises 63.82% to 70.82–70.95%, saving correct answers wrongly dropped by common errors.
- What we learn: Don't trust a single AI judge; combine multiple votes and rankings to pick the best answer.
- How to apply: When using AI to evaluate or rank sales opportunities/projects, have AI evaluate multiple times and rank, rather than trusting one evaluation.

### [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (arXiv 2610.11370v2)
- What it does: RIT-RAG separates evidence discovery from reading content — retrieval ensures recall, retrieval structure ensures accuracy; don't commit to a single document before seeing content; best on WixQA, QASPER, FinanceBench, EntQABench (2.84M pages), +6.6–11.4 points over best baseline.
- What we learn: When using RAG, separate finding documents from reading/reasoning, and don't commit to one document too early.
- How to apply: When researching competitors or market with AI, have AI find many different sources first, then read and synthesize, rather than trusting the first source found.

### [10] Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval (arXiv 2609.05110v1)
- What it does: Embedding surgery applies localized, minimal updates to document embeddings (how machines understand text) at query time via convex optimization (quadratic function optimization), enforcing ranking constraints, minimizing representation change; symmetry works best, up to +60.64% relative nDCG@10 (top-10 search metric) on DL-Hard.
- What we learn: Instead of retraining the whole model, you can locally update the needed representation to improve search ranking at low cost.
- How to apply: When using internal search (e.g., find old products in photo/article library), prioritize updating important parts rather than rebuilding from scratch, saving time and cost.

### [11] MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups (arXiv 2610.23480v1)
- What it does: The harness (tool wrapper), not the model, is the unit of improvement — same harness doubles accuracy on 3 backbones (base models) from 2 developers (0.387→0.874 Qwen3.8-27B); naive top-5 RAG is worse than bare model on all backbones because retrieval without verification loop is net harm; system knows when to abstain (refuse to answer when unsure): removing documents → system refuses 86–92% (Qwen)/80% (gpt-oss) with 0 fabricated citations over 100 fake documents × 3 backbones; reading full text in 1 call beats summarize-then-reason (0.497→0.864).
- What we learn: How you wrap and use the model matters more than the model itself; RAG without verification can be worse than not using it.
- How to apply: When building an internal document assistant, invest in the verification process (AI cites sources and you check them) rather than just picking the biggest model.

### [12] Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows (arXiv 2610.21411v2)
- What it does: Multi-agent workflow coordination only needs bounded decisions — separate "decide" (Jev decision model) from "generate" (LLM expert) cuts 12.7–54.6% tokens (text processing units) with accuracy within ±1.34 points, but the router must see the actual artifact (real output) to keep accuracy (loses 18 points if content-blind — not seeing content).
- What we learn: In multi-agent workflows, use a small cheap model for decisions (routing, evaluation) and only call the large model when generating actual content, cutting big costs.
- How to apply: When building an AI content workflow, use rules or a small model to classify customer messages (complaint / price inquiry / order), and only call the big model to write detailed replies, cutting API cost.

### [13] How language model agents reshape price competition (arXiv 2610.21711v1)
- What it does: Same foundation model can pick completely opposite regimes (0.88 vs 0.05 lift) just by changing deployment interface (information interface: hide rival prices + summarize history), not output type; one strategy captures 71–72% industry profit via fast undercutting, another via anchor-and-harvest; consumer share 15% vs 95%.
- What we learn: How you deploy (what info to show/hide) changes competitive outcome completely, not just which model you use.
- How to apply: When selling on e-commerce, carefully consider what info you display (price, stock, ratings) because it directly affects customer and competitor reactions.

### [14] EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs (arXiv 2610.22412v1)
- What it does: 45 verified trajectories (action sequences) from OpenAPI specs with zero execution (not run for real) lift a 0.5B model from 12.5% to 87.5% on held-out API; verifier must be adversarially tested (57–80% initial → 98%); endpoint accuracy 48.9% but end-to-end (args + values) only 21.3%.
- What we learn: You can generate training data from technical specs (OpenAPI spec — API interface description) without real execution, but must adversarially test to ensure quality.
- How to apply: When you want AI to work with internal software (CRM, accounting), provide detailed function specs and test thoroughly before deploying in production.

### [15] Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents (arXiv 2610.18007v1)
- What it does: Local contract-conditioned rewriting (local Gemma 4B + information-release contract with 4 fields) before checker: leakage 11.41→4.03% normal / 28.19→18.79% attack, remote tokens −17.6%/−36.6%, checker-call amplification 1.69×→1.02×, utility INCREASES (85.2→92.6%) — contract beats generic privacy prompt 36.3–54.1% relative.
- What we learn: Applying an information-release contract (specific fields) before checking reduces data leakage and increases utility better than a generic privacy prompt.
- How to apply: When using AI to write customer email replies, set clear rules about what information must NOT be included (phone number, address, card number) before asking AI to write, instead of just saying "keep it confidential".

### [16] SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV (arXiv 2610.22588v1)
- What it does: SAG2 multi-hop retrieval (multi-hop search) needs no vector database/embedding service — just 1 SQLite FTS5 + BM25 + JEV decision model local: R@10 86.62%/97.43%/99.00% (MuSiQue/2Wiki/HotpotQA), beats all 7B embedding models + SAG +3.25–3.86 points; indexes 11,656 passages in 2.36s/25.87MiB/$0 offline; $4.33 per 1,000 queries.
- What we learn: Multi-hop search doesn't require an expensive vector database; can use text search (FTS5) combined with a small decision model to cut cost.
- How to apply: When needing multi-step lookup in internal documents (e.g., warranty policy then product code), use simple text search combined with rules rather than a complex expensive vector DB.

### [17] Designing for Imperfect Prompts: KG Semantic Mediation for Enterprise Data Assistant (arXiv 2610.23304v1)
- What it does: Enterprise user prompts are extremely short (1–14 sentences/~10 words, 0/158 with schema reference); use knowledge graph (KG — knowledge network) auto-built from schema (273 nodes/540 edges) to mediate prompts: GPT-4.1 precision 90.67% (schema-only 69.05%, +21.62pp), F1 89.47% (71.02%); schema-only hallucinated joins reliably cause downstream execution failure.
- What we learn: When user prompts are short and unstructured, use a knowledge graph auto-built from existing data to mediate and understand intent, better than using raw database schema.
- How to apply: When customers send short requests ("how much", "renew service"), build a simple lookup table from your business data for AI to answer accurately, rather than letting AI guess from raw database structure.

### [18] Asymmetric Dynamic Routing (ADR) for Hypergraph RAG (arXiv 2609.29282v2)
- What it does: "Static retrieval fallacy" — uniform traversal depth for every query wastes tokens (simple queries) + lacks context (complex queries); ADR uses a classifier + 3 asymmetric operators: latency 435→238ms (−45.3%), prompt tokens 3,760→1,929 (−48.7%), quality 82.05→83.91 (+1.86) over DHI baseline; beats every frozen mode on every dataset +0.94–+2.11 points.
- What we learn: Don't use the same retrieval depth for every query; adjust flexibly per query to save tokens and improve quality.
- How to apply: When using AI to look up info, use simple queries (few keywords) for quick lookup and detailed queries (many keywords) for deep lookup, not the same approach for every question.

### [19] MEMORILLA: Latent Semantic Memory for LLMs (arXiv 2610.21375v1)
- What it does: Separates persistent storage from per-query context — uses a fixed embedding model (text representation) to embed corpus once, then trains a small module (194M params) to return K soft memory tokens prepended to the input of a frozen large model (Qwen3-8B) without changing any LLM layer: average 49.68 beats every baseline, Pareto frontier on all 8 benchmarks, token compression 394× over full context (range 20–4,212×, >4,000×), latency 0.74s vs 19.9s. But memory does not help verbatim recall.
- What we learn: You can compress large knowledge into small memory tokens and prepend to input to cut inference cost a lot, but don't use it for remembering exact details.
- How to apply: When you need AI to remember lots of long-term info (customer history, product knowledge), summarize knowledge into short memory tokens and give to AI, rather than sending the full long history every time.

### [20] Can LLMs Fix It Without Code? No-Code Bug Fix Execution Verification (arXiv 2610.11963v1)
- What it does: Execution verification (verify by actually running) of AI-generated no-code fixes in a real Brave browser: apply fix → scripted sanity gate #1 (bug absent) → rollback → sanity gate #2 (bug present) → executor (executor agent) applies fix via GUI in ≤20 steps → deterministic issue-specific checker (DevTools Protocol) decides — the executor's own "DONE" claim is NEVER the verdict. Resolution 49.7% Sonnet 5 / 45.7% OpenCUA / 14.6% Muse Glimmer.
- What we learn: Don't send AI-generated fixes to users before verifying by actually running them; text similarity (BERTScore 0.83 for both classes) completely cannot distinguish working/failing fixes.
- How to apply: When using AI to create processes or fixes for your work (e.g., configure software, write automation scripts), check the actual result on a real machine/browser before applying to customers, don't trust AI saying "done".

## WHAT YOU CAN APPLY TO YOURSELF

Top insights from today's 20 papers, each with an example you can apply right now as a Vietnam solopreneur:

1. **Separate decision-making from content generation:** use rules or a small model to classify customer messages (complaint / price inquiry / order), only call the big AI to write detailed replies → cut API costs (from Jev-LiteMAS).
2. **Don't let one big AI proofread itself:** collect real, highly-rated feedback and use it to train a smaller, cheaper internal model (from Iterate on an LLM, Serve on an SLM).
3. **Don't send AI-generated fixes to customers before testing on a real machine** → avoid false positives and fixes that don't actually work (from No-Code Fix Execution Verification).
4. **When using RAG/document lookup, have AI quote the source passage and you verify the quote before using** to avoid hidden instructions tricking the AI (from TRACER, RIT-RAG, SAG2).
5. **Build a simple lookup table from your business data** for AI to answer short customer requests ("how much", "renew service"), rather than letting AI guess from raw database structure (from Designing for Imperfect Prompts, MEMORILLA).

---

*Auto-generated daily report by watchdog_daily.sh after distilling 20 papers (#175–#194). All papers went through the distill process and were committed+pushed to GitHub.*
