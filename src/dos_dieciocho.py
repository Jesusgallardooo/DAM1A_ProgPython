

def conversor_Minusculas(NombreCompleto):
    print(NombreCompleto.lower())

def conversor_Mayusculas(NombreCompleto):
    print(NombreCompleto.upper())

def conversor_Iniciales_Mayusculas(Nombre, PrimerApellido, SegundoApellido):
    print((Nombre[0]).capitalize() + " " +  (PrimerApellido[0]).capitalize()  + " " + (SegundoApellido[0]).capitalize())

if __name__ == "__main__":

    Nombre = str(input("Introduzca su nombre: "))
    PrimerApellido = str(input("Introduzca su primer apellido: "))
    SegundoApellido = str(input("Introduzca su segundo apellido: "))
    NombreCompleto = Nombre + " " +  PrimerApellido + " " + SegundoApellido
    
    conversor_Minusculas(NombreCompleto)
    conversor_Mayusculas(NombreCompleto)

    conversor_Iniciales_Mayusculas(Nombre, PrimerApellido, SegundoApellido) 