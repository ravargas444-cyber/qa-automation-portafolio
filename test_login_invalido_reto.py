def test_login_invaldo_reto(page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("username", "usuario_fake")
    page.fill("#password", "Clave mala")
    page.click("button[type='submit']")
    
    mensaje = page.locator("#flash").inner_text()
    assert "your username is invalid!" in mensaje
    
    