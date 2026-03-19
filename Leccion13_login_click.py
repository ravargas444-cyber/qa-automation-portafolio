from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    pagina.goto("https://the-internet.herokuapp.com/login")
    
    # Escribir usuario
    pagina.fill("#username", "usuario incorrrecto")
    
    # Escribir contraseña
    pagina.fill("#password", "password incorrecto")
    
    #Click en login
    pagina.click("button[type='submit']")
    
    try:
        mensaje_error = pagina.locator("#flash")
        if mensaje_error.is_visibe():
            print("TEST PASA: Mensaje de error visible")
        else:
            print("TEST FALLA: No aparecio mensaje de error")
    except:
        print("ERROR: No se pudo validar el mensaje")
        
    pagina.wait_for_timeout(5000)
    navegador.close()