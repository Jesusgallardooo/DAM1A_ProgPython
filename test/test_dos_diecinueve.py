import pytest

#Test del ejercicio 2_18

from src.dos_diecinueve import contar_letras

def test_contar_letras():
    assert contar_letras("jesus", contador= 0) == 5