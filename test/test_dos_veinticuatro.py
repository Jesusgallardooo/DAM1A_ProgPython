import pytest

#test del ejercicio 2_24

from src.dos_veinticuatro import calcular_Centimos, calcular_Euros

def test_calcular_Euros():
    assert calcular_Euros("1.54") == "1"

def test_calcular_Centimos():
    assert calcular_Centimos("1.54") == "54"