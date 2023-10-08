def suma():
    return "El resultado de la suma de tus tres numeros es: " + str(int(input("Introduzca el primer número: ")) + int(input("Introduzca el segundo número: ")) + int(input("Introduzca el tercer número: ")))

if __name__ == "__main__":
    print(suma())