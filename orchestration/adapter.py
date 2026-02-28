from datetime import datetime
from typing import List, Dict

from orchestration.contracts import GenerationOutput


def to_core_schema(output: GenerationOutput) -> List[Dict]:

    timestamp = datetime.utcnow().isoformat() + "Z"
    dataset = []

    for idx, (prompt, response) in enumerate(zip(output.prompts, output.responses)):

        dataset.append({
            "id": idx + 1,
            "prompt": prompt,
            "response": response,
            "scores": {
                "instruction_adherence": 0,
                "factual_accuracy": 0,
                "logical_coherence": 0,
                "safety": 0,
                "tone_alignment": 0
            },
            "metadata": {
                "model": output.model,
                "timestamp": timestamp,
                "group": "generated"
            }
        })

    return dataset