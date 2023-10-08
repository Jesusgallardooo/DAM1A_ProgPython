



def mostrar_Fecha_Nacimiento(fecha):
    dia = fecha[:fecha.find('/')]
    MesDelAño = fecha[fecha.find('/')+1:]
    mes = MesDelAño[:MesDelAño.find('/')]
    año = MesDelAño[MesDelAño.find('/')+1:]


    print("dia: " + dia)
    print("mes: " + mes)
    print( "año: " + año)

if __name__ == "__main__":
    
    fecha = input("Introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")


    mostrar_Fecha_Nacimiento(fecha)