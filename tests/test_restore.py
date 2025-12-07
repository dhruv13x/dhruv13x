# tests/test_restore.py
import sys
from unittest.mock import MagicMock, patch
import pytest

# Mock dependencies before import
sys.modules["projectrestore"] = MagicMock()
sys.modules["projectrestore.cli"] = MagicMock()
sys.modules["projectclone"] = MagicMock()
sys.modules["projectclone.cli"] = MagicMock()

from dhruv13x.cli import restore

def test_restore_command():
    with patch('dhruv13x.cli.projectrestore_cli.main') as mock_main, \
         patch('dhruv13x.cli.console.print') as mock_print:
        restore()
        mock_print.assert_any_call("[yellow]Launching projectrestore...[/yellow]")
        mock_main.assert_called_once()
        mock_print.assert_any_call("[green]✅ Restore operation complete.[/green]")
