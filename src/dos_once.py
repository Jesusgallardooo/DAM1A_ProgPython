


def suma_Enteros_Hasta(Numero):
    SumaEnteros = (Numero * (Numero + 1)) / 2
    return SumaEnteros

if __name__ == "__main__":
    Numero = int(input("Introduzca un número entero positivo: "))


    SumaEnteros = suma_Enteros_Hasta(Numero)


    if(Numero >= 0):
        print("La suma de todos los enteros desde 1 hasta " + str(Numero) + " es: " + str(SumaEnteros))
    else:
        print("Error, fin del programa")