# Daily Distill Report 2026-10-20 — Morning batch of 10 papers (#175–#184)

arXiv scan 2026-10-20 morning, high group (scores 82–93). Each paper: What it does / Key result / What you can apply.

### [1] Iterate on an LLM, Serve on an SLM (arXiv 2610.14576v1)
**What:** Design agent behavior on a frontier model by iterating prompts, then distill the converged behavior into a small SLM (Qwen3-8B) using real production data (549 batches, 11,621 training examples). Case study: yes/no classification for caregiver-shift scheduling at a home-care agency.
**Key result:** Fine-tuned Qwen3-8B reaches 91.3% agreement with production traces — HIGHER than the teacher GPT-5.4-nano itself (72.7% self-agreement). Cost drops ~10x ($0.19–0.38 vs $1.9–7.7 per 1,000 decisions), 2.5x faster (2.9s vs 7.1s p50). Professional coordinators approved the student 48 times vs teacher 29 on 77 disagreements.
**Apply:** Prototype behavior prompts on a big model, record real traces, then LoRA-tune a small model for high-volume, repetitive decisions (lead triage, reply suggestion).

### [2] Tool Recommendation for Multi-Step Agents (arXiv 2610.23707v1)
**What:** Instead of stuffing a whole catalog of ~8,200 tools (definitions total ~1.76M tokens — beyond every evaluated model's context window) into the agent, expose only 3 fixed tools (SelectTools, UseTool, ListApps) at a gateway; a 1.2B-parameter system retrieves and re-ranks tools per task.
**Key result:** Completeness@10 45.2% vs BM25 28.8% (+57% relative); Recall@10 55.2 vs 37.0. Total bill drops 13.6% (95% CI 7.4–18.4%, p=0.006), every session cheaper; task completion unchanged (276/327 vs 273/327, p=0.80).
**Apply:** When your agent calls many tools/APIs, don't list them all in context — add a tool-recommendation layer to cut tokens and cost while keeping completion rate.

### [3] TRACER: Trace-Regularized Training Against Indirect Prompt Injection (arXiv 2610.19133v1)
**What:** Channel-aware adversarial training against indirect prompt injection (attackers hide malicious instructions in documents the agent reads): samples attacks from 4 channels (follow-up message, retrieved document/RAG, tool output, other agent message) during training, plus evidence-gated rewards and ATRC trace regularization.
**Key result:** Same payload: attack success rate (ASR) 18% via follow-up vs 53% via retrieved context (+35pp) on models trained only on follow-ups. TRACER on GSM8K with Qwen2.5-3B: RAG-framed ASR 65.5%→6.1%, clean accuracy kept at 78–82%; held-out paraphrase 10.0% vs 62.7% base.
**Apply:** Documents/emails are the most dangerous channel — test safety per channel, not just chat; when building RAG agents, red-team with payloads inserted into retrieved documents.

### [4] Be Careful Who You Trust (arXiv 2609.31704v1)
**What:** Measures LLM multi-agent coordination in a Stag Hunt game under corrupted public communication — separating each agent's private choice, the visible public action, and the executed outcome, so coordination collapse can be mechanical (message corruption) rather than a real behavior change.
**Key result:** N=5 agents, 3 public channels: true success 78% at 80% corruption while public success only 12%; mechanical boundary 1−M/N = 40%; exertion at 60% corruption: 1.702 vs 3.218 under truth. Llama-3.1-8b weakest (~0.62 match rate).
**Apply:** Don't judge multi-agent cooperation from public logs alone — measure private decisions; give critical decisions a private channel.

### [5] Forty Shades of Blue: MODA (arXiv 2609.14896v1)
**What:** MODA, an online post-training RL algorithm jointly optimizing quality and response diversity: mode-conditioning via abstract tokens in a shared policy, each mode a competing MARL agent, plus prompt-conditioned quality gates against reward hacking.
**Key result:** SBERT semantic diversity +265% on Infinite-Chat held-out prompts while general capability +10.3% vs Qwen3-8B base; vs DivPO (strongest baseline): SBERT 0.274→0.482 (+75.9%), E-Vendi 2.86→4.4 (+53.8%). "Name a shade of blue": 40 distinct shades (+122% vs base, +150% vs SSoT); 7 general-capability benchmarks don't degrade.
**Apply:** When LLMs generate content (captions, slogans, product descriptions), actively fight mode collapse — request distinct variants/angles instead of one "best" output.

### [6] Believed but Not Said (arXiv 2610.22138v1)
**What:** Measures hidden belief collapse in multi-agent discussions by tracking each agent's private answer (private probe, hidden from peers) and public stance simultaneously, exposing belief infection never voiced in the transcript.
**Key result:** 1 attacker: final belief infection (FPI) 44.8% average; 3 attackers: 60.5%. Loyal agents privately hold the wrong answer in 51.6% of turns but publicly agree only 19.7% (2.6x gap). ~80% of final infection is present by turn 4. Knowledge doesn't predict robustness: GPT-OSS-120B knows 85% of truths yet ends wrong on 80% of those under 3 attackers.
**Apply:** Multi-agent debate is unsafe against a few sybil attackers — use private probes, cap turns (infection plateaus at turn 4); never treat agent consensus as truth.

### [7] When Debate Helps (arXiv 2610.04686v1)
**What:** Shows multi-agent debate beats majority vote ONLY when BOTH hold: the correct proposal gets surfaced (proposal supply creates recoverable headroom) AND the readout identifies it via verified evidence (LVD — Latent Verification Debate). Symmetric truth-agnostic debate is a martingale null (no positive accuracy drift).
**Key result:** Qwen3-4B: Vanilla Debate 92.69 vs self-consistency@20 91.20; AC-Greedy Debate +1.46 pts (5 seeds). Controlled probe: correct support lifts accuracy 0.325→0.655 at d=3; R0→R3: 76.09%→78.52%.
**Apply:** Debate pays off only with a verifier reading evidence — plain voting adds nothing; use debate when you need diverse candidates plus verification, not for every task.

### [8] Candidate Supply and Answer Selection (arXiv 2608.25937v2)
**What:** Decomposes the value of LLM judging in multi-agent systems into proposal supply (is the right answer generated, majority or minority?) and the final answer-selection rule (combining vote frequency with judge ranking to rescue minority correct answers).
**Key result:** Single response 39.88% at 1.0x tokens; majority vote 41.06% at 4.96x; open committee 42.20% at 10.73x (+1.14pp). Generation-retention gap 13–14pp. When the correct answer is a minority: committee picks the wrong majority 73.25%. Hybrid selection (vote + judge rank, t=2–4): 70.82–70.95% vs majority 63.82% (+7pp). 90–95% of runs finish after 1 round; forcing 6 rounds costs 33–49x tokens with no consistent gain.
**Apply:** With committees/judges: (a) ensure correct candidates are generated first, (b) use hybrid vote+rank selection, (c) stop after 1–2 rounds.

### [9] RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (arXiv 2610.11370v2)
**What:** Combines content retrieval with structure-aware navigation: retrieval (BM25 + dense with gte-modernbert-base) finds "where to look", then guides the agent to the structural subtree (ToC edges extracted with Qwen3-32B) around retrieved passages for selective reading.
**Key result:** Highest accuracy (LLM-judged) on WixQA (6,221 help pages), QASPER (416 NLP papers), FinanceBench (364 SEC reports), EntQABench (2.84M pages): +10.5/+5.0/+4.5 pts vs Agentic Search on WixQA; +12.2–13.3 vs PageIndex on QASPER; FinanceBench +9.3/+8.0/+4.6 vs best baseline. Online cost 5.7–13.3 cents/query (more than Agentic Search 1.3–6.3 cents but more accurate).
**Apply:** For RAG over structured corpora (help centers, product docs, reports): extract ToC/headings to build trees, combine lexical + semantic retrieval, let the agent read selectively along structure — accuracy beats pure agentic search.

### [10] Embedding Surgery (arXiv 2609.05110v1)
**What:** Fixes dense-retrieval ranking errors with minimal, localized updates to document embeddings at query time, guided by feedback (expert annotations, user interactions, LLM pseudo-labels), formulated as a convex quadratic program enforcing ranking constraints while minimizing representation change.
**Key result:** Consistent gains, up to +60.64% relative nDCG@10 (TAS-B on DL-Hard with expert feedback); 4 zero-shot models (Contriever, TAS-B, E5, Snowflake-Arctic Embed), 7 benchmarks (TREC DL'19/'20, DL-Hard, Robust'04, CAsT'19, QSharedRel, MS MARCO Dev).
**Apply:** When retrieval mis-ranks a few specific queries, "surgically" patch embeddings locally from feedback instead of re-finetuning the whole index — lightweight, per-query adaptive.

## WHAT YOU CAN APPLY TODAY

1. **Prototype big, serve small:** design behavior on a frontier model, distill to an SLM — ~10x cheaper, 2.5x faster ([1]). Copy: prototype the prompt on a big model, record real traces, LoRA-tune a 4–8B model for repetitive tasks (lead triage, reply suggestion).
2. **Tool recommendation over static lists:** 3 fixed tools at a gateway, bill −13.6%, same completion ([2]). Copy: give marketing/scheduling agents only 3 tools in context; fetch the rest per task via MCP.
3. **Test safety per channel:** retrieved documents are ~3x more dangerous than chat (ASR 53% vs 18%) ([3]). Copy: red-team RAG agents by inserting malicious instructions into the documents they read, not just chat messages.
4. **Hybrid selection + early stop:** vote + judge-rank rescues minority-correct (+7pts); pure majority picks the wrong answer 73%; stop after 1–2 rounds ([7][8]). Copy: when an LLM judges options, take top-2 by vote then re-rank by a judge; don't run more than 2 rounds.
5. **Private probes for debate:** agents publicly agree while 51.6% privately hold wrong beliefs; 1–3 attackers can collapse the discussion ([6][4]). Copy: collect each agent's private assessment before concluding; never trust "unanimous" agent consensus.

---
Source: scans/2026-10-20.json (05:11 scan) + distill_queue.txt. All numbers from per-paper README.md in papers/2026/10/20/. Licenses remain each paper's original (mostly Apache-2.0/MIT — see per-paper metadata.json).
