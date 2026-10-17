# arXiv Distill — Report

Báo cáo tổng hợp. Mục tiêu: ~300 papers, chất lượng ưu tiên. Hiện tại: 113 papers. 🎉

---

## Paper #1–10: LongTraceRL, Choosing Lens, RELATE, Strategic Foresight, Multi-Agent Marketing, Skill Reuse, Human-Like Attributes, SAE Feature Death, Persona Brand, Augmentation→Reconstruction

## Paper #11–20: Personalized Persuade, Multi-Agent Oracle, DeFi Agents, Recon, JobBench, LinTree, Balanced LoRA, AutoSci, Salesbots, DRIFT

## Paper #21–30: Skill Availability, SCOPE, FiVeD, Sword/Shield/Achilles, LLM Ads, AI Agent Buying, RAMP, AI is Strategy, Less is More, Privacy Recommendations

## Paper #31–49: DeepAgent, Agent Evaluation Survey, PARL, Offline RL Code, ES-CoT, PURE, Terminal Agents, Few-shot Dilemma, A-RAG, Opir Safety, Efficiency Frontier, AgentsNet, SCR, FACTS, Agent-First Tool API, Comprehensive LLM SE Evaluation, AgencyBench, MSIFR, ReMemR1

## Paper #50 — GRASP: Gated Self-Improving Agents (2605.29668) [applied] 🎉
✓ Skill: grasp-gated-self-improvement | Insight: Validate skills before accepting. Hard regression budget. +48 points on MedAgentBench. Frozen libraries transfer: stronger → weaker.

→ Tiếp tục: [YES]

## Paper #51 — Context-CoT: Enhancing Context Learning via High-Quality Reasoning Synthesis (2605.25354) [applied]
✓ Skill: context-cot-data-synthesis | Test: SKILL VALID
✓ Insight: Answer-conditioned CoT DEGRADES performance — hide answers from teacher, use minimal rubric feedback. 4K samples, LoRA → +3.79 points on CL-Bench.

→ Tiếp tục: [YES]

## Paper #52 — Pay for Hints, Not Answers: LLM Shepherding for Cost-Efficient Inference (2601.22132) [applied]
✓ Skill: llm-shepherding-cost-optimization | Test: SKILL VALID
✓ Insight: Request only prefix tokens ("hints") from LLM instead of full response. 42-94% cost reduction, 2.8× better than cascading, cross-domain transfer works.

→ Tiếp tục: [YES]

## Paper #53 — Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies (2605.03596) [applied]
✓ Skill: N/A — benchmark framework
✓ Insight: Best agent (DeepAgent+GLM-5.1) reaches only 60% vs human 80.7%. Bottleneck: cross-file dependency reasoning, heterogeneous file understanding, lineage tracing.

→ Tiếp tục: [YES]

## Paper #54 — Pre-Route: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context (2605.10235) [applied]
✓ Skill: pre-route-rag-lc-routing | Test: SKILL VALID
✓ Insight: LLMs have latent routing ability — structured prompts elicit RAG vs LC decisions proactively. Distill to 1.7B model. Minimal metadata (length+head snippet) sufficient.

→ Tiếp tục: [YES]

## Paper #55 — Multi-Agent Teams Hold Experts Back (2602.01011) [applied]
✓ Skill: N/A — observational/cautionary study
✓ Insight: LLM teams underperform best individual by 6.3-41.1%. Integrative compromise (averaging views) instead of deferring to expert. Trade-off: consensus-seeking helps adversarial robustness.

→ Tiếp tục: [YES]

## Paper #56 — Ocean4Rec: Offline LLM-Derived OCEAN Profiles for Request-Time VOD Reranking (2605.27429) [applied]
✓ Skill: ocean4rec-offline-personality-profiling | Test: SKILL VALID
✓ Insight: Use LLM OFFLINE only for personality profiling, ZERO request-time LLM calls. +61.5% NDCG@20 on LightGCN. OCEAN as auxiliary feature, not standalone.

→ Tiếp tục: [YES]

## Paper #57 — Data-Efficient LLM RL Fine-tuning: DOTS + Rollout Replay (2506.05316) [applied]
✓ Skill: data-efficient-rl-finetuning | Test: SKILL VALID
✓ Insight: Prioritize moderate-difficulty questions + reuse rollouts → 40.7% average training time reduction. 256 reference questions sufficient for difficulty estimation.

→ Tiếp tục: [YES]

## Paper #58 — MSumBench: Multi-dimensional Summarization Evaluation (2506.00549) [applied]
✓ Skill: multi-agent-debate-annotation | Test: SKILL VALID
✓ Insight: Multi-agent debate (Advocate+Skeptic+Adjudicator) improves evaluation quality. LLMs have systematic self-bias when evaluating own outputs.

→ Tiếp tục: [YES]

## Paper #59 — HAGE: RL-Driven Weighted Graph Memory for Agentic Retrieval (2605.09942) [applied]
✓ Skill: hage-weighted-graph-memory | Test: SKILL VALID
✓ Insight: Memory retrieval as query-conditioned graph traversal, not flat vector search. RL-trained edge weights adapt to query intent. Best on LoCoMo long-horizon reasoning.

→ Tiếp tục: [YES]

## Paper #60 — Novelty-based Tree-of-Thought Search for LLM Reasoning (2605.06040) [applied]
✓ Skill: novelty-pruning-tree-of-thought | Test: SKILL VALID
✓ Insight: Novelty-based pruning reduces ToT token cost up to 20×. Many reasoning problems have width <3 — only explore 2-3 truly different approaches.

→ Tiếp tục: [YES]

## Paper #61 — ConsumerSimBench: Can LLMs Think Like Consumers? (2605.17079) [applied]
✓ Skill: N/A — benchmark, cautionary
✓ Insight: Best model covers only 47.8% of real consumer reactions. Technical benchmark strength ≠ consumer intuition. Structured reasoning HURTS prediction.

→ Tiếp tục: [YES]

## Paper #62 — LLM-SAA: LLM-persona Generated Distributions for Decision Making (2602.06357) [applied]
✓ Skill: llm-saa-decision-simulation | Test: SKILL VALID
✓ Insight: LLM-simulated distributions useful for pricing/assortment in low-data regimes. Wasserstein distance misleading — evaluate by decision quality. Persona-sampling improves simulation.

→ Tiếp tục: [YES]

## Paper #63 — Safety Self-Play (SSP): Be Your Own Red Teamer (2601.10589) [applied]
✓ Skill: safety-self-play-alignment | Test: SKILL VALID
✓ Insight: Single LLM as both Attacker+Defender in RL self-play. Lowest ASR + lowest refusal rate. Diversity emerges from adversarial dynamics. UCB replay on failures.

→ Tiếp tục: [YES]

## Paper #64 — OccuBench: Evaluating AI Agents on Real-World Professional Tasks (2604.10866) [applied]
✓ Skill: N/A — benchmark
✓ Insight: No single model dominates all industries. Implicit faults (missing data) harder than explicit errors. Open-source models competitive. Higher reasoning effort +27.5 points.

→ Tiếp tục: [YES]

## Paper #65 — LDKE: Localized and Disentangled Knowledge Editing for Multimodal LLMs (2605.29826) [applied]
✓ Skill: ldke-knowledge-editing | Test: SKILL VALID
✓ Insight: Localize fact-specific layers + disentangle relevant/irrelevant inputs for precise knowledge editing. Solves Causal Misalignment and Feature Entanglement.

→ Tiếp tục: [YES]

## Paper #66 — When Efficiency Backfires: LLM Cascade Attack Vulnerability (2605.17288) [applied]
✓ Skill: cascade-attack-awareness | Test: SKILL VALID
✓ Insight: Cascade systems have expanded attack surface. Adversarial suffixes can simultaneously fool lightweight models AND manipulate routing decisions. Monitor escalation rates.

→ Tiếp tục: [YES]

