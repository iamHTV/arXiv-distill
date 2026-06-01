# [2605.31514v1] If LLMs Have Human-Like Attributes, Then So Does Age of Empires II

## Problem
Many studies ascribe anthropomorphic attributes to LLMs such as morality or natural language understanding. However, these conclusions could be incorrect because: there are no explicit measurement criteria — interpretation depends on the observer's representation. Ascribing generalized anthropomorphic attributes leads to circular or uninformative conclusions.

## Contribution
1. **Demonstrates non-uniqueness of anthropomorphic attributes**: Builds and trains a simple neural network on the videogame Age of Empires II — any entity on a sufficiently powerful substrate (LEGO, Greater Boston Area, or a game) could present similar attributes
2. **Proposes "null assumption"**: Instead of assuming LLMs have anthropomorphic attributes, assume LLM non-uniqueness — design experiments that test the inverse
3. **Proof of Turing-completeness**: Proves Age of Empires II is functionally-complete and Turing-complete

## Method (core summary)
The author builds a neural network on Age of Empires II, trains it to perform complex tasks, and demonstrates that any sufficiently powerful substrate can exhibit the same attributes people ascribe to LLMs. Core argument: if you ascribe "understanding" to an LLM because it answers correctly, you must also ascribe "understanding" to AoE2 because it also processes correctly — both are just computation on a substrate. Proposes experimental framework: instead of asking "does LLM have X?", ask "is X unique to LLM? Show substrate-independent measurement."

## Key Findings
- [NO BENCHMARK] — purely philosophical/theoretical argument
- Demonstrated: AoE2 neural network exhibits behaviors that, if interpreted like LLM research, would be ascribed as "understanding", "planning", "strategy"
- Proved: AoE2 is functionally-complete and Turing-complete
- Showed: assuming anthropomorphic attributes exist independent of substrate → circular or uninformative conclusions, regardless of experimenter's viewpoint

## Actionable Insights
1. **When evaluating AI capabilities, always ask "is it unique?"**: Before claiming LLM "understands" or "reasons", check: does similar behavior appear on other substrates? Example: when vendor claims AI "understands" customer intent — ask: can a rule-based system produce the same output? If yes, "understanding" is just interpretation.

2. **Use null assumption in AI evaluation**: Design experiments with default assumption that AI does NOT have attribute X, and require inverse proof. Example: when evaluating AI creativity — assume AI is not creative, require demonstration that output cannot be explained by simple pattern matching.

3. **Substrate-independent measurement**: Define measurement criteria before interpreting behavior. Example: define "reasoning" = ability to solve novel problems with >80% accuracy on unseen distribution — not "AI responds like humans" because humans can also use pattern matching.

## Assumptions & Limitations
**Conditions for the argument to work:**
- Must accept that computation on substrate is substrate-independent
- Must accept that behavioral observation alone is insufficient to infer internal attributes

**Limitations the paper acknowledges:**
- Does not argue for or against existence of attributes — only argues conclusions could be incorrect
- Proving Turing-completeness of AoE2 is supporting argument, not main contribution

**Limitations the paper does NOT mention:**
- Does not address practical differences between LLM and game substrate — LLM has scale and generalization that AoE2 does not
- Argument could apply too broadly — every AI system gets dismissed
- Does not propose concrete alternative methodology for AI evaluation
- Philosophical argument, not empirical — hard to verify
- Turing-completeness proof may be irrelevant — modern LLMs are also Turing-complete but argument still holds

## Metadata
- Year: 2026
- Author: Adrian de Wynter
- Category: cs.CL, cs.AI, cs.CY
- PDF: https://arxiv.org/pdf/2605.31514v1
- Citation count: [EXTRACTION FAILED]
