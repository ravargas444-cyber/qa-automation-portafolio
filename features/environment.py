#features/environment.py 
#Configuración simplificada de behave

#from playwright.sync_api import sync_playwright

#def before_scenario(context, scenario):
    #Antes de cada escenario: iniciar todo
    #context.plywright = sync_playwright().start()
    #context.browser = context.playwright.chromium.launch(headless=False, slow_mo=500)
    #context.page = context.browser.new_page()
    
#def after_scenario(context, scenario):
    #Después de cada escenario: cerrar todo
    #context.browser.close()
    #context.playwright.stop()