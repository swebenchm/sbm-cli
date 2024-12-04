import typer
import requests
from typing import Optional
from rich.console import Console
from sbm_cli.config import API_BASE_URL, DEMO_API_KEY
from sbm_cli.utils import verify_response

app = typer.Typer(help="Delete a specific run by its ID")

def delete_run(
    split: str = typer.Argument(..., help="Split of the run to delete"),
    run_id: str = typer.Argument(..., help="Run ID to delete"),
):
    """Delete a specific run by its ID"""
    console = Console()
    headers = {
        "x-api-key": DEMO_API_KEY
    }
    payload = {
        "run_id": run_id,
        "split": split,
        "subset": 'swe-bench-m'
    }
    
    with console.status(f"[blue]Deleting run {run_id}..."):
        response = requests.delete(
            f"{API_BASE_URL}/delete-run",
            headers=headers,
            json=payload
        )
        verify_response(response)
        result = response.json()
    
    if response.status_code == 200:
        typer.echo(f"Run {run_id} successfully deleted for subset swe-bench-m and split {split}")
    else:
        typer.echo(f"Failed to delete run {run_id}: {result.get('message', 'Unknown error')}")

if __name__ == "__main__":
    app()
