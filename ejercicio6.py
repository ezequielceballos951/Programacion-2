import re

def validar_contraseña(contraseña):
    if len(contrasena) < 8:
        return False

    if not re.search("[A-Z]", contraseña):
        return False
    if not re.search("[a-z]", contraseña):
        return False
    if not re.search("[0-9]", contraseña):
        return False
    if not re.search("[!@#$%^&*()_+{}:<>?]", contraseña):
        return False

    return True

contrasena = input("Ingrese su contraseña: ")

if validar_contrasena(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")
