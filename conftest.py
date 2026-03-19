import pytest
from playwright.sync_api import sync_playwright, Page
import os #importamos os para crear carpetas en el sistema operativo

@pytest.fixture
def browser_page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
                
        yield page  # <-- aquí corre el test
   
    
        # esto se ejecutó despues del test
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True) #crea la carpeta "screenshots" si no existe / axist_ok=True no da error si ya existe
            page.screenshot(path=f"screenshots/{request.node.name}.png")
            
        browser.close()

@pytest.fixture
def login_page(browser_page: Page): 
    browser_page.goto("https://the-internet.herokuapp.com/login")
    return browser_page
        
        
        
# Hook para saber si el test falló
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    
        