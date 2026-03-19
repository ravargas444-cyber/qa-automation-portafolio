#Mi fabrica de usuarios
fabrica = [
    {"nombre": "tomsmith", "clave": "SuperSecretPassword!"},
    {"nombre": "admin", "clave": "admin123"},
    {"nombre": "pepito", "clave": "papito456"}
]

#El bucle mágico: prueba con cada Usuario.
for usuario in fabrica:
    print("probando con:", usuario["nombre"])
    print("clave:", usuario["clave"])
    print("resultado: Login exitoso (fingido)")
    print("---")
    
print("Terminé todas las pruebas!")