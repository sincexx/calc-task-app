from app.constants import CalculationOperators
from app.calculation import perform_calculation


def test_addition():
    result = perform_calculation(5, 3, CalculationOperators.ADD.value)
    assert result == 8


def test_subtraction():
    result = perform_calculation(5, 3, CalculationOperators.SUB.value)
    assert result == 2


def test_multiplication():
    result = perform_calculation(5, 3, CalculationOperators.MUL.value)
    assert result == 15


def test_division_by_nonzero():
    result = perform_calculation(6, 3, CalculationOperators.DIV.value)
    assert result == 2.0


def test_division_by_zero():
    result = perform_calculation(5, 0, CalculationOperators.DIV.value)
    assert result is None
