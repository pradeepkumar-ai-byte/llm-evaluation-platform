import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from orchestration.contracts import GenerationInput, GenerationOutput


class ModelRunner:

    def __init__(self, model_name: str):
        self._model_name = model_name
        self._device = "cuda" if torch.cuda.is_available() else "cpu"

        self._tokenizer = AutoTokenizer.from_pretrained(model_name)
        self._model = AutoModelForCausalLM.from_pretrained(model_name).to(self._device)

    def run(self, request: GenerationInput) -> GenerationOutput:

        inputs = self._tokenizer(
            request.prompts,
            return_tensors="pt",
            padding=True,
            truncation=True
        ).to(self._device)

        with torch.no_grad():
            outputs = self._model.generate(
                **inputs,
                max_new_tokens=request.max_tokens
            )

        decoded = [
            self._tokenizer.decode(o, skip_special_tokens=True)
            for o in outputs
        ]

        return GenerationOutput(
            model=self._model_name,
            prompts=request.prompts,
            responses=decoded
        )