## Paper #67 — Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows (2610.21411v1) [applied]
✓ Skill: jev-litemas-multi-agent-decision-routing | Test: SKILL VALID
✓ Insight: Thay LLM lớn cho mọi quyết định điều phối bằng decision model nhẹ (Jev), chỉ gọi LLM review khi artifact cần sửa → giảm 12.7–54.6% token, accuracy trong 1.34 điểm.
→ Tiếp tục: [YES]

## Paper #68 — AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows (2609.22951v1) [applied]
✓ Skill: agentrouter-step-level-model-routing | Test: SKILL VALID
✓ Insight: Chỉ dùng frontier model cho bước cần reasoning sâu, dùng model nhỏ cho bước định dạng → giảm 72% chi phí inference, giữ 97.3% chất lượng.
→ Tiếp tục: [YES]

## Paper #69 — StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents (2610.10942v1) [survey/benchmark]
✓ Skill: N/A — benchmark framework
✓ Insight: Agent chưa thay được judgment kinh tế: model tốt nhất đạt 49% vs heuristic 97%; dùng agent làm trợ thủ, không thay thế quyết định định giá/tồn kho.
→ Tiếp tục: [YES]

## Paper #70 — Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return (2609.14758v1) [applied]
✓ Skill: tool-failure-honesty-detection | Test: SKILL VALID
✓ Insight: Bắt agent khai báo công cụ OK/FAILED trước khi trả lời → giảm phản hồi không trung thực từ 14.10% xuống 0.87%, chỉ cần thêm 1 câu prompt.
→ Tiếp tục: [YES]

## Paper #71 — Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows (2610.03010v1) [applied]
✓ Skill: sustainable-agent-design-pareto | Test: SKILL VALID
✓ Insight: Không mặc định multi-agent — MA tốn 6.36× năng lượng, 6.07× thời gian vs non-agentic, chỉ 1/66 cấu hình Pareto-optimal là MA; few-shot mạnh hơn việc thêm agent.
→ Tiếp tục: [YES]

## Paper #72 — Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents (2609.26760v2) [applied]
✓ Skill: harness-learning-reusable-specialist-agents | Test: SKILL VALID
✓ Insight: Thay vì để LLM tái thiết quyết định điều khiển mỗi tác vụ, hãy biến feedback thành code điều khiển tái sử dụng → giảm 76–92% LLM calls, 74–99% chi phí, thành công 44.7–45.3% ngay cả với mô hình 4B.
→ Tiếp tục: [YES]

## Paper #73 — Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation (2609.38660v2) [applied]
✓ Skill: self-evolving-multi-agent-translation | Test: SKILL VALID
✓ Insight: Dùng multi-agent + judge-refiner cập nhật prompt không retrain, tích luỹ memory cấp series → thắng 15/15 hướng Subtitle Arena, giảm penalty 6.9%.
→ Tiếp tục: [YES]

## Paper #74 — CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval (2608.30255v1) [applied]
✓ Skill: co-engagement-multimodal-embedding-ads | Test: SKILL VALID
✓ Insight: Fine-tune embedding trên cặp item cùng tương tác (co-engagement) thay vì nhãn tĩnh → production A/B: +18.958% CTR / +13.12% CVR over text control, đã deploy tại Snap.
→ Tiếp tục: [YES]

## Paper #75 — CEO Arena: Evaluating Long-Horizon Multi-Agent Decision-Making in Competitive Markets (2609.34821v1) [applied]
✓ Skill: ceo-arena-multi-agent-business-competition | Test: SKILL VALID
✓ Insight: Nhiều agent lỗ nhưng có private gain kèm market loss → đoán ảnh hưởng toàn thị trường, không chỉ lời agent riêng lẻ; GPT-6 Astra thắng 66%/24 runs.
→ Tiếp tục: [YES]

## Paper #76 — Harness Engineering in LLM Tool Use via Agent-Native Reusable Tool Primitives (2609.01736v1) [applied]
✓ Skill: heart-tool-use-planner-router-verifier | Test: SKILL VALID
✓ Insight: HEART (Planner-Router-Verifier) + tool primitives tái sử dụng → 84% task completion, 3.8× các mô hình thương mại, giảm chi phí API lên đến 85%, ASR 0.0% chống prompt injection.
→ Tiếp tục: [YES]

## Paper #77 — Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents (2609.25991v1) [applied]
✓ Skill: knowledge-as-skill-3-layer-kb | Test: SKILL VALID
✓ Insight: Tổ chức KB theo 3 lớp (SKILL.md, index.md, YAML), agent tự quyết định khi nào truy xuất → beating RAG trên WixQA (Factuality 0.889, Hallucination 4.5%).
→ Tiếp tục: [YES]

## Paper #78 — Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for Complex Tasks (2610.05750v1) [applied]
✓ Skill: agentic-retrieval-react-loop | Test: SKILL VALID
✓ Insight: Agentic retrieval (ReAct loop) cải thiện nDCG@10 +8.7 điểm nhưng tốn 107.4s và 764K tokens/query → chỉ bật cho truy vấn phức tạp, dùng standard retrieval cho đơn giản.
→ Tiếp tục: [YES]

## Paper #79 — Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows (2609.32917v1) [applied]
✓ Skill: planner-as-router-model-routing | Test: SKILL VALID
✓ Insight: Định tuyến từng subtask đến model tier phù hợp (small/mid/frontier) thay vì frontier cho mọi bước → giảm 44% chi phí, mất 2.9 điểm accuracy; 43% SIMPLE, 57% COMPLEX.
→ Tiếp tục: [YES]

## Paper #80 — A Hybrid Agentic AI Framework for Intelligent Supply Chain Analytics (2609.13561v1) [applied]
✓ Skill: hybrid-agentic-supply-chain-analytics | Test: SKILL VALID
✓ Insight: Reasoning model đạt >90% accuracy vs non-reasoning ~65%; multi-agent coordinator+specialist cho supply chain analytics.
→ Tiếp tục: [YES]

## Paper #81 — Re-ranking and Late Interaction Drive Retrieval Quality (2609.38473v1) [applied]
✓ Skill: rag-retrieval-strategy-comparison | Test: SKILL VALID
✓ Insight: ColBERTv2 late interaction answer rate 99.9%, top-3 gold paper 92.8–94.8% (gấp đôi single-vector); rewriting đơn lẻ không kèm re-ranking làm giảm Hit@3.
→ Tiếp tục: [YES]

## Paper #82 — What LLM Trading Agents Actually Do in Production (2609.05663v1) [applied]
✓ Skill: llm-trading-agents-production-lessons | Test: SKILL VALID
✓ Insight: Agent giao dịch chỉ 41% win rate vs retail 50%, 16.2% vaults lời; giữ vị thế 24h+ có lợi (+0.23%), viết hướng dẫn số cụ thể lời 4.2×.
→ Tiếp tục: [YES]

## Paper #83 — Forms of LLM-Integrated Applications from LLM-Chats to Autonomous AI Agent Systems (2610.11899v1) [survey]
✓ Skill: N/A — taxonomy/survey
✓ Insight: 7 dạng hệ thống kết hợp LLM (chat, custom agent, RAG, workflow, copilot, coding agent, agentic RAG), 4 kích thước cấu trúc, 22 hệ thống minh họa; copilot = router-worker, agent = multi-step AI-planned.
→ Tiếp tục: [YES]

## Paper #84 — Understanding Issues, Causes and Solutions in Open-Source LLM-based Multi-Agent Systems (2610.00905v1) [applied]
✓ Skill: open-source-mas-issues-causes-solutions | Test: SKILL VALID
✓ Insight: Orchestration & Execution là vấn đề lớn nhất (22.0% issues), Workflow Problem là nguyên nhân phổ biến nhất (29.4%), Optimize Workflow là giải pháp phổ biến nhất (26.0%).
→ Tiếp tục: [YES]

## Paper #85 — PILOT Technical Report: Proactive Insight Learner for Online Tree-Experiments (2608.18637v2) [applied]
✓ Skill: pilot-proactive-insight-learner-experiments | Test: SKILL VALID
✓ Insight: Agent tự thiết kế thí nghiệm A/B + guardrails deterministik → +1.40% IPV, search efficiency 53.3%→93.3%, không cần can thiệp con người.
→ Tiếp tục: [YES]

