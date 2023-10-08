
def repetir_nombre(NombreUsuario, NumeroDeVeces, Contador):
    while Contador < NumeroDeVeces:
        print(str(NombreUsuario))
        Contador = Contador +1

if __name__ == "__main__":

    NombreUsuario = input("Introduzca su nombre de usuario: ")
    NumeroDeVeces = int(input("Introduzca el nº de veces que quiere que se repita: "))

    Contador = 0

    repetir_nombre(NombreUsuario, NumeroDeVeces, Contador)
