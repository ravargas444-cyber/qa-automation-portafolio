def validar_status(respuesta):
    try:
        print(f"Status recibido: {respuesta['status']}")
        print("El sistema respondío correctamente")
    except:
        print("Error: no existe el campo 'status'")
        
respuesta_correcta = {"status": 200}
respuesta_incorrecta = {"mensaje": "Error"}

validar_status(respuesta_correcta)
validar_status(respuesta_incorrecta)