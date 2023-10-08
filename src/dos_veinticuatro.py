

def calcular_Euros(Precio):
    Euros = Precio[:Precio.find('.')]
    return Euros

def calcular_Centimos(Precio):
    Centimos = Precio[Precio.find('.')+1:]
    return Centimos

if __name__ == "__main__":
    
    Precio = (input("Introduzca el precio de su producto: "))

    Euros = calcular_Euros(Precio)
    Centimos = calcular_Centimos(Precio)

    print("El precio del producto es de " + str(Euros) +" euros con " + str(Centimos) + " centimos.")

