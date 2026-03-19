#Este archivo guarda TODOS Los datos de prueba
#Lo separamos del test para organizar mejor
#Así podemosagregar más usuarios sin tocar el código del test


#USUARIOS es una lista (fila) de diccionarios (cajas)
#cada caja tiene 3 etiquetas: nombre, clave, debe_funcionar

USUARIOS = [
    #Primer usuario: este SÏ debería poder entar
    {"nombre": "tomsmith", "clave": "SuperSecretPassword!", "debe_funcionar":
True},
    #Segundo uasuario: este NO debería poder entrar (contraseña mala)
    {"nombre": "admin", "clave": "admin123", "debe_funcionar": False},
    #Tercer usuario: este tampoco debería entrar
    {"nombre": "pepito", "clave": "pepito456", "debe_funcionar": False} 
]