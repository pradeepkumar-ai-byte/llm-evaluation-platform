import logging
from fastapi import FastAPI, Depends

from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService
from orchestration.logging_config import configure_logging

from api.schemas import EvaluationRequest, MultiModelRequest
from api.auth import validate_api_key
from api.database import store_result, get_leaderboard

from benchmarks.multi_model import run_multi_model_evaluation
from benchmarks.ranking import rank_models


# Initialize structured logging
configure_logging("INFO")
logger = logging.getLogger(__name__)

app = FastAPI(title="LLM Evaluation Service")

service = EvaluationService()


@app.post("/evaluate")
def evaluate(
    request: EvaluationRequest,
    role: str = Depends(validate_api_key)
):
    logger.info(f"Received evaluation request model={request.model}")

    generation_input = GenerationInput(
        model=request.model,
        prompts=request.prompts,
        max_tokens=request.max_tokens
    )

    result = service.run(generation_input)

    experiment_id = store_result(
        result["model"],
        result["report"],
        result["metrics"]
    )

    logger.info(f"Evaluation completed model={request.model} experiment_id={experiment_id}")

    return {
        "model": result["model"],
        "metrics": result["metrics"],
        "experiment_id": experiment_id
    }


@app.post("/compare")
def compare(
    request: MultiModelRequest,
    role: str = Depends(validate_api_key)
):
    logger.info(f"Running multi-model comparison models={request.models}")

    results = run_multi_model_evaluation(
        models=request.models,
        prompts=request.prompts,
        max_tokens=request.max_tokens
    )

    ranked = rank_models(results)

    logger.info("Multi-model comparison completed")

    return ranked


@app.get("/leaderboard")
def leaderboard(role: str = Depends(validate_api_key)):
    logger.info("Leaderboard requested")
    return get_leaderboard()