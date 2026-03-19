from playwright.sync_api import Page
#import pytest

#@pytest.fixture
#def page():
 #   with sync_playwright() as p:
  #      browser = p.chromium.launch(headless=False, slow_mo=500)
   #     page = browser.new_page()
    #    yield page
     #   browser.close()
        
        
def test_login_y_logout_exitoso(browser_page: Page):
    # 1. Abrir página de Login
    browser_page.goto("https://the-internet.herokuapp.com/login")
    
    # 2. Ingresar credenciales válidas
    browser_page.fill("#username", "tomsmith")
    browser_page.fill("#password", "SuperSecretPassword!")
    
    # 3. Clic en Login
    browser_page.click("button[type='submit']")
    
    # 4. Validar redirección correcta
    browser_page.wait_for_url("**/secure")
    
    # 5. Validar mensaje de texto
    #mensaje = page.locator("#flash").inner_text()
    
    # 6. Validar que existe botón Logout
    #assert page.locator("a.button").is_visible()
    
    # 7. Click en Logout
    browser_page.click("a.button")
    
    # 8. Validar regreso al Login
    browser_page.wait_for_url("**/login")
    assert "/login" in browser_page.url
    
    
def test_login_solo(login_page):
    login_page.fill("#username", "tomsmith")
    login_page.fill("#password", "SuperSecretPassword!")
    login_page.click("button[type='submit']")
    
    assert "secure" in login_page.url

#esto toma evidencia cuando el test falla    
#def test_que_falla(browser_page):
    #browser_page.goto("https://the-internet.herokuapp.com/login")
    #browser_page.fill("#username", "tomsmith")
    #browser_page.fill("#password", "SuperSecretPassword!")
    #browser_page.click("button[type='submit']")
    
    # Esto siempre falla porque ese texto no existe
    #assert "TEXTO_FALSO" in browser_page.inner_text("body")
    