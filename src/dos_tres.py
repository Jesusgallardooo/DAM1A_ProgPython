
def tipoDeVariable(operacionUno):
    return   str(type(operacionUno))

def tipoDeVariable(operacionDos):
    return  str(type(operacionDos))

def tipoDeVariable(operacionTres):
    return  str(type(operacionTres))

def tipoDeVariable(operacionCuatro):
    return  str(type(operacionCuatro))



if __name__ == "__main__":
    ancho = 17
    alto = 12.0

    operacionUno = ancho / 2
    operacionDos = ancho // 2
    operacionTres = alto / 3
    operacionCuatro = 1 + 2 * 5
    print("1. Ancho / 2 = " + str(operacionUno))
    print("2. Ancho // 2 = " + str(operacionDos))
    print("3. Alto / 3 = " + str(operacionTres))
    print("4. 1 + 2 * 5 = " + str(operacionCuatro))
    mensajeOperacionUno = "1. " + tipoDeVariable(operacionUno)
    mensajeOperacionDos = "2. " + tipoDeVariable(operacionDos)
    mensajeOperacionTres= "3. " + tipoDeVariable(operacionTres)
    mensajeOperacionCuatro = "4. " + tipoDeVariable(operacionCuatro)

    print(mensajeOperacionUno)
    print(mensajeOperacionDos)
    print(mensajeOperacionTres)
    print(mensajeOperacionCuatro)