from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GenerationInput:
    model: str
    prompts: List[str]
    max_tokens: int = 50


@dataclass(frozen=True)
class GenerationOutput:
    model: str
    prompts: List[str]
    responses: List[str]


@dataclass(frozen=True)
class EvaluationOutput:
    model: str
    report: str
