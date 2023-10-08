import pytest

#test del ejercicio 2_27

from src.dos_veintisiete import calcular_importe_Final

def test_calcular_importe_final():
    assert calcular_importe_Final(1,1) == 1