import pytest
from solution import convert


def test_single_symbol():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10
    assert convert("L") == 50
    assert convert("C") == 100
    assert convert("D") == 500
    assert convert("M") == 1000


def test_multiple_symbols():
    assert convert("II") == 2
    assert convert("III") == 3
    assert convert("VI") == 6
    assert convert("XVI") == 16


def test_subtractive_notation():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90
    assert convert("CD") == 400
    assert convert("CM") == 900


def test_mixed_case():
    assert convert("XIX") == 19


def test_invalid_roman():
    with pytest.raises(ValueError):
        convert("VX")

    with pytest.raises(ValueError):
        convert("XXC")