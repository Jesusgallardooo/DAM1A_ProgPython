import pytest

#Test del ejercicio 2_6

from src.dos_seis import Calcular_Iva_Pagado

def test_Calcular_Iva_Pagado():
    assert Calcular_Iva_Pagado(100, 10/100) == 10
