#Mostrar por pantalla el resultado de una aplicación aritmética concreta


def operacion_concreta():
    operacion = ((3+2)/(2*5))*((3+2)/(2*5))
    return "El resultado es " + str(operacion)

if __name__=="__main__":
    print(operacion_concreta())