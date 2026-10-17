# Skill: self-evolving-multi-agent-translation
Source: 2609.38660v2
Type: framework

## When to use this skill
- Building multi-agent systems for long-form subtitle translation.
- Need to maintain terminology and style consistency across multiple episodes.
- Have subtitle data and parallel translations for training.

## When NOT to use this skill
- Sentence-level translation tasks that don't need context.
- No subtitle data available for training.
- Don't need long-form context consistency.

## Input needed
- Dataset of TV series episodes and their corresponding subtitles.
- Parallel subtitle datasets for training.
- LLM models for translation and evaluation.
- Tool-calling modules for terminology verification, subtitle constraint validation, and contextual retrieval.

## Steps to execute
1. Build a series-level memory from TV series episodes and their corresponding subtitles.
2. Build a multi-agent system with a dynamic graph router and Mixture-of-Agents translation layer.
3. Add tool-calling modules for terminology verification, subtitle constraint validation, and contextual retrieval.
4. Add a judge-refiner loop to evaluate each candidate translation and back-propagate textual critiques to refine agent prompts and routing policy.
5. Evaluate on subtitle translation datasets.

## Expected output
- Multi-agent subtitle translation system with high fidelity.
- Reduced average penalty compared to strongest competing agent system.
- High composite score in human evaluation.

## Application example
- Build a multi-agent system to translate TV series episodes. Use a multi-agent system with dynamic graph router and Mixture-of-Agents translation layer to translate each episode, while maintaining terminology and style consistency across multiple episodes.

## Gotchas
- Evaluated on 14 genres, 2–198 episodes per series, 15 target locales.
- No detailed information about training time and computational cost.
