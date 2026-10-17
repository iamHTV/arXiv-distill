# [2609.38743v2] Learning to Route in Visual Space via Multi-Step Embedding Retrieval

## Problem
LLM agents rely on retrieval tools to access external knowledge, but visual agentic search is severely bottlenecked by standard single-step retrievers. In current pipelines, the agent must issue text queries for every intermediate step, struggling when visual clues are difficult to describe in text or when the retriever fails to surface necessary intermediate evidence within its top results. The agent only sees the few results returned, cannot reason over evidence it never receives.

## Contribution
- Introduces VHop, a flexible data generation framework and benchmark with five core difficulty levels testing both visual matching and search planning.
- Develops VHop-Router, an end-to-end training pipeline — combining supervised fine-tuning, online imitation learning, and reinforcement learning — that transforms a standard embedding model into an autoregressive multi-step retriever.
- Operating directly in the visual latent space, VHop-Router retrieves linked image chains in a single tool call without requiring the agent to formulate intermediate text queries.

## Method
- VHop-Router transforms a standard embedding model (Qwen3-VL-Embedding-2B) into a multi-step retriever through three stages: (1) Supervised Fine-Tuning (SFT) teaches next-hop retrieval from gold trajectory prefixes with InfoNCE objective; (2) Online Imitation Learning (Online IL) teaches recovery and stopping from states visited during search; (3) Reinforcement Learning with Verifiable Rewards (RLVR) optimizes final-answer success.
- State: instruction x and active stack σt = (q0, q1, ..., qdt). Action space: {Select(a) : a ∈ corpus} ∪ {Backtrack, Stop}.
- State encoder Es and action encoder Ea both start from Qwen3-VL-Embedding-2B with LoRA. Ea frozen after SFT, cached corpus embeddings reused.
- Candidates scored by cosine similarity, selected from top-K candidates using softmax with temperature τ.
- Two learned gates control stopping and backtracking (two-layer MLPs). At evaluation, policy acts deterministically: stops if p_stop ≥ 0.5, otherwise selects highest-scoring image.

## Key Findings
- VHop-Router boosts retrieval performance from under 5% to 76.3%.
- In agentic search, improves task success rates by 52.7% and reduces average token length by 61% (from 1886 to 728).
- Upgrading the agent yields only 3.7% gain, while replacing the retrieval tool with VHop-Router yields 52.7% increase.
- Compared to a strong baseline (agent retrieves top-50 results per step), VHop-Router maintains superior performance while reducing in-context images by 23× and cutting cumulative API payload by 35×.
- Models generalize robustly to unseen difficulty levels and realistic test sets.

## Actionable Insights
1. Offload multi-step navigation from agent to retrieval tool — instead of having the agent construct intermediate queries, let the retrieval tool navigate directly across the entire embedding space. Apply: when building visual/multimodal search systems, train a multi-step embedding retriever instead of letting the LLM agent do multi-hop retrieval itself. First step: Build a retriever that returns linked image chains in a single tool call.
2. Improving the retrieval tool is far more effective than upgrading the agent model. Apply: before spending money upgrading to a larger agent model, invest in a better retrieval tool. First step: Compare retrieval tool replacement vs agent model upgrade on your task.
3. Reduce in-context images to cut API costs. Apply: instead of retrieving top-50 results per step, use a multi-step retriever that returns a concise chain. First step: Limit the number of images sent to the LLM agent, only sending the most relevant ones from the retriever chain.

## Assumptions & Limitations
- Evaluated on VHop benchmark (synthetic image corpus); may differ on real-world image data.
- Only 2 embedding models evaluated (Qwen3-VL-Embedding-2B, Gemini Embedding 2); does not generalize to all embedding models.
- Trained exclusively on L4 difficulty level; evaluated on L1–L5 without further fine-tuning.
- Some external tools are synthetic stubs in the prototype, not connected to live APIs.

## Metadata
- Year: 2026, Authors: Tianyu Chen, Mingyuan Zhou (The University of Texas at Austin), Jiaxing Wu (Google DeepMind), arXiv category: cs.AI, PDF link: https://arxiv.org/pdf/2609.38743v2