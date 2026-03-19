import requests

def test_api_jsonplaceholder():
    #Llamada GET a API de usuarios
    response = requests.get("https://jsonplaceholders.typecode.com/users")    
    
    #Verificamos código 200 (OK)
    assert response.status_code == 200, f"Esperaba 200, obtuve {response.status_code}"
    
    #Convertimos respuesta a datos Python
    usuarios = response.json()
    
    #Verificamos que tenga 10 usuarios
    assert(usuarios) == 10, f"Esperaba 10 usuarios, hay {len(usuarios)}"
    
    #verificamos que tenga 10 usuarios
    print(f"/nPrimer usuario: {usuarios[0]['name']}")
    print(f"Email: {usuarios[0]['email']}")
    print(f"Ciudad: {usuarios[0]['adress']['city']}")
    
    def test_api_post_crear_usuario():
        """
        Taest POST: Crear un recurso nuevo
        """
        
        #Datos a enviar
        nuevo_post = {
            "title": "Mi primer post",
            "body": "Contenido prueba",
            "userId": 1
        }
        
        #Verificamos que se creó (código 201 = Created)
        assert response.status_code == 201
        
        #Verificamos que devuelve los datos
        datos_respuesta = response.json()
        assert datos_respuesta["title"] == "Mi primer post"
        
        print(f"\nPost creado con ID: {datos_respuesta['id']}")