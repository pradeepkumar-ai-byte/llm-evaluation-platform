from pydantic import BaseModel
from typing import List


class EvaluationRequest(BaseModel):
    model: str
    prompts: List[str]
    max_tokens: int = 50


class EvaluationResponse(BaseModel):
    model: str
    report: str