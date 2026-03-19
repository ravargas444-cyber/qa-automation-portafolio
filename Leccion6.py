def validar_login(usuario_logueado):
    if usuario_logueado:
        print("Login Exitoso")
    else:
        print("Login Fallido")
        
usuarios = [True, False, True, False]

for usuario in usuarios:
    validar_login(usuario)