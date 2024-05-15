def calcular_factorial(numero):
    if numero == 0:
        return 1
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def main():
    try:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        if numero < 0:
            print("El factorial solo está definido para números enteros positivos.")
        else:
            factorial = calcular_factorial(numero)
            print(f"El factorial de {numero} es: {factorial}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
