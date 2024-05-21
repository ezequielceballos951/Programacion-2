import random

palabras = ["python", "programacion", "ahorcado", "juego", "simple"]

palabra = random.choice(palabras)
palabra_oculta = "_" * len(palabra)
intentos_restantes = 6
letras_adivinadas = []

def mostrar_estado():
    print(f"Palabra: {palabra_oculta}")
    print(f"Intentos restantes: {intentos_restantes}")
    print(f"Letras adivinadas: {' '.join(letras_adivinadas)}")

while intentos_restantes > 0 and "_" in palabra_oculta:
    mostrar_estado()
    letra = input("Adivina una letra: ").lower()
    
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
    elif letra in palabra:
        letras_adivinadas.append(letra)
        palabra_oculta = "".join([letra if letra == c else oculta for c, oculta in zip(palabra, palabra_oculta)])
    else:
        letras_adivinadas.append(letra)
        intentos_restantes -= 1
        print(f"Letra incorrecta. Pierdes un intento.")

if "_" not in palabra_oculta:
    print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
else:
    print(f"Te has quedado sin intentos. La palabra era: {palabra}")
