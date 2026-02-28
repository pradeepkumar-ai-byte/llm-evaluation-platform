import argparse

from benchmarks.dataset_loader import load_prompts
from benchmarks.benchmark_runner import BenchmarkRunner
from benchmarks.comparison import compare_results

from experiments.run_registry import register_run
from reports.exporter import export_json, export_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Run structured LLM benchmark with experiment tracking"
    )

    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to benchmark dataset (JSON list of prompts)"
    )

    parser.add_argument(
        "--models",
        nargs="+",
        required=True,
        help="Model names to evaluate"
    )

    parser.add_argument(
        "--max_tokens",
        type=int,
        default=50
    )

    args = parser.parse_args()

    prompts = load_prompts(args.dataset)
    runner = BenchmarkRunner()

    results = []

    for model in args.models:
        result = runner.run(
            model=model,
            prompts=prompts,
            max_tokens=args.max_tokens,
        )
        results.append(result)

    comparison = compare_results(results)

    run_id = register_run(
        dataset=args.dataset,
        models=args.models,
        results=comparison,
    )

    export_json(run_id, comparison)
    export_markdown(run_id, comparison)

    print("\nBenchmark Completed")
    print("Run ID:", run_id)
    print("Reports saved in /reports")
    print(comparison)


if __name__ == "__main__":
    main()