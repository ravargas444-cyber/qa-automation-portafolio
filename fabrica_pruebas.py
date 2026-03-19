#Mi fábrica muchas cajas en fila.
fabrica = [
    {"nombre": "tomsmith", "clave": "SuperSecretPassword!"},
    {"nombre": "admin", "clave": "admin123"},
    {"nombre": "pepito", "clave": "pepito456"}
]

#Primera caja (posición 0)
primera = fabrica[0]
print("primera prueba con:", primera["nombre"])
print("Su clave es:", primera["clave"])

print("---")

#Segunda caja (posición 1)
segunda = fabrica[1]
print("Segunda prueba con:", segunda["nombre"])

print("---")

#¿Cuantas pruebas tengo?
print("Total de pruebas:", len(fabrica)) 