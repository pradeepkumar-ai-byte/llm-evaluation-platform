from collections import defaultdict
from typing import List, Dict

from experiments.storage import load_all_experiments


def generate_leaderboard() -> List[Dict]:

    experiments = load_all_experiments()

    scores = defaultdict(list)

    for exp in experiments:
        score = exp["metrics"]["mean_score"]
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