# Skill: Task-based prompting technique selection
Source: 2610.24913
Type: workflow

## When to use this skill
- Need to select a prompting technique for an LLM-based system on a specific domain.
- Have an evaluation dataset representative of the target task.
- Do NOT use when assuming more complex prompting is always better without empirical evaluation.

## Input needed
- Evaluation dataset representative of the target task.
- An LLM (e.g. GPT-4o-mini).
- Candidate prompting techniques: Zero-Shot, Few-Shot, RAG, PE2.
- Task-specific example pools (100–300 examples).

## Steps
1. Run a small experiment on the representative dataset with Zero-Shot, Few-Shot (100/200/300 examples), RAG (example pools 100/200/300, k=5 retrieval), and PE2.
2. Measure accuracy for each technique and configuration.
3. Compare highest and second-highest configurations with statistical testing (McNemar test, Holm adjustment).
4. Select the technique performing best on the target task rather than defaulting to the most complex.
5. For structured reasoning tasks, prefer RAG with larger example pools (up to 300).

## Expected output
- The best-fitting prompting technique for the target task.
- Understanding of domain/task dependency (no universally optimal technique).

## Example application
- Enterprise QA system: run a small experiment on real questions with Zero-Shot, Few-Shot, RAG, and select the highest-accuracy technique instead of defaulting to Few-Shot with 300 examples.

## Gotchas
- No technique consistently outperforms across all domains; no statistically significant differences between top configurations.
- Increasing example count does not consistently improve performance.
- Results only for GPT-4o-mini; may not transfer to other models.