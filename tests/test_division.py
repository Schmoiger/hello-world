# test_division.py

from src.calculator import divide
import pytest


def test_divide():
    result = divide(12, 4)
    assert result == 3


def test_divide_string():
    with pytest.raises(TypeError):
        divide('string', 4)
