import pytest

#Test del ejercicio 2_20

from src.dos_veinte import hallar_numero_Sin_Formato

def test_hallar_Numero_simple():
    assert hallar_numero_Sin_Formato(NumeroSinPref= +34-123456789-52 ) == 123456789