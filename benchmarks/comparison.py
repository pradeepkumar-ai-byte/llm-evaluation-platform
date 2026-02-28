from typing import List, Dict
import math


def _mean(values: List[float]) -> float:
    return sum(values) / len(values)


def _variance(values: List[float]) -> float:
    m = _mean(values)
    return sum((x - m) ** 2 for x in values) / (len(values) - 1)


def _welch_t_test(a: List[float], b: List[float]) -> float:
    mean_a = _mean(a)
    mean_b = _mean(b)

    var_a = _variance(a)
    var_b = _variance(b)

    n_a = len(a)
    n_b = len(b)

    numerator = mean_a - mean_b
    denominator = math.sqrt((var_a / n_a) + (var_b / n_b))

    return numerator / denominator if denominator != 0 else 0.0


def _cohens_d(a: List[float], b: List[float]) -> float:
    mean_diff = _mean(a) - _mean(b)
    pooled_std = math.sqrt(
        ((_variance(a) + _variance(b)) / 2)
    )
    return mean_diff / pooled_std if pooled_std != 0 else 0.0


def compare_results(results: List[Dict]) -> Dict:

    if len(results) < 2:
        return {"error": "At least two models required for comparison"}

    sorted_results = sorted(
        results,
        key=lambda x: x["metrics"]["mean_score"],
        reverse=True
    )

    best = sorted_results[0]
    second = sorted_results[1]

    scores_a = best["metrics"]["per_prompt_scores"]
    scores_b = second["metrics"]["per_prompt_scores"]

    t_stat = _welch_t_test(scores_a, scores_b)
    effect_size = _cohens_d(scores_a, scores_b)

    return {
        "best_model": best["model"],
        "runner_up": second["model"],
        "mean_difference": round(
            best["metrics"]["mean_score"] -
            second["metrics"]["mean_score"],
            4
        ),
        "welch_t_statistic": round(t_stat, 4),
        "cohens_d": round(effect_size, 4)
    }