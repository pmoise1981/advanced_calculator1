import pytest
import logging
from app.history import History
from app.logger import setup_logger

def test_log_test_operations(caplog):
    """Ensure error log is captured when division by zero occurs."""
    history = History("mock_test_history.csv")

    with caplog.at_level(logging.ERROR):
        try:
            history.add_entry("divide", 1, 0, 0)
        except ZeroDivisionError:
            pass  # Expected exception

    assert "Error encountered: division by zero" in caplog.text  # Check if the error log is present

def test_warning_log_operations(caplog):
    """Ensure subtraction operations trigger a warning log."""
    history = History("mock_test_history.csv")

    with caplog.at_level(logging.WARNING):
        history.add_entry("subtract", 5, 3, 2)

    assert "Warning: Operation near completion." in caplog.text  # Check if warning log is present

from app.logger import setup_logger

def test_logger_initialization():
    """Test that the logger is initialized without errors."""
    logger = setup_logger()
    assert logger is not None

def test_logger_logs_messages(caplog):
    """Ensure the logger logs messages at different levels."""
    logger = setup_logger()

    with caplog.at_level(logging.INFO):
        logger.info("Test info log")

    with caplog.at_level(logging.ERROR):
        logger.error("Test error log")

    assert "Test info log" in caplog.text
    assert "Test error log" in caplog.text

