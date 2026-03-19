from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    #1. Abrir navegador
    browser = p.chromium.launch(headless=False, slow_mo=500)
    
    #2. Crear página
    page = browser.new_page()
    
    #3. Ir al login
    page.goto("https://the-internet.herokuapp.com/login")
    
    #4. Ingresar datos inválidos
    page.fill("#username", "usuario_fake")
    page.fill("#password", "Clave_mala")
    
    #5. Click en Login
    page.click("button[type='submit']")
    
    #6. Capturar mensaje
    mensaje = page.locator("#flash").inner_text()
    print("Mensaje recibido:", mensaje)
    
    #7. Validar manualmente
    if "your username is invalido!" in mensaje:
        print("Test correcto: mensaje esperado")
    else:
        print("Test incorrecto")
        
    #8. Cerrar navegador
    browser.close()