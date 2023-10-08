import pytest

#test del ejercicio 2_25

from src.dos_venticinco import mostrar_Fecha_Nacimiento

def test_mostrar_Fecha_Nacimiento():
    assert mostrar_Fecha_Nacimiento("7/1/2005") == "día: 7"; "mes: 1"; "año: 2005"