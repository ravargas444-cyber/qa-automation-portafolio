class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = "#username"
        self.password = "#password"
        self.login_btn = "button[type='submit']"
        self.flash = "#flash"
        
    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self. page.click(self.login-btn)
        
    def error_message(self):
        return self.page.locator(self.flash)