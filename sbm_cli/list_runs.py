import os
import requests
import typer
from typing import Optional
from rich.console import Console
from sbm_cli.config import API_BASE_URL, DEMO_API_KEY
from sbm_cli.utils import verify_response

app = typer.Typer(help="List all existing run IDs", name="list-runs")

def list_runs(
    split: str = typer.Argument(..., help="Split to list runs for"),
):
    """List all existing run IDs in your account"""
    console = Console()
    headers = {"x-api-key": DEMO_API_KEY}
    with console.status("[blue]Fetching runs..."):
        response = requests.post(
            f"{API_BASE_URL}/list-runs",
            headers=headers,
            json={"split": split, "subset": "swe-bench-m"}
        )
        verify_response(response)
        result = response.json()
    
    if len(result['run_ids']) == 0:
        typer.echo(f"No runs found for split {split}")
    else:
        typer.echo(f"Run IDs (swe-bench-m - {split}):")
        for run_id in result['run_ids']:
            typer.echo(run_id)
