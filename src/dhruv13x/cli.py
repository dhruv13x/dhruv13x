# src/dhruv13x/cli.py
import sys
import subprocess
import click
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print
from projectclone import cli as clone_cli
from importlib import metadata

console = Console()
app = typer.Typer(help="Dhruv13x — The Unified Developer Toolchain for Modern Python Engineering.")

from .banner import print_logo

def banner():
    print_logo()

# Custom Command Class to override help behavior
class DuplifinderHelpCommand(click.Command):
    def get_help(self, ctx: click.Context) -> str:
        try:
            result = subprocess.run(
                ["duplifinder", "--help"],
                text=True,
                capture_output=True,
                check=False
            )
            return result.stdout
        except FileNotFoundError:
            return "Error: duplifinder CLI not found in PATH."
        except Exception as e:
            return f"Error getting duplifinder help: {e}"

@app.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context):
    """Show banner or command help."""
    banner()
    if ctx.invoked_subcommand is None:
        console.print("[bold yellow]Use[/bold yellow] [green]dhruv13x --help[/green] for available commands.\n")


# === CORE COMMANDS ===

@app.command()
def tools():
    """List all installed meta tools."""
    console.print(Panel.fit("""
[bold green]✅ Installed meta tools:[/bold green]

• duplifinder         → detect duplicate definitions
• create-dump         → monorepo code dumper
• autoheader          → header template generator
• enterprise-docs     → doc compliance enforcer
• pyinitgen           → auto __init__.py generator
• pypurge             → clean project clutter
• import-surgeon      → rewrite unsafe imports
• projectclone        → atomic project snapshot
• projectrestore      → restore from snapshot
• importdoc           → import documentation scaffolder
• routine-workflow    → daily developer automation
""", border_style="green", title="Installed Tools"))


@app.command()
def version():
    """Show unified version info."""
    try:
        __version__ = metadata.version("dhruv13x")
    except metadata.PackageNotFoundError:
        __version__ = "0.0.0"
    console.print(Panel.fit(f"[bold cyan]dhruv13x meta-suite version:[/bold cyan] [white]{__version__}[/white]",
                            border_style="cyan", title="Version"))


@app.command()
def purge():
    """Run pypurge cleanup tool."""
    import subprocess
    console.print("[yellow]Running pypurge cleanup via subprocess...[/yellow]")

    try:
        result = subprocess.run(
            ["pypurge", "--allow-root", "-y"],
            text=True,
            capture_output=True,
            check=True
        )
        console.print(result.stdout)
        console.print("[green]✅ Cleanup complete![/green]")
    except FileNotFoundError:
        console.print("[red]❌ pypurge CLI not found in PATH.[/red]")
    except subprocess.CalledProcessError as e:
        console.print(f"[red]❌ pypurge failed with exit code {e.returncode}[/red]")
        console.print(e.stderr)


@app.command()
def clone():
    """Run projectclone CLI."""
    console.print("[yellow]Launching projectclone...[/yellow]")
    clone_cli.main()
    console.print("[green]✅ Clone operation complete.[/green]")


# === FUTURE COMMANDS (add 1 per release) ===
# @app.command()
# def restore(): from projectrestore import cli; cli.main()
@app.command(
    cls=DuplifinderHelpCommand, # Use custom command class for help
    context_settings={
        "allow_extra_args": True, 
        "ignore_unknown_options": True,
    }
)
def dedupe(ctx: typer.Context):
    """Run duplifinder tool."""
    console.print("[yellow]Launching duplifinder...[/yellow]")
    
    command = ["duplifinder"] + ctx.args
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=False)
        console.print(result.stdout)
        if result.stderr:
            console.print(f"[red]Duplifinder stderr:[/red]\n{result.stderr}")
        console.print("[green]✅ Duplication check complete.[/green]")
        sys.exit(result.returncode)
    except FileNotFoundError:
        console.print("[red]❌ duplifinder CLI not found in PATH. Please ensure 'duplifinder' is installed and accessible.[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]❌ An unexpected error occurred: {e}[/red]")
        sys.exit(1)
# @app.command()
# def import_fix(): from import_surgeon import cli; cli.main()
# @app.command()
# def init(): from pyinitgen import cli; cli.main()
# @app.command()
# def routine(): from routine_workflow import full_routine_workflow; full_routine_workflow.run()
# @app.command()
# def docs(): from enterprise_docs import cli; cli.main()


def run():
    """Entry point for `python -m dhruv13x`."""
    # This is a test comment to trigger a Git update.
    app()


if __name__ == "__main__":
    run()