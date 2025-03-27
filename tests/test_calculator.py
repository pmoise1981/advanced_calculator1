import pytest
import math
from app.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator(history=None)

def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(3, 5) == -2
    assert calculator.subtract(0, 0) == 0

def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 100) == 0

def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(1, 3) == pytest.approx(0.3333333333333333, rel=1e-15)
    with pytest.raises(ValueError):
        calculator.divide(1, 0)

def test_floating_point(calculator):
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3, rel=1e-9)
    # Adjust the precision for dividing 1 by 3
    assert calculator.divide(1.0, 3.0) == pytest.approx(0.3333333333333333, rel=1e-15)

def test_edge_cases(calculator):
    assert calculator.add(float('inf'), 1) == float('inf')
    assert calculator.add(float('-inf'), 1) == float('-inf')
    assert math.isnan(calculator.add(1, float('nan')))
    assert math.isnan(calculator.subtract(1, float('nan')))
    assert math.isnan(calculator.multiply(1, float('nan')))
    assert math.isnan(calculator.divide(1, float('nan')))
    assert calculator.subtract(float('inf'), 1) == float('inf')
    assert calculator.subtract(float('-inf'), 1) == float('-inf')
    assert math.isnan(calculator.subtract(1, float('nan')))
    assert calculator.multiply(float('inf'), 2) == float('inf')
    assert calculator.multiply(float('-inf'), 2) == float('-inf')
    assert math.isnan(calculator.multiply(0, float('nan')))
    assert calculator.divide(float('inf'), 2) == float('inf')
    assert calculator.divide(float('-inf'), 2) == float('-inf')
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
    assert math.isnan(calculator.add(1, float('nan')))
    assert math.isnan(calculator.subtract(1, float('nan')))
    assert math.isnan(calculator.multiply(1, float('nan')))
    assert math.isnan(calculator.divide(1, float('nan')))

