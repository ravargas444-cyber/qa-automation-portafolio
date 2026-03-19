respuesta_login = {
    "status": 200,
    "mensaje": "unauthorized",
    "token": None
}

def validar_login(respuesta):
    if respuesta["status"] == 200:
        print(f"{respuesta['status']}: Login exitoso")
    else:
        print (f"{respuesta['status']}: Login fallido")
        
validar_login(respuesta_login)
    
               