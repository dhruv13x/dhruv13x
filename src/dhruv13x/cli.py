# src/dhruv13x/cli.py

import typer
from rich import print
from pypurge import main as purge_main
from projectclone import cli as clone_cli

app = typer.Typer(help="Dhruv13x unified developer toolkit.")


@app.command()
def tools():
    """List all installed meta tools."""
    print("""
[bold green]✅ Installed meta tools:[/bold green]

- duplifinder
- create-dump
- autoheader
- enterprise-docs
- pyinitgen
- pypurge
- import-surgeon
- projectclone
- projectrestore
- importdoc
- routine-workflow
""")


@app.command()
def version():
    """Show meta-suite version."""
    from .version import __version__
    print(f"[cyan]dhruv13x meta-suite version:[/cyan] [bold]{__version__}[/bold]")


@app.command()
def purge():
    """Run pypurge cleanup tool."""
    print("[yellow]Running pypurge cleanup...[/yellow]")
    purge_main()


@app.command()
def clone():
    """Run projectclone CLI."""
    print("[yellow]Running projectclone...[/yellow]")
    clone_cli.main()  # assuming projectclone exposes cli.main()


# === Upcoming staged commands (each unlocked in next release) ===
# @app.command()
# def restore(): from projectrestore import cli; cli.main()
#
# @app.command()
# def dedupe(): from duplifinder import main; main()
#
# @app.command()
# def import_fix(): from import_surgeon import cli; cli.main()
#
# @app.command()
# def init(): from pyinitgen import cli; cli.main()
#
# @app.command()
# def routine(): from routine_workflow import full_routine_workflow; full_routine_workflow.run()
#
# @app.command()
# def docs(): from enterprise_docs import cli; cli.main()


def run():
    """Entry point for `python -m dhruv13x`."""
    app()


if __name__ == "__main__":
    run()