## Paper #86 — Vela: User Behavior as Supervision Sparks LLM Intelligence (2610.14709v1) [applied]
✓ Skill: vela-user-behavior-as-supervision | Test: SKILL VALID
✓ Insight: Dùng real user behavior làm tín hiệu huấn luyện thay vì văn bản tĩnh → +11.5 points VelaBench, +11.2 points user-related OOD, RL sau fine-tuning +7.7 points.
→ Tiếp tục: [YES]

## Paper #87 — Beyond Symmetric Agents: Cognitive Diversity and Multi-Agent Debate in Small Language Models (2609.35875v1) [applied]
✓ Skill: cognitive-diversity-multi-agent-debate | Test: SKILL VALID
✓ Insight: Không coi agent là cùng cấp — đa dạng nhận thức tạo lợi ích; debate chỉ có ích vòng đầu tiên, independent pooling tốt hơn debate (+8.9pp).
→ Tiếp tục: [YES]

## Paper #88 — RAG for Scientific Code Understanding (2609.12190v1) [applied]
✓ Skill: rag-scientific-code-understanding | Test: SKILL VALID
✓ Insight: Mô hình nhỏ (9B) đạt 0.795 trên 100-question benchmark, vượt qua mô hình lớn hơn; tách biệt offline ingestion khỏi online answering để chạy local, bảo mật dữ liệu.
→ Tiếp tục: [YES]

## Paper #89 — SurveyAgent-HKA: A multi-agent framework for scientific survey generation (2609.05938v1) [applied]
✓ Skill: surveyagent-hka-scientific-survey | Test: SKILL VALID
✓ Insight: Human knowledge augmentation cải thiện citation F1 (+3.86% CS, +2.62% Medicine); citation expansion, re-ranking, clustering, few-shot đều quan trọng.
→ Tiếp tục: [YES]

## Paper #90 — STRATA: Self-Maintaining Structured Experience Graphs for Self-Evolving Language Agents (2610.19386v1) [applied]
✓ Skill: strata-self-maintaining-experience-graphs | Test: SKILL VALID
✓ Insight: Tổ chức kinh nghiệm agent thành hệ thống phân cấp (metas→episodes→traces) + cơ chế quên → deletion precision 13.2%→4.8%, churn 28.6%→3.1%, best average score at lowest latency.
→ Tiếp tục: [YES]

## Paper #91 — When "Must" Becomes "Maybe": Erosion of Workflow Constraints in LLM Agent Handoffs (2608.24569v2) [applied]
✓ Skill: workflow-constraint-erosion-agent-handoffs | Test: SKILL VALID
✓ Insight: Ownership deferral gây 76.7% blocker deactivation; full blocker description nâng recognition 6.2%→99.2% và giảm forbidden action 85.2%→0.0%.
→ Tiếp tục: [YES]

## Paper #92 — When Efficiency Backfires: Cascading LLMs Trigger Cascade Failure under Adversarial Attack (2605.17288v1) [applied]
✓ Skill: cascade-attack-awareness | Test: SKILL VALID
✓ Insight: Tấn công đối thủ làm giảm accuracy 84.6%, tăng token cost 148.9%, thời gian 108.9%, attack success rate 81.4%; cascade LLM không an toàn tự động.
→ Tiếp tục: [YES]

## Paper #93 — INFUSE: A Unified Surface Benchmark for Indirect Prompt Injection in Agentic Systems (2610.20776v1) [applied]
✓ Skill: infuse-indirect-prompt-injection-benchmark | Test: SKILL VALID
✓ Insight: Mean attack success 19.6% (LLM-based), 15.4% (heuristic); instructional hardening giảm từ 58.2% xuống 14.3%; Meta-SecAlign giảm ASR-L 55% (8B) và 74% (70B).
→ Tiếp tục: [YES]

## Paper #94 — AdCoEvo: A Co-Evolving Multi-Agent Advertising Delivery System (2610.19454v1) [applied]
✓ Skill: adcoevo-co-evolving-multi-agent-advertising | Test: SKILL VALID
✓ Insight: AdCoEvo tăng ADV 14.02%, giảm CPA 7.07% (vs Rule); Inspector +4.95% ADV, -9.57% CPA; API cost CNY 0.235, 65.59% thấp hơn Gemini-3.1-Flash-Lite.
→ Tiếp tục: [YES]

## Paper #95 — DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration (2609.33403v1) [applied]
✓ Skill: datamagic-declarative-multi-agent-data-videos | Test: SKILL VALID
✓ Insight: DataMagic cải thiện chất lượng video dữ liệu từ 2.13/5 lên 3.89/5 (+83%), tỷ lệ thực thi 48.62%–86.24%→95%+, thời gian tạo từ 39.2→8.0 phút (-79.7%).
→ Tiếp tục: [YES]

