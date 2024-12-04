# SWE-bench-M CLI

A command-line interface for interacting with the SWE-bench M API. Use this tool to submit predictions, manage runs, and retrieve evaluation reports.

## Installation

```bash
pip install -e .
```

## Subsets and Splits

SWE-bench M has two different splits available:

### Splits
- `dev`: Development/validation split
- `test`: Test split

You'll need to specify a split for each command.

## Usage

### Submit Predictions

Submit your model's predictions to SWE-bench M:

```bash
sbm-cli submit test \
    --predictions_path example_preds/gpt-4o-swe-agent-m/all_preds_dev.json
```

Options:
- `--run_id`: Run ID to submit predictions to (optional) (default e.g.: gpt-4o-swe-agent-m)
- `--instance_ids`: Comma-separated list of specific instance IDs to submit (optional)
- `--output_dir`: Directory to save report files (default: sbm-cli-reports)
- `--overwrite`: Overwrite existing report files (default: False)
- `--gen_report`: Generate a report after evaluation is complete (default: True)

### Get Report

Retrieve evaluation results for a specific run:

```bash
sbm-cli get-report dev my_run_id -o ./reports
```

### List Runs

View all your existing run IDs for a specific subset and split:

```bash
sbm-cli list-runs dev
```

## Predictions File Format

Your predictions file should be a JSON file in one of these formats:

As a mapping:
```json
{
    "instance_id_1": {
        "model_patch": "...",
        "model_name_or_path": "..."
    },
    "instance_id_2": {
        "model_patch": "...",
        "model_name_or_path": "..."
    }
}
```

Or as a list:

```json
[
    {
        "instance_id": "instance_id_1",
        "model_patch": "...",
        "model_name_or_path": "..."
    },
    {
        "instance_id": "instance_id_2",
        "model_patch": "...",
        "model_name_or_path": "..."
    }
]
```
