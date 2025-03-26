import pytest
from unittest.mock import patch
from app.main import REPL

@pytest.fixture
def repl():
    """Fixture to create a fresh REPL instance for each test."""
    return REPL()

def test_repl_addition(repl, capsys):
    """Test addition command in REPL."""
    with patch("builtins.input", side_effect=["add 5 3", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Result: 8.0" in captured.out

def test_repl_subtraction(repl, capsys):
    """Test subtraction command in REPL."""
    with patch("builtins.input", side_effect=["sub 10 4", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

def test_repl_multiplication(repl, capsys):
    """Test multiplication command in REPL."""
    with patch("builtins.input", side_effect=["mul 2 3", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Result: 6.0" in captured.out

def test_repl_division(repl, capsys):
    """Test division command in REPL."""
    with patch("builtins.input", side_effect=["div 8 2", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Result: 4.0" in captured.out

def test_repl_divide_by_zero(repl, capsys):
    """Test division by zero handling."""
    with patch("builtins.input", side_effect=["div 5 0", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Error" in captured.out

def test_repl_unknown_command(repl, capsys):
    """Test handling of unknown commands."""
    with patch("builtins.input", side_effect=["unknown", "exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

def test_repl_exit(repl, capsys):
    """Test exit command."""
    with patch("builtins.input", side_effect=["exit"]):
        with pytest.raises(SystemExit):
            repl.run()
    captured = capsys.readouterr()
    assert "Exiting calculator." in captured.out

