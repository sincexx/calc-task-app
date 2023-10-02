from app.constants import CalculationOperators


def _perform_safe_division(x: int, y: int) -> float | int | None:
    return None if y == 0 else x / y


def perform_calculation(
    x: int, y: int, operator: CalculationOperators
) -> float | int | None:
    match operator:
        case CalculationOperators.ADD.value:
            return x + y
        case CalculationOperators.SUB.value:
            return x - y
        case CalculationOperators.MUL.value:
            return x * y
        case CalculationOperators.DIV.value:
            return _perform_safe_division(x, y)
