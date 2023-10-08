import pytest

#Test del ejercicio 2_13

from src.dos_trece import calcular_Cociente, calcular_Resto

def test_calcular_Cociente():
    assert calcular_Cociente(8,3) == 2

def test_calcular_Resto():
    assert calcular_Resto(8,3) == 2