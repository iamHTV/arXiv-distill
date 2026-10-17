# Skill: Multi-Step Embedding Retriever for Visual Search

Source: 2609.38743v2
Type: framework

## When to use this skill
- You are building visual agentic search and want to reduce token cost while improving success rate.
- You have an existing embedding model and want to turn it into a multi-step retriever without fine-tuning the agent LLM.
- You need to handle image search where visual clues are hard to describe in text.

## When NOT to use this skill
- Text-only retrieval without multi-hop needs.
- You don't have image data to train a multi-step retriever.

## Input required
- Image corpus and multimodal queries.
- Base embedding model (e.g., Qwen3-VL-Embedding-2B).
- Gold trajectories for SFT.
- Oracle guidance for Online IL.

## Steps to execute
1. SFT teaches next-hop retrieval: encode state (instruction + current image stack) and align with next gold image using InfoNCE objective. Two phases: first freeze action encoder, update only state encoder; then jointly optimize both.
2. Online IL teaches recovery and stopping: collect fresh rollouts using current policy, get oracle guidance, do dead-end exploration. Update state encoder and control gates using per-state loss.
3. RLVR optimizes final-answer success: sample G rollouts per query, assign reward 1 only when policy stops with valid answer, use PPO-style clipped surrogate with DAPO-style asymmetric clipping.
4. At inference, policy acts deterministically: stop if p_stop ≥ 0.5, otherwise select highest-scoring image by cosine similarity.
5. Return linked image chains in a single tool call — no intermediate text queries needed from agent.

## Expected output
- A multi-step retriever that can navigate across the image embedding space.
- Retrieves linked image chains in a single tool call.
- Reduces in-context images and cuts API payload.
- Higher task success rate than single-step retriever.

## Example application
You build an agent to search in an e-commerce product image catalog. Instead of having the agent send multiple text queries to find an item, use VHop-Router — a multi-step retriever that navigates directly across the image embedding space and returns related image chains in a single tool call. The agent just inspects the resulting image chain and gives the answer. Reduces 61% token vs agent doing multi-hop retrieval itself.

## Gotchas
- Need image data and gold trajectories for SFT training.
- Trained exclusively on L4 difficulty; generalizes to L1–L5 but may not work on completely different image domains.
- Stop/backtrack gates need gate temperature tuning for stable operation.