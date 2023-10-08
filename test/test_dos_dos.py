import pytest

#Test del ejercicio 2_2
from src.dos_dos import calcula_sueldo

def test_calcula_sueldo():
    assert calcula_sueldo(2,3) == 6