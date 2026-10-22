# Skill: Tool-grounded coordination for quantitative multi-domain agents (methane framework)
Source: 2608.18473
Type: framework

## When to use this skill
- Need to automate multi-step workflows with quantitative components (field data analysis, business reporting).
- Have existing deterministic processing components to coordinate.
- Sensitive data requiring local processing.
- Do NOT use when fully autonomous final decisions are needed without human review, or when the dispersion model is unsuitable for the environment.

## Input needed
- Natural language request from user or CSV data file.
- Existing deterministic sensor processing routines and physical models.
- Meteorological data source (API or local data).
- Local LLM models (Llama 3.1 8B, Qwen 30B, Qwen-VL 8B via Ollama).

## Steps
1. Build the data input layer: receive natural language requests or CSV files, convert into structured task specifications (Request Parser + Task Classifier).
2. Build the coordination layer (Agent Router): route requests to appropriate analysis agents and tools.
3. Build the mission planning layer: extract time, target location, facility type; retrieve meteorological conditions; estimate downwind region.
4. Build the data analysis layer: preprocess measurements (unit conversion, background estimation); apply steady-state Gaussian plume model for source localization and emission-rate estimation.
5. Build the decision support and report generation layer: Validity Agent computes validity score from diagnostic factors; Report Generator Agent produces editable reports.
6. Deploy locally: keep sensitive data in the local computing environment, query external services only when needed.

## Expected output
- 92.0% workflow routing accuracy, 85.0% emission-rate/plume prediction success, 95.0% editable report generation.
- Workflow time reduced from hours-level to minutes-level.
- Report quality score averaging 9.0/10.

## Example application
- Enterprise field sensor data analysis system: LLM agent coordinates existing deterministic processing components, produces editable reports, data stays local without cloud upload.

## Gotchas
- Source localization performs poorly in built-up environments (wastewater facility 50%) — needs human review.
- Results are decision-support information, not autonomous final decisions.
- Depends on measurement quality and the underlying dispersion model.