# Skill: maps-multi-agent-video-ad-pipeline

Source: 2610.25748v1
Type: framework / workflow

## When to use this skill
- When building a personalized video ad creative generation system for each user, not dependent on a pre-existing creative inventory.
- When wanting to apply multi-agent to分工 work: user analysis, scriptwriting, video production, feedback revision.
- When needing a system that continuously adapts to changing user preferences over time via online feedback loops.

## When NOT to use this skill
- When video generation cost per impression is too high relative to personalization benefits.
- When you don't have historical user interaction data or product visual assets.
- When the task is simple and doesn't need deep personalization.

## Required inputs
- Historical user interaction data (video views, play duration, likes, comments, collections, shares, follows).
- Product visual assets (images, logos, brand information).
- MLLM (Qwen3-VL-32B-Instruct or equivalent) for Profile and Reflector Agents.
- Language model (Qwen3-VL-8B-Instruct or equivalent) for Scripter Agent.
- Video generation model (Kling-Omni or equivalent) for Director Agent.
- GPU resources (recommended 8 H100 or equivalent).

## Steps to execute
1. Deploy Profile Agent: extract structured user profiles across 4 dimensions (topical interests, preferred presentation styles, implicit needs, decision-making tendencies) from historical interaction data and real-time contextual signals; continuously refine as new observations accumulate.
2. Train Scripter Agent: SFT on human-authored personalized ad script corpus (LoRA rank 32, AdamW LR 1.0e-5, batch 4, max seq 8192, 20 epochs); then RL via GRPO (KL coeff 0.04, AdamW LR 1.0e-6, batch 4, 5000 steps).
3. Set up multi-dimensional reward function: Rtotal = 0.3·Rstruct + 0.4·Rpers + 0.3·Rprod; Rstruct checks format compliance/script completeness/scene-character consistency/physical rationality; Rpers uses LLM-as-a-Judge for presentation style + content preference alignment (0–10 scale); Rprod uses LLM-as-a-Judge for product identity/brand elements/selling points factual consistency (0–10 scale).
4. Deploy Director Agent: receive script from Scripter, combine with product visual assets, synthesize complete ad video.
5. Deploy Reflector Agent: collect online interaction signals (play duration, likes, comments, purchases) after each impression; attribute to profile-level or script-level causes; route minimal revision directives back to Profile and Scripter Agents.
6. Run closed-loop loop: Profile → Scripter → Director → creative → Reflector → feedback → Profile/Scripter, repeating across successive impressions.

## Expected output
- A personalized video ad creative generation system on demand per user.
- Evaluation report: CTR, CVR, ARPU, personalization score, product alignment score, diversity score.
- Deployment decision: deploy widely, keep as-is, or adjust reward function/agents.

## Example application
A cosmetics brand wants to run video ads on Kuaishou/TikTok, where each user sees a different video ad suited to their preferences and skin type. MAPS analyzes user profile (skincare concerns, preferred video style), Scripter writes ad script for skincare product, Director generates video with actual product images, Reflector collects interaction after each view and adjusts script for next time. Expected results: CTR +2–5%, CVR +2–4%, ARPU +9–13%.

## Gotchas
- Reward function needs balancing: if Rpers is too light vs Rprod, script is product-correct but not personalized; if vice versa, script is personalized but has wrong product info.
- GRPO needs K candidate samples per input, higher compute cost than standard DPO.
- Online feedback loop needs low latency; minimal revision avoids regenerating entire creative.
- Online results only from one specific scenario at Kuaishou, cannot generalize directly to all platforms.
- No real inference cost data vs retrieval-based systems.