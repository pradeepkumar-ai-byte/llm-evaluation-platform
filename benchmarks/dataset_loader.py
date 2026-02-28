import json
from pathlib import Path
from typing import List


def load_prompts(path: str) -> List[str]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"Benchmark dataset not found: {path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Benchmark dataset must be a list of prompt strings")

    return data