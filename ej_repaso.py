url = "https://the-internet.herokuapp.com/login"
assert "/login" in url
print("¡Pasó!")

assert "/perfil" in url
print("Esto no se verá porque falla antes")