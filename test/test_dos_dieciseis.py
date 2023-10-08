import pytest

#Test del ejercicio 2_16

from src.dos_dieciseis import calcular_Precio_Con_Descuento

def test_Calcular_Precio_Con_Descuento():
    assert calcular_Precio_Con_Descuento(3.49, 2.094, 1) == 1.3960000000000004