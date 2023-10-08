import pytest

#Test del ejercicio 2_11

from src.dos_once import suma_Enteros_Hasta

def test_suma_Enteros_Hasta():
    assert suma_Enteros_Hasta(3) == 6.0