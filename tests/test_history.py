import pytest
import pandas as pd
import logging
import os
from app.history import History

@pytest.fixture
def cleanup_history_file():
    """Fixture to clean up history file before tests run."""
    file_path = "mock_test_history.csv"
    if os.path.exists(file_path):
        os.remove(file_path)
    yield
    if os.path.exists(file_path):
        os.remove(file_path)

def test_add_entry_zero_division(cleanup_history_file):
    """Ensure ZeroDivisionError is raised when dividing by zero."""
    history = History("mock_test_history.csv")
    
    with pytest.raises(ZeroDivisionError, match="division by zero"):  # Ensure exception is raised
        history.add_entry("divide", 1, 0, 0)

def test_add_entry_logging(cleanup_history_file, caplog):
    """Ensure addition operation is logged properly."""
    history = History("mock_test_history.csv")
    
    with caplog.at_level(logging.INFO):
        history.add_entry("add", 1, 1, 2)
    
    assert "Added history entry: add 1 1 = 2" in caplog.text  # Match expected log format

def test_warning_log_operations(cleanup_history_file, caplog):
    """Ensure warning is logged for subtraction operations."""
    history = History("mock_test_history.csv")
    
    with caplog.at_level(logging.WARNING):
        history.add_entry("subtract", 5, 3, 2)

    assert "Warning: Operation near completion." in caplog.text  # Ensure warning is logged

def test_error_handling_zero_division(cleanup_history_file, caplog):
    """Ensure ZeroDivisionError is logged and raised."""
    history = History("mock_test_history.csv")

    with caplog.at_level(logging.ERROR):
        with pytest.raises(ZeroDivisionError, match="division by zero"):
            history.add_entry("divide", 1, 0, 0)

    assert "Error encountered: division by zero" in caplog.text  # Ensure error log is captured


def test_history_file_creation_if_not_exists(cleanup_history_file):
    """Ensure the history file is created when missing."""
    history = History("mock_test_history.csv")
    assert os.path.exists("mock_test_history.csv")  # Ensure file is created

def test_add_entry_edge_cases(cleanup_history_file):
    """Test adding an entry with edge cases (large numbers, negative values)."""
    history = History("mock_test_history.csv")
    history.add_entry("multiply", -99999999, 99999999, -9999999800000001)

    df = pd.read_csv("mock_test_history.csv")
    assert df.iloc[-1]["Operation"] == "multiply"
    assert df.iloc[-1]["Operand1"] == -99999999
    assert df.iloc[-1]["Operand2"] == 99999999
    assert df.iloc[-1]["Result"] == -9999999800000001

