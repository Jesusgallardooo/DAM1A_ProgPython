



def calcular_Peso_Paquete(PesoPayaso, PesoMuñeca, Payasos, Muñecas):
    PesoTotal = (Payasos*PesoPayaso) + (Muñecas*PesoMuñeca)
    return PesoTotal

if __name__ == "__main__":
    
    PesoPayaso = 112
    PesoMuñeca = 75

    Payasos = int(input("Introduzca el numero de payasos vendidos: "))
    Muñecas = int(input("Introduzca el numero de muñecas vendidas: "))

    PesoTotal = calcular_Peso_Paquete(PesoPayaso, PesoMuñeca, Payasos, Muñecas)

    print("El peso total del paquete es de " + str(PesoTotal) + " gramos")