import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def save_experiment(model: str, report: str, metrics: Dict[str, Any]) -> str:
    experiment_id = str(uuid.uuid4())

    record = {
        "id": experiment_id,
        "model": model,
        "report": report,
        "metrics": metrics,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    file_path = RESULTS_DIR / f"{experiment_id}.json"

    with open(file_path, "w") as f:
        json.dump(record, f, indent=2)

    return experiment_id


def load_all_experiments() -> List[Dict[str, Any]]:
    experiments = []

    for file in RESULTS_DIR.glob("*.json"):
        with open(file) as f:
            experiments.append(json.load(f))

    return experiments