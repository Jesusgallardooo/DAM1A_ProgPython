import pytest

#Test del ejercicio 2_7

from src.dos_siete import funcion_Suma

def test_funcion_suma():
    assert funcion_Suma(1,1,1) == 3