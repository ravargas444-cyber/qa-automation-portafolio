respuesta = {"mensaje": "Error"}

try:
    print(respuesta["status"])
except:
    print("X Falta el campo status en la respuesta")