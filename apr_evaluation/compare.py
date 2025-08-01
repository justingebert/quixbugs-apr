import json
import argparse
from pathlib import Path
from collections import defaultdict

def compare_model_attempts(data, output_path=None):
    """
    Groups runs by model and compares metrics between 1 and 3 attempts.
    Optionally saves the results as JSON if output_path is provided.
    """
    results = {}
    model_runs = defaultdict(dict)
    for run in data:
        model = run.get("model")
        attempts = run.get("max_attempts")
        if model and attempts in [1, 3]:
            model_runs[model][attempts] = run

    print("Comparison of Model Performance (3 attempts vs. 1 attempt):\n")
    for model, attempts_data in sorted(model_runs.items()):
        if 1 in attempts_data and 3 in attempts_data:
            run_1_attempt = attempts_data[1]
            run_3_attempts = attempts_data[3]

            # Calculate changes
            success_change = run_3_attempts["repair_success_rate"] - run_1_attempt["repair_success_rate"]
            time_change = run_3_attempts["avg_execution_time_per_issue"] - run_1_attempt["avg_execution_time_per_issue"]
            cost_change = run_3_attempts["avg_cost_per_issue"] - run_1_attempt["avg_cost_per_issue"]

            # Calculate percent changes
            time_percent_change = (time_change / run_1_attempt["avg_execution_time_per_issue"] * 100) if run_1_attempt["avg_execution_time_per_issue"] else 0
            cost_percent_change = (cost_change / run_1_attempt["avg_cost_per_issue"] * 100) if run_1_attempt["avg_cost_per_issue"] else 0

            print(f"--- Model: {model} ---")
            print(f"  Repair Success Rate Change: {success_change:+.2f}%")
            print(f"  Avg. Time/Issue Change:   {time_change:+.2f}s ({time_percent_change:+.2f}%)")
            print(f"  Avg. Cost/Issue Change:   ${cost_change:+.6f} ({cost_percent_change:+.2f}%)\n")

            results[model] = {
                "repair_success_rate_change": success_change,
                "avg_execution_time_per_issue_change": time_change,
                "avg_execution_time_per_issue_percent_change": time_percent_change,
                "avg_cost_per_issue_change": cost_change,
                "avg_cost_per_issue_percent_change": cost_percent_change
            }
    if output_path:
        with open(output_path, 'w') as out_f:
            json.dump(results, out_f, indent=2)
        print(f"Results saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Compare model performance between 1 and 3 attempts from aggregated metrics."
    )
    parser.add_argument(
        "metrics_file",
        type=Path,
        nargs='?',
        default=Path("apr_evaluation/aggregated_metrics.json"),
        help="Path to the aggregated metrics JSON file (defaults to 'apr_evaluation/aggregated_metrics.json')."
    )
    parser.add_argument(
        "--save",
        "-s",
        action="store_true",
        help="save the comparison results to a JSON file."
    )
    args = parser.parse_args()

    if not args.metrics_file.exists():
        print(f"Error: Metrics file not found at '{args.metrics_file}'")
        return 1

    with open(args.metrics_file, 'r') as f:
        aggregated_data = json.load(f)

    compare_model_attempts(
        aggregated_data,
        output_path="comparison_results.json" if args.save else None
    )
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())