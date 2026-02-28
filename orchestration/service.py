from orchestration.contracts import GenerationInput
from orchestration.evaluator import CoreEvaluator
from inference.runner import ModelRunner


class EvaluationService:

    def __init__(self):
        self._evaluator = CoreEvaluator()

    def run(self, request: GenerationInput):

        runner = ModelRunner(request.model)
        generation = runner.run(request)

        return self._evaluator.evaluate(generation)