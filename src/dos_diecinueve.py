
def contar_letras(NombreUsuario, contador):
    for i in NombreUsuario:
        contador = contador + 1
    return contador

if __name__ == "__main__":
    
    NombreUsuario = str(input("Introduzca su nombre de usuario: "))
    contador = 0

    contador = contar_letras(NombreUsuario, contador)

    print(NombreUsuario.upper() + " tiene " + str(contador) + " letras.")