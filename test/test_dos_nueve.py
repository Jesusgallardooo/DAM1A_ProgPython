import pytest

#test del ejercicio 2_9

from src.dos_nueve import suma

def test_suma():
    assert suma(2,2,2) == 6