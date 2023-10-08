import pytest

#Test del ejercicio 2_12

from src.dos_doce import calcular_IMC

def test_Calcular_IMC():
    assert calcular_IMC(16,4) == 1.0