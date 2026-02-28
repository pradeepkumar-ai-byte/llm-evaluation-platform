# LLM Evaluation Platform

Service layer responsible for orchestrating model inference and delegating evaluation to `llm-evaluation-framework`.

This repository does not implement statistical logic.  
All validation, statistical rigor, drift detection, and reporting are handled by the core engine.

---

## Architecture

```
ModelRunner
    ↓
GenerationOutput
    ↓
Schema Adapter
    ↓
Core Evaluator (llm-evaluation-framework)
    ↓
EvaluationOutput
```

Strict separation of responsibilities is maintained.

---

## Installation

Install the core repository locally:

```bash
pip install -e ../llm-evaluation-framework
```

Install platform dependencies:

```bash
pip install -r requirements.txt
```

---

## Example Usage

```python
from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService

request = GenerationInput(
    model="distilgpt2",
    prompts=["Explain quantum computing in simple terms."]
)

service = EvaluationService()
result = service.run(request)

print(result.report)
```

---

## Design Principles

- No statistical duplication
- Strict domain typing
- Deterministic schema mapping
- Thread-safe execution
- Clean boundary separation
- API-ready architecture
- Infrastructure-first design