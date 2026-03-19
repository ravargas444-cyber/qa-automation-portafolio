#features/steps/login_steps.py
#este archivo conecta el lenguje natural (feature) con el código Pyrhon.

from behave import given, when, then
from pages.login_page import LoginPage

#Usamos el browser_page del conftest.py a través de context
@given('que estoy en la página de login')
def step_ir_a_login(context):
    #el navegador viene del fixture de pytest/behave
    context.login_page = LoginPage(context.browser_page)
    context.login_page.ir_a_login()
    
@when('ingreso el usuario "{usuario}"')
def step_ingresar_usuario(context, usuario):
    context.login_page.ingresar_usuario(usuario)
    
@when('ingreso la contraseña "{password}"')
def step_ingresar_password(context, password):
    context.login_page.ingresar_password(password)
    
@when('hago clic en el botón login')
def step_click_login(context):
    context.login_page.hacer_click_login()
    
@then('deberia ver la página segura')
def step_verificar_pagina_segura(context):
    url = context.login_page.obtener_url_actual()
    assert "secure" in url #, f"Esperaba 'secure' en la URL, pero estaba en: {url}"
    
@then('deberia seguir en la pagina de login')
def step_verificar_pagina_segura(context):
    url = context.login_page.obtener_url_actual()
    assert "login" in url #, f"Esperaba 'login' en la URL, pero estaba en: {url}"