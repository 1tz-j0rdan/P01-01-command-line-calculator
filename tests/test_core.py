import pytest

from calculator import CalculatorError, calculate


@pytest.mark.parametrize("expression, expected", [
    ("2 + 3", 5),
    ("(2 + 3) * 4", 20),
    ("10 / 4", 2.5),
    ("2 ** 3", 8),
    ("7 // 2", 3),
    ("7 % 2", 1),
    ("-5 + 2", -3),
    ("2 + 3 * 4", 14),
])
def test_calculate(expression, expected):
    assert calculate(expression) == expected


@pytest.mark.parametrize("expression", [
    "", "1 / 0", "hello", "__import__('os')", "[1, 2]", "2 ** 1000", "1 +", "True + 2",
])
def test_invalid(expression):
    with pytest.raises(CalculatorError):
        calculate(expression)
