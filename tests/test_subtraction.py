# test_subtraction.py

from src.calculator import subtract
import pytest


def test_subtract():
    result = subtract(12, 4)
    assert result == 8


def test_subtract_string():
    with pytest.raises(TypeError):
        subtract('string', 4)
