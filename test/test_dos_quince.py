import pytest

#Test del ejercicio 2_15

from src.dos_quince import calcular_Ahorros_año1, calcular_ahorros_año2, calcular_Ahorros_año3

def test_calcular_Ahorros_año1():
    assert calcular_Ahorros_año1(5, 5*0.04 ) == 4.8

def test_calcular_Ahorros_año2():
    assert calcular_ahorros_año2(5, 4.8*0.04, 4.8) == 9.608

def test_calcular_Ahorros_año3():
    assert calcular_Ahorros_año3(5, 9.608*0.04, 9.608) == 14.22368