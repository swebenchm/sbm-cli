import typer

app = typer.Typer(help="CLI tool for interacting with the SWE-bench M API")

from . import (
    get_report,
    list_runs,
    submit,
)

app.command(name="get-report")(get_report.get_report)
app.command(name="list-runs")(list_runs.list_runs)
app.command(name="submit")(submit.submit)
def main():
    """Run the SWE-bench M CLI application"""
    import sys
    if len(sys.argv) == 1:
        app(['--help'])
    else:
        app()
