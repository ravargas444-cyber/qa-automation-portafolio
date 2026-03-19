from playwright.sync_api import sync_playwright #

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False) # Código para: quiero ver  el navegador.
    pagina = navegador.new_page()
    pagina.goto("https://example.com") # Código para: ver esta página.
    pagina.wait_for_timeout(5000) # Código para: Espera 5 segundos.
    navegador.close()