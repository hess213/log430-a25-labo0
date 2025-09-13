"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator
import pytest
import math

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests
@pytest.mark.parametrize(
    "a,b,expected",
    [(2, 3, 5), (-1, 1, 0), (0, 0, 0), (100, -7, 93)]
)
def test_addition(a, b, expected):
    calc = Calculator()
    assert calc.addition(a, b) == expected
    assert calc.last_result == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(5, 3, 2), (0, 1, -1), (-2, -2, 0)]
)
def test_subtraction(a, b, expected):
    calc = Calculator()
    assert calc.subtraction(a, b) == expected
    assert calc.last_result == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(2, 3, 6), (-1, 1, -1), (0, 99, 0)]
)
def test_multiplication(a, b, expected):
    calc = Calculator()
    assert calc.multiplication(a, b) == expected
    assert calc.last_result == expected

def test_division_ok():
    calc = Calculator()
    res = calc.division(10, 4)
    assert math.isclose(res, 2.5)
    assert math.isclose(calc.last_result, 2.5)

def test_division_by_zero():
    calc = Calculator()
    msg = calc.division(10, 0)
    assert msg == "Erreur : division par zéro"
    assert calc.last_result == "Error" 

# échec volontaire
"""def test_echec_volontaire():
    calc = Calculator()
    assert calc.addition(2, 2) == 5"""
#test
