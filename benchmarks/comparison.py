from typing import List, Dict


def compare_results(results: List[Dict]) -> List[Dict]:

    if not results:
        return []

    sorted_results = sorted(
        results,
        key=lambda x: x["metrics"]["mean_score"],
        reverse=True
    )

    best_score = sorted_results[0]["metrics"]["mean_score"]

    comparison = []

    for result in sorted_results:
        comparison.append({
            "model": result["model"],
            "mean_score": result["metrics"]["mean_score"],
            "delta_from_best": round(
                best_score - result["metrics"]["mean_score"],
                4
            )
        })

    return comparison