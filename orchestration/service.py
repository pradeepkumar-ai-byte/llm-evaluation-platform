from typing import Dict, Any
import logging

from orchestration.contracts import GenerationInput
from inference.hf_runner import ModelRunner


logger = logging.getLogger(__name__)


class EvaluationService:
    """
    Coordinates model execution and evaluation flow.
    """

    def __init__(self) -> None:
        self.runner = ModelRunner()

    def run(self, generation_input: GenerationInput) -> Dict[str, Any]:
        """
        Execute evaluation pipeline for a given model input.
        """

        logger.info(f"Starting evaluation for model={generation_input.model}")

        outputs = self.runner.generate(
            model=generation_input.model,
            prompts=generation_input.prompts,
            max_tokens=generation_input.max_tokens,
        )

        # Basic metrics example
        metrics = {
            "total_prompts": len(generation_input.prompts),
            "total_outputs": len(outputs),
        }

        report = {
            "model": generation_input.model,
            "metrics": metrics,
        }

        logger.info(f"Completed evaluation for model={generation_input.model}")

        return {
            "model": generation_input.model,
            "outputs": outputs,
            "metrics": metrics,
            "report": report,
        }