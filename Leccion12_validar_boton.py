from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    
    pagina.goto("https://the-internet.herokuapp.com/login")
    
    try:
        boton_login = pagina.locator("button[type='submit']")
        if boton_login.is_visible():
            print("TEST PASA: Botón Login existe")
        else:
            print("TEST FASLLA: Botón Login no visible")
    except:
        print("ERROR: No se pudolocaizar el botón")
        
    pagina.wait_for_timeout(5000)
    navegador.close()