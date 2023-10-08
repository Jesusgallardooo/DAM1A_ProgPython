

def calcular_Precio_Con_Descuento(PrecioBarra, Descuento, BarrasVendidasNoDelDía):
    CosteFinal = (BarrasVendidasNoDelDía * PrecioBarra) - (BarrasVendidasNoDelDía*Descuento)
    return CosteFinal

if __name__ == "__main__":

    PrecioBarra = 3.49

    # si no es del día, se le aplica un 60% de descuento, luego: 

    Descuento = PrecioBarra * (60/100)
    BarrasVendidasNoDelDía = int(input("Introduzca cuantas barras que no son del día se han vendido: "))

    print("El precio de una barra de pan del día es de " + str(PrecioBarra))
    print ("El descuento que se le hace a cada barra vendida que no es del día es de " + str(round(Descuento,2)) + " euros.")

    CosteFinal = calcular_Precio_Con_Descuento(PrecioBarra, Descuento, BarrasVendidasNoDelDía)

    print("El coste final de todas las barras no del día vendidas es de " + str(round(CosteFinal,2)) + " euros.")