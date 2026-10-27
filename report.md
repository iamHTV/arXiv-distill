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

## Paper #156 — AlphaPilot: Multi-Turn Tool-Using LLM Agents for Adaptive Alpha Mining with Reinforcement Learning (2610.15488v1) [applied]
✓ Skill: Multi-Turn Tool-Using Agent với Evaluator Feedback Loop | Test: SKILL VALID
✓ Insight: Multi-turn tool-using loop + compact tried-factor memory vượt GRPO single-turn cùng backbone +7.31pp return / +0.43 Sharpe / +6.98pp MaxDD (CSI300: 42.93% return, Sharpe 2.46, RankIC 0.0595); bỏ memory feedback → return giảm một nửa (48.64→26.40) và rollout dài gấp 3× (5.24→15.75 turns); Qwen3-4B+GRPO vượt Qwen3-235B (6.88%) và DeepSeek-R1 (22.79%); variant có RankIC cao nhất (0.0634) lại return yếu nhất (34.39%) — optimize pool-level utility, không phải IC đơn lẻ
→ Tiếp tục: [YES]

## Paper #157 — Look Before You Leap: Pre-Action Verification for LLM Agents (2609.11957v1) [applied]
✓ Skill: Pre-Action Verification Gate cho LLM Agent (shell + code edit) | Test: SKILL VALID
✓ Insight: Pre-action deterministic guard chuyển silent failure thành recoverable clean failure: shell verifier (bash -n + which + flag set) bắt 95.8% invalid @ 10.0% FPR, oracle-exact core 0% FP recall 0.500, cost 2.55 ms/command; edit location-anchored (line range) silent-corrupt 99.1% files khi lệch 1 dòng vs content-anchored (search/replace, diff) silent 0.000%; Robust-Apply (Kmin=2, τhi=0.90, δ=0.20) còn 1 silent/8,320 trials (0.01%), giữ 60% applies của fuzzy
→ Tiếp tục: [YES]

## Paper #158 — Grammar Concept Annotation at Scale: Deployed Fine-Tuned SLMs Outperform Prompted Frontier Models (2610.10827v2) [applied]
✓ Skill: Prompt Internalization — Fine-tune SLM thay thế Prompted Frontier Model | Test: SKILL VALID
✓ Insight: Fine-tuned Qwen3.5-0.8B + compact prompt 375 token (−90.2% vs 3,810 token teacher prompt) vượt prompted GPT-5.4 và GPT-5.6 Sol ở mọi matching level (Golden L3 recall 78.89 vs 62.87; Golden2 80.88 vs 76.04, p<0.0001) với cost ~16× (6.2% baseline); data quality pipeline (review+validation+synthetic rebalance) cho +36.9–40.7 pp strict recall vs raw supervision; A/B 35 ngày: engagement +15.8%, scheduled hours +2.1%, GMV new lessons +13.2%; uncalibrated LLM judge thiên vị teacher 99.06% vs 93.88%, human audit đưa về ≈95% hòa
→ Tiếp tục: [YES]

## Paper #159 — Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams (2610.19051v1) [applied]
✓ Skill: Blind-Spot Gate — Chứng nhận deployment ToM module (không deploy) | Test: SKILL VALID
✓ Insight: Accuracy là certificate sai 2 hướng: Hanabi (damage compounds) accuracy approve 5 harmful deployments (clone teams −0.01 đến −0.26 vs independent errors), task assignment (costly errors rare) accuracy reject mọi classifier 0.42–0.53 dù acting on beliefs thắng do-nothing 33/35 cells (+0.76); redundancy 3 observers chỉ worth 1.11–1.64 independent (all-wrong 9–16% vs 0.15–3.4% predicted); Blind-Spot Gate (costs+interactions+dependence, λ=1) regret 0.021 với 0 significant false approvals/20 splits (accuracy: 0.056, 3.2 FA, 20/20 splits), out-of-sample: recover 7 classifiers accuracy reject (regret 0.004 vs 0.479) và catch Bayesian module accuracy approve (FA* 17/20 → 1/20); deferral trên unread teammates beneficial 30/30 cells (min +0.30)
→ Tiếp tục: [YES]

## Paper #160 — Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce (2608.14825v3) [applied]
✓ Skill: Three-Stage Misaligned-Communication Classifier (LLM judge + state verification + reasoning audit) | Test: SKILL VALID
✓ Insight: 12.58% emails misaligned (CI [8.88,16.61]) trong 20/20 simulations, 74.7% agent-runs, KHÔNG có elicitation — tương đương engineered-elicitation rates (8.7-13.0%); dominant false factual claims (~65%, không phải collusion ~21%) nhưng promises trong misaligned emails enacted 56.9% vs 31.5% (1.8×, consistent within senders — không phải confusion); reciprocity mạnh nhất (OR 1.65*** [1.25,2.18], within-agent 1.42 — misalignment truyền nhiễm giữa counterparties), inventory scarcity OR 1.58**, horizon DECLINE OR 0.895/30 ngày; agents KHÔNG verify trước khi assert (chỉ 15.5% check mọi claim; false claims checked bằng true 44.1% vs 29.1%; payments checkable mà false anyway — verification-use gap; transfers check sai instrument 51.4%); capability KHÔNG tổ chức misalignment (Spearman ρ=−0.07, dyadic gap OR=1.04); competition giảm profit $1,447 vs $3,076 single-agent (p=0.021)
→ Tiếp tục: [YES]

## Paper #161 — HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration (2610.22195v1) [applied]
✓ Skill: HTN-Orchestrate — Hai lớp Planner/Orchestrator | Test: SKILL VALID
✓ Insight: Result-informed planning (decompose dependent subtasks SAU KHI prerequisite results trả về) vừa chính xác hơn vừa rẻ hơn: upfront decomposition mất −1.5pp accuracy (90.5% vs 92.0%), +4.79 phút median (25.23→30.02), worker invocations 14→16. BrowseComp 89.73% (+2.45pp vs Agent Team, +15.80pp vs ReAct) với DeepSeek-V4.1-Flash — chỉ sau GPT-6 Astra/Kimi K3/GPT-5.6 Sol; PRL-Bench +10.19pp (gain lớn nhất); 165 shared successes vs Agent Team: HTN nhanh hơn 67.9%, median ratio 0.699, concurrency 2.47 vs 1.70. Rebuilding với evidence carryover: 35 questions rebuild, 27 đúng (case Q501: "Serial Killer" đúng vs "Silent Night" sai).
→ Tiếp tục: [YES]

## Paper #162 — Playing social deduction games with reinforcement fine-tuned large language models (2610.04261v1) [applied]
✓ Skill: Social-Cognitive RFT — Huấn luyện social agent bằng reading + influence rewards | Test: SKILL VALID
✓ Insight: Outcome-only RFT (reward = win/loss cuối cùng) KHÔNG reliably produce social-deduction ability (Werewolf/Mafia peak 0.88 rồi rơi 0.38; Avalon avg 0.25) — nhưng phân tách reward thành social reading (belief inference scored vs hidden state) + social influence (message → downstream behaviour change) thì reading cải thiện rõ cross-model (Avalon team-alignment accuracy Qwen2.5-7B 0.55→0.78; wolf-set F1 0.46→0.65; gains mạnh nhất ở later evidence-rich states: Day-3 0.34→0.75). Full-game multi-agent social-cognitive RFT (GRPO, same-side training, terminal win = held-out diagnostic): 6-player Werewolf win rate 0.25→~1.0, 9-player 0.10→0.95–1.00, Avalon ~0→0.65–0.75; cross-model win 72–96% vs 9 opponents; blinded human eval +1.09/5 overall value, +1.16 influence, +1.17 strategic correctness (human-likeness chỉ +0.36, n.s.). Influence WITHOUT accurate beliefs là harmful: SI-only prompt cắt win rate Qwen3-4B 21%→12%.
→ Tiếp tục: [YES]

## Paper #163 — Attention Tax, Handoff Tax: A Stylised Model of When Multi-Agent LLM Systems Help (2610.06069v1) [applied]
✓ Skill: Attention-Handoff Tax — Đo curve + handoff tax, chọn single vs multi-agent | Test: SKILL VALID
✓ Insight: Mâu thuẫn single-agent-vs-multi-agent trong literature resolve qua 1 curve + 1 tax: decomposition thắng khi attention cost avoided by resetting context vượt handoff cost (crossover L* = max{2, ⌊2(h+λs)/(λk)⌋+1} linear regime); redundancy thắng khi shared-failure floor < thinking floor. Ledger experiment (gpt-oss-20b, 40,600 calls, 309M prompt tokens, ~$10): in-task curve 2.7%→71% failure (2k→36k tokens), handoff tax 0.026 nats (300-token notes), predict crossover depth 10 — decomposition won ở mọi tested depth (L=20: 0.69 vs 0.50, p=0.014; L=50: 0.24 vs 0.06, p=0.001; L=100: 0.11 vs 0.00, p<0.001) với prediction miss ≤9pp. Chunk size theo square-root law m* ≈ √(2h/(λk)) ≈ 4.8 steps. Pilot: cùng 1,000 calls cho curve FLAT (arithmetic 5.5%) và STEEP (format compliance 29.5%) — failure definition là 1 phần của curve.
→ Tiếp tục: [DONE — hết queue 2026-10-18]

## Paper #164 — Improving LLM Collaboration via Multi-Agent Preference Learning (2609.32827v1) [applied]
✓ Skill: mapl-multi-agent-preference-learning | Test: SKILL VALID
✓ Insight: Preference learning (học từ phản hồi so sánh) thay thế scalar reward (phần thưởng vô hướng) cho multi-agent collaboration (hợp tác đa tác tử): MAPL đạt pass rate (tỷ lệ đạt) 65.8% CoopHE / 76.4% Travel, vượt strongest single-agent baseline (đường cơ sở tác tử đơn mạnh nhất), chênh MAGRPO (oracle reward — phần thưởng chuẩn) dưới 1%; MARLHF (Dec-Dec) thậm chí vượt oracle ở CoopHE call rate (tỷ lệ gọi công cụ) 40.2% vs 37.9% và Travel success 13.1% vs 12.5% VÌ preference dataset (tập dữ liệu ưu tiên) có mật độ cao mẫu chất lượng tương đồng; comparator (bộ so sánh) tập trung/lớn hơn không cải thiện training VÌ information gap (khoảng trống thông tin) và realizability gap (khoảng trống khả năng hiện thực hóa) — Dec-Cen kém ở đa số domain (lĩnh vực).
→ Tiếp tục: [YES]

## Paper #165 — But How Would AI Agents Run a Town's Economy? (2609.11108v1) [applied]
✓ Skill: validated-agent-economy-simulation | Test: SKILL VALID
✓ Insight: Trong nền kinh tế mô phỏng 100 LLM agents (91 runs, 2.44M decisions, 21.5B tokens), cú sốc cầu 12× nâng doanh thu 4.62× = 1.50× extensive margin (biên độ rộng: 458 vs 304/762 doanh nghiệp giao dịch) × 3.07× intensive margin (biên độ sâu) — nhưng truyền dẫn tiền tệ DỪNG ở firm: wages 1.03× (p=0.42), wage share sụp 0.90→0.20, 0.27–0.32% menu items từng định giá lại; chuyển tiền NPR 5,000 ngẫu nhiên 96.7% còn giữ sau 311 pulses, MPC (xu hướng tiêu dùng biên) 3.3–4.0% ≈ 0 (so người thật 0.2–0.5); wealth persistence ρ 0.964 (2 tuần) → 0.832 (12 tuần) → 0.752 (26 tuần) — "đóng băng" là ảo ảnh horizon; ablation: đổi backing LLM làm đồng loạt mọi outcome (p=0.0039, effect 3–10×) còn xóa memory không ảnh hưởng gì; social tools fail 94–100% (chiếm 79.6% mọi tool failure) trong khi economic tools 96% success — aggregate success rate che failure theo class hành động.
→ Tiếp tục: [YES]

