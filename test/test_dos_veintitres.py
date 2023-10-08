import pytest

#test ejercicio 2_23

from src.dos_veintitres import cambiar_Dominio_Correo

def test_cambiar_Dominio_Correo():
    assert cambiar_Dominio_Correo("hola@gmail.com") == "hola@ceus.es"