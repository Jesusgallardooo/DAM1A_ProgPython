
def saludo(nombre):
    return ("Hola, " + (nombre))

if __name__=="__main__":
    
    nombre = input("Escribe tu nombre: ")
    print(saludo(nombre))