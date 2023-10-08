import pytest

#Test del ejercicio 2_4

from src.dos_tres import tipoDeVariable

def test_Tipo_De_Variable():
    assert tipoDeVariable(operacionUno = 8.5) == "1. <class 'float'>"
    assert tipoDeVariable(operacionDos = 8 ) == "2. <class 'int'>"
    assert tipoDeVariable(operacionTres = 4.0) == "3. <class 'float'>"
    assert tipoDeVariable(operacionCuatro = 11) == "4. <class 'int'>"
    


