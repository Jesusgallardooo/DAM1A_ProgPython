
def funcion_Suma(NumeroUno, NumeroDos, NumeroTres):
    Resultado = NumeroUno + NumeroDos + NumeroTres
    return Resultado

def Mensaje_Resultado(Resultado):
    return "La suma de los tres numeros introducidos es = " + str(Resultado)

if __name__ == "__main__":

    NumeroUno = float(input("Introduzca el primer número: "))
    NumeroDos = float(input("Introduzca el segundo número: "))
    NumeroTres = float(input("Introduzca el tercer número: "))


    Resultado = funcion_Suma(NumeroUno, NumeroDos, NumeroTres)
    MensajeResultado = Mensaje_Resultado(Resultado)


    print(MensajeResultado)