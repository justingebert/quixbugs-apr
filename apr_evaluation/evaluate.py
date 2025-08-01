import argparse
import json
import sys
from pathlib import Path


def calculate_metrics(run_path):
    """Calculate metrics from a pipeline run folder"""
    bugfix_results_file = run_path / "bugfix_results.json"
    ci_run_data_file = run_path / "ci_run_data.json"

    if not bugfix_results_file.exists() or not ci_run_data_file.exists():
        print(f"Error: Required files not found in {run_path}. Ensure 'bugfix_results.json' and 'ci_run_data.json' exist.")
        return None

    bugfix_results = {}
    with open(bugfix_results_file, 'r') as f:
        bugfix_results = json.load(f)

    ci_run_data = {}
    with open(ci_run_data_file, 'r') as f:
        ci_run_data = json.load(f)

    issues = bugfix_results.get("issues_processed", [])
    num_issues = len(issues)

    # Calculate per-issue metrics
    total_attempts = sum(issue.get("attempts", 0) for issue in issues)
    total_execution_time = sum(issue.get("execution_time", 0) for issue in issues)
    total_cost = sum(issue.get("tokens", {}).get("cost", 0) for issue in issues)

    avg_attempts = total_attempts / num_issues
    avg_execution_time = total_execution_time / num_issues
    avg_cost = total_cost / num_issues

    successful_repairs = bugfix_results.get("successful_repairs", 0)
    repair_success_rate = (successful_repairs / num_issues) * 100 if num_issues > 0 else 0

    # Get max_attempts from the first issue metrics file found
    max_attempts = 0
    issue_metrics_files = list(run_path.glob("issue_*_metrics.json"))
    if issue_metrics_files:
        with open(issue_metrics_files[0], 'r') as f:
            issue_metrics_data = json.load(f)
            max_attempts = issue_metrics_data.get("config", {}).get("max_attempts", 0)


    metrics = {
        "run_id": bugfix_results.get("github_run_id"),
        "model": bugfix_results.get("model", "unknown"),
        "max_attempts": max_attempts,
        "total_issues": num_issues,
        "successful_repairs": successful_repairs,
        "repair_success_rate": repair_success_rate,
        "avg_attempts_per_issue": avg_attempts,
        "avg_execution_time_per_issue": avg_execution_time,
        "avg_cost_per_issue": avg_cost,
        "total_execution_time": bugfix_results.get("total_execution_time", 0),
        "ci_run_duration": ci_run_data.get("total_duration_seconds", 0),
        "total_tokens": bugfix_results.get("llm_usage", {}).get("total_tokens", 0),
        "total_cost": bugfix_results.get("llm_usage", {}).get("total_cost", 0)
    }

    return metrics

def print_metrics(metrics):
    """Print metrics in a formatted way"""
    if not metrics:
        return

    print("\n===== Pipeline Run Metrics =====\n")
    print(f"Run ID: {metrics['run_id']}")
    print(f"Model: {metrics['model']}")
    print(f"Max Attempts: {metrics['max_attempts']}")
    print(f"Total Issues: {metrics['total_issues']}")
    print(f"Successful Repairs: {metrics['successful_repairs']}")
    print(f"Repair Success Rate: {metrics['repair_success_rate']:.2f}%")
    print("\n--- Per Issue Metrics ---")
    print(f"Average Attempts: {metrics['avg_attempts_per_issue']:.2f}")
    print(f"Average Execution Time: {metrics['avg_execution_time_per_issue']:.2f} seconds")
    print(f"Average Cost: ${metrics['avg_cost_per_issue']:.6f}")
    print("\n--- Overall Metrics ---")
    print(f"APR Execution Time: {metrics['total_execution_time']:.2f} seconds")
    print(f"CI Run Duration: {metrics['ci_run_duration']:.2f} seconds")
    print(f"Total Tokens: {metrics['total_tokens']}")
    print(f"Total Cost: ${metrics['total_cost']:.6f}")
    print("\n=============================")

def save_metrics(metrics, path):
    """Save metrics to a JSON file"""

    output_path = Path(path)
    if output_path.is_dir():
        output_path = output_path / f"run_{metrics['run_id']}_metrics.json"

    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"\nMetrics saved to: {output_path}")

def save_aggregated_metrics(metrics, output_path):
    """Save aggregated metrics to a JSON file"""
    output_path = Path(output_path)
    if output_path.is_dir():
        output_path = output_path / "aggregated_metrics.json"

    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"\nAggregated metrics saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Evaluate metrics from a pipeline run")
    parser.add_argument("run_path", nargs="?", default=None, help="Path to the run folder (default: most recent run)")
    parser.add_argument("--save", "-s", action="store_true", help="Save metrics to a JSON file")
    parser.add_argument("--all", "-a", action="store_true", help="aggergate all runs in the apr_evaluation directory")

    args = parser.parse_args()

    # process all runs in the apr_evaluation directory
    if args.all:
        evaluation_dir = Path("apr_evaluation")
        run_folders = [f for f in evaluation_dir.glob("run_*") if f.is_dir()]
        if not run_folders:
            print("Error: No run folders found in the apr_evaluation directory")
            return 1

        run_folders.sort()
        all_metrics = []
        for run_path in run_folders:
            print(f"Processing run folder: {run_path}")
            metrics = calculate_metrics(run_path)
            if metrics:
                print_metrics(metrics)
                all_metrics.append(metrics)

        if args.save:
            save_aggregated_metrics(all_metrics, evaluation_dir)

    # If no run_path provided, find most recent run
    elif not args.run_path and not args.all:
        evaluation_dir = Path("apr_evaluation")
        run_folders = [f for f in evaluation_dir.glob("run_*") if f.is_dir()]

        if not run_folders:
            print("Error: No run folders found in the apr_evaluation directory")
            return 1

        run_folders.sort(reverse=True)
        run_path = run_folders[0]
        print(f"Using latest run folder: {run_path}")

        metrics = calculate_metrics(run_path)

        if metrics:
            print_metrics(metrics)
            if args.save:
                save_metrics(metrics, run_path)
    # If run_path is provided, calculate metrics for that specific run
    else:
        run_path = Path(args.run_path)
        metrics = calculate_metrics(run_path)

        if metrics:
            print_metrics(metrics)
            if args.save:
                save_metrics(metrics, run_path)


    return 0

if __name__ == "__main__":
    sys.exit(main())