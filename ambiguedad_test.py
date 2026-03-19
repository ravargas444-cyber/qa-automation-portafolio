from playwright.sync_api import sync_playwright

html_content = """
<html>
    <body>
        <button aria-label="Guardar"></button>
        <button>Guardar</button>
    </body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.set_content(html_content)
    
    # Aquí provocamos la ambigüedad
    page.get_by_label("Guardar").click()
    
    browser.close()