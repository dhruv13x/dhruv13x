# tests/test_banner.py
import os
from unittest.mock import patch
from dhruv13x.banner import print_logo, lerp, blend

def test_print_logo():
    with patch('rich.console.Console.print') as mock_print:
        print_logo()
        assert mock_print.call_count > 0

def test_print_logo_with_palette():
    with patch('rich.console.Console.print') as mock_print, \
         patch.dict(os.environ, {"CREATE_DUMP_PALETTE": "1"}):
        print_logo()
        assert mock_print.call_count > 0

def test_print_logo_with_palette_bad_value():
    with patch('rich.console.Console.print') as mock_print, \
         patch.dict(os.environ, {"CREATE_DUMP_PALETTE": "bad"}):
        print_logo()
        assert mock_print.call_count > 0

def test_print_logo_with_palette_out_of_bounds():
    with patch('rich.console.Console.print') as mock_print, \
         patch.dict(os.environ, {"CREATE_DUMP_PALETTE": "100"}):
        print_logo()
        assert mock_print.call_count > 0

def test_lerp():
    assert lerp(0, 10, 0.5) == 5
    assert lerp(-10, 10, 0.5) == 0
    assert lerp(10, 20, 0) == 10
    assert lerp(10, 20, 1) == 20

def test_blend():
    c1 = (0, 0, 0)
    c2 = (255, 255, 255)
    # Just checking if it returns a valid color string format
    assert blend(c1, c2, 0.5).startswith("#")
    assert len(blend(c1, c2, 0.5)) == 7
