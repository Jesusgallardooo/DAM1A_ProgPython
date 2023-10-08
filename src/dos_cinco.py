



def precio_Final(ImporteSinIva, IvaAplicado):
    PrecioFinal = ImporteSinIva + (ImporteSinIva * IvaAplicado / 100)
    return PrecioFinal

def resultado(PrecioFinal):
    return "El precio final del producto con el IVA aplicado es: " + str(PrecioFinal)

if __name__ == "__main__":

    ImporteSinIva = float(input("Introduzca el importe sin IVA de su producto: "))
    IvaAplicado = float(input("Introduzca el porcentaje de IVA que le tendrá que aplicar: "))

    PrecioFinal = precio_Final(ImporteSinIva, IvaAplicado)

    print(resultado(PrecioFinal))