import pytest

#Test del ejercicio 2_5

from src.dos_cinco import precio_Final

def test_precio_Final():
    assert precio_Final(ImporteSinIva = 100, IvaAplicado = 10 ) == 110