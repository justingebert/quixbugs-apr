# LLM-based Automated Program Repair (APR) Evaluation

This repository was used to evaluate the application of a portable, LLM-based automated bug fixing prototype. The prototype aims to automatically repair bugs in software by leveraging Large Language Models (LLMs). It can be found at [github](https://github.com/justingebert/bugfix-ci)

This repository contains:
*   The buggy programs from the QuixBugs benchmark used for the evaluation.
*   The evaluation framework, including scripts to collect data, and analyze results.
*   The raw data and aggregated metrics from the evaluation runs.
*   Scripts to generate plots and comparisons from the evaluation data.

## Repository Structure

-   `python_programs/`: Contains the buggy Python programs from the QuixBugs benchmark.
-   `correct_python_programs/`: Contains the corrected versions of the programs.
-   `python_testcases/`: Pytest test cases to validate the correctness of program repairs.
-   `apr_evaluation/`: Holds all scripts and data related to the evaluation.
    -   `get_run_data.py`: Fetches run data from GitHub Actions.
    -   `evaluate.py`: Calculates and aggregates metrics from run data.
    -   `plot_model_metrics.py`: Generates plots from the aggregated metrics.
    -   `compare.py`: Compares performance between different run configurations (e.g., 1 vs. 3 attempts).
    -   `run_*`: Directories containing raw data from individual pipeline runs.
-   `scripts/`: Utility scripts, such as for creating GitHub issues for each bug.

## Evaluation

The core of this project is the evaluation of different LLMs on their ability to fix bugs. The scripts in the `apr_evaluation` directory are used to process the results of the APR pipeline runs and generate insights.
