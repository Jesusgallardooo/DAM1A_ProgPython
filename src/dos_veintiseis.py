


def mostrar_Cada_Producto_Linea(cestaDeLaCompra):
    print(cestaDeLaCompra.replace(", ","\n"))

if __name__ == "__main__":

    cestaDeLaCompra = input("Introduzca los productos que quiera comprar separados por ', ' --> \n")

    mostrar_Cada_Producto_Linea(cestaDeLaCompra)