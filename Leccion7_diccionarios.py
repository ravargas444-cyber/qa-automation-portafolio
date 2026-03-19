usuarios = [
    {"nombre": "Pedro", "activo": True},
    {"nombre": "María", "activo": False},
    {"nombre": "Juan", "activo": True}
]

def validar_estado(usuario):
    if usuario["activo"]:
        print(f"{usuario['nombre']}: Usuario activo Test PASA")
    else:
        print (f"{usuario['nombre']}: Usuario inactivo Test FALLA")
        
for usuario in usuarios:
    validar_estado(usuario)