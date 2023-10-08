



def calcular_IMC(Peso, Estatura):
    IMC = Peso / (Estatura * Estatura)
    return IMC

if __name__ == "__main__":
    Peso = float(input("Introduzca su peso en Kg: "))
    Estatura = float(input("Introduzca su estatura en metros: "))

    IMC = calcular_IMC(Peso, Estatura)

    print("Tu índice de masa corporal es " + str(round(IMC,2)))