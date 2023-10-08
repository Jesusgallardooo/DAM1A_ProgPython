



def conversor_Celsius_Fahrenheit(temperatura):
    fahrenheit = temperatura * 33.8
    return "Su temperatura equivale a " + str(fahrenheit) + " grados Fahrenheit"

if __name__ == "__main__":
    
    temperatura = float(input("Escriba la temperatura en grados Celsius: "))
    resultado = conversor_Celsius_Fahrenheit(temperatura)
    
    print(resultado)