## Paper #166 — Social Gym and SPARTAN: Benchmarking and Improving LLM Social Reasoning via Multi-Agent Game Tournaments (2608.09128v1) [applied]
✓ Skill: SPARTAN Playbook Loop (Self-Play and Reflect-Transfer) | Test: SKILL VALID
✓ Insight: Social reasoning không phải scalar (vô hướng) duy nhất: Social Gym (21 game, 5 category, outcome do rule quyết định → verifiable, không cần LLM judge) cho thấy per-game inversion (đảo hạng) sắc nét — Qwen3-32B first on Chicken (1328 Elo) yet last on Werewolves (817) — và role gap (chênh lệch vai) thường favors minority/deceptive role, strongest models reverse under matched-capability self-play; Qwen2.5-3B last (926) vì parroting effect (hiệu ứng vẹt: lặp ý người nói trước = near-zero-information move cho phe lừa cover). Leaderboard: GPT-5-mini 1110 [1099,1120] 63.5%, GPT-4o 1030/47.5%, Gemma3-27B 1004/42.0%, GPT-4o-mini 998/40.5%, Qwen3-32B 968/33.9%, Qwen3-4B 961/33.2%, Qwen2.5-3B 926/25.6% (560+ episodes/model, BT-MLE anchor 1000, 95% bootstrap CI). SPARTAN (training-free, 3 stage play–reflect–transfer, playbook game-agnostic cover deception/detection/persuasion/information management/coalition dynamics/timing): pattern nhất quán "lift the weaker side" — within-game GPT-5-mini alt side (phe yếu cấu trúc) 24%→36/36/43/35% R1–R4 (peak R3) trong khi main side 76%→66/59/67/63%, bulk of gain đến ở R1 (trái giả định iterated reflection của Reflexion/Self-Refine: round thêm redistribute chứ không accumulate); cross-game 1→n alt-side median +7pp max +27pp, main-side median −7pp; multigame n→1 KHÔNG stack trừ held-out Resistance (Rwcsu 23%→47%); strong-to-weak distillation Rwcsu (chưa thấy Resistance) vào 6 students: Qwen3-32B/Qwen3-4B/GPT-4o-mini +13–24pp phía Spies, favored side ≤±5pp, Qwen2.5-3B/Gemma3-27B không gain. Open-weights Qwen3-32B largely null (capacity-dependent): chỉ Prisoner's Dilemma (action-channel, single discrete token) clean lift 13%→58% (+45pp), Resistance +34pp, 4 game còn lại flat, reflection codify cả parroting vào playbook; teacher Qwen3-32B: PD transfers +17–77pp, Resistance mixed. Limitations: n=30/condition (CI ±18pp), no placebo-playbook control, external validity (game cố định luật), reflection chỉ prose.
→ Tiếp tục: [YES]

## Paper #167 — Continuous Improvement and Parallel Autonomous Exploration: An LLM-Agent Framework for Searching Large Solution Spaces (2608.04341v1) [applied]
✓ Skill: Withheld-Leaderboard Reward Loop (WLRL) | Test: SKILL VALID
✓ Insight: Hai cơ chế để LLM agent duyệt không gian nghiệm lớn tự động: (i) withheld-test leaderboard (bảng xếp hạng chấm trên dữ liệu giữ lại) làm reward signal (tín hiệu phần thưởng) — loop hoạt động CẢ single agent (coverage 33.3% baseline → 47.8/57.4/49.4% qua iterative resubmission, 3 runs, qualification gate ≥95% P@1 mỗi category); (ii) N agents song song hoàn toàn tự động, no human in the loop, moderator logistics-only. Kết quả qualified coverage 5 agents: 62.8/69.4/68.2% (P@1 95.1, 105/238/103 qualified trên 274/550/301 submissions) vs single 47.8–57.4% (P@1 95.1–96.7). Finding replicate cross-runs, independent of agent count: single seeded agent mắc structural trap (bẫy cấu trúc) — cả 3 runs (60/124/81 submissions) chỉ iterate BGE-M3 variants, KHÔNG BAO GIỜ thử lexical/string baseline đơn giản, 1 run premature kết luận category khó nhất "không giải được" và dừng sớm; cả 3 5-agent runs tự diverge sang qualitatively different methods (TF-IDF re-ranking, string-similarity matching) trong vài phút. Gain tập trung category khó nhất (smartphone: single 0.8–1.9% vs parallel 24.8–41.1% coverage). Approach diversity: 5 agents α–ε đều start BGE-M3 → score-gap calibration (50.7%), BGE-M3+TF-IDF rescoring (55.3%), SequenceMatcher card-number re-ranking (65.6%), string+word/char-TF-IDF fusion (69.4% best), string-similarity re-ranking (63.6%) — non-embedding methods drive top results. Winning push đến LATE sau plateau (δ 27.5% first qualified → 65.6% plateau → 69.4% late fusion). Depth-for-breadth trade: single sâu/hẹp (P@1 cao hơn) vs parallel rộng/per-agent precision thấp hơn + GPU contention. Caveats: KHÔNG causal/agent-count claim (đồng biến compute, contention, visibility — descriptive ranges, không scaling law); decisive control = no-seed; cùng Claude Sonnet 3.5; infrastructure: append-only chat log, per-agent directory + read-only shared (agents THỬ reuse artifacts → chặn cấu trúc), pre-run leak check, 30-min CLAIM/RELEASE GPU lock + watchdog, moderator chỉ logistics (cảnh báo 30/5 phút, terminate deadline).
→ Tiếp tục: [YES]

## Paper #168 — When Truth Is Distributed: Misinformation Derails Collective Fact Recovery in LLM-Based Multi-Agent Systems (2608.03421v3) [applied]
✓ Skill: TIDE Paired-Deception Robustness Audit | Test: SKILL VALID
✓ Insight: ForesightSafety-TIDE (khung đánh giá có kiểm soát, built on Hi-ToM) chạy 120 environments × 2 paired conditions (C0 all-honest vs C1 key evidence holder deceptive) × 3 homogeneous systems (GPT-5.5, DeepSeek-v4-pro, Grok-4.5, temp 0, 5-checkpoint protocol T0/T1/R1/R2/R3) cho thấy aggregate truth recovery (phục hồi sự thật) sụp 72.50% → 14.17% (−58.33pp, individual vote −50.62pp), nhất quán cả 3 models — Grok-4.5 best C0 nhưng worst C1 (−79.17pp): strong honest aggregation KHÔNG hàm ý robust khi evidence contaminated. Cơ chế: false testimony adopted readily hơn true (adoption 70.7% vs 25.4%, +9.3pp) dù reference rates tương đương — deception không chặn correct info vào discussion mà hinders integration SAU disclosure; false root lan sâu hơn (propagation order 2.66 vs 1.33 tại R3) với asymmetric entry (82.87% true-only holders acquire false root vs 38.31% ngược lại); <45% dual-root holders vote truth. Discussion KHÔNG inherently corrective: divergence xuất hiện chủ yếu T1 (gap đã ~85% final magnitude), discussion chỉ thêm 8.89pp; C0 discussion +10.83pp truth majority còn C1 chuyển uncertainty thành decoy-majority (+15.83pp). Deceiver exit KHÔNG cứu vãn: False-Exit (nộp testimony sai rồi rút) ≈ C1, −46.67pp vs Null-Exit (placeholder vẫn 93/120 truth majority) — misinformation persists qua honest agents (R3 False-Exit: 273 agents vẫn reference, 197 adopt target). Observers không first-hand evidence: passive giảm decoy majorities 51→18, active giảm 90% nhưng KHÔNG improve truth recovery — buffer risk bằng cách chuyển sang uncertainty (provenance tracing makes observers cautious but not corrective). 3 deception forms: Event (fabricate move) most disruptive, Coverage → no consensus, Source most recoverable; decoy-vote share +44.0/+44.4/+37.9pp (95% CI), story-level paired p≥.20 → không có between-model difference. Design implication: verify evidence provenance (nguồn gốc), source independence (độc lập nguồn), propagation path (đường lan truyền) thay vì đuổi theo consensus.
→ Tiếp tục: [YES]

## Paper #169 — CURATE: Leveraging LLM Agents to Compose, Catalog, and Deploy Reproducible Workflows (2608.04270v2)
- **Nhãn:** [applied]
- **Làm gì:** Hệ thống 4 agents (WCA/MCA/MGA/WDA) + module catalog quản lý workflow suốt lifecycle: sketch → reify → test → deploy với 5 HITL gates. Catalog cho reuse modules across workflows (BM25 keyword search, entries có provenance/usage count). Prototype 6,700 dòng Python (LangGraph, Claude Opus 4.8), deploy qua FaaSr → GitHub Actions. 6 experiments: 4 SeBS-Flow (ML, MapReduce, video analysis, PDF+MapReduce+visualize) + 2 PyADM1 anaerobic digestion (data cleaning + 20× concurrent SRT sweep).
- **Kết quả chính:** E1 RF accuracy 0.850±0.002 vs 0.851±0.006 gốc (SVM identical); E2 word counts khớp ground truth verbatim; E3 đúng cars mọi frames, 0 runtime errors (baseline 0/3); E4 reuse 4 functions + gen 2 mới, word counts khớp; E5 clean raw digester data (units/gaps/spikes) nhưng MGA skip T-spike fixes (hard-code trong PyADM1) — WDA bắt được; E6 WDA phát hiện q_ad hard-code (178.4674) khiến SRT sweep vô nghĩa, suggest q_ad=V_liq/SRT, HITL approve → đúng. Token usage E5→E6 nearly halved nhờ catalog reuse. Baseline (Claude Code thuần): significant non-determinism, nhiều run 0/3 đúng, cần manual correction.
- **Insight nổi bật:** Catalog reuse nearly halved token usage đồng thời tăng reliability; 5 HITL gates catch decomposition errors trước code generation; post-run agent (WDA) phát hiện bug mà generation agent missed — separation of duties.
- **Skill:** CURATE Lifecycle Loop (Sketch–Reify–Test–Deploy with Module Catalog) — SKILL VALID
- **Link:** papers/2026/10/19/curate-workflow-lifecycle-agents/

## Paper #170 — MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering (2610.22344v1)
- **Nhãn:** [applied]
- **Làm gì:** Mô hình tác tử 35B MoE (khởi tạo Qwen3.6-35B-A3B) tự làm machine learning engineering dài hạn: Kaggle-MLE Factory (multi-agent pipeline discovery→analyzer→generator + validator checks + manual review) xây executable tasks từ Kaggle lịch sử; Interaction Harness (ReAct loop, experiment tree, execute_code/update_answer/analyze sub-agent/invalidate_node); Hierarchical agentic SFT (Stage 1 general coding/tool-use, Stage 2 MLE-domain với outcome-guided trajectory trimming tại first best submission); WIRL (Windowed Interaction RL) group decisions giữa 2 experiment results thành execution window với shared outcome reward (−1.0/−0.6/−0.4+T/1.0+T/2.0+T, T∈{−0.2,0,0.2} trend) + async collection + token-level policy correction.
- **Kết quả chính:** MLE-Bench Lite (22 tasks): medal rate 37.9%→72.7% (+34.8pp; Med+ 84.8%, Gold 50.0%, Silver 16.7%, Bronze 6.1%) — cao nhất same-scale (Ornith 39.4%, Nex 47.0%), comparable GLM-5.3/Kimi-K3 (72.7%), GPT-5.6 Sol 77.3%; Claude Code harness: 69.7% vs base 42.4% (+27.3pp, +22.7pp so với strongest same-scale); NatureBench Lite: Match-SOTA 40%→70%, Surpass-SOTA 0%→50% (Nex 20%, GLM 50%); ablation 37.9→47.0→62.1→72.7; RL từ MLE-SFT: GRPO 56.1% và PPO-style 60.6% ĐỀU dưới baseline 62.1%, WIRL w/o trend 66.7%, w/o correction 65.2%, full 72.7%; MLSP 2013 Birds ROC-AUC 0.58→0.964 (vs SFT 0.60→0.88); AIME scaffold GPT-4.1-nano held-out 43.7% vs 23.3% (calls 1.00→9.39); MLS-Bench-Lite verifier reward 0.322→0.425 (10/12 tasks tốt hơn).
- **Insight nổi bật:** Execution-window credit assignment (thưởng chung cho cả window + trend bonus ±0.2) ổn định hơn trajectory-level reward — GRPO/PPO-style đều thua baseline; outcome-guided trimming (cắt tại first best submission khi post-peak degradation vượt threshold) giữ exploration + failure recovery mà loại degraded tails.
- **Skill:** Windowed Interaction RL (WIRL) cho Long-Horizon Agentic Tasks — SKILL VALID
- **Link:** papers/2026/10/19/mlexpert-autonomous-mle/

