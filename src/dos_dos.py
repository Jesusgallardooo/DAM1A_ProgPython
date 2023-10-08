

def calcula_sueldo(HorasTrabajadas: int, CosteHora: int) -> int:
    ''' Calcula el suledo del empleado'''
    importeTotal = HorasTrabajadas * CosteHora
    return importeTotal

def mensajeHoras(horasTrabajadas):
    return "Horas trabajadas: " + str(horasTrabajadas)

def mensajeCosteHoras(costeHora):
    return "Coste por hora: " + str(costeHora)

def mensajeImporteTotal(importeTotal):
    return "Importe total: " + str(importeTotal)

if __name__ == "__main__":
    #Entrada
    horasTrabajadas = int(input("Introduzca cuantas horas trabajas: ")) 
    costeHora = int(input("Introduzca cuanto te pagan por hora: ")) 

    #Procesado
    importeTotal = calcula_sueldo(horasTrabajadas, costeHora)
    mensaje_horas = mensajeHoras(horasTrabajadas)
    mensajeCoste = mensajeCosteHoras(costeHora)
    mensajeImporte = mensajeImporteTotal(importeTotal)
    
    #Salida    
    print(mensaje_horas)
    print(mensajeCoste)
    print(mensajeImporte)