#Importamos Page de Playwright para decirle a python qué tipo de dato es
from playwright.sync_api import Page

#Importamos la fábrica de usuarios que xreamos en el otro archivo
#"from datos_prueba_data_driven" = del archivo de datos_prueba_data_driven.py
#"omport USUARIOS" = traeme la variable USUARIOS
from datos_prueba_data_driven import USUARIOS

#Esta es la función de test
#"def" = definir (crear) una función
#"test_login_con_varios_usuarios" = nombre que describe qué hace
#"browser_page: Page" = recibimos el navegador de fixture (ya lo teníamos)
def test_login_con_varios_usuarios(browser_page: Page):
    
    #FOR = bucle mágico que repite algo varias veces
    #"usuarios in USUARIOS" = aggara una carga de la fábrica, llámala "usuario"
    #Esto se repite 3 veces (una por cada usuario en la lista)
    for usuario in USUARIOS:
        
        #Imprimimos en pantalla qué usuario estamos probando
        #Las f {} permiten poner variables dentro del texto
        print(f"Probando con: {usuario['nombre']}")
        
        #PASO 1: Ir a la página login
        #"browser_page.goto" = navegador, ve a esta dirección
        browser_page.goto("https://the-internet.herokuapp.com/login")
        
        #PASO 2: Escribir el nombre de usuario
        #"fill" = llenar (escribir en un campo)
        #"#username" = busca el elemento con id="username"
        #usuario["nombre"] = sacamos el nombre de la caja actual
        browser_page.fill("#username", usuario["nombre"])
        
        #PASO 3:Escribir la contraseña
        #Mismo proceso, pero con la clave y el campo pasword
        browser_page.fill("#password", usuario["clave"])
        
        #PASO 4: Hacer click en botón de login
        #"button[type='submit']" =busca botón con atributo type="submit
        browser_page.click("button[type='submit']")
        
        #PASO 5: Verificar si entró o no
        #IF = si (condición)
        #"usuario['debe_funcionar']" = miramos la etiquerta de la caja 
        #Si es True, esperamos de SÏ entró
        if usuario["debe_funcionar"]:
            
            #ASSERT = afirmar (asegurar que algo es verdad)
            #"secure in browser_page.url" = ¿La URL contiene palabra "secure"?
            #Si sí, el login funcionó. Si no, el test falla.
            assert "secure" in browser_page.url
            
            #Imprimimos que todo bien
            print(f"{usuario['nombre']} entró correctamente")
            
        #ELSE = si no (La condición era False)
        #este usuario NO debería poder entrar
        else:
            
            #Verificamos que sigue en la página de login (no entró)
            assert "login" in browser_page.url
            
            #Importamos que fue rechazado (y eso es lo esperado, no es error)
            print(f"{usuario['nombre']} fue rechazado (esto es correcto)")
            
        #Separador visual para leer mejor
        print("---")
        
    #Este mensaje aparece cuando el bucle terminó las 3 vueltas.
    print("Todas las pruebas terminaron!")