# test_addition.py

from src.calculator import multiply
import pytest


def test_multiply():
    result = multiply(12, 4)
    assert result == 48


def test_multiply_string():
    with pytest.raises(TypeError):
        multiply('string', 4)
