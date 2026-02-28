import json
from pathlib import Path
from typing import Dict


REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def export_json(run_id: str, content: Dict):
    path = REPORTS_DIR / f"{run_id}.json"
    with open(path, "w") as f:
        json.dump(content, f, indent=2)


def export_markdown(run_id: str, content: Dict):
    path = REPORTS_DIR / f"{run_id}.md"

    with open(path, "w") as f:
        f.write(f"# Benchmark Report\n\n")
        f.write(f"**Run ID:** {run_id}\n\n")

        for key, value in content.items():
            f.write(f"## {key}\n")
            f.write(f"{value}\n\n")