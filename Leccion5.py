edad_minima = 18

def validar_edad(edad_usuario):
    if edad_usuario >= edad_minima:
        print(f"Edad {edad_usuario}: Acceso permitido")
    else:
        print(f"Edad {edad_usuario}: Acceso denegado")
        
edades_a_probar = [16, 18, 25]

for edad in edades_a_probar:
    validar_edad(edad)