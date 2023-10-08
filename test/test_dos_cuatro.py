import pytest

#Test del ejercicio 2_4

from src.dos_cuatro import conversor_Celsius_Fahrenheit 

def test_conversor_celsius_fahrenheit():
    assert conversor_Celsius_Fahrenheit(temperatura=1) == "Su temperatura equivale a 33.8 grados Fahrenheit"