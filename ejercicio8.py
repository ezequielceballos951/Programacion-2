import random
import string

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ""
    for _ in range(12):
        caracter_aleatorio = random.choice(caracteres)
        contraseña += caracter_aleatorio
    return contraseña

def main():
    contraseña_generada = generar_contraseña()
    print("Tu nueva contraseña es:", contraseña_generada)

if __name__ == "__main__":
    main()
