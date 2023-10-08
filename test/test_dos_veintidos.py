import pytest

#test del ejercicio 2_22

from src.dos_veintidos import hacer_Mayusc_vocales

def test_hacer_Mayusc_vocales():
    assert hacer_Mayusc_vocales("hala","a") == "hAlA"