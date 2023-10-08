import pytest

# test del ejercicio 2_21

from src.dos_veintiuno import invertir_Frase

def test_invertir_Frase():
    assert invertir_Frase(Frase = "hola") == "aloh"