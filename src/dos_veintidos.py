

def hacer_Mayusc_vocales(Frase, Vocal):
    FraseVocalMayúsc = (Frase.replace(Vocal, Vocal.upper()))
    return FraseVocalMayúsc

if __name__ == "__main__":
    
    Frase = str(input("Introduzca una frase: "))
    Vocal = str(input("Introduzca una vocal: "))

    FraseVocalMayúsc = hacer_Mayusc_vocales(Frase, Vocal)

    print(FraseVocalMayúsc)
