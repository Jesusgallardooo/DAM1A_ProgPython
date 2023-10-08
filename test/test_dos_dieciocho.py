import pytest

#Test del ejercicio 2_18

from src.dos_dieciocho import conversor_Iniciales_Mayusculas, conversor_Mayusculas, conversor_Minusculas

def test_conversor_Minusculas():
    assert conversor_Minusculas(NombreCompleto = "Jesus Gallardo Dominguez") == "jesus gallardo dominguez"

def test_conversor_Mayusculas():
    assert conversor_Mayusculas(NombreCompleto = "Jesus Gallardo Dominguez" ) == "JESUS GALLARDO DOMINGUEZ"

def test_conversor_Iniciales_Mayusculas():
    assert conversor_Iniciales_Mayusculas("Jesus", "Gallardo", "Dominguez") == "J G D"
