def validar_boton(boton_valido):
    if boton_valido:
        print(f"botón existe: Test PASA")
    else:
        print(f"botón existe: Test FALLA")
        
botones = [True, False, False, True]

for boton in botones:
    validar_boton(boton)
     
