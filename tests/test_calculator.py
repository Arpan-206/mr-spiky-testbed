from src.calculator import add, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_divide_by_zero_raises():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
