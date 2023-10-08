


def calcular_Cociente(n, m):
    c = n // m
    return c

def calcular_Resto(n, m):
    r = n % m
    return r

if __name__ == "__main__":

    n = int(input("Introduzca el numero que quiera dividir:")) #n = dividendo
    m = int(input("Introduzca el numero entre el que quiere dividirlo: ")) #m = divisor

    c = calcular_Cociente(n, m) #c = cociente
    r = calcular_Resto(n, m) #r = resto

    print("El cociente de la división es = " + str(c))
    print("El resto de la división es = " + str(r))