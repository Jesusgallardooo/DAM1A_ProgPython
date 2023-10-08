



def Calcular_Iva_Pagado(ImporteFinal, IvaAplicado):
    IvaPagado = (ImporteFinal)* IvaAplicado
    return IvaPagado

def Mensaje_Uno(IvaPagado):
    return "El IVA que ha pagado en esta compra equivale a " + str(IvaPagado)

def Mensaje_Dos(ImporteFinal, IvaPagado):
    return "El importe sin IVA de su producto equivaldría a " + str(ImporteFinal-IvaPagado)

if __name__ == "__main__":
    
    ImporteFinal = float(input("Introduzca el importe final de su producto: "))


    # Suponemos que el IVA es del 10% ya que es un dato del ejercicio.
    IvaAplicado = 10/100
    IvaPagado = Calcular_Iva_Pagado(ImporteFinal, IvaAplicado)
    MensajeUno = Mensaje_Uno(IvaPagado)
    MensajeDos = Mensaje_Dos(ImporteFinal,IvaPagado)

    print(MensajeUno)
    print(MensajeDos)