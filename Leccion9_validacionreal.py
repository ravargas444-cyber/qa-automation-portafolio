def test_login(respuesta):
    try:
        if respuesta["status"] == 200:
            print("TEST PASA: Login exitoso")
        elif respuesta["status"] == 401:
            print("TEST FALLA: Credenciales incorrectas")
        else:
            print(f"TEST INDETERMINADO: Status {respuesta['status']}")
            
    except: 
        print("X ERROR CRÍTICO: Falta el xampo 'status'")
        
respuesta_ok = {"status": 200}
respuesta_falla = {"satus": 401}
respuesta_rara = {"status": 500}
respuesta_invalida = {"mensaje": "error"}

test_login(respuesta_ok)
test_login(respuesta_falla)
test_login(respuesta_rara)
test_login(respuesta_invalida)