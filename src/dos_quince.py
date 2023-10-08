

def calcular_Ahorros_año1(Capital, Interés):
    AhorrosPrimerAño = Capital - Interés
    return AhorrosPrimerAño


def calcular_ahorros_año2(Capital, Interés, AhorrosPrimerAño):
    AhorrosSegundoAño = (AhorrosPrimerAño + Capital) - Interés
    return AhorrosSegundoAño

def calcular_Ahorros_año3(Capital, Interés, AhorrosSegundoAño):
    AhorrosTercerAño = (AhorrosSegundoAño + Capital) - Interés
    return AhorrosTercerAño

if __name__ == "__main__":

    Capital = float(input("Introduzca la cantidad depositada al año: "))
    Interés = Capital * (4/100)

    # Esta cuenta de ahorros tiene el interés de un 4% al año, luego:
    
    print("     AHORROS DE LOS TRES PRIMEROS AÑOS CON INTERÉS APLICADO      ")
    AhorrosPrimerAño = calcular_Ahorros_año1(Capital, Interés)

    print("Los ahorros del primer año son: " + str(round(AhorrosPrimerAño,2)))

    Interés = AhorrosPrimerAño * (4/100)

    AhorrosSegundoAño = calcular_ahorros_año2(Capital, Interés, AhorrosPrimerAño)

    print("Los ahorros del segundo año son: " + str(round(AhorrosSegundoAño,2)))

    Interés = AhorrosSegundoAño * (4/100)
    AhorrosTercerAño = calcular_Ahorros_año3(Capital, Interés, AhorrosSegundoAño)
    
    print("Los ahorros del tercer año son: " + str(round(AhorrosTercerAño,2)))