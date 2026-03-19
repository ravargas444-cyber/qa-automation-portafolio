from pages.login_page import LoginPage

def test_login_invalido(page):
    page.goto("https://the-internet.herokuapp.com/login")

    login = LoginPage(page)
    login.login("fake", "fake")

    mensaje = login.error_message()
    mensaje.wait_for(state="visible")

    assert "invalid" in mensaje.text_content()