## Paper #96 — Chronos Enables Code Agents to Reason over Software Evolution (2610.11578v1) [applied]
✓ Skill: chronos-code-agents-software-evolution | Test: SKILL VALID
✓ Insight: Lịch sử pull requests giúp agent hiểu tại sao code viết như vậy; mean resolution 69.2%→72.9%, SWE-Bench Pro 48.3%→51.7%, useful experience 68%→89%.
→ Tiếp tục: [STOP — 30/30 bài đã distill xong]
## Paper #97 — AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework (2609.30541v1) [applied]
✓ Skill: autoresearch-production-scaffolding | Test: SKILL VALID
✓ Insight: 5 failure mode production scale (infrastructure fragility, memory decay, stagnation, cost asymmetry, metric fixation); scaffold prevent-persist-redirect thành 3 agent; Criticizer chỉ bắn khi plateau (8%/5 iteration) → directive lớn nhất +50bps; Code Fixer single-pass bắt 14 latent bugs.
→ Tiếp tục: [YES]
## Paper #98 — LLM-based User-Product Relevance Evaluation for Dynamic Product Advertising (2610.14550v1) [applied]
✓ Skill: query-free-relevance-judge-pipeline | Test: SKILL VALID
✓ Insight: Nén engagement history bằng SID-grouping + event-stratification → 0.99 Spearman fidelity ở 3.4% cost (giảm 30× LLM calls); guideline mang phần lớn lift (Pro không guideline thua student có guideline); fine-tune nén p95 theo bậc (8,807→1,117ms), prompt-only không nén được long-tail.
→ Tiếp tục: [YES]
## Paper #99 — Structured Pre-generation Elicitation vs Single-shot Prompting (2610.09593v1) [applied]
✓ Skill: pre-generation-elicitation-scaffold | Test: SKILL VALID
✓ Insight: Elicit trước generate (3 clarification Q + posture choice + rationale) → composite quality +32.2% (d=1.02), off-task 34.2%→4.9%; gain tập trung trade-off articulation + strategic coherence, technical specificity KHÔNG cải thiện; self-rating không track quality thật.
→ Tiếp tục: [YES]
## Paper #100 — (When) Should a Software Factory be Lights-off? CRBugBench (2610.13668v1) [applied]
✓ Skill: crbugbench-review-agent-evaluation | Test: SKILL VALID
✓ Insight: Review agent catch 71.9% bugs top-5 (47.7%→71.9% trong 5 tháng model evolution), vẫn miss 20%+ → chưa lights-off; proprietary repo drop 25.5% (cần project context); exploration-nudging prompt +5.8% @1.10× cost hiệu quả hơn multi-agent +4.7% @5.55×.
→ Tiếp tục: [YES]
## Paper #101 — ReST: Scaling Sequence Transformers for Industrial Recommendation Ranking (2609.01240v1) [applied]
✓ Skill: rest-rec-native-transformer-scaling | Test: SKILL VALID
✓ Insight: LLM scaling recipe thất bại ở ranking vì sequence starvation (main loss shortcut qua DLRM branch) + computation asymmetry; rec-native design (DGA gates, RoPE+RoTE temporal, SRN) + asymmetric encoder/decoder + shared-prefix (5.8× train, 20× inference) → online AUC +1.31%, revenue +11.93% trong 50ms P99; MoE +500% params = 0 gain.
→ Tiếp tục: [YES]
## Paper #102 — What Stops a Small Language Model From Driving a Database Agent (2609.21341v1) [applied]
✓ Skill: agent-failure-ledger-taxonomy | Test: SKILL VALID
✓ Insight: 75.7% agent failure đến từ runs ĐÃ invoke tool (transport 36.2% là class lớn nhất, capability chỉ 17.3%) — "model yếu" framing sai; 27/69 stopping turns chứa tool call đúng nhưng nằm trong text channel; 5 server changes (không đụng model/prompt/sampling) move 6 models 6–21 cells/30; uncapped context (262k-token window, 51GB RAM) tạo fake yếu 0/5→5/5.
→ Tiếp tục: [YES]
## Paper #103 — Hybrid Semantic Tool Discovery for Enterprise MCP Gateway: SCOUT (2608.23992v1) [applied]
✓ Skill: scout-mcp-meta-tool-gateway | Test: SKILL VALID
✓ Insight: 2 synthetic meta-tool (tool_search + execute_tool) collapse 2,000-tool catalog thành 1,300 token (0.8% context, giảm 99% từ 140.2k/70.1%) — orchestration nằm hết trong tool description text, không fine-tune, không sửa client (6 clients); hybrid BM25+dense RRF k=60 + 3× over-fetch → Hit@1 84.8%, Hit@5 95.6%, MRR 0.821; dense branch cứu vocabulary gap (Slack query → Teams tool, BM25 = 0 match); authorization enforced BÊN TRONG vector DB; P95 latency 936ms VƯỢT mục tiêu 500ms.
→ Tiếp tục: [YES]
## Paper #104 — When Deep Research Agents Stagnate: Retrieval-Aware Agent Control — RAAC (2608.15191v1) [applied]
✓ Skill: raac-stagnation-controller | Test: SKILL VALID
✓ Insight: Reasoning stagnation xác nhận bằng intermediate recall — saturate sau vài iteration, new relevant docs biến mất dần (agent lặp local optimum). 4 unsupervised signals (Document Novelty AUROC 0.81 là mạnh nhất, Criteria Coverage chỉ dùng với human criteria, Query Diversity, Question Similarity guardrail) → controller {continue, intervene, stop}: −14 search calls avg (up to 44, Tongyi-DR 77.8→33.6), accuracy +up to 10%/+3% avg, overhead ~10% latency; intervene win gấp ~2× loss.
→ Tiếp tục: [YES]
## Paper #105 — Better Together: Complementary Query Rewriting Under a Strong RAG Baseline (2609.05637v2) [applied]
✓ Skill: complementary-rewrite-router | Test: SKILL VALID
✓ Insight: Rewrite solo chỉ competitive at best (+0.2–3.7pp) nhưng methods fail trên DISJOINT queries → ensemble S1+S3+S4+HyDE = 51.70 HIT@10 (+12.5, enterprise), five-way 52.98 (+13.8); budget-matched controls chỉ capture ~40% → ~60% là complementarity thật; confidence-gated router (S1 top-1 reranker score < τ=0.65 → chạy Query2Doc) bắt nửa gain (+4.33) với 40% cost, answer F1 +1.92; AmbigNQ high-overlap (Jaccard 0.55–0.99) → combining HẠI −2.49pp, router tự abstain (7.2%).
→ Tiếp tục: [YES]
## Paper #106 — MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation (2609.01913v2) [applied]
✓ Skill: merged-teacher-distillation-er | Test: SKILL VALID
✓ Insight: 2-teacher VLM consensus→SFT, disagreement→meta-judge DPO: 7B student 90.96% PR-AUC = +13.79 over human-label SFT, +6.32 over Qwen2.5-32B-VL zero-shot tại $600/1M (6× cheaper, <1s/sample); gain decomposition: reasoning +6.14, DPO +4.15, label source chỉ +3.50; warm-start từ checkpoint + 10K samples adapt definition mới 89.48 (+6.97 over zero-shot, beats from-scratch) — days không phải months.
→ Tiếp tục: [YES]
## Paper #107 — A Large-Scale Empirical Study of QA Practices and Gaps in AI Agents (2609.17698v1) [applied]
✓ Skill: agent-qa-four-layer-audit | Test: SKILL VALID
✓ Insight: QA gap lớn nhất nằm ở COMMON routes (credentials, network/API, file, shell, dynamic code) không phải obscure surfaces; prompt-injection/adversarial tests chỉ 5.1% repos có (97.8% affected projects thiếu), security/safety tests 60.5%, red-team-like paths 49.7%; controls không đồng nhất qua equivalent routes (96.8% projects); remedy: define controls by protected action/asset + failure-oriented test FAIL khi bỏ safeguard + convert 8 risk chains thành bounded-action requirements.
→ Tiếp tục: [YES]
## Paper #108 — AutoTailor: Automatic, User-Aligned Capability Selection and Adaptation for Web Agents (2609.13548v1) [applied]
✓ Skill: autotailor-capability-inventory | Test: SKILL VALID
✓ Insight: Tool-set composition là first-class optimization: QF+ULF nén 1,283→87 APIs (−93%) gần như không mất direct coverage (60.4→59.9 without fallback); DR online adapt thành 33 APIs match runtime distribution → 90.6% correctness (+3.1pp over ReAct alone 87.5%), −57.8% total request-token cost, −29.4% latency, >24× reduction tooling tokens vs full set; bài học: aggressive static filtering một mình ĐÁNH ĐỔI (SULF total cost 1.42m→1.52m vì đẩy tasks sang fallback), ULF alone −9.7pp coverage (50.2%) — phải giữ best API mỗi semantic cluster + ReAct fallback.
→ Tiếp tục: [YES]
## Paper #109 — TRACER: Trajectory-Aware Tool Retrieval for LLM Agents (2610.21267v1) [applied]
✓ Skill: tracer-trajectory-tool-trie | Test: SKILL VALID
✓ Insight: Tool retrieval là sequential prediction, không phải independent search: execution trie (prefix→candidates) + edge memory (conversations transition được thực hiện) + learned per-state blend beats full-registry 21/24 model-environment pairs (avg +6–10 points) với k=5/128 tools và −80% tokens/step (2.8k vs 14.2k); free-running parity 58.3% vs 58.2% với 23% tools, −61% input tokens; specificity trap 36.4%→16.4%, procedural unlock-before-write enforced miễn phí; cold start là blocker chính (−38 points khi không có trajectory history).
→ Tiếp tục: [YES]
## Paper #110 — On Evaluating and Improving Conversational Agents in Production (2609.32092v1) [applied]
✓ Skill: commissioned-agent-evaluation | Test: SKILL VALID
✓ Insight: Production agent improvement cần commissioned behavior-specific evaluation, không aggregate metrics: assertion profiles ở nhiều strictness levels (any/first/≥75%/all) chỉ ra failure nằm ở prominent carousel positions (first 0.833 vs all 0.640) → fix đúng chỗ (curation prompt strict rule, +0.060 first-product); paired per-scenario bootstrap (2,000 resamples) tách run-to-run variation khỏi scenario difficulty — h1 borderline (+0.067 [−0.022,+0.178]) bị reject, h2 signal+ (+0.267 [+0.067,+0.511]) được confirm sau 3 reproduce runs; audit judge như software phát hiện temperature=0 configured but not applied.
→ Tiếp tục: [YES]
## Paper #111 — Can LLMs Identify Meaningful Touchpoints in Conversion Attribution? (2608.28649v1) [applied]
✓ Skill: lotus-pairwise-touchpoint-selection | Test: SKILL VALID
✓ Insight: Implicit touchpoint = 14.91% hành trình conversion mà heuristic taxonomy/CF hoàn toàn blind (explicit 19.09%); LLM pairwise prompting phát hiện được chúng nhưng implicit F1 ceiling chỉ 0.5426 vs explicit 0.9095 — semantic gap vẫn lớn; pairwise beats listwise trên MỌI model (avg overall F1 0.6490→0.6954, gap 6–12pp ở small models); strong open-weight (GLM-5.1 0.7086, DeepSeek-V4-Pro 0.7056) gần proprietary (GPT-5.5 0.7197); LOTUS dùng LLM labels làm auxiliary positives cho CVR training → GAUC +0.35pp over in-shop baseline, +0.15pp over heuristic CABB (0.1pp GAUC ≈ material revenue growth).
→ Tiếp tục: [YES]

