# pages/login_page.py
# esta clase representa la pagina de login
# Solo dice QUË elementos hay, no CÖMO se usan

class LoginPage:
    """
    Clase que representa la página del login de the-internet.herokuapp.com
    """
    
    def __init__(self, page):
        """Constructor: recibe el navegador (page) y lo guarda
        """
        
        self.page = page #Guardamos el navegador para usarlo después.
        
        #Selectores: direcciones de los elementos en la página
        self.username_input = "#username"     #campo de usuario
        self.password_input = "#password"     #campo de contraseña
        self.login_button = "button[type='submit']"   #Botón de login
        self.logout_botton = "a.button"       #Botón de logout (aparece después)
        
    def ir_a_login(self):
        """
        Navega a la página de login
        """
        self.page.goto("https://the-internet.herokuapp.com/login")
        
    def ingresar_usuario(self, usuario):
        """
        Escribe el nombre de usuario en el campo
        """
        self.page.fill(self.username_input, usuario)

    def ingresar_password(self, password):
        """
        Escribe la contraseña en el campo
        """
        self.page.fill(self.password_input, password)
        
    def hacer_cilck_login(self):
        """
        Hace click en el botón de login
        """
        self.page.click(self.login_button)
        
    def hacer_cilck_logout(self):
        """
        Hece click en el botón de logout
        """
        self.page.click(self.logout_botton)
        
    def login_completo(self, usuario, password):
        """
        hace todo el proceso de login en un solo paso
        """
        self.ir_a_login()
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_cilck_login()
        
    def obtener_url_actual(self):
        """
        Devuelve la URL dende estamos ahora
        """
        return self.page.url
    
        