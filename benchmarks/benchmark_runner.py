from typing import Dict, List

from orchestration.contracts import GenerationInput
from orchestration.service import EvaluationService


class BenchmarkRunner:

    def __init__(self):
        self._service = EvaluationService()

    def run(
        self,
        model: str,
        prompts: List[str],
        max_tokens: int
    ) -> Dict:

        request = GenerationInput(
            model=model,
            prompts=prompts,
            max_tokens=max_tokens
        )

        return self._service.run(request)