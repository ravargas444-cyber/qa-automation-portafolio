edad_minima = 18
def validar_edad(edad_usuario):
    if edad_usuario >= edad_minima:
        print("Test PASA: Acceso permitido")
    else:
        print("Test FALLA: Acceso denegado")
        
validar_edad(16)
validar_edad(18)
validar_edad(25)