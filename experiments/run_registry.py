import json
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


RUNS_DIR = Path("benchmark_runs")
RUNS_DIR.mkdir(exist_ok=True)


def register_run(
    dataset: str,
    models: list,
    results: Dict[str, Any]
) -> str:

    run_id = str(uuid.uuid4())

    record = {
        "run_id": run_id,
        "dataset": dataset,
        "models": models,
        "results": results,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "platform_version": "0.1.0"
    }

    path = RUNS_DIR / f"{run_id}.json"

    with open(path, "w") as f:
        json.dump(record, f, indent=2)

    return run_id