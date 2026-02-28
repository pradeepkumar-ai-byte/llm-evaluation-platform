import json
import tempfile
from pathlib import Path
from typing import Dict, Any

from llm_eval.config import Config
from llm_eval.validation import load_and_validate_dataset
from llm_eval.reporting import generate_report

from orchestration.adapter import to_core_schema
from orchestration.contracts import GenerationOutput


class CoreEvaluator:

    def __init__(self):
        self._config = Config()

    def evaluate(self, generation: GenerationOutput) -> Dict[str, Any]:

        dataset = to_core_schema(generation)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
            json.dump(dataset, tmp)
            tmp_path = Path(tmp.name)

        validated = load_and_validate_dataset(tmp_path, self._config)
        report = generate_report(validated, self._config)

        tmp_path.unlink(missing_ok=True)

        # Extract structured metrics directly from validated dataset
        scores = [
            sum(item["scores"].values()) / len(item["scores"])
            for item in validated
        ]

        mean_score = sum(scores) / len(scores) if scores else 0.0

        return {
            "model": generation.model,
            "report": report,
            "metrics": {
                "mean_score": round(mean_score, 4),
                "num_samples": len(scores)
            }
        }