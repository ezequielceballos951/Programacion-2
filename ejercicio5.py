def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Bienvenido al programa de conversión de temperatura!")
    print("¿Qué tipo de conversión desea realizar?")
    print("1. Convertir de Celsius a Fahrenheit")
    print("2. Convertir de Fahrenheit a Celsius")
    
    choice = input("Ingrese el número correspondiente a su elección: ")

    if choice == '1':
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
    elif choice == '2':
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
    else:
        print("Selección no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
