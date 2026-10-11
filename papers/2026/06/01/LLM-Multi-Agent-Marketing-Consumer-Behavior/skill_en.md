# Skill: Marketing Simulation with LLM Multi-Agents
Source: 2510.18155
Type: workflow

## When to use this skill
- When testing marketing strategy before real-world deployment — reduce risk and cost
- When simulating consumer behavior under different scenarios — pricing, promotions, product launches
- When observing emergent social dynamics — word-of-mouth, habit formation, social coordination

## When NOT to use
- Need high quantitative accuracy — simulation provides qualitative insights only
- Market too large (10K+ consumers) — LLM simulation is expensive
- Need real-time results — simulation runs slowly

## Required inputs
- Virtual environment design: locations, spatial dynamics
- Agent personas: demographics, income, preferences, needs
- Marketing strategy to test: discount, promotion, pricing, etc.
- LLM access: DeepSeek-V3 or equivalent
- Simulation parameters: duration, agent count, location count

## Steps

### Step 1 — Design Virtual Environment
1. Create town map with locations: residential, business, shopping, dining, leisure
2. Define spatial dynamics: distances, paths between locations
3. Place shops/stores strategically: maximize exposure
4. Define shared resources: location tracker, time system

### Step 2 — Create Agent Personas
1. Diverse demographics: ages, professions, income levels
2. Unique preferences: food, activities, social tendencies
3. Needs system: grocery, energy, finance — triggers behavior
4. Memory system: short-term and long-term memory per agent

### Step 3 — Implement Agent Cognition
1. LLM-powered planning: agents plan daily routines based on needs, preferences, memory
2. Decision logic: agents make choices (dining, shopping, socializing) based on context
3. Conversation system: agents interact, share information, make plans together
4. Reflection: agents review past experiences, update preferences

### Step 4 — Run Simulation & Analyze
1. Inject marketing strategy: discount, promotion, new product
2. Run simulation N days, track all agent decisions
3. Analyze: sales performance, market share, loyalty patterns, social dynamics
4. Compare: treatment group (with promotion) vs control (no promotion)
5. Extract insights: substitution vs expansion, habit formation, word-of-mouth

## Expected output
- Sales impact: revenue change, market share shift
- Consumer behavior patterns: loyalty, exploration, switching
- Social dynamics: word-of-mouth, coordination, habit formation
- Strategy recommendations: optimal discount level, timing, targeting

## Example application
**Scenario**: Coffee chain wants to test "buy 1 get 1 free" promotion for new product launch. Doesn't want to spend real budget before knowing effectiveness.

**Application**:
1. Virtual town: 10 coffee shops, 20 agents with diverse coffee preferences
2. Agents have needs: caffeine, social, budget. Memory: past coffee experiences
3. Inject BOGO promotion at 1 shop, days 3-5
4. Run 7-day simulation
5. Analyze: did promotion attract new customers? Did they return? Did word-of-mouth spread? Did it cannibalize other shops?

## Gotchas
1. **Qualitative, not quantitative**: Simulation provides behavioral patterns, NOT exact numbers — use to generate hypotheses, not predict exact ROI
2. **Scale limitation**: 11 agents too few — need 100+ for meaningful market simulation
3. **LLM hallucination**: Agents may generate unrealistic behavior — validate against known consumer psychology
4. **Cost**: LLM calls expensive at scale — budget before running large simulations
5. **Environment design matters**: Spatial layout strongly affects behavior — design carefully
6. **Single scenario limitation**: Paper only tests discount — need multiple strategies to generalize
