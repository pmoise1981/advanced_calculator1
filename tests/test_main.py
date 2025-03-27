import pytest
from unittest.mock import patch
from app.main import main

def test_main_function_execution_add(capfd):
    with patch('builtins.input', side_effect=['1', '5', '3', '6']):  # Add 5 + 3, then exit
        main()
    captured = capfd.readouterr()
    assert "Result: 8.0" in captured.out  # Ensure correct result
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_subtract(capfd):
    with patch('builtins.input', side_effect=['2', '5', '3', '6']):  # Subtract 5 - 3, then exit
        main()
    captured = capfd.readouterr()
    assert "Result: 2.0" in captured.out  # Ensure correct result
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_multiply(capfd):
    with patch('builtins.input', side_effect=['3', '5', '3', '6']):  # Multiply 5 * 3, then exit
        main()
    captured = capfd.readouterr()
    assert "Result: 15.0" in captured.out  # Ensure correct result
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_divide(capfd):
    with patch('builtins.input', side_effect=['4', '5', '0', '6']):  # Divide 5 / 0 (error), then exit
        main()
    captured = capfd.readouterr()
    assert "Cannot divide by zero" in captured.out  # Ensure divide-by-zero error
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_history(capfd):
    with patch('builtins.input', side_effect=['5', '6']):  # View history, then exit
        main()
    captured = capfd.readouterr()
    assert "History:" in captured.out  # Ensure history is displayed
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_invalid_choice(capfd):
    with patch('builtins.input', side_effect=['7', '6']):  # Invalid choice, then exit
        main()
    captured = capfd.readouterr()
    assert "Invalid choice" in captured.out  # Ensure invalid choice is handled
    assert "User exited the calculator" in captured.out  # Ensure graceful exit

def test_main_function_execution_exit(capfd):
    with patch('builtins.input', side_effect=['6']):  # Exit the calculator
        main()
    captured = capfd.readouterr()
    assert "User exited the calculator" in captured.out  # Ensure exit message is shown

def test_unexpected_error_handling(capfd):
    with patch('builtins.input', side_effect=['1', 'a', '3', '6']):  # Invalid input 'a', then exit
        main()
    captured = capfd.readouterr()
    assert "An unexpected error occurred" in captured.out  # Ensure error handling works
    assert "User exited the calculator" in captured.out  # Ensure graceful exit after error

