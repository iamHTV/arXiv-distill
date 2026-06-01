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
