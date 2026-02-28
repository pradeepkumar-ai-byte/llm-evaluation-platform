import json
from pathlib import Path
from typing import Dict, Any

REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def export_json(run_id: str, content: Dict[str, Any]) -> Path:
    """
    Export structured JSON report.
    Returns file path.
    """
    path = REPORTS_DIR / f"{run_id}.json"

    with path.open("w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)

    return path


def export_markdown(run_id: str, content: Dict[str, Any]) -> Path:
    """
    Export human-readable Markdown report.
    Returns file path.
    """
    path = REPORTS_DIR / f"{run_id}.md"

    with path.open("w", encoding="utf-8") as f:
        f.write("# Benchmark Report\n\n")
        f.write(f"**Run ID:** `{run_id}`\n\n")

        for key, value in content.items():
            f.write(f"## {key}\n\n")
            f.write("```json\n")
            f.write(json.dumps(value, indent=2, ensure_ascii=False))
            f.write("\n```\n\n")

    return path