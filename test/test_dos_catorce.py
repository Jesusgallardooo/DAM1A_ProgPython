import pytest

#Test del ejercicio 2_14

from src.dos_catorce import calcular_Peso_Paquete

def test_calcular_Peso_Paquete():
    assert calcular_Peso_Paquete(112, 75, 1, 1) == 187