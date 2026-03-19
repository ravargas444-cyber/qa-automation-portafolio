from playwright.sync_api import sync_playwright

def test_login_invalido():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()
        
        # Abrir página de login
        pagina.goto("https://the-internet.herokuapp.com/login")
        
        # ESPERAR que el imput exista
        pagina.wait_for_selector("#username")
        
        # Escriir credenciales inválidas
        pagina.fill("#username", "usuario_invalido")
        pagina.fill("#password", "clave_invalida")
        
        # Click en lógin
        pagina.click("button[type='submit']")
        
        # Selector del mensaje de error
        mensaje_error = pagina.locator("#flash")
        
        texto = mensaje_error.inner_text()
        
        # Validación del mensaje
        print("MENSAJE REAL:")
        print(texto)
        
        if "username is invalid" in texto:
            print("TEST PASA: Mensaje de error correcto")
        else:
            print("TEST FALLA: Mensaje de error incorrecto")
            pagina.screenshot(path="error_login.png")
            
        navegador.close()
        
test_login_invalido()