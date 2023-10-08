import pytest

#Test del ejercicio 2_10

from src.dos_diez import operacion_concreta

def test_Operacion_Concreta():
    assert operacion_concreta() == "El resultado es 0.25"