# tests/test_cli.py
import sys
import subprocess
from unittest.mock import MagicMock, patch
import pytest
from importlib import metadata
from typer.testing import CliRunner

# Mock the problematic dependency before it's imported by the app
sys.modules["projectclone"] = MagicMock()
sys.modules["projectclone.cli"] = MagicMock()
sys.modules["projectrestore"] = MagicMock()
sys.modules["projectrestore.cli"] = MagicMock()

from dhruv13x.cli import app, main_callback, tools, version, purge, clone, dedupe, DuplifinderHelpCommand, run

runner = CliRunner()

def test_main_callback():
    ctx = MagicMock()
    ctx.invoked_subcommand = None
    with patch('dhruv13x.cli.console.print') as mock_print:
        main_callback(ctx)
        mock_print.assert_called_with("[bold yellow]Use[/bold yellow] [green]dhruv13x --help[/green] for available commands.\n")

def test_tools():
    with patch('dhruv13x.cli.console.print') as mock_print:
        tools()
        assert mock_print.call_count == 1

def test_version():
    with patch('dhruv13x.cli.metadata.version', return_value="2.0.0"), \
         patch('dhruv13x.cli.console.print') as mock_print:
        version()
        mock_print.assert_called_once()

def test_version_not_found():
    with patch('dhruv13x.cli.metadata.version', side_effect=metadata.PackageNotFoundError), \
         patch('dhruv13x.cli.console.print') as mock_print:
        version()
        mock_print.assert_called_once()

def test_purge_success():
    with patch('dhruv13x.cli.subprocess.run') as mock_run:
        mock_run.return_value.stdout = "Purged"
        purge()
        mock_run.assert_called_once_with(
            ["pypurge", "--allow-root", "-y"],
            text=True,
            capture_output=True,
            check=True
        )

def test_purge_file_not_found():
    with patch('dhruv13x.cli.subprocess.run', side_effect=FileNotFoundError), \
         patch('dhruv13x.cli.console.print') as mock_print:
        purge()
        mock_print.assert_called_with("[red]❌ pypurge CLI not found in PATH.[/red]")

def test_purge_called_process_error():
    with patch('dhruv13x.cli.subprocess.run', side_effect=subprocess.CalledProcessError(1, "cmd", stderr="error")), \
         patch('dhruv13x.cli.console.print') as mock_print:
        purge()
        mock_print.assert_any_call("[red]❌ pypurge failed with exit code 1[/red]")

def test_clone():
    with patch('dhruv13x.cli.clone_cli.main') as mock_main:
        clone()
        mock_main.assert_called_once()

def test_dedupe_success():
    ctx = MagicMock()
    ctx.args = ["--path", "."]
    with patch('dhruv13x.cli.subprocess.run') as mock_run, \
         patch('dhruv13x.cli.sys.exit') as mock_exit:
        mock_run.return_value.stdout = "Deduplicated"
        mock_run.return_value.stderr = "error"
        dedupe(ctx)
        mock_run.assert_called_once_with(
            ["duplifinder", "--path", "."],
            text=True,
            capture_output=True,
            check=False
        )
        mock_exit.assert_called_once()

def test_dedupe_file_not_found():
    ctx = MagicMock()
    ctx.args = ["--path", "."]
    with patch('dhruv13x.cli.subprocess.run', side_effect=FileNotFoundError), \
         patch('dhruv13x.cli.console.print') as mock_print, \
         patch('dhruv13x.cli.sys.exit') as mock_exit:
        dedupe(ctx)
        mock_print.assert_called_with("[red]❌ duplifinder CLI not found in PATH. Please ensure 'duplifinder' is installed and accessible.[/red]")
        mock_exit.assert_called_once_with(1)

def test_dedupe_exception():
    ctx = MagicMock()
    ctx.args = ["--path", "."]
    with patch('dhruv13x.cli.subprocess.run', side_effect=Exception), \
         patch('dhruv13x.cli.console.print') as mock_print, \
         patch('dhruv13x.cli.sys.exit') as mock_exit:
        dedupe(ctx)
        mock_print.assert_any_call("[red]❌ An unexpected error occurred: [/red]")
        mock_exit.assert_called_once_with(1)

def test_dedupe_nonzero_returncode():
    ctx = MagicMock()
    ctx.args = ["--path", "."]
    with patch('dhruv13x.cli.subprocess.run') as mock_run, \
         patch('dhruv13x.cli.sys.exit') as mock_exit:
        # Mock subprocess.run to return a CompletedProcess with a non-zero returncode
        mock_run.return_value = MagicMock(
            stdout="Some output",
            stderr="Some error",
            returncode=2
        )
        dedupe(ctx)
        mock_run.assert_called_once()
        mock_exit.assert_called_once_with(2)

def test_duplifinder_help_command():
    cmd = DuplifinderHelpCommand("dedupe")
    with patch('dhruv13x.cli.subprocess.run') as mock_run:
        mock_run.return_value.stdout = "Duplifinder help"
        help_text = cmd.get_help(MagicMock())
        assert help_text == "Duplifinder help"

def test_duplifinder_help_command_file_not_found():
    cmd = DuplifinderHelpCommand("dedupe")
    with patch('dhruv13x.cli.subprocess.run', side_effect=FileNotFoundError):
        help_text = cmd.get_help(MagicMock())
        assert help_text == "Error: duplifinder CLI not found in PATH."

def test_duplifinder_help_command_exception():
    cmd = DuplifinderHelpCommand("dedupe")
    with patch('dhruv13x.cli.subprocess.run', side_effect=Exception):
        help_text = cmd.get_help(MagicMock())
        assert "Error getting duplifinder help" in help_text

@patch('dhruv13x.cli.app')
def test_run(mock_app):
    run()
    mock_app.assert_called_once()
