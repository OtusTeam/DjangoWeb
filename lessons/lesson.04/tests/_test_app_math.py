import pytest
from app_math import my_sum


def test_example():
    assert True


def test_my_sum():
    assert my_sum(1, 4) == 5
    assert my_sum(0, 5) == 5
    assert my_sum(1, -2) == -1
    assert my_sum(7, 5) == 12


@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 4, 5),
        (2, 4, 6),
        (0, 5, 5),
        (1, -4, -3),
        (2, 5, 7),
    ])
def test_my_sum_param(num1, num2, expected):
    assert my_sum(num1, num2) == expected


@pytest.mark.parametrize("num1", [1, 2, 0])
@pytest.mark.parametrize("num2", [4, 5])
def test_my_sum_param_2(num1, num2):
    assert my_sum(num1, num2) == num1 + num2