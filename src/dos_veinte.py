

def hallar_numero_Sin_Formato(NumeroConFormato):
    NumeroSinPref = NumeroConFormato[NumeroConFormato.find('-')+1:]
    NumeroSimple = NumeroSinPref[:NumeroSinPref.find('-')]
    return NumeroSimple

if __name__ == "__main__":
    
    NumeroConFormato = input("Introduzca su numero de teléfono en formato prefijo-número-extension: ")


    NumeroSimple = hallar_numero_Sin_Formato(NumeroConFormato)


    print( "Tu numero de teléfono sin prefijo ni extensión es " + str(NumeroSimple))