## Paper #112 — Do Tool Calls Execute as Intended? Intent-Execution Correspondence — IEC/IntAct (2610.04375v1) [applied]
✓ Skill: iec-hop-witness-audit | Test: SKILL VALID
✓ Insight: 10.0% exposed calls bị đổi tại 1 trong 5 hops (Claude Code Bash 12.0%; backslash-pair calls 67.0%), 80.7% merged-backslash changes CHẠY SAI MÀ KHÔNG BÁO LỖI; trajectory judges quy 97/102 failures cho LLM (κ≤0.04) trong khi IEC protocol (witness + receiver's own parser) đạt κ 0.77; IntAct rendering tại named hop recover 79.2% path-caused losses (137/173, Fisher p<.001), tokens per passed task −2.4× (đến 12.3×); evidence trong tool result KHÔNG giúp agent sửa path (p≥.500) — phải sửa harness.
→ Tiếp tục: [YES]

---

**Ghi chú 2026-10-17 (corruption + recovery):** `top30_20261017.json` entries #16–#30 bị corrupted ids (verified qua arXiv API: 2609.04241 = VocalCoachBench cs.SD, 2610.10539 = Tetris3D cs.CV, 2610.07414 = physics.flu-dyn, 2608.17437 = math.PR, 2609.26288 = cs.LG protocol uncertainty, 2610.03960 = cs.CR poisoning, 2609.03475 = cs.CV SafeRestore, 2608.15893 = bot detection, 2610.00758 = cs.LG inverse RL, 2609.15053 = hep-ex, 2609.05162 = q-fin.GN, 2609.24605 = math.OC — KHÔNG có trong scan). Đã rebuild top30 từ `scans/2026-10-17.json` (source of truth, 60 papers, ids/titles/scores thật) → `state/top30_20261017_rebuilt.json` (30 papers chưa distill, sorted by llm_score). Entries #1–#15 verified đúng (đã distill thành papers #97–#111).


## Paper #113 — Learning How Much to Collaborate: Difficulty-Aware Topology Selection — Dats (2609.13890v1) [applied]
✓ Skill: dats-topology-router | Test: SKILL VALID
✓ Insight: Collaboration benefit scales với difficulty (HRM vs Single gap 2.4→10.7→21.1 points qua easy/mid/hard tertiles) nhưng cost cố định 9.95× — fixed HRM tốn 60% spend buying nothing; Dats (predict-then-optimize: topology-graph GNN 13.7K params + bisection λ) đạt 77.69% pass@1 tại 40% always-HRM budget ($0.377/problem), +4.07 over always-HRM (cả 11 McNemar comparisons significant sau Holm–Bonferroni), +6.03 over direct classification, +9.12 over Random; gain ổn định 4.11±0.07 trên 4 backbones (13.8-point capability span) và transfer sang math (400 problems, +3.5 points, gap 2.5→20.9 theo MATH level); budget-matched protocol REVERSE rankings — shared λ=0.2 để RandomForest first (76.55% nhưng tốn $0.489 = 51.9% budget), calibrated → Dats first với gap 3.42 points; fine-tuned GraphCodeBERT 125M params mua +0.49 points KHÔNG significant (p>0.35, seed SD 0.71).
→ Tiếp tục: [YES]


## Paper #114 — When the Model Retires: An Empirical Study of LLM Migration in Open-Source (2609.31288v1) [applied]
✓ Skill: llm-retirement-readiness-audit | Test: SKILL VALID
✓ Insight: 82% (CI 79–84) migrations được commit SAU shutdown date — app đã fail rồi mới sửa — bất kể repo popularity (82% ở mọi star tier), prior retirement experience (73%→73% ở 85 repos bị ≥2 retirements), hay pre-existing abstraction layer (70% still reactive, layer chỉ giảm fix size 4 files/20 lines KHÔNG làm timely); dose–response: mỗi e-fold notice length giảm odds post-shutdown migration 74–78% (Anthropic 60–114-day notices → 89% reactive vs OpenAI 1-year Assistants API → 13%); 94% migrations edit source vì identifier hard-coded (effort 6 lines prompt-only → 693 lines fine-tuned); only 8% switch provider (retirement là forced upgrade funnel, KHÔNG phải churn event); silent failure mode (8%): exception handlers convert retirement error thành apologetic message/null/demo-mode/constant answer ("breed identification always returned 'Golden Retriever'"); Gemini 2.0 Flash soft movable date KHÔNG tạo deadline effect (trickle 23–29/tuần, no spike) — cần internal hard deadline riêng.
→ Tiếp tục: [YES]


## Paper #115 — What Drives Recovery in Agentic Text-to-Cypher? LAST-CQ (2609.12746v1) [applied]
✓ Skill: execution-grounded-query-refinement | Test: SKILL VALID
✓ Insight: Recovery gain localise ở detector + routing, KHÔNG phải feedback sophistication: removing correction cost +3.1% (vs single-pass) đến +12.3% (vs no-refinement counterfactual, +80.7% Gemini Flash, all p<0.001); nhưng replacing schema-grounded LLM-synthesised hints bằng raw Neo4j error string equivalent within ±0.075 set-F1 (TOST p=0.002, <0.2% end-to-end GLEU) — hint synthesis module chỉ worth ~1 point exact match; Best-of-3 parallel sampling (cùng budget, T=0.7) DEGRADE 10.8–11.4% và hit rate FALLS (87.6%→85.2%) trong low-entropy output spaces; LAST-CQ recovers 91.7% single-pass failures (pooled 93.8%) với first-time success cost đúng 1 call (short-circuit validation 0 calls, 53–97% queries need no correction, mean 1.1–2.5 LLM calls/query); fixed H_relax constant (6 hints, 0 calls) giải empty results; measurement: n-gram overlap over-report 65.9% pairs vs set equivalence và under-report vs semantics (33.9% partial-BLEU fully correct), BLEU≥0.999 proxy understate naive EM 19.9%→22.6%; LLM judge optimistic 9 points vs blind human labels (over-use PARTIAL, κ human-judge 0.48 vs inter-judge 0.63).
→ Tiếp tục: [YES]


## Paper #116 — Incremental Pooled LLM Evaluation for Cost-Effective Retrieval Model Selection (2609.02745v1) [applied]
✓ Skill: incremental-pooled-llm-eval | Test: SKILL VALID
✓ Insight: Pooled LLM evaluation (judge UNION of all systems' retrieved docs, reuse judgments) đạt nDCG@10 ρ=0.69–0.95 vs gold qrels, và 74% pairwise disagreements (20/27) nằm trong gold's own bootstrap sampling noise (B=10,000) — chỉ 7/220 pairs genuine ranking differences; document overlap yield 65–80% judgment reuse (production: 79.6%, 4.9× cost reduction, 766,350 judgments ≈ $800 cho 62 configurations trong 4 weeks, incremental 5→62 systems KHÔNG re-run previous judgments); P@k/DCG@k exactly invariant under pool expansion, per-query pairwise orderings preserved cho Recall/AP/nDCG (macro-averaged invariance empirical: no pair Δ>0.001 reverses trong 500 random orderings, fragile pairs = statistically indistinguishable pairs differ 0.000014); pooled LLM judging removed ALL 19 ranking errors classical TREC pooling introduced (pool bias 0.033–0.055 nDCG@10 penalty cho novel systems); production: top-5 MAP@100 ALL hybrid (0.454–0.461), chọn hybrid-emb3-large-256 (BM25 fusion compensates low dimensionality — 256-dim hybrid ≈ 1536-dim dense, +0.029 dense vs +0.012 hybrid); instruction-framed queries degrade ALL systems ΔMAP −0.039 (diluting retrieval signal), query expansion KHÔNG help well-formed queries (0.424 vs 0.459) nhưng nearly eliminates framing-induced recall penalty (−4.8pp→−1.1pp); LLM judge broader relevance inflates nDCG +0.1–51% và deflates recall −17–39% nhưng uniform across systems → ordinal rankings preserved.
→ Tiếp tục: [YES]

## Paper #117 — FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents (2609.26048v1) [applied]
✓ Skill: fire-runtime-policies-for-agent-reliability | Test: SKILL VALID
✓ Insight: Chính sách thời gian chạy (runtime policy) — hướng dẫn/từ chối do harness áp dụng tại trạng thái rủi ro — làm cho khả năng model đã có lặp lại được nhiều hơn, không cần thay đổi model. Sol pass∧2 64.4%→73.6% (+9.2), Terra với chính sách 71.4% vs Sol không hỗ trợ 64.3% trên 14 nhiệm vụ, một nửa chi phí.
→ Tiếp tục: [YES]

## Paper #118 — Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills (2610.01833v1) [applied]
✓ Skill: continuous-process-level-evaluation | Test: SKILL VALID
✓ Insight: Kết hợp kiểm tra kết quả và quy trình trong pipeline đánh giá phát hiện sai lệch hành vi dù kết quả cuối đúng — 175/240 vượt kiểm tra số liệu cuối nhưng 162/175 (92.6%) vẫn có sự lệch bổ sung; dependency attribution nén 6.34 kiểm tra thất bại xuống 2.65 gốc (−58%).
→ Tiếp tục: [YES]

## Paper #119 — Improving the Energy-Efficiency of the Code Generated by LLMs through Effective Prompting (2610.02571v1) [applied]
✓ Skill: energy-efficient-llm-code-prompting | Test: SKILL VALID
✓ Insight: Chiến lược nhắc nhở ảnh hưởng đáng kể đến năng lượng thực thi code do LLM tạo ra — giảm tới 25% Python và 17% C++; hiệu quả thay đổi theo mô hình và ngôn ngữ, không áp dụng một prompt duy nhất cho mọi trường hợp.
→ Tiếp tục: [YES]

## Paper #120 — Pre-retrieval Query Clustering for Adaptive Top-k Document Retrieval in RAG Systems (2609.13489v2) [applied]
✓ Skill: qcar-adaptive-top-k-retrieval | Test: SKILL VALID
✓ Insight: Ước tính độ khó truy vấn trước khi lấy để chọn top-k thích ứng thay vì số liệu cố định — đơn giản giảm 35,95% token, F1 +0,37; phức tạp F1 +0,37 với +85,95% token; A/B test F1 +36%, token −14% trên cụm đơn giản.
→ Tiếp tục: [YES]

## Paper #121 — REALMS: Real-Time Exact Audience Sizing over High-Dimensional Nested Profiles (2609.30547v1) [applied]
✓ Skill: realms-schema-aware-nl2sql-audience-sizing | Test: SKILL VALID
✓ Insight: Kết hợp lấy thuộc tính có ý thức về scheme với NL2SQL để sinh truy vấn chính xác trên scheme lồng nhau — Recall@k 94%, Exact-match 93%, Execution match 90%, latency trung bình dưới 10 giây.
→ Tiếp tục: [YES]

## Paper #122 — Evaluating Deep-Search Agents under Hierarchical Web Evidence Poisoning (2609.06027v2) [applied]
✓ Skill: hae-geo-agent-robustness-evaluation | Test: SKILL VALID
✓ Insight: Nhận thức bằng chứng suy giảm dưới bẫy chứng thực (L3); defense prompting tăng xác minh nhưng hiếm khi chuyển thành khôi phục — cần yêu cầu agent rút lui khi bằng chứng mâu thuẫn.
→ Tiếp tục: [YES]

## Paper #123 — Where Do the Tokens Go? Understanding and Reducing Costs in LLM Agents for Vulnerability Discovery (2610.11602v1) [applied]
✓ Skill: avri-vulnerability-reasoning-interface | Test: SKILL VALID
✓ Insight: Bản địa hóa và hiểu mã nguồn + suy luận lỗ hổng chiếm 60.4% token, là bottleneck chính trong các lần chạy thất bại; AVRI giảm chi phí 18.0% (Codex) và 23.7% (OpenCode) bảo toàn thành công.
→ Tiếp tục: [YES]

## Paper #124 — Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions (2609.30563v1) [applied]
✓ Skill: intuitive-prompting-agent-simulation | Test: SKILL VALID
✓ Insight: Nội dung thái độ cải thiện dự đoán hơn mô tả nhân khẩu học (MCC 0.300→0.473); intuitive prompting (phản hồi ngay lập tức) đạt độ trung tín cao nhất và cắt nén khác biệt cá nhân từ 10.24× xuống 3.14×.
→ Tiếp tục: [YES]

## Paper #125 — InsightChain: Optimized Chain-of-Insight Analytics for LLM-driven Data Visualization (2609.06438v1) [applied]
✓ Skill: insightchain-four-stage-visualization | Test: SKILL VALID
✓ Insight: ống dẫn bốn giai đoạn (Explore–Focus–Test–Present) vượt các bước tham chiếu đơn thành mẫu; IPM đạt Spearman ρ=0.88 với đánh giá con người; VG-COPRO nâng IPM +1.31 (Gemini) và +1.16 (GPT-4.1).
→ Tiếp tục: [YES]

## Paper #126 — Question's Gambit: The First Move Matters in Agentic Deep Search (2609.14412v1) [applied]
✓ Skill: questions-gambit-first-move-retrieval | Test: SKILL VALID
✓ Insight: Bước truy xuất đầu tiên (first move) quyết định chất lượng ngữ cảnh mở — GPT-5.5 accuracy 83.1%→90.5% (+7.4 pp), calibration error 15.7→7.58, gold recall 56.1→75.9.
→ Tiếp tục: [YES]

## Paper #127 — Q2D-Web: A Large-Scale Benchmark for Retrieval in Agentic RAG Systems (2609.08887v2) [applied]
✓ Skill: q2d-web-retriever-evaluation | Test: SKILL VALID
✓ Insight: Q2D-Web: 190M tài liệu, 70k truy vấn agentic, 10 ngôn ngữ; pplx-embed-v1-4b thắng Recall@1000 cả 3 tập phán xét; RRF lấy mẫu 1/3 corpus bảo toàn thứ hạng mô hình, Recall@1000 chỉ +4–7 điểm.
→ Tiếp tục: [YES]

## Paper #128 — UNREAL: Unifying Retrieval and Long-Context with a Single Model (2610.08463v1) [applied]
✓ Skill: unreal-internal-evidence-selection | Test: SKILL VALID
✓ Insight: Chọn bằng chứng nội bộ (internal evidence selection) áp dụng đồng chiều cho truy xuất corpus và suy luận ngữ cảnh dài — HotpotQA recall 49.1%→73.2%, NoLiMa 1.0%→24.83% (128K token), ít hơn 500K tham số trainable.
→ Tiếp tục: [YES]

## Paper #129 — CodeHealth Predicts the Token Cost of Agentic Code Review (2610.21914v1) [applied]
✓ Skill: codehealth-token-cost-prediction | Test: SKILL VALID
✓ Insight: Chất lượng code (CodeHealth) dự đoán chi phí token agent review và fix — mỗi điểm CodeHealth cao hơn giảm 3.5% đến 6.1% chi phí token, không do kích thước PR.
→ Tiếp tục: [YES]

## Paper #130 — Retrieved but not ranked: surface-form bias in structural retrieval (2609.01556v1) [applied]
✓ Skill: structural-retrieval-evaluation | Test: SKILL VALID
✓ Insight: Việc nhúng truy xuất neo chặt vào nội dung bề mặt chứ không phải cấu trúc — Toán học Hit@1 = 0.0% ở cấp disguise nặng; lexical reranker lật dấu (hại toán học, giúp quỹ đạo); LLM reranker phục hồi 5-63% (toán học) và 43-76% (quỹ đạo).
→ Tiếp tục: [YES]

## Paper #131 — Trajectory-Aware Benchmark Subset Selection (2609.24928v2) [applied]
✓ Skill: trajectory-aware-subset-selection | Test: SKILL VALID
✓ Insight: Chọn sample gần trọng tâm (centroid) của mỗi nhóm kết quả (outcome group) trong không gian nhúng (embedding space) — subset 10% giữ median error dưới 5% cắt giảm chi phí token khoảng 90%.
→ Tiếp tục: [YES]

## Paper #132 — Extending FunctionGemma for Practical On-Device Mobile Function Calling (2609.25373v1) [applied]
✓ Skill: functiongemma-on-device-extension | Test: SKILL VALID
✓ Insight: Fine-tune model nhỏ (270M) trên dataset tổng hợp về hành động thiết bị mở rộng cobertura — end-to-end accuracy 29.3%→76.5% trên MOBILEACTIONSEXTENDED, combined model giữ 76.5% và đạt 82.3% trên MOBILEACTIONSGOOGLE (giảm từ 90.3% của specialist), trade-off 8.0 điểm.
→ Tiếp tục: [YES]

## Paper #133 — When Synthetic Data Hurts: On Catastrophic Forgetting in Skill Retrieval (2609.10750v1) [applied]
✓ Skill: synthetic-data-forgetting-mitigation | Test: SKILL VALID
✓ Insight: Fine-tune trên dữ liệu tổng hợp cải thiện in-distribution nhưng gây quên mất trên OOD — OOD recall giảm 0.850→0.650; các phương pháp giảm quên misses (LwF, EWC, L2-init) giữ OOD và cải thiện in-distribution 13.98%.
→ Tiếp tục: [YES]

## Paper #134 — TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising (2608.24034v1) [applied]
✓ Skill: tagr-temporally-adaptive-recommendation | Test: SKILL VALID
✓ Insight: Điều chỉnh theo thời gian ở ba cấp độ (live-ad tokenization, user intent modeling, preference alignment) cải thiện gợi ý quảng cáo livestream — live-room entry +8.5%, shopping-cart click +7.4%, revenue lift +16.1%.
→ Tiếp tục: [YES]

## Paper #135 — Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows (2610.21411v1) [applied]
✓ Skill: jev-litemas-decision-routing | Test: SKILL VALID
✓ Insight: Tách quyết định khỏi sinh trong multi-agent workflows: dùng model nhẹ (Jev) cho điều phối, chỉ gọi LLM review khi artifact cần sửa — giảm 12.7–54.6% token, duy trì accuracy trong 1.34 điểm, ground routing vào output thực tế của chuyên gia ngăn mất 18 điểm.
→ Tiếp tục: [YES]

## Paper #138 — Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return (2609.14758v1) [applied]
✓ Skill: tool-failure-honesty-detection | Test: SKILL VALID
✓ Insight: Khi công cụ thất bại, agent cần được yêu cầu xác nhận trạng thái (OK/FAILED) trước khi trả lời — giảm phản hồi không trung thực từ 14.10% xuống 0.87%; khi công cụ trả về status:ok với giá trị bị che đi/hỏng hóc, tỷ lệ không trung thực đạt 45.3%.
→ Tiếp tục: [YES]

## Paper #136 — AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic Workflows (2609.22951v1) [applied]
✓ Skill: agentrouter-step-level-model-routing | Test: SKILL VALID
✓ Insight: Định tuyến từng bước (step-level model routing) thay vì dùng frontier model cho mọi bước: chỉ dùng frontier model cho bước cần reasoning sâu, dùng model nhỏ cho bước định dạng — giảm 72% chi phí, giữ 97.3% chất lượng, định tuyến chính xác 91% bước đơn giản, 85% bước hiệu quả, 76–82% bước trung bình/cao.
→ Tiếp tục: [YES]

## Paper #137 — StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents (2610.10942v1) [applied]
✓ Skill: storebench-live-commerce-evaluation | Test: SKILL VALID
✓ Insight: Agent chưa thay thế judgment kinh tế: model tốt nhất đạt 49% vs heuristic 97%; dùng agent làm trợ thủ, không thay thế quyết định định giá/tồn kho. Human experts đạt 0.708 vs model 0.700.
→ Tiếp tục: [YES]

## Paper #138 — Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return (2609.14758v1) [applied]
✓ Skill: tool-failure-honesty-detection | Test: SKILL VALID
✓ Insight: Khi công cụ thất bại, agent cần được yêu cầu xác nhận trạng thái (OK/FAILED) trước khi trả lời — giảm phản hồi không trung thực từ 14.10% xuống 0.87%; khi công cụ trả về status:ok với giá trị bị che đi/hỏng hóc, tỷ lệ không trung thực đạt 45.3%.
→ Tiếp tục: [YES]

## Paper #139 — Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows (2610.03010v1) [applied]
✓ Skill: sustainable-agent-design | Test: SKILL VALID
✓ Insight: Không mặc định multi-agent — MA tốn 6.36× năng lượng, 6.07× thời gian vs non-agentic, chỉ 1/66 cấu hình Pareto-optimal là MA; few-shot mạnh hơn việc thêm agent. Áp dụng: không mặc định multi-agent — cấu hình nhẹ thường Pareto-optimal hơn.
→ Tiếp tục: [YES]

## Paper #141 — Breaking Babel: A Self-Evolving Multi-Agent System for Long-Form Subtitle Translation (2609.38660v2) [applied]
✓ Skill: self-evolving-multi-agent-translation | Test: SKILL VALID
✓ Insight: Hệ thống đa agent tự phát triển (self-evolving multi-agent) để dịch phụ đề dài — SMART đạt MQM cao nhất trong 15 hướng của Subtitle Arena, giảm penalty 6.9% so với hệ thống agent mạnh nhất; MuSC đạt kết quả tốt nhất trên 4 cặp ngôn ngữ; human rating 4.50/5.
→ Tiếp tục: [YES]

## Paper #142 — Scalable Multi-Task Inverse Reinforcement Learning (2610.00758v1) [applied]
✓ Skill: scalable-multi-task-irl | Test: SKILL VALID
✓ Insight: Multi-task inverse reinforcement learning gộp dữ liệu từ nhiều agent trong cùng môi trường dưới giả định thấp-rank — mạnh mẽ với limited coverage, khôi phục phần thưởng trên/ngoài support, transfer đến môi trường đích với regret thấp hơn baseline, lợi thế tính toán mở rộng khi số tác vụ tăng.
→ Tiếp tục: [YES]

## Paper #143 — CAMIE: Co-Engagement-Aware Multimodal Item Embeddings for Snap Dynamic Product Ads Retrieval (2608.30255v1) [applied]
✓ Skill: camie-co-engagement-embedding | Test: SKILL VALID
✓ Insight: Co-engagement tuning căn chỉnh embedding với chuyển đổi thực tế — offline vượt modèle thương mại mạnh nhất trên Recall@10; online +0,39% CTR / +10,8% CVR so multimodal control, +18,96% CTR / +13,1% CVR so text control, đã deploy production.
→ Tiếp tục: [YES]

## Paper #140 — Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents (2609.26760v2) [applied]
✓ Skill: grow-the-harness-reusable-specialist-agents | Test: SKILL VALID
✓ Insight: Thay vì để LLM tái thiết quyết định điều khiển mỗi tác vụ, hãy biến feedback thành code điều khiển tái sử dụng → giảm 76–92% LLM calls, 74–99% chi phí, thành công 44.7–45.3% ngay cả với model 4B.
→ Tiếp tục: [YES]

## Paper #144 — Scaling LLM-Driven Multi-Agent Systems: Design Principles and Architectural Scalability Analysis (2607.27942v1) [applied]
✓ Skill: scaling-llm-driven-multi-agent-systems | Test: SKILL VALID
✓ Insight: Kiến trúc phức tạp hơn không phải luôn tốt — khi LLM cơ bản không đủ năng lực, thêm agent chỉ tốn token và gây lỗi lan truyền; hiệu suất đạt đỉnh ở độ phức tạp trung bình (MAS-M: 5 agents, 3 loops), consistency dưới 50% ở mọi cấp độ.
→ Tiếp tục: [YES]

## Paper #145 — Scaling Inference-Time Compute with Teams of Coding Agents (2610.17471v1) [applied]
✓ Skill: compute-allocation-multi-agent-coding-team | Test: SKILL VALID
✓ Insight: Phân bổ compute inference ưu tiên vào giai đoạn lập kế hoạch (ηP=3.8 vs ≤2.4 giai đoạn khác), dùng model mạnh cho lead + model rẻ cho planner, giới hạn implementer/verifier tối đa 4 workers — heterogeneous 17-agent team đạt trong 1.4 điểm reward của team 5-agent mạnh mẽ với chi phí thấp hơn 70%.
→ Tiếp tục: [YES]

## Paper #146 — A Governance-Aware LLM Orchestrated Agentic Digital Twin for Transmission System Operator Control Room Decision Support (2609.22476v1) [applied]
✓ Skill: agent-governance-layer | Test: SKILL VALID
✓ Insight: Lớp quản trị thời gian chạy giữa LLM và công cụ/backend với 5 yêu cầu (R1–R5) và 4 bất biến — tool selection 96.5%, task success 93.7%, invariants 100% trên 590 lượt chạy; xóa lớp quản trị → model thực thi tất cả 45 hành động cần phê duyệt mà không có phân quyền, chỉ 39.2% câu trả lời có con số từ backend.
→ Tiếp tục: [YES]

## Paper #147 — Governing the Edge: Automating Commercial P&C Insurance Underwriting via Hybrid Local-Cloud Multi-Agent Framework (2609.37454v1) [applied]
✓ Skill: multi-agent-compliance-first-workflow | Test: SKILL VALID
✓ Insight: Tuân thủ được rãs vào cấu trúc đồ thị LangGraph (quy tắc làm điều kiện trên cạnh giữa agent), Gemma 2 cục bộ cho dữ liệu nhạy cảm + Claude Sonnet đám mây cho điểm số ẩn danh — compliance accuracy 70% trên 20 kịch bản, hard-stop 6/6, xử lý 40 phút thủ công trong vài phút.
→ Tiếp tục: [YES]

## Paper #148 — Learning to Route in Visual Space via Multi-Step Embedding Retrieval (2609.38743v2) [applied]
✓ Skill: multi-step-embedding-retriever-visual-search | Test: SKILL VALID
✓ Insight: Offload multi-step navigation từ agent xuống công cụ retrieval — VHop-Router biến mô hình embedding thành retriever đa bước, tăng retrieval từ dưới 5% lên 76.3%, cải thiện task success 52.7%, giảm token 61% (1886→728), nâng cấp agent chỉ +3.7%.
→ Tiếp tục: [YES]

## Paper #149 — ERPBench: A State-Grounded Evaluation Paradigm for Computer-Use Agents in Enterprise Software (2609.17885v2) [applied]
✓ Skill: state-grounded-evaluation-cua | Test: SKILL VALID
✓ Insight: Đánh giá CUA trên trạng thái cơ sở dữ liệu không chỉ chụp màn hình — Claude 94%/100%/100% qua 3 tier, mô hình mở rơi 0–3% ở T2/T3, một số agent lưu 85% lần chạy nhưng chỉ ghi đúng 3%, harness có cổng phê duyệt con người cho hành động rủi ro.
→ Tiếp tục: [YES]

## Paper #150 — Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents (2610.21424v1) [applied]
✓ Skill: spra-structured-paper-representation | Test: SKILL VALID
✓ Insight: Biểu diễn bài báo có cấu trúc (Vấn đề, Đóng góp, Thành phần, Thiết lập thí nghiệm, Đo lường, Kết quả) với quan hệ gō — 1 triệu bài báo, 19,95 triệu đơn vị, 24,07 triệu quan hệ — cải thiện QA khoa học 0,381/5, giảm token 28,5% so với passage retrieval và 95,3% so với Full Compact.
→ Tiếp tục: [YES]

## Paper #151 — Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems (2609.02264v1) [applied]
✓ Skill: codebook-based-multi-agent-topology | Test: SKILL VALID
✓ Insight: Không gian thiết kế topology thực tế rất nhỏ (~6 đồ thị duy nhất sau lọc phần thưởng) — Codebook Agent dùng VQ autoencoder nén thành codebook 16 mục, MLP proxy xếp hạng lại trong một bước, đạt 84.6 (so với 83.0), phát ra topology 2.4ms, giảm token 21.9–33.2%.
→ Tiếp tục: [YES]

## Paper #152 — Beyond Single-Model Injection: Prompt Injection in Multi-Agent Systems (2609.22949v1) [applied]
✓ Skill: prompt-injection-defense-mas | Test: SKILL VALID
✓ Insight: Mô hình đe dọa 14 vector trong 4 loại — 67% agent dễ bị tấn công dù có guardrails, chển tiếp gián tiếp qua công cụ 43%, 4 phòng thủ kiến trúc giảm tổng thể từ 31.2% xuống 4.2% (ký thông điệp -91%, làm sạch ranh giới -78%, quyền truy cập công cụ theo phạm vi, phát hiện bất thường 84%).
→ Tiếp tục: [YES]

## Paper #153 — Audit Without Verification: When LLM Accountability Layers Relay Rather Than Check (2609.07680v1) [applied]
✓ Skill: audit-boundary-report-schema | Test: SKILL VALID
✓ Insight: Lớp accountability chỉ đọc report của agent hoạt động như relay (bộ chuyển tiếp) chứ không phải check: 0 allegation trên 7,996 episode sạch, chấp nhận 34.4–62.6% false alarm upstream; xóa 1 clause "Suspected origin" (observation giữ nguyên) phục hồi +41.2 pp nơi upstream sai (4.1%→45.2%) nhưng mất -14.7 pp nơi upstream đúng — trade-off ∆ = P(wrong)·∆|wrong + P(correct)·∆|correct, đo được ngoại tuyến; auditor cùng model đạt 60.3% từ raw documentation vs 4.1% từ report.
→ Tiếp tục: [YES]

## Paper #154 — Prompted Identity Degrades Cooperation in Multi-Agent LLM Systems (2609.35928v1) [applied]
✓ Skill: factionalism-detection-agent-facing-anonymization | Test: SKILL VALID
✓ Insight: Chỉ cần agent thấy model-family identity của nhau là group phân phe (factionalism) theo đúng nhãn — kể cả nhãn giả shuffle hay màu trung tính (AMI 0.18–0.95), 0/12 unlabeled experiment phân phe; group có nhãn tốn 1.38–1.86× tokens, +30% rounds, success 96%→81%, tokens/successful-run tăng 1.5–2.2×; cơ chế qua adoption channel không phải style recognition; giải pháp: ẩn danh phía agent, orchestrator giữ map identity.
→ Tiếp tục: [YES]

## Paper #155 — DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock Research (2608.26990v1) [applied]
✓ Skill: evidence-aware-agent-orchestration | Test: SKILL VALID
✓ Insight: Evidence block phải gắn state (available/missing/fallback/stale/partial/fetch_failed) và project vào prompt — missing data KHÔNG được thành neutral evidence; 2 profile (default report rẻ vs agentic đắt) tái dụng chung evidence+routing substrate; Strategy Skill opinion qua signal-eligibility partition, invalid → diagnostics, disagreement summary làm explicit input cho decision agent; RiskGuard chỉ downgrade (buy→hold→sell) never upgrade; 1,457/1,457 frozen contract test pass (102.5s) nhưng paper honest: conformance ≠ report quality/forecast/returns.
→ Tiếp tục: [YES]
