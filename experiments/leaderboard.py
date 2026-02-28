from collections import defaultdict
from typing import List, Dict

from experiments.storage import load_all_experiments


def extract_mean_score(report: str) -> float:
    # Simple parser assuming "Mean Score: X"
    for line in report.split("\n"):
        if "Mean" in line:
            try:
                return float(line.split(":")[-1].strip())
            except:
                continue
    return 0.0


def generate_leaderboard() -> List[Dict]:

    experiments = load_all_experiments()

    scores = defaultdict(list)

    for exp in experiments:
        score = extract_mean_score(exp["report"])
        scores[exp["model"]].append(score)

    leaderboard = []

    for model, model_scores in scores.items():
        avg_score = sum(model_scores) / len(model_scores)
        leaderboard.append({
            "model": model,
            "average_score": round(avg_score, 4),
            "runs": len(model_scores)
        })

    leaderboard.sort(key=lambda x: x["average_score"], reverse=True)

    return leaderboard