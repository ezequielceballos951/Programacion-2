def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def main():
    numero = int(input("Ingresa un número entero para calcular su factorial: "))
    if numero < 0:
        print("El factorial de un número negativo no está definido.")
    else:
        resultado = calcular_factorial(numero)
        print("El factorial de", numero, "es:", resultado)

if __name__ == "__main__":
    main()