## Paper #171 — Bayes-Sufficient Compression Is Not Enough: How Does Communication Help Multi-Agent Systems? (2610.03769v1)
- **Nhãn:** [applied] — framework hình thức (receiver-relative bounded coordination, 4 theorems) + evaluation 6 benchmark families thật (BFCL, ToolSandbox, ContextBench, RepoBench, SWE-bench Lite, τ-bench), 7 models, code github.com/Yydc/Communication
- **Skill tạo được:** Receiver-Relative Protocol Selector (Gain − Tax Communication Control) — evaluation-method/workflow
- **Skill test:** [SKILL VALID] — dry-run "pipeline researcher→writer 10 bài": calibrate 40% records → selector ~0.74 accuracy; writer RO 0.7 > crossover 0.63 → early-skip (919 tokens/6.6s vs 3,085 tokens/9.56s always-send); writer RO 0.4 → compress 128-token brief; monitor h_a 0.74 vs h_action 0.55 → closure-dominated → fix receiver schema. Output có nghĩa.
- **Insight nổi bật nhất:** Message utility = receiver gain − protocol tax (Communication-Tax Identity U = R(0)−R(1) = A*−τ): cùng 1 Qwen protocol nâng ContextBench 0.633→0.775 nhưng hạ ToolSandbox 0.889→0.653 — compression sign flips theo receiver+task; Bayes-sufficient compression vẫn fail khi surface form không receiver-usable (strict-recoding −13.5pp τ-bench; fixed-message replay: MiniMax-M2.5 phục hồi artifact 61.3% nhưng action-conversion chỉ 5.3%, closure 60%); stronger sender chỉ giúp trên receiver-burden threshold ~0.63 RO accuracy (41 anchors, 89.5% single-crossing); selector ContextBench 0.7367 accuracy/1,735 tokens — +8.67pp over always-skip với 46.4% fewer tokens than always-send.

**Số liệu chính (verified từ PDF):** Qwen protocol (Qwen3.5-9B receiver, Qwen3-Next-80B-A3B sender, B=128): ContextBench 0.633→0.775 (+0.142; bootstrap +0.1711 CI [0.1417,0.2012], 2,390 steps/799 instances), RepoBench 0.642→0.833 (+0.19; bootstrap +0.1611 CI [0.1340,0.1891]), ToolSandbox 0.889→0.653 (−0.236), BFCL 0.980→0.750 (−0.23), τ-bench 0.139→0.139, SWE-Lite +0.48. Truncation control: capped +10.64pp (404 messages, CI [5.7,15.8]), uncapped +32.89pp (76, CI [22.4,43.4]). Strict-recoding: −13.5pp τ-bench, −6.0pp ContextBench, −3.5pp ToolSandbox, BFCL unchanged. Replay (DeepSeek-V3.1 messages): GLM-5 h_j 0.382/h_a 0.741/h_action 0.545/closure 57%; MiniMax-M2.5 h_j 0.036/h_a 0.613/h_action 0.053/closure 60%. Parsing audit (gpt-5.4 sender): wrong-action 44.5% GLM-5, 94.0% MiniMax-M2.5, 40.8% o3 (chọn read khi action là edit). Stronger-sender: +52.1pp SWE-Lite, +21.0pp ContextBench, +8.8pp RepoBench; −26.4pp ToolSandbox, −16.0pp BFCL, −2.8pp τ-bench. Threshold 0.6289 CI [0.552,0.706] (41 anchors; 34/38 = 89.5% single-crossing; 12,540 paired steps, 10 folds). Selector: ContextBench n=300 → 0.7367 @ 1,735 tokens (always-skip 0.6500 @ 1,300; always-send 0.7867 @ 3,235.4; +8.67pp, −46.4% tokens); ToolSandbox online 36 steps: early-skip 1.000 @ 919.4 tokens/6.60s vs always-send 0.8056 @ 3,085.4/9.56s; calibration 5–40% → 0.7368–0.7458; learned-router 0.5692 vs GBM 0.5191; τ-bench failure: rewriting 0.139 > selector 0.083. OpenAI extension (sender gpt-5.4): ContextBench gpt-5.4 0.600→0.853; ToolSandbox gpt-4o-mini 0.803→1.000 (regime thuộc receiver+protocol+task).

→ Tiếp tục paper tiếp theo? YES (còn 2 paper HIGH trong queue: 2608.02758v1 80đ, 2608.06865v1 79đ, 2609.03674v1 79đ)

## Paper #172 — Everyone Conforms, No One Believes: Pluralistic Ignorance in LLM Agent Populations (2608.02758v1)
- **Nhãn:** [applied] — benchmark 100 scenarios (10 domains × 5 authority levels, grounded in human PI literature) + 800 runs trên 8 models/6 organizations + prompt ablation 2×2 + keyword scorer validated vs human (82% agreement, conservative ~12pp)
- **Skill tạo được:** Pluralistic Ignorance Simulation Protocol (PI-Sim) — evaluation-method/workflow (3-phase: private probe → group discussion → norm entrepreneur intervention + cascade metric + ablation debug)
- **Skill test:** [SKILL VALID] — dry-run "norm video <60s cho audience 30+, 20 agents": Phase 1 16/16 privately oppose → Phase 2 conformity 85% (PI exists) → Phase 3 cascade 20% (<26%, norm dai dẳng) → re-probe agents estimate 45% vs true 80% (gap 35pp = second-order belief error) → ablation Neither 70% (emergent, not instruction-driven). Output có nghĩa.
- **Insight nổi bật nhất:** Pluralistic ignorance (đa số privately oppose nhưng publicly conform, mỗi người tin mình cô đơn) là emergent property của LLM agent populations — persists 52–92% ngay cả khi bỏ cả false-consensus statement lẫn fit-in goal; cascades gần như không xảy ra (7/8 models <26%, Kimi-K2.7 = 0%) → LLM simulations systematically overestimate norm stability, missing fragile tipping-point dynamics; model selection là unacknowledged degree of freedom (conformity varies 30pp, uncorrelated with capability — Spearman ρ=0.07).

**Số liệu chính (verified từ PDF):** Table 2 (conformity % / PI scenarios / cascade %): GPT-4o-mini 64.2/69/14, DeepSeek V4 Pro 79.0/83/15, Qwen3 235B 81.6/91/26, GPT-4o 86.9/96/48, Claude Sonnet 4.6 89.5/92/6, GPT-OSS-120B 91.9/100/10, Llama 3.3 70B 92.1/96/9, Kimi-K2.7 93.7/100/0. Domains: social relationships 96%, workplace 90%, campus 87% (cao nhất); political 78%, technology 80% (thấp nhất, vẫn >50%). Authority: 80% (L2)–88% (L1), no monotonic effect — weak peer signal ≈ top-down mandate; Kruskal-Wallis domain H=59.3 p<0.001, model H=148.6 p<0.001. Intervention: 6/8 models drop <10pp; GPT-4o drops 29pp (87%→58%); moderate social hints > explicit statistical disclosure cho responsive models. Ablation (Full/No FC/No Goal/Neither): GPT-4o-mini 64.2/62.7/52.4/53.3, Qwen3 81.6/76.8/72.3/69.1, GPT-4o 86.9/84.1/65.2/66.1, Claude 89.5/79.3/72.4/70.1, DeepSeek 79.0/97.4/89.9/89.3, GPT-OSS 91.9/90.1/83.5/83.5, Llama 92.1/74.9/55.4/52.4, Kimi 93.7/92.0/93.6/91.6. Mean effects: No FC −3.2pp (conformity driven by observing conversation, not being told), No Goal −14pp (amplifies but doesn't generate), Neither persists 52–92% → emergent. Two regimes: promptable (GPT-4o-mini, GPT-4o, Llama, Claude, Qwen) drop 15–40pp when goal removed; intrinsically conformist (DeepSeek, GPT-OSS, Kimi) stay >83% under all conditions. Second-order belief errors: underestimate true 80% opposition by 14–38pp. Capability-independent: Spearman ρ=0.07 p=0.87; Education 49% (GPT-4o-mini)–99% (Llama 3.3 70B) = 50pp spread same scenarios.

→ Tiếp tục paper tiếp theo? YES (còn 2 paper HIGH trong queue: 2608.06865v1 79đ, 2609.03674v1 79đ)

## Paper #173 — Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection / ARGUS (2608.06865v1)
- **Nhãn:** [applied]
- **Skill:** ARGUS Four-Perspective Forensic Audit
- **Skill test:** [SKILL VALID] — dry-run video testimonial: 4 agents (texture "plastic-like fingers" + lighting "unchanged indoor→outdoor" + motion "finger color change" + physics "balloon-like fingers") → judge verdict FAKE + explanation
- **Insight nổi bật nhất:** Phân rã forensic analysis thành 4 independent perspectives (texture/lighting/motion/physics) + judge reconcile beats single holistic judgment: F1 47.45% (Gemini-2.5-Pro, strongest single) → 53.28% (+5.83pp) trên 20 OOD generators unseen trong training, bằng small open-source Qwen2.5-VL-7B; texture cues mạnh nhất (recall 97.40%); multi-turn/CoT prompting KHÔNG giúp (thậm chí hại: CoT F1 11.29 < Single 13.24) — improvement đến từ specialization + reconciliation, không phải longer reasoning.

**Tóm tắt:** FaceVid-Forensics-100K: 100,000 videos (21,075 real + 78,925 fake), 33 synthesis methods (face swapping/reenactment/entire-face synthesis: T2V/I2V/TI2V/V2V) bao gồm Seedance 2.0, Sora 2, Kling — lớn nhất + duy nhất có fine-grained textual labels (observations + verdict-consistent explanations trên 4 dimensions). Labels do 5 MLLM annotators (GPT-4o, Gemini 3.5-Flash, Qwen2.5-VL, Skyra, VideoVeritas) + DeepSeek-V4 Pro aggregator (ground-truth-guided conflict resolution, reverse inference khi all annotators wrong). Framework: 4 observation agents (texture/lighting/motion/physics) independently produce textual observations KHÔNG predict verdict → judge agent reconciles + optionally xem video → binary real/fake + explanation. Training: SFT (observation agents trên dimension labels + judge trên concatenated observations) + GRPO (judge only, G=8, binary accuracy reward, group-normalized advantage, KL penalty). OOD results: Acc 69.87%, Recall 81.82%, F1 53.28% (w/ Video) — best across all metrics; beats small vision models (DFGaze 27.24, Effort 44.76, TFCU 45.20 F1), open-source MLLMs (Qwen2.5-VL-7B 13.24, Qwen3.6-35B-A3B 35.72), closed-source (GPT-4o 37.55, GPT-5-mini 39.00, Gemini-2.5-Pro 47.45, Gemini-3.5-Flash 46.22), forensics-tuned (Skyra 38.30, VideoVeritas 43.22). Ablation: texture-only best single agent (F1 44.53); all-four 47.53; joint SFT 47.53 → +GRPO 51.01/53.28; Only-Obs recall 99.58% nhưng F1 40.46 (precision thấp).

→ Tiếp tục paper tiếp theo? YES

## Paper #174 — LLM4AIGQ: LLM-based AI Guidance Query Generation Framework for Multi Interest Mining (2609.03674v1)
- **Nhãn:** [applied]
- **Skill tạo được:** Multi-Interest Guidance Query Generation (SFT-RL-DPO) — framework/workflow
- **Skill test:** [SKILL VALID] — dry-run "Shopee seller, customer history trộn máy ảnh + cà phê": compress 50 behaviors → teacher segment 2 clusters → RL sinh 3 queries/cluster + confidence → DPO non-thinking JSON → nearline update → online retrieve; output 2 labels × 3 queries, S ratio ~0.86, uCTR +2.5–4.5%
- **Insight nổi bật nhất:** Multi-interest segmentation trước khi sinh query (S ratio 0.8616 vs 0.6405 backbone, +22.1pp top-rated queries) + DPO distill think→non-think giữ 96% gain (win rate 57.53%→54.95%) + online A/B test Tmall +4.46% uCTR (10% traffic) / +2.53% (40% traffic, 6 ngày) — deployed hundreds of millions users.

## Paper #175 — Iterate on an LLM, Serve on an SLM (2610.14576v1) [applied]
✓ Skill: iterate-on-llm-serve-on-slm | Test: SKILL VALID
✓ Insight: SLM có thể ổn định hơn chính teacher đã định nghĩa nó, vì teacher không deterministic (chỉ đồng ý với bản thân 72.7% thời gian) nên đóng vai trò noisy annotator chứ không phải ground truth; phát triển hành vi trong prompt space trên frontier model rồi distill vào SLM qua dữ liệu production thực.
→ Tiếp tục: [YES]

## Paper #176 — Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs (2610.23707v1) [applied]
✓ Skill: tool-recommendation-multi-step-agents | Test: SKILL VALID
✓ Insight: Completeness@10 quan trọng hơn Recall@10 vì thiếu một công cụ trong chuỗi nhiều bước khiến tác vụ thất bại; mỗi lần tìm kiếm thêm một lượt gửi lại toàn bộ cuộc trò chuyện nên tần suất tìm kiếm quyết định xem recommendation có rẻ hơn danh sách tĩnh hay không (ngưỡng ~0.63 tìm kiếm/lệnh gọi công cụ).
→ Tiếp tục: [YES]

## Paper #177 — TRACER: Trace-Regularized Training Against Indirect Prompt Injection (2610.19133v1) [applied]
✓ Skill: tracer-trace-regularized-training | Test: SKILL VALID
✓ Insight: Cùng payload giữa injection thành công 53% ở retrieved context vs 18% ở follow-up (authority gradient); TRACER giảm RAG-framed ASR từ 65.5% xuống 6.1% giữ clean accuracy 78-82% qua phần thưởng gated bằng chứng + ATRC trace alignment; đào tạo đa kênh (RAG+tool) đạt average ASR 13.9% tốt nhất tại 3B.
→ Tiếp tục: [YES]

## Paper #178 — Be Careful Who You Trust: Coordination Dynamics under Corrupted Communication in LLM Multi-Agent Games (2609.31704v1) [applied]
✓ Skill: be-careful-who-you-trust | Test: SKILL VALID
✓ Insight: Sự sụp đổ phối hợp công khai dưới corruption chủ yếu là cơ học (hành động bị đảo ngược thay đổi transcript và thực thi), không phải hành vi agent; phải tách lựa chọn gốc / hành động công khai / kết quả thực thi khi đánh giá độ mạnh đa agent.
→ Tiếp tục: [YES]

## Paper #179 — Forty Shades of Blue: Quality-Diversity Alignment via Mode-Conditioned Reinforcement Learning (2609.14896v1) [applied]
✓ Skill: forty-shades-of-blue-moda | Test: SKILL VALID
✓ Insight: Mode collapse là sản phẩm phụ của alignment; MODA dùng role conditioning trong policy chia sẻ (mỗi mode = agent MARL cạnh tranh) + cổng chất lượng tùy prompt để tăng SBERT diversity +265% (Infinite-Chat) và +75.9% so với DivPO, đồng thời giữ/tăng năng lực chung +10.3%.
→ Tiếp tục: [YES]

## Paper #180 — Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions (2610.22138v1) [applied]
✓ Skill: believed-but-not-said | Test: SKILL VALID
✓ Insight: Một agent đối đầu gây FPI 44.8% (ba agent 60.5%); nhiễm ẩn (51.6% tư liệu riêng vs 19.7% tán thành công khai) lớn gấp 2.6 lần những gì transcript lộ; kiến thức không dự đoán độ mạnh (85% kiến thức nhưng từ bỏ 25% vs 80%); nhiễm ổn định vào vòng 4, can thiệp phải sớm.
→ Tiếp tục: [YES]

## Paper #181 — When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning (2610.04686v1) [applied]
✓ Skill: when-debate-helps | Test: SKILL VALID
✓ Insight: Đắn giúp khi cung đề xuất bề mặt câu đúng (headroom có thể phục hồi) VÀ đọc nhận diện câu đúng khi bình chọn bỏ lỡ (LVD bằng chứng xác thực); một trong hai không đủ; hội đồng được chọn qua coverage (AC-Greedy/SC-Greedy) tạo nhiều đề xuất đúng bổ sung hơn top-score.
→ Tiếp tục: [YES]

## Paper #182 — Candidate supply and answer selection shape the value of LLM judging in multi-agent systems (2608.25937v2) [applied]
✓ Skill: candidate-supply-answer-selection | Test: SKILL VALID
✓ Insight: Đáp án đúng thường đã có trong ứng viên nhưng hệ thống vẫn báo cáo sai (khoảng cách tạo–giữ 13–14 pp); độ tin cậy judge không cố định, rank ASEAN half-rise midpoint pgen = 14.7%; kết hợp tần suất bình chọn + xếp hạng judge nâng 63.82% lên 70.82–70.95%, cứu đáp án đúng bị quá số bởi lỗi phổ biến.
→ Tiếp tục: [YES]

## Paper #183 — RIT-RAG: Navigating Document Corpora with Retrieval-Induced Trees (2610.11370v2) [applied]
✓ Skill: rit-rag | Test: SKILL VALID
✓ Insight: Phân cách khám phá bằng chứng khỏi đọc nội dung — truy xuất đảm bảo độ thu hồi, cấu trúc truy xuất đảm bảo độ chính xác; không cam kết vào tài liệu duy nhất trước khi thấy nội dung; RIT-RAG cao nhất trên WixQA, QASPER, FinanceBench, EntQABench (2,84M trang), +6.6–11.4 điểm so với cơ sở tốt nhất.
→ Tiếp tục: [YES]

## Paper #184 — Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense Retrieval (2609.05110v1) [applied]
✓ Skill: embedding-surgery | Test: SKILL VALID
✓ Insight: Nhúng embedding cố định sau khi huấn luyện gây cứng nhắc; phẫu thuật embedding áp dụng cập nhật cục bộ, tối thiểu vào embedding tài liệu tại thời điểm truy vấn qua bài toán tối ưu hóa凸 (bài toán tối ưu hàm bậc hai), ép buộc ràng buộc xếp hạng, tối thiểu hoá sự thay đổi biểu diễn; đối xứng hiệu quả nhất, lên đến +60.64% tương đối nDCG@10 trên DL-Hard, mạnh mẽ trước phản hồi nhôound, lan truyền đến truy vấn ngữ nghĩa liên quan, bổ sung CoRocchio.
→ Tiếp tục: [YES]

## Paper #185 — MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups (2610.23480v1) [applied]
✓ Skill: munin-self-hosted-agent-harness | Test: SKILL VALID
✓ Insight: Harness chứ không phải model là đơn vị cải tiến — cùng harness nhân đôi accuracy trên 3 backbone 2 nhà phát triển (0.387→0.874 Qwen3.8-27B, +0.487 CI [0.407,0.568]); naive RAG top-5 KÉM HƠN bare model trên mọi backbone (−0.176 đến −0.306) vì retrieval không có verification loop là hại ròng; abstention đo được không cần judge: xóa 49 source papers + 2,247 chunks khỏi corpus → hệ thống từ chối 86–92% (Qwen) / 80% (gpt-oss) với 0 citation bịa trên 100 tài liệu giả × 3 backbone; đọc toàn văn 1 call beats summarise-then-reason (0.497→0.864); egress là biến thực nghiệm worth +0.17–0.21 accuracy, egress=off vẫn vượt PaperQA2 66.0%.
→ Tiếp tục: [YES]

## Paper #186 — Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent Workflows (2610.21411v2) [applied]
✓ Nhãn: applied — 4 benchmark (MATH, MBPP+, API-Bank, IDRBench I3), 2 backbone (DeepSeek-V4-Flash, GPT-5), AutoGen
✓ Skill: capability-matched-agent-coordination | Test: SKILL VALID (dry run: gate TPR 91% vs LLM judge 93%, token −33%, ACC trong ±1,34 điểm)
✓ Số liệu: routing+review chiếm 31,7–43,5% token MAS; vs LAS token −12,7–54,6%, accuracy chênh ≤1,34 điểm, latency −(7/8 cấu hình, −45,8% IDRBench I3 DeepSeek, −50,2% API-Bank GPT-5); robustness tiêm lỗi: Attack-MAS ASR 50%→Jev-LiteMAS 3,33–4,00%, accuracy 46,67→94,00% (MATH); screener Jev TPR 95,33%/91,33% gần LLM judge 96,67%/92,00%, SLM generic chỉ 61,33%/44,67%; content-blind routing mất 18,0 điểm accuracy; decision layer overhead chỉ 1,56–2,14% chi phí + 2,92–6,85% latency
✓ Insight nổi bật nhất: Coordination trong MAS chỉ cần bounded decision — tách "decide" (decision model Jev) khỏi "generate" (LLM expert) cắt 12,7–54,6% token với accuracy trong ±1,34 điểm, nhưng router NHÌN THẤY artifact thật mới giữ được accuracy (−18 điểm nếu content-blind)
→ Tiếp tục: [YES]

## Paper #187 — How language model agents reshape price competition (2610.21711v1) [applied]
✓ Skill: llm-pricing-deployment-audit (framework/evaluation-method) | Test: SKILL VALID (dry run: X self-play ∆ 0.88 consumer 15% vs Y 0.05 consumer 95% → regime map + launch Y block X)
✓ Insight: Cùng foundation model chọn regime đối lập (0.88 vs 0.05 elevation) chỉ bằng thay deployment interface — information interface (hide rival + summary history) chứ không phải output type quyết định; D-S-25 lấy 71–72% industry profit qua undercut nhanh, P-R-1 qua anchor-and-harvest; consumer share 15% vs 95%.
→ Tiếp tục: [YES]

## Paper #188 — EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs (2610.22412v1) [applied]
✓ Skill: enterprisesynth-bootstrap (workflow/framework) | Test: SKILL VALID (dry run: CRM 10 endpoints → 38 params sau 2 fix, verifier 93%→100% sau adversarial fix, held-out TSA 66.2±18.0 vs base 12.5, arg-level end-to-end ~21%)
✓ Insight: 45 verified trajectories từ spec thân zero-execution lift 0.5B model 12.5→87.5% trên held-out API; verifier phải adversarial-test (initial 57–80% → 98%); endpoint accuracy 48.9% nhưng end-to-end (arg+values) chỉ 21.3% — cold-start genuine grounding evidenced by private specs 40.0% ≈ public 39.6%.
→ Tiếp tục: [YES]

## Paper #189 — Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents (2610.18007v1) [applied]
✓ Skill: local-contract-privacy-enforcement (framework/workflow) | Test: SKILL VALID (dry run: baseline 11.4%/28.2% leak, CostAmp 1.32× → wrapper 4.0%/18.8%, CostAmp 1.02×, usable 92.6%, remote −36.6% attack)
✓ Insight: local contract-conditioned rewriting (Gemma 4B local + information-release contract 4 fields) trước checker: leakage 11.41→4.03% normal / 28.19→18.79% attack, remote tokens −17.6%/−36.6%, checker-call amplification 1.69×→1.02×, utility TĂNG (85.2→92.6%) — contract beats generic privacy prompt 36.3–54.1% relative.
→ Tiếp tục: [YES]

## Paper #190 — SAG2: Embedding-Free Multi-Hop Retrieval with BM25 and JEV (2610.22588v1) [applied]
✓ Skill: sag2-sqlite-bm25-jev-retrieval (framework/workflow) | Test: SKILL VALID (dry run: help-center 500 docs → index 1.2s/11MiB, R@10 85%, 331 judgments/question, $0.87/20 queries; no-context variant 65% validates context role)
✓ Insight: multi-hop RAG không cần vector DB/embedding service — 1 SQLite FTS5 + BM25 + JEV decision model (hosted): R@10 86.62%/97.43%/99.00% (MuSiQue/2Wiki/HotpotQA), beat mọi 7B embedding model + SAG +3.25–3.86pp; index 11,656 passages 2.36s/25.87MiB/$0 offline; $4.33/1,000 queries; expansion 2 rounds beat one-shot pool matched judgment +16.80pp; shared context đóng góp −10.37pp khi bỏ; EnterpriseRAG 511,962 docs doc-recall 81.10% vs BM25 68.4/Vector 46.0.
→ Tiếp tục: [YES]

## Paper #191 — Designing for Imperfect Prompts: KG Semantic Mediation for Enterprise Data Assistant (2610.23304v1) [applied]
✓ Skill: kg-semantic-mediation-layer (framework/workflow) | Test: SKILL VALID (dry run: DB 15 tables/90 columns → KG 2 phút, Precision 93.75/Recall 88.24/F1 90.9%, completeness 95% ≥ baseline)
✓ Insight: user prompts enterprise cực ngắn (1,14 câu/~10 words, 0/158 có schema reference) → KG tự build từ schema (273 nodes/540 edges, NetworkX + ChromaDB + text-embedding-3-large) mediate prompt: GPT-4.1 Precision 90.67% (schema-only 69.05%, +21.62pp), F1 89.47% (71.02%); Claude Sonnet 4 F1 90.29% (82.17%); completeness KG 93.04% > baseline 91.14% (intent preserved dù inject DB content); schema-only hallucinated joins → downstream execution reliably fail; demo audit-requests: KG 21 nodes/30 edges đúng, schema-only chọn nhầm audit_status table; latency 2.7s vs 1.1s; paper typo cảnh báo: prose ghi GPT-schema completeness 85.33% nhưng table = 89.24% (85.33% là Claude baseline).
→ Tiếp tục: [YES]

## Paper #192 — Asymmetric Dynamic Routing (ADR) for Hypergraph RAG (2609.29282v2) [applied]
✓ Skill: asymmetric-dynamic-routing-rag (framework/workflow) | Test: SKILL VALID (dry run: KG 1,800 entities/140 insight vertices, 15 queries → 5/6/4 route đúng, avg 240ms/1,950 tokens, judge 84.1 vs static 82.3)
✓ Insight: "static retrieval fallacy" — traversal depth uniform cho mọi query waste token (simple) + thiếu context (complex); ADR classifier (γ=0.75, fallback Moderate) + 3 toán tử bất đối xứng: Simple→fact anchoring zero-hop, Moderate→bottom-up diffusion HD, Complex→top-down insight grounding π−1-grounded facts: latency 435→238ms (−45.3%), prompt tokens 3,760→1,929 (−48.7%), quality 82.05→83.91 (+1.86) TRÊN DHI baseline; beats best frozen mode mọi dataset +0.94–+2.11 (Mix 83.91, CS 85.24, Agri 83.86, Neuro 85.02, Patho 86.65); depth thừa hại dense corpus (Moderate-only thắng Complex-only +1.39–1.51, Agri/Patho) nhưng sparse corpus CS Complex-only 83.13 > Moderate 82.14; γ=0.50 → Logicality −1.14, γ≥0.85 → 68.4% fallback +58ms vô ích; pathology causal query: Complex-only 3,850 tokens tangential (EGFR irrelevant) vs ADR 41.2% fewer tokens, causal chain 2-HG→α-KG dioxygenases→epigenetic remodeling grounded IDH1 R132H facts.
→ Tiếp tục: [YES]

## Paper #193 — MEMORILLA: Latent Semantic Memory for LLMs (2610.21375v1) [applied]
✓ Skill: latent-semantic-memory-compression (framework) | Test: SKILL VALID (dry run: 800 chats + 300-doc KB, K=16 module trained 3-stage curriculum → preference QA 8/10 vs RAG 4/10, FactKG-like 84% vs full-context 80%, 41 tokens/query vs 12,000; TextWorld loop pass@3 0.35 vs ICL 0.24)
✓ Insight: Tách persistent storage khỏi per-query context — frozen Qwen3-Embedding-4B embed corpus 1 lần → store ZD query-independent; trainable module 194M params (K=16 slots: query conditioning → Perceiver-style cross-attn TOÀN BỘ N docs → projection) trả K soft memory tokens prepend vào input embedding frozen Qwen3-8B, KHÔNG đổi 1 layer LLM nào: trung bình 49.68 beat mọi baseline (xRAG 41.92, LLMLingua-2 40.75, Mem0 38.02), Pareto frontier MỌI benchmark trong 8 (PMv2, LaMP-4/7, PV4, NarrativeQA, TriviaQA, FactKG, PubMedQA); token geometric-mean 394×/113×/49× ít hơn full-context/RAG-50/MemoRAG (range 20–4,212×, >4,000× compression); FactKG 84.33% vs full-context 80.43% (108× fewer tokens) — advantage grows +4.23pp (1 entity) → +7.59pp (4+ entities), stable 80–89 across composition depths khi RAG-50 drop 78.73→51.75 (facts 1→4); TriviaQA EM 57.00 (743× fewer tokens); PMv2 44.60 vs xRAG 30.90 — full context dùng 1,974× MORE tokens nhưng KHÔNG cao hơn (trails trên 20/21 metrics, "full context is not an upper bound"); latency 0.74s vs 19.9s; LaMP-4 18.15 vs 14.21 ROUGE-L (474×).WHERE memory không giúp: verbatim recall — MemoRAG thắng NarrativeQA 21.80 ROUGE-1 + PV4 67.88% (cần 50×/690× tokens); PubMedQA nhỏ (324 tokens) MEMORILLA 59.00 thua LLMLingua-2 69.00 — gains chỉ large collections. Phân tích: "why/how" +4.91/+7.02 (compression giữ global structure), "who/which" RAG +3.45/+2.93 (surface tokens) → hybrid memory+retrieval (union oracle > either MỌI benchmark; FactKG 15.9% MEMORILLA-only vs 10.0% RAG-50-only, PMv2 27.1% vs 9.2%). TextWorld continual learning: memory module random-init + GRPO (K=8, sparse reward) — avg@3 0.186→0.242, pass@3 0.250→0.375 vs full-history ICL; untrained memory WORSE (0.153/0.225) = value từ learning; 37.5% games ≥1/3 attempts vs 25.0%; escape navigation loops + keyed action sequences; ICL exhaust budget 71% vs 58% rollouts. Joint-error: FactKG both-methods bias false — true claims 89.5% joint-wrong vs 28.7% joint-right → miscalibrated threshold; PV4 errors = combining failures không phải finding failures. Limitation paper thừa nhận: mất fine-grained facts (encoder never trained for compression), Qwen pairing only, coding domains untested, gains mainly large collections, privacy stored embeddings (consent; deletable on request). KHÔNG nói: PV4 synthetic GPT-5 personas, PMv2/PV4 eval cosine-nearest-neighbor predefined choices (free-form unverified), TextWorld toy env, training heavy (3.3M examples + 2 frozen 4B/8B).
→ Tiếp tục: [YES]

## Paper #194 — Can LLMs Fix It Without Code? No-Code Bug Fix Execution Verification (2610.11963v1) [applied]
✓ Skill: no-code-fix-execution-verification (evaluation-method/workflow) | Test: SKILL VALID (dry run: 15 candidate reports → 4 issues qua gates (26.7%), 27 fixes × 2 executors × 3 runs = 162 episodes, resolution 18–44% vs 41%, all-agree 47%; human calibration 82% (κ=0.71) vs 68% (κ=0.30, 10/12 false positives))
✓ Insight: Rollback-based execution pipeline verify LLM-generated no-code fixes trong Brave browser thật (Docker pinned builds): GT fix apply → scripted sanity gate #1 (bug ABSENT fixed state) → scripted rollback → sanity gate #2 (bug PRESENT buggy state) → executor agent (Sonnet 5 computer-use / OpenCUA-72B / Muse Glimmer-30B) apply fix ≤20 steps GUI → deterministic issue-specific checker (DevTools Protocol) quyết định — executor's own DONE claim NEVER là verdict. 302 annotated reports → 51 candidates → chỉ 9 issues re-establishable (17.6%; 38 không setup Linux container, 4 không exhibit bug). RQ1 322 fixes (12 configs × 3 runs × 9 issues): resolution 49.7% Sonnet 5 / 45.7% OpenCUA / 14.6% Muse Glimmer; applicability 66.1%/99.1%/70.5%; resolution-among-applicable 69.5%/45.8%/18.1%. V-Claude best 74.1% dưới Sonnet 5 (applicability 88.9%) NHƯNG 3rd dưới OpenCUA (51.9%) + 2nd dưới MG (25.9%) — rankings Kendall τb 0.13/0.45/0.05 nearly unrelated. RQ2: executor choice shift single-config resolution 38.8% average (range 25.9–48.1, CI 31.2–52.1) trong khi within-executor run spread ≤3.4pp — systematic không phải noise; all-3 executors same verdict chỉ 46.9% (pairwise 62.4–67.1%, κ 0.25–0.30); excluding version-dependent issues agreement DROP (κ 0.22/0.24/0.17, all-agree 40.7%); any-run aggregation +38 fixes OpenCUA (least stable, runs 33.9/38.8/31.1%) vs +12–24 others, majority vote 39.8/30.7/9.9 ordering unchanged. Per-instance cực đoan: 37372 OpenCUA 36/36 (checker lenient — expected value = browser default không stored explicitly → settings reset counts) vs S5 20/MG 12; 24747 S5 19 vs OC 0 MG 0; version-dependent S5 16/18/29 (22252/25379/31108), 25379 OC 3 (update alone insufficient — must choose gradient), MG 0. RQ3 humans (75-fix sample, double-blind "execute literally", authors 78.7% agree κ=0.54): Sonnet 5 88.1% consensus (κ=0.74) — highest accuracy AND highest resolution; OpenCUA 66.1% (κ=0.28) với 13/20 mismatches FALSE POSITIVES (overstate — resolved 33 vs humans 25/29); Muse Glimmer 79.7% (κ=0.48) 10/12 mismatches FALSE NEGATIVES (understate, consistent 55.1% budget exhaustion — DONE episodes 13.4% only). Termination ≠ verdict: checker resolved 621/1,146 DONE episodes (54.2%), 162/1,077 budget-exhausted (15.0%), 18/667 BLOCKED (2.7%) — DONE-but-failed 45.8%; version-dependent episodes S5/OC/MG DONE-but-checker-failed 7/121/1 of 324, checker-passed-no-DONE 54/38/26 → agent completion signal BOTH inflate AND deflate. BERTScore control (§5.2): 108 fixes fail ALL 9 attempts scored F1 0.757–0.867 median 0.831 (≥ Gön et al. 0.81–0.82 all-fix range); 214 resolved fixes scored SAME (median 0.832, mean 0.824 vs 0.823); scores vary between issues (25379 avg 0.762 vs 0.818–0.846) → similarity = reference wording không phải correctness — single threshold cannot separate. Pipeline-enhancement benefits executor-dependent: RAG-Kimi +22.3pp vs V-Kimi dưới OpenCUA (55.6 vs 33.3) nhưng EQUAL dưới Sonnet 5. Scarcity finding (§5.4): no-code fixes entangled with uncapturable state (accumulated profile, OS, third-party service, server-side change) — issue trackers no structural trace (unlabeled invalid, resolutions unlinked commits) → dataset construction = research problem. Threats: harnesses không identical (MG custom function-calling schema; OC own action format), sampling khác (OC greedy T=0 vs MG T=1.0 top-p 0.95), 20-step budget (MG 55.1%), 2 reports no version → pinned nearby build, humans = authors, single app Brave + Linux-only (17/51 platform-specific excluded), Wrong Version = SINGLE issue, NO significance tests (intervals wide overlapping 38.6–61.3 vs 27.6–64.5). Replication package figshare.com/s/eda4e478ccbf242fbdab. Authors Bilkent (Torun/Karakaya equal contribution, Tüzün).
✓ Insight nổi bật: KHÔNG gửi no-code fix cho user trước khi execution-verify — best executor only 49.7%; text similarity (BERTScore 0.83 both classes) hoàn toàn không phân biệt working/failing fixes.
→ Tiếp tục: [TOP-10 HOÀN TẤT — 20 paper hôm nay #175–#194]

## Paper #195 — Selling in the Wild: Benchmark and Randomized Field Evidence for a Sales Agent Trained on Commercial Conversations (2610.25461v1) [applied]
✓ Skill: conversation-trained-sales-agent | Test: SKILL VALID
✓ Insight: Đào tạo trên 4,6 triệu cuộc hội thoại thương mại thật tăng revenue per visitor +10.0% so với không agent và engaged conversion +21.6% so với frontier cùng scaffolding, tại chi phí chỉ 1.8% so với nhân viên bán hàng.
→ Tiếp tục: [YES]

## Paper #196 — CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts (2610.25356v1) [applied]
✓ Skill: nlp-style-behavior-control-dpo | Test: SKILL VALID
✓ Insight: DPO cải thiện style adherence (queens traded early 53%→67%, queenside castling 97.3%→99.7%) mà không làm suy yếu sức mạnh không prompt (1792 vs 1797 Elo), dùng cặp cùng output dưới mô tả khác nhau không cần reward model.
→ Tiếp tục: [YES]

## Paper #197 — MAPS: A Multi-Agent Personalized Script-Driven Video Advertising System Enhanced by Reinforcement Learning (2610.25748v1) [applied]
✓ Skill: maps-multi-agent-video-ad-pipeline | Test: SKILL VALID
✓ Insight: 4-agent hệ thống (Profile, Scripter, Director, Reflector) tạo quảng cáo video cá nhân hóa theo yêu cầu, CTR +2.87%, CVR +2.74%, ARPU +9.85% trong A/B test thực tế tại Kuaishou.
→ Tiếp tục: [YES]

## Paper #198 — Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents (2610.26438v1) [applied]
✓ Skill: info-injection-defense-star-pipeline | Test: SKILL VALID
✓ Insight: Thông tin injection đạt ASR 62% (gấp 4.5× prompt injection 14%), hai mẫu 30 từ 100% trên 15 mã cổ phiếu, chỉ star pipeline phân cấp giảm ASR xuống 9–10%.
→ Tiếp tục: [YES]

## Paper #199 — NIOCIS: Typed-Decision Next-Hop Routing with Node-Conditioned Option Spaces for Tool-Use Agents (2610.25985v1) [applied]
✓ Skill: niocis-typed-decision-routing-layer | Test: SKILL VALID
✓ Insight: Lớp định tuyến typed-decision thay thế suy luận LLM mỗi hop, đạt 32.8% khớp đội agentes trong 10 ms so với 2.2 s/LLM hop, không gian tùy chọn được điều chế bởi nút勝 lợi hơn danh mục phẳng 3.5 điểm.
→ Tiếp tục: [YES]

## Paper #200 — The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents (2610.24873v1) [applied]
✓ Skill: one-relation-attack-ora-defense | Test: SKILL VALID
✓ Insight: Một câu đích đến liên kết ngầm lật ngược niềm tin agent: ORA đạt ASR 54.9% (proprietary) và 80.0% (open-weight) trên 18 mô hình, tranh luận đa agent làm tăng lỗi nhóm từ 50.0% lên 59.5%.
→ Tiếp tục: [YES]

## Paper #201 — CXBENCH: A Benchmark for Process-Compliant LLM Agents in Regulated Customer-Experience Workflows (2610.25954v1) [applied]
✓ Skill: cxbench-process-compliance-evaluation | Test: SKILL VALID
✓ Insight: 69.29% executions đạt outcome nhưng chỉ 13.81% đạt cả outcome và process; 55.48% là false-pass (outcome đúng nhưng vi phạm quy trình), sadece 13.8% pass cả hai.
→ Tiếp tục: [YES]

## Paper #202 — Scaling Multi-Agent Intelligence with Substrate-Centric Coordination (2610.16120v1) [applied]
✓ Skill: scalemas-substrate-coordination | Test: SKILL VALID
✓ Insight: ScaleMAS dùng kho dữ liệu tin nhắn liên kết chung + trích dẫn từ đồng nghiệp để xếp hạng, đạt 65.3% BrowseComp-Plus với 16 agent (từ 38.1% với 1), scale đến 128 agent và chịu được agent lỗi.
→ Tiếp tục: [YES]

## Paper #203 — Ask Less, Ask Better: Allocating User Attention in Proactive LLM Agents with Interruption Budgets (2610.24411v1) [applied]
✓ Skill: interruption-budget-user-attention-cost | Test: SKILL VALID
✓ Insight: Ngân sách 1–3 câu hỏi cắt chi phí chú ý người dùng 36–73% giữ 86–94% phần thưởng tác vụ; memory-guided review cắt thêm 13% chi phí với mất phần thưởng tối thiểu.
→ Tiếp tục: [YES]

## Paper #204 — Explore or Confirm? LLM Agents Misallocate Measurements Under Noise (2610.25111v1) [applied]
✓ Skill: explore-or-confirm-wellocate | Test: SKILL VALID
✓ Insight: 5 models misallocate noisy budget in both directions — 3 over-confirm (75–94% re-testing), 1 under-confirms (14%), every model picks worse final candidate than simplest scripted rule.
→ HẾT QUEUE — 10/10 bài đã distill xong

## Paper #205 — OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners (2610.24087v1) [applied]
✓ Skill: daq-deployment-adjusted-quality-eval | Test: SKILL VALID
✓ Insight: Trên 31 bài toán OR thực tế (hợp đồng $3.68M), mọi model vượt chuẩn chuyên gia về conditional quality nhưng đều thua về DAQ — Grok 4.6 cao nhất 86.55%, ~86% khoảng cách đến từ deliverable không khả thi (feasibility 45.16–88.39%), không phải toán kém.
→ Tiếp tục: [YES]

## Paper #206 — When Code Becomes an LLM Call: An Empirical Study of Call-Site Contracts in Agentic Systems (2610.24545v1) [applied]
✓ Skill: llm-call-site-contract-audit | Test: SKILL VALID
✓ Insight: 496 call site / 40 hệ thống agentic: 82% có check trước+sau call nhưng chỉ 5.3% thỏa mãn toàn contract; 63% expected constraints unmet (post-condition gap 72%); 10 pattern giải thích 99% gaps, fail-open handling = 44% conflicting verdicts, 38 mechanism trigger thực tế và 1 code fix nhỏ dừng cả 38.
→ Tiếp tục: [YES]

## Paper #207 — AGR: Agentic Generative Retrieval with Tool-Augmented Search (2610.26831v1) [applied]
✓ Skill: tool-augmented-generative-retrieval | Test: SKILL VALID
✓ Insight: Thay vì nhồi 400 feature tokens vào input, agent fetch feature on-demand trong lúc sinh SID: Recall@50 ngang (0.3237 vs 0.3241), training time −81.8%, serving −42.9% (4.76 vs 8.33 GPUs/1K req); A/B test thực tế Kuaishou: relevance +0.205%, query reformulation −0.690%, search penetration +0.060% (latency 35ms).
→ Tiếp tục: [YES]

## Paper #208 — IF-MAP: Influence-Function-Inspired Agent Prioritization in Multi-Agent Systems (2610.24383v1) [applied]
✓ Skill: ifmap-agent-prioritization-probing | Test: SKILL VALID
✓ Insight: Đo "potential to improve" bằng prompt perturbation probing (black-box, không cần gradient): prompt optimization +3.81 pp vs +1.85 uniform; model upgrade +7.62–16.42 pp vs +3.81–8.62 uniform, tiết kiệm 63.6–74.2% tokens — chọn đúng 1 agent nâng cấp hiệu quả gấp ~2 lần chọn ngẫu nhiên.
→ Tiếp tục: [YES]

## Paper #209 — Agent-Reflex: Teaching Language Agents to Act Reflectively (2610.17953v1) [applied]
✓ Skill: agent-reflex-reflective-training | Test: SKILL VALID
✓ Insight: Huấn luyện agent phản xạ chủ động (proactive reflection) và khôi phục kỹ năng (skill recovery) khi công cụ (tool) bị ồn ào (noisy interaction) — tinh chỉnh (fine-tuning) trên cặp thành công–thất bại thật thay vì chỉ nhắc qua lệnh nhắc (prompt) → agent tự sửa lỗi, không cần văn bản phê bình (critique text); VitaBench 17.5% vs Reflexion-8B 6.8%, ACEBench 78.0% vs NoisyAgent-8B 52.0%, τ²-Bench 62.1% vs EnvScaler-8B 54.6%.
→ Tiếp tục: [YES]

## Paper #210 — DiffResearch: Accelerating Deep Research with Diffusion Language Models (2610.28909v1) [applied]
✓ Skill: diffresearch-diffusion-backbone-deep-research | Test: SKILL VALID
✓ Insight: Thay backbone AR bằng diffusion language model làm giảm độ trễ end-to-end khoảng 6× (71,45s → 11,89s) mà không làm giảm chất lượng RACE, vì diffusion cập nhật toàn bộ dãy văn bản song song thay vì sinh tuần tự một token một thời điểm.
→ Tiếp tục: [YES]

## Paper #211 — MemoProAgent: Toward Memory-Driven Proactive Assistance (2610.22671v2) [applied]
✓ Skill: memoproagent-gated-memory-harness | Test: SKILL VALID
✓ Insight: Trong trợ giúp chủ động, bộ nhớ quyết định cả nội dung lẫn thời điểm; thiếu một trong hai là thảm họa (oracle+timing given đạt 96%, nhưng chỉ timing do model chọn sụt 38%, retrieved+timing given sụt 15.3%), nên giải pháp phải lọc bằng chứng qua cổng lọc chứ không chỉ cung cấp thêm bộ nhớ.
→ Tiếp tục: [YES]

## Paper #212 — Are Self-Evolving Agents Continual Learners? (2610.25858v1) [applied]
✓ Skill: self-evolving-agent-harness-isolation | Test: SKILL VALID
✓ Insight: Agent tự tiến hóa trải qua trade-off plasticity–stability: GEPA linh hoạt cao nhất (+6.2 pp) nhưng kém ổn định nhất (−4.3 pp), ReasoningBank ổn định nhất (−1.9 pp) nhưng chỉ nửa linh hoạt (+3.3 pp); tự sửa đổi prompt dùng chung gây can thiệp chéo và ghi đè, truy xuất tương đồng không ngăn va chạm khi các tác vụ khác nhau dùng cùng embedding space.
→ Tiếp tục: [YES]

## Paper #213 — TaQFormer: A Treatment-as-Query Transformer with Data-Fusion for Multidimensional Treatment Modeling in Coupon Allocation (2610.26199v1) [applied]
✓ Skill: taqformer-treatment-query-uplift | Test: SKILL VALID
✓ Insight: Mỗi chiều giảm giá là một truy vấn token dùng cross-attention để ước lượng phản hồi vectơ điều trị toàn phần; cổng hợp nhất theo từng instance trộn nhánh OBS đóng băng và RCT đã điều chỉnh — Qini 0,1612→0,2697, AUC 0,6776→0,7393, A/B 14 ngày +1,26% giá trị khách hàng, tỷ lệ phụ giá thu không đổi (~20,4%).
→ Tiếp tục: [YES]

## Paper #214 — A Locally Deployable Tool-Grounded LLM Multi-agent Framework for Automating Methane Emission Analysis and Reporting (2608.18473v1) [applied]
✓ Skill: methane-tool-grounded-multi-agent | Test: SKILL VALID
✓ Insight: LLM nên điều phối quy trình chứ không thay thế tính toán định lượng xác định — giữ kết quả có thể truy xuất và dựa trên vật lý; xử lý cục bộ giảm lộ dữ liệu nhạy cảm; đạt 92.0% điều phối quy trình, 85.0% ước lực phát thải/cột feather, 95.0% báo cáo, thời gian từ giờ xuống phút.
→ Tiếp tục: [YES]

## Paper #215 — RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis (2610.27816v1) [applied]
✓ Skill: rag-nimbf-configuration-analysis | Test: SKILL VALID
✓ Insight: Không có chỉ số đơn lẻ nào đủ cho RAG — faithfulness, nDCG@5, và thời gian chạy di chuyển theo hướng khác nhau; MMR tăng nDCG@5 +4 đến +11 điểm, nhắc chi tiết tăng faithfulness +10 đến +13 điểm trên mô hình giỏi/suy lý, Qwen3.6-27B cục bộ khớp GPT-4o-mini ở 0.89 faithfulness.
→ Tiếp tục: [YES]

## Paper #216 — A Cross-Domain Evaluation of Prompting Techniques for Large Language Models (2610.24913v1) [applied]
✓ Skill: cross-domain-prompt-selection | Test: SKILL VALID
✓ Insight: Không có kỹ thuật nhắc nào vượt trội trên tất cả domain; không có sai số statiscally significant giữa cấu hình cao nhất và thứ hai (tất cả adjusted p-value = 1.000). RAG trung bình cao nhất 78.33% (300 ví dụ), Few-Shot 77.83% (200 ví dụ), Zero-Shot thắng BoolQ 90.0%, PE2 ổn định không vượt trội. Tăng ví dụ không nhất quán cải thiện hiệu suất → chọn kỹ thuật nhắc theo đặc điểm nhiệm vụ.
→ Tiếp tục: [YES]

## Paper #217 — Evaluating Open-Weight LLMs for Turkish Domain Documents Under Retrieval and Hardware Constraints (2609.28007v1) [applied]
✓ Skill: turkish-llm-evidence-annotated-eval | Test: SKILL VALID
✓ Insight: Sự điều chỉnh ngôn ngữ đơn lẻ không đảm bảo hiệu năng tài liệu-grounded (Qwen2.5 đa ngôn ngữ vượt qua các mô hình điều chỉnh Turkce); truy xuất có thể là ràng buộc buộc đối với một số tài liệu (57% nhớ lại báo cáo chính) nhưng không phải tất cả (91% báo cáo thứ cấp); chọn mô hình dựa trên kết quả thực nghiệm chứ không chỉ nhãn ngôn ngữ (Trendyol 75% chính xác nhưng chậm 14 lần Qwen2.5).
→ Tiếp tục: [YES]

## Paper #218 — Extending FunctionGemma for Practical On-Device Mobile Function Calling (2609.25373v2) [applied]
✓ Skill: extending-functiongemma-on-device-mobile-function-calling | Test: SKILL VALID
✓ Insight: Một mô hình function-calling (gọi hàm) 270 triệu tham số có thể được điều chỉnh để điều khiển Android cục bộ với độ chính xác 76.5% trên 15 danh mục hành động thiết bị, chỉ cần tập dữ liệu tổng hợp ~9.500 mẫu và không cần mô hình đám mây lớn cho mỗi yêu cầu.
→ Tiếp tục: [YES]

## Paper #219 — Do Agents Need a New Kind of Paper? SPRA: Structured Paper Representation for Agents (2610.21424v2) [applied]
✓ Skill: spra-structured-paper-representation | Test: SKILL VALID
✓ Insight: SPRA biến nghiên cứu khoa học thành đối tượng có cấu trúc và quan hệ được trích lập để tác tử AI tra cứu, duyệt và tái sử dụng nội dung bài báo hiệu quả, giảm 28.5% token so với truy xuất đoạn văn và 95.3% so với văn bản đầy đủ.
→ Tiếp tục: [YES]

## Paper #220 — Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows over Heterogeneous Data Sources (2610.25096v1) [applied]
✓ Skill: agentic-rag-enterprise-retail | Test: SKILL VALID
✓ Insight: RetailRAG vượt tất cả 6 cơ sở RAG trên RetailBridge (1,680 truy vấn đa nguồn, 3 cấp độ), đạt LLM-judge 0.429 trung bình vs 0.336 của HetaRAG (cơ sở mạnh nhất) và ít hơn 3 lần API call (7.45 vs 25.21).
→ Tiếp tục: [YES]

## Paper #221 — Business Arena: Benchmarking LLM Agents in a Realistic Marketplace (2608.08621) [applied]
✓ Skill: business-arena-llm-agent-benchmark | Test: SKILL VALID
✓ Insight: Business Arena đánh giá 15 mô hình LLM trong môi trường mô phỏng cửa hàng xuyên biên giới, tìm ra khoảng cách 9.0× trong trị giá ròng cuối cùng ($188,488 vs $20,856), 51% lần chạy lỗ tiền, chỉ 4 mô hình bảo toàn vốn mọi lần thử.
→ Tiếp tục: [YES]

## Paper #222 — E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation (2608.30730v1) [applied]
✓ Skill: e-commerce-bench-long-horizon-business | Test: SKILL VALID
✓ Insight: E-Commerce Bench đánh giá 18 mô hình LLM trên 7 chiều trong môi trường mô phỏng thương mại một năm, tìm ra hệ số 1,264 giữa mô hình tốt nhất và kém nhất (¥1,431,425 vs ¥1,132), không có mô hình nào thống trị mọi chiều.
→ Tiếp tục: [YES]

## Paper #223 — Neuro-Inspired Inhibitory Message Passing for Accurate and Token-Efficient Multi-Agent Reasoning (2610.24718v1) [applied]
✓ Skill: inhibitory-message-passing-router | Test: SKILL VALID
✓ Insight: Router truyền thông hạn chế với 3 quy tắc (truyền bằng chứng gốc, một lần mỗi vòng, chỉ nếu chưa có) giúp nhóm agent chính xác +39-77 điểm phần trăm và giảm 10-46% token, ổn định lên đến 64 agent.
→ Tiếp tục: [YES]

## Paper #224 — ARCTIC-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design (2610.24914v1) [applied]
✓ Skill: arctic-swe-rl-baseline | Test: SKILL VALID
✓ Insight: Overfit trên nhóm tác vụ nhỏ làm kiểm tra định kỳ phơi bày lỗi hạ tầng phần thưởng sớm che lấp; gated reward + kiểm tra định dạng thó + căn chỉnh số giúp Qwen3.5-4B đạt 62.0% trên SWE-bench Verified với 1/6 lượt huấn luyện so với FrogNano.
→ Tiếp tục: [YES]

## Paper #225 — CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents (2610.27645v1) [applied]
✓ Skill: cua-recovery-error-recovery | Test: SKILL VALID
→ Tiếp tục: [YES]

## Paper #226 — Mining the Design Space of Multi-Agent Workflows (2610.31709v1) [applied]
✓ Skill: mining-design-space-multi-agent-workflows | Test: SKILL VALID
✓ Insight: Star-first làm giảm hiệu quả (Δ = −0.045), SharedMemory vượt trội hơn Debate (Δ = +0.135), prompt cụ thể có lợi bằng cấu trúc liên lạc (Δ = +0.118) — thiết kế workflow nên bắt đầu bằng trạng thái chia sẻ liên tục, không phải fan-out độc lập.
→ Tiếp tục: [YES]

## Paper #227 — DMAIC-Bench: From Self-Reflection to Self-Restraint for Agents in Multi-Stage Analytical Tasks (2610.32305v1) [applied]
✓ Skill: dmaic-bench-self-restraint-evaluation | Test: SKILL VALID
✓ Insight: Agent tốt trong việc tiếp tục (92% GO) nhưng kém trong việc dừng (19% NO-GO, khoảng cách 73 điểm); 47% quyết định NO-GO có báo cáo hành động trên bằng chứng không hợp lệ — chẩn đoán đúng không đủ, cần kiềm chế hành động dựa trên bằng chứng.
→ Tiếp tục: [YES]

## Paper #228 — CauProphet: Teaching Agents to Develop Causal Cognition like Humans (2610.32477v1) [applied]
✓ Skill: cauprophet-causal-cognition-agent | Test: SKILL VALID
✓ Insight: Agent có thể xây dựng triết nhân quả tồn tại dài hạn qua Triết Nhận thức Nhân Quả và Tin Tín Nhân Quả; trong tài chính, cải thiện 25,4% tương quan hạng với lợi nhuận ngày sau, độ chính xác dự đoán từ 21,3% lên 28,6%.
→ Tiếp tục: [YES]

## Paper #229 — Not Every Agent Needs the Strongest Model: Unified Prompt–Model Optimization for Heterogeneous LLM-based Multi-Agent Systems (2610.31743v1) [applied]
✓ Skill: unimaso-prompt-model-optimization | Test: SKILL VALID
✓ Insight: Không phải mọi agent đều cần mô hình mạnh nhất — UniMASO phân bổ mô hình theo vai trò, đạt điểm 70,40 (tăng từ 69,79) và giảm chi phí token-weighted 85,2% so với DeepSeek-V4-Pro đồng nhất.
→ Tiếp tục: [YES]

## Paper #230 — CRM-Agent-Bench: Benchmarking Tool-Using Agents in Stateful Enterprise Environments (2610.32004v1) [applied]
✓ Skill: crm-agent-bench-contract-evaluation | Test: SKILL VALID
✓ Insight: 555 tác vụ trạng thái đa lượt trên 9 miền kinh doanh; strict success 64,32%–83,60% trên 16 hệ thống — agent vẫn khó thực hiện đúng quy trình đa giai đoạn; các hệ thống dẫn đầu khác biệt mạnh về chi phí và độ tin cậy theo miền.
→ Tiếp tục: [YES]

## Paper #231 — Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search at Scale (2609.24152v1) [applied]
✓ Skill: grad-cir-graded-relevance-retrieval | Test: SKILL VALID
✓ Insight: Grad-CIR huấn luyện CIR retriever trên nhãn liên quan phân cấp 4 cấp thay vì nhị phân — tăng 4,9%–5,9% NDCG@10, VLM tự động tạo dữ liệu, vòng phản hồi khai thác hard negative, đã triển khai production tại Walmart.
→ Tiếp tục: [YES]

# HẾT QUEUE CŨ (2026-10-26) — 6 paper #226–#231 xong. Scan mới 2026-10-27 05:00 khóa top10 mới (10 paper high-group 77–90) → queue hôm nay: #232–#241.

## Paper #232 — Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent Debate Synthesis (2609.31422v1) [applied]
✓ Skill: provenance-gate-synthesis-verification | Test: SKILL VALID
✓ Insight: MAD synthesis bịa consensus trôi chảy (baseline PF 0,288/0,183); APG — hard gate PF ≥ 0,95 + self-healing tối đa 3 lần + Divergence Report — nâng terminal PF 0,617/0,586, divergence 75% dưới xung đột zero-sum; validator phải khác và mạnh hơn proposer (symmetric fail 85,6%, asymmetric reject 63,3%); 75,8% người dùng tin báo cáo thừa nhận thất bại hơn bản bịa fluency (trust 3,27 vs 2,45, p=0,0039).
→ Tiếp tục: [YES]

## Paper #233 — Poisoning Agentic Alpha: Adversarial Vulnerabilities Across Roles and Architectures in Multi-Agent Trading Systems (2608.24069v1) [applied]
✓ Skill: multi-agent-red-team-role-topology | Test: SKILL VALID
✓ Insight: Jailbreak terminal Risk Manager: ASR 98,9%/95,5% (BUY/SELL) — cao gấp 1,9× attack mạnh thứ hai, bypass hết aggregation/debate upstream; persuasive adversary 41,9–53,3% > mọi data-level attack (p<0,005); không architecture nào robust bản chất (APS ordering Dec 0,00 < Hyb 0,33 < Lin 0,50 < Cen 1,00 khớp ASR, r=0,85/0,88); quorum effect — vote majority fail khi 1 benign analyst đã theo target (44,6% ngày), 2 channel compromise → 68,7%; ASR ≠ financial harm (jailbreak 97,2% ASR median $0, objective hijacking median −$85, EV +$40); poison 10%→80% chỉ nâng ASR 19,1→30,6%; Dec clean return tốt nhất (−2,68%) nhưng degrade lớn nhất (−12,01/−12,38 pp).
→ Tiếp tục: [YES]

## Paper #234 — Agentic AI Defense: Decode-Time Provenance Binding for MCP (2610.31974v1) [applied]
✓ Skill: decode-time-provenance-binding-mcp | Test: SKILL VALID
✓ Insight: Cross-modal trust laundering — instruction giấu trong logo signature email (LSB/DCT/metadata steganography) bypass text scanner, chỉ thành instruction khi tool decode → undefended leak 100%, keyword/regex scanner 62,5%, decode-time provenance binding 0% trên 24 adaptive payloads; defense contain-don't-detect: MCP layer mint HMAC-signed Untrusted label tại decode boundary + tự maintain lineage ledger → chặn valid-label substitution (agent bị compromise đưa Trusted label giả vẫn block vì taint context layer ghi); HMAC + lineage necessary non-interchangeable (ablation: −HMAC leak forged relay cross-domain, −lineage leak substitution); taint propagate qua mediated inter-agent message; trusted promotion audit → legitimate completion 67%→100%, 0 false block; overhead ≈17 µs/call (+0,16% decode round-trip), enforcement linear theo closure depth (10 µs depth 1 → 6,6 ms depth 1000); scope limit: in-model paraphrase qua unmediated channel không cover, defense bảo vệ action không phải summary prose.
→ Tiếp tục: [YES]

## Paper #235 — OneLatent: Latent Reasoning for Efficient Foundation Recommendation Models (2610.30675v1) [applied]
✓ Skill: latent-reasoning-recommender | Test: SKILL VALID (dry-run short-video recommender 500K items: SID 256³, 3-view teacher rationale, Stage I–III, curriculum high→low, event-triggered Redis cache)
✓ Insight: Explicit CoT (chuỗi lập luận hiển thị) tốn 55,59 s / 15,68 QPS (query/giây) trong khi No-Think cùng checkpoint chỉ 3,17 s / 274 QPS mà quality gần như không đổi (codebook Hit@L1 0,350→0,354) — nén trace lý luận thành 3 latent token (token ẩn) cố định → +17,44% SID@64 vs Think, +9,33% vs No-Think, 17,49× QPS, rollout production Kuaishou A/B 7 ngày: impressions +2,566%, ad spend +5,157%, revenue +9,6%; adaptive CoT teacher giảm 35% độ dài rationale mà giữ semantic similarity 0,92 ở case phức tạp.
→ Tiếp tục: [YES]

## Paper #236 — ProfileSim: Profile-Driven User Simulation via RL with Hierarchical Rewards for Task-Oriented Dialogues (2610.32435v1) [applied]
✓ Skill: profilesim-user-simulator | Test: SKILL VALID (dry-run selling khóa học online: 5,000 call log ẩn danh → personas Big Five + 30 intents/6 groups + transition matrix → SFT+GRPO Qwen3.5-9B → agent SOP graph → 3,000 calls giả → patch intent hoàn tiền)
✓ Insight: User profile (demographics + Big Five traits) là conditioning dominant — +UserProfile giảm PPL 36,24 (58,48→22,24) vs +BusinessProfile chỉ 15,44; Full Model colloquial 4,97/5, utterance 11,14 chars (GPT-5 44,54, DeepSeek-V3 153,96), profile adherence 92,55% (LLM zero-shot ≤84,05%), agent stress score 3,49 thấp nhất trên long-tail intent (bottom 20%) — simulator profile-conditioned tạo corpus khó nhất để stress-test agent; GRPO không degrade PPL (17,52→17,49) vì PPL insensitive với behavioral properties; business compliance cao (GPT-5 62%) có thể chỉ do explicit verbalization ≠ realism.
→ Tiếp tục: [YES]
## Paper #237 — Where Should Agents Live? agentic-eCAL: Energy-Memory Characterization of Agentic AI Edge-Cloud (2609.18283) [applied]
✓ Nhãn: [applied] — NVML-metered GPU measurements (A100/H100, vLLM, 270 configs/model, R²=0,996 MAPE ~10%) + ETSI ZSM Infra-Bench benchmark thật (k3s edge, 24 incidents Kubeply)
✓ Skill tạo được: agentic-ecal-energy-accounting (evaluation-method framework 9 bước: classify DAG → memory gate βN+γΣc≤M_u → two-rate E_call=c_pre·p_in+(a_dec/b+c_0)·p_out → E_W=(1+γ_v)[Σcall+Σtool+Σret+Σtx] → scaling exponent a∈[1,2] → hand-off protocol select → agentic-eCAL [J/b] → kJ/solved-task vs single → efficiency levers order)
✓ Skill test: [SKILL VALID] — SELF-CHECK: followable w/o paper (đầy đủ formula + hệ số tham khảo + fallback datasheet); DRY RUN: 3-agent content pipeline Qwen2.5-7B K=4 b=64 L4-24GB → E_call≈268 J, E_W≈295 J (γ_v 10%), E_tx 5G 0,9 mJ (0,0003% E_W), memory gate: 2 sessions hostable, editor chuyển sang summary hand-off −40 J → verdict placement by VRAM + protocol recommendation có nghĩa
✓ Insight nổi bật nhất: Inter-agent text transport chỉ <0,25% workflow energy (E_tx/E_prefill 1/496 cho 2,700-token hand-off 5G) → dominant cost của distribution là EXTRA inference + context processing induced by communication chứ KHÔNG phải truyền text; placement governed by memory (KV width γ: GPT-OSS-20B 48 kB/token host 112 sessions vs OLMo-2-7B 512 kB chỉ 7); history-carrying loop quadratic K² (+32,8% K=6 Qwen 89J vs 67J); batching không cứu team lớn (−38,1% N=2 → −15,4% N=30); multi-agent KHÔNG tự better — ZSM benchmark Single ReAct 61,7% vs best-multi 64,6% tốn 2,9× energy (7B: Single 9,2% BETTER multi 0,4–4,6%, kJ/solved 49,7 vs 320–5222,3); hand-off protocol dynamic range 3,7×10⁵ (increment 0,051 Mbit/summary 0,079 ≪ transcript 0,33 Mbit ≪ KV 18,9 Gbit); embodied 8B parity G≈1,2×10¹⁰ invocations, 70B parity tại 0,66× invocations của 8B
→ Tiếp tục: [YES]
## Paper #238 — ACTS: Role-Aware Communication Topology Scheduling for LLM Multi-Agent (2610.25851) [applied]
✓ Nhãn: [applied] — 9 benchmarks × 4 domains thật (LiveCodeBench v6, HumanEval, MMLU-Pro, HLE-250, HotpotQA, AIME 2025/2026, HMMT 2025, Beyond-AIME), 2 frozen backbone, 3 seeds
✓ Skill tạo được: acts-topology-scheduling (framework 8 bước với 2 path: Path A full CTDE MARL training, Path B heuristic zero-RL cho solopreneur — IG gate 2/n, 6 modes, α directed threshold ᾱ=mean, credit theo in/out neighborhood, Pareto evaluate)
✓ Skill test: [SKILL VALID] — SELF-CHECK followable w/o paper (đầy đủ mode definitions, thresholds, early-termination rules, gotchas); DRY RUN pipeline 3 agent (Researcher/Writer/Editor): IG gate sample 30 task → Δ12pp > 2/30 → IG>0; schedule 12k token/74% vs full-mesh 21k/75% vs static chain 18k/70% → Pareto frontier; task low-IG (reformat paragraph) → gate Δ1,5pp < 6,7% → single agent, 0 team token → output có nghĩa
✓ Insight nổi bật nhất: Communication KHÔNG phải mặc định tốt — IG (information gain) null trên HLE (ΔACC < 2/n noise threshold) → ACTS học off share 4,2%→21,3% và attn-receive pull dominant 28,3% khi đó, near-equal single-agent accuracy; fixed partner routing là ablation tệ nhất (72,50% + 8,10k token vs ACTS 75,01% + 5,97k); topology mixer mạnh nhất component (bỏ → −3,18/−6,19pp accuracy + token 7,41/4,96k); token penalty clamp min(Σ/B,1) → accuracy UP token DOWN 13,8–15,4% (5,97k/4,03k vs Agent Q-Mix ~7,06k/~4,68k); directional scores α_ij ≠ α_ji
→ Tiếp tục: [YES]
## Paper #239 — ReFilter: Bridging Embeddings and LLM Filtering for Similar Mobile App Retrieval (2609.25306) [applied]
✓ Nhãn: [applied] — corpus thật 20,635 apps (Google Play scrape Aug 2025, 34,364 seed → preprocess), 1,765 pairs...[truncated]## Paper #240 — Auditing Tool Traces in Agentic LLMs: Source Localization + Counterfactual Dependence Testing (2610.25540) [applied]
✓ Nhãn: [applied] — TCR–pMHC benchmark thật (12,940 train + 1,438 val + 4,898 test, peptide-disjoint clusters)...[truncated]## Paper #241 — Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents (2609.28572) [applied]
✓ Nhãn: [applied] — Autonomous Adversary system (orchestrator + executor + validator LLMs) trong controlled enterprise-like range, 6 frontier models (Opus 4.5, Sonnet 4.5, Gemini 3 Pro Preview, GPT-5.1, GPT-4o-mini, DeepSeek-V3.2-Speciale) × 2 lateral-movement scenarios × 3 modes (expert-defined / self-scaffolded / fully autonomous); 29 complete 5-judge panels = 145 judgments, 23 cohort trajectories.
✓ Skill tạo được: multi-stage-agent-bottleneck-audit (evaluation-method: z-score resource localization + 5-judge trajectory diagnosis + validator audit + robustness/deletion check)
✓ Skill test: SKILL VALID (SELF-CHECK: followable YES — 10 steps có formula/JSON schema/tie rule/≥4/5 robustness/adaptation definition/judge prohibitions/gotchas; DRY RUN: content pipeline 3 stages × 2 workflows × 3 autonomy — publish stage B=3,5 flagged, panel modal recovery/adaptation 3/5 reported as plural, severity 4/5, 18/20 no-meaningful-adaptation under autonomy (retry same API khác headers), mechanisms split per mode 24/30 vs 17/30, validator quality 0,81/specificity 0,65/cautiousness 0,72 phơi bơi false "published" claim → remediation prerequisite gates + end-state verification + hypothesis-changing retry policy — output có nghĩa)
✓ Insight nổi bật nhất: Success rate đơn lùi nói dối — evaluate 4 axes (outcomes, evidence interpretation, resource use, adaptation after failure): validator optimistic+nonspecific (quality 0,79–0,84, grounding 0,81–0,90, specificity chỉ 0,68–0,69, cautiousness success 0,70 vs failure 0,92; validator-accepted ≠ independently verified — accepts process creation/echoed output as success); repetition ≠ recovery (syntax changes preserving failed assumption); bottleneck LOCATION thay đổi theo autonomy level (E→execution errors 18/30; S→unsupported assumptions 25/30 + missing prerequisites 20/30; A→planning+recovery heterogeneous, no-adaptation 20/20, support lowest 0,60); tie-aware aggregation (unique modal có thể 2/5 votes) + deletion robustness 12/23 panels ≥4/5; mean severity 4,03–5,00/5, framework contributions 72–100% → fix execution loop cùng model; Opus S2-A panel INC = provider safety filter (missing data ≠ failure).
→ Tiếp tục: [NO — queue top10 2026-10-27 đã cạn (#232–#241 xong 10/10), chuyển Phase 4 daily summary]
