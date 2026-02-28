# LLM Evaluation Platform

Service layer responsible for orchestrating model inference, structured benchmarking, experiment tracking, and report export while delegating statistical evaluation logic to the `llm-evaluation-framework` core engine.

This repository does not duplicate statistical methods.
All validation, scoring logic, drift detection, and evaluation rigor remain inside the core engine.

---

## System Overview

This platform provides:

- Model inference orchestration
- API service layer (FastAPI)
- Multi-model benchmarking
- Statistical comparison integration
- Versioned experiment registry
- JSON and Markdown report export
- CLI benchmark runner
- Dockerized deployment
- CI validation pipeline
- Structured production logging

---

## Repository Structure

llm-evaluation-platform/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── schemas.py
│   └── database.py
│
├── orchestration/
│   ├── __init__.py
│   ├── contracts.py
│   ├── adapter.py
│   ├── evaluator.py
│   ├── service.py
│   ├── job_registry.py
│   └── logging_config.py
│
├── inference/
│   ├── __init__.py
│   └── hf_runner.py
│
├── benchmarks/
│   ├── __init__.py
│   ├── dataset_loader.py
│   ├── benchmark_runner.py
│   └── comparison.py
│
├── experiments/
│   ├── __init__.py
│   ├── storage.py
│   ├── leaderboard.py
│   └── run_registry.py
│
├── reports/
│   ├── __init__.py
│   └── exporter.py
│
├── benchmark_cli.py
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── pyproject.toml
└── README.md

---

## Architecture

Inference & Evaluation Flow:

hf_runner (ModelRunner)
        ↓
GenerationInput
        ↓
Schema Adapter
        ↓
Core Evaluator (llm-evaluation-framework)
        ↓
EvaluationOutput
        ↓
Experiment Registry
        ↓
Report Export

Layered Responsibilities:

- inference/ → Model execution layer
- orchestration/ → Coordination and service logic
- benchmarks/ → Multi-model evaluation pipeline
- experiments/ → Persistent run tracking
- reports/ → Exportable artifacts
- api/ → External service interface
- benchmark_cli.py → Reproducible CLI benchmarking

Strict separation of statistical engine and platform orchestration is maintained.

---

## Installation

Install the core repository locally:

pip install -e ../llm-evaluation-framework

Install platform dependencies:

pip install -r requirements.txt

---

## Running the API Service

uvicorn api.main:app --reload

Available endpoints:

- POST /evaluate
- POST /compare
- GET /leaderboard

---

## CLI Benchmarking

Run structured multi-model benchmark:

python benchmark_cli.py \
  --dataset sample_dataset.json \
  --models distilgpt2 gpt2 \
  --max_tokens 50

Outputs:

- Versioned run artifact in benchmark_runs/
- JSON report in reports/
- Markdown report in reports/

Each run generates a unique run_id with timestamp and metadata.

---

## Experiment Tracking

Each benchmark execution records:

- run_id (UUID)
- Dataset reference
- Model list
- Aggregated comparison results
- Timestamp
- Platform version

Artifacts are stored for reproducibility and auditing.

---

## Logging

Structured logging is configured via:

orchestration/logging_config.py

Logs are:

- Streamed to console
- Persisted to logs/platform.log
- JSON-formatted
- Production-ready

---

## Docker

Build image:

docker build -t llm-eval-platform .

Run container:

docker run -p 8000:8000 llm-eval-platform

.dockerignore ensures clean container builds.

---

## CI Pipeline

GitHub Actions workflow:

- Checks out platform repository
- Checks out core repository
- Installs dependencies
- Validates lightweight imports
- Ensures build integrity

CI enforces structural correctness and import stability.

---

## Example Usage (Programmatic)

from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService

request = GenerationInput(
    model="distilgpt2",
    prompts=["Explain quantum computing in simple terms."],
    max_tokens=50,
)

service = EvaluationService()
result = service.run(request)

print(result["metrics"])

---

## Design Principles

- No statistical duplication
- Clean boundary between platform and core engine
- Deterministic schema mapping
- Infrastructure-first architecture
- Reproducible benchmarking
- Versioned experiment tracking
- Production-ready logging
- Deployment-ready structure

---

## Responsibility Boundary

This platform handles orchestration, benchmarking, persistence, and service exposure.

All evaluation logic, statistical rigor, and metric computation remain inside:

llm-evaluation-framework

The separation is intentional and strictly enforced.