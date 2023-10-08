import pytest

#Test de ejercicio 1 

from src.dos_uno import saludo

def test_saludo():
    assert saludo("Jesús") == "Hola, Jesús"