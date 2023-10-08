import pytest

#test ejercicio 2_26

from src.dos_veintiseis import mostrar_Cada_Producto_Linea

def test_mostrar_cada_producto_linea():
    assert mostrar_Cada_Producto_Linea("cocacola, fanta, pepsi") == "cocacola\n fanta\n pepsi"