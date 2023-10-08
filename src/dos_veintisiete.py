



def calcular_importe_Final(precio, cantidad):
    importeFinal = precio * cantidad
    return importeFinal

def datos_Pedido(producto, precio, importeFinal):
    print("nombre del producto: " + producto)
    print("Precio del producto: " + str(precio))
    print("Importe final del pedido: " + str(importeFinal))

if __name__ == "__main__":
    
    producto = input("Introduzca el nombre del producto: \n")
    precio = float(input("Introduzca el precio del producto: \n"))
    cantidad = int(input("Introduzca el numero de " + producto + " que quiere: \n"))

    importeFinal = calcular_importe_Final(precio, cantidad)

    print(datos_Pedido(producto, precio, importeFinal))