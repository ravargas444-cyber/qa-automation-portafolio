#Mi caja con etiquetas.
caja = {
    "nombre": "tomsmith",
    "clave": "SuperSecretPassword!",
    "pagina": "https://the-internet.herokuapp.com/login"
}

#Leemos etiqueta por etiqueta.
print("El nombre es:", caja["nombre"])
print("La clave es:", caja["clave"])
print("La pagina es:", caja["pagina"])

#Verificamos que la pagina tenga "login".
if "login" in caja["pagina"]:
    print("¡Si! Esta página es de login")