# tests/test_login.py
# Este archivo solo dice QUÉ queremos probar, no CÓMO
# El CÓMO está en pages/login_page.py

from playwright.sync_api import Page
from pages.login_page import LoginPage  # Importamos nuestra clase
from datos_prueba_data_driven import USUARIOS
def test_login_con_varios_usuarios(browser_page: Page):
    """
    Test que prueba login con múltiples usuarios usando Page Object Model
    """
    
    # Creamos un objeto LoginPage (nuestra caja de herramientas)
    login = LoginPage(browser_page)
    
    # Bucle que prueba con cada usuario
    for usuario in USUARIOS:
        print(f"🧪 Probando con: {usuario['nombre']}")
        
        # Usamos los métodos de nuestra clase (más limpio!)
        login.login_completo(usuario['nombre'], usuario['clave'])
        
        # Verificamos resultado
        if usuario['debe_funcionar']:
            assert "secure" in login.obtener_url_actual()
            print(f"   ✅ {usuario['nombre']} entró correctamente")
        else:
            assert "login" in login.obtener_url_actual()
            print(f"   ❌ {usuario['nombre']} fue rechazado (esperado)")
        
        print("---")
    
    print("✅ Todas las pruebas terminaron!")