Feature: Login en la aplicación
  Como usuario
  Quiero poder iniciar sesión
  Para acceder a la página segura

  Scenario: Login exitoso con credenciales válidas
    Dado que estoy en la página de login
    Cuando ingreso el usuario "tomsmith"
    Y ingreso la contraseña "SuperSecretPassword!"
    Y hago clic en el botón login
    Entonces debería ver la página segura

  Scenario: Login fallido con credenciales inválidas
    Dado que estoy en la página de login
    Cuando ingreso el usuario "admin"
    Y ingreso la contraseña "mala123"
    Y hago clic en el botón login
    Entonces debería seguir en la página de login