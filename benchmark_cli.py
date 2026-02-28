import argparse
from benchmarks.dataset_loader import load_prompts
from benchmarks.benchmark_runner import BenchmarkRunner
from benchmarks.comparison import compare_results


def main():

    parser = argparse.ArgumentParser(
        description="Run structured LLM benchmark"
    )

    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        help="Path to benchmark prompt dataset (JSON list)"
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
            max_tokens=args.max_tokens
        )
        results.append(result)

    comparison = compare_results(results)

    print("Benchmark Results:")
    print(comparison)


if __name__ == "__main__":
    main()