from fastapi import FastAPI, Depends

from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService

from api.schemas import EvaluationRequest
from api.auth import validate_api_key
from api.database import store_result, get_leaderboard


app = FastAPI(title="LLM Evaluation Service")

service = EvaluationService()


@app.post("/evaluate")
def evaluate(
    request: EvaluationRequest,
    role: str = Depends(validate_api_key)
):

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

    return {
        "model": result["model"],
        "metrics": result["metrics"],
        "experiment_id": experiment_id
    }


@app.get("/leaderboard")
def leaderboard(role: str = Depends(validate_api_key)):
    return get_leaderboard()