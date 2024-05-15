import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Intenta adivinar el número: "))
        intentos += 1

        if intento < numero_secreto:
            print("El número es demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("El número es demasiado alto. Intenta nuevamente.")
        else:
            print(f"Felicidades, ¡adivinaste el número en {intentos} intentos!")
            break

juego_adivinanza()
