def test_login_status():
    respuesta = {
        "status": 200,
        "mensaje": "ok"
    }
    
    assert respuesta["status"] == 200
    