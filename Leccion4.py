def validar_boton(boton_existe):
    if boton_existe:
        print("Test PASA: el botón existe")
    else:
        print("Test FALLA: el botón no existe")
        
validar_boton(True)
validar_boton(False)