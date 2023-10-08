import pytest

#Test del ejercicio 2_17

from src.dos_diecisiete import repetir_nombre

def test_repetir_nombre():
    assert repetir_nombre("jesus", 1, 0) == "jesus" 