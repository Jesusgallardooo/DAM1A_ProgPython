


def cambiar_Dominio_Correo(Correo):
    CorreoNuevo = Correo[:Correo.find('@')] + '@ceus.es'
    return CorreoNuevo

if __name__ == "__main__":
    
    Correo = input("Introduzca su correo electrónico: ")

    CorreoNuevo = cambiar_Dominio_Correo(Correo)

    print (CorreoNuevo)