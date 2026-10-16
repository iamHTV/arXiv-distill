# arXiv Distill — Report

Báo cáo tổng hợp. Mục tiêu: ~300 papers, chất lượng ưu tiên. Hiện tại: 50 papers. 🎉 MILESTONE!

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
