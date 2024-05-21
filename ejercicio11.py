def adivinar_numero():
    print("Piensa en un número entre 1 y 100 y yo intentaré adivinarlo.")
    
    bajo = 1
    alto = 100
    intentos = 0
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        intentos += 1
        
        respuesta = input(f"¿Es {medio} tu número? (responde 'mayor', 'menor' o 'igual'): ").lower()
        
        if respuesta == "igual":
            print(f"¡He adivinado tu número en {intentos} intentos! Es {medio}.")
            break
        elif respuesta == "mayor":
            bajo = medio + 1
        elif respuesta == "menor":
            alto = medio - 1
        else:
            print("Respuesta no válida. Por favor, responde 'mayor', 'menor' o 'igual'.")

adivinar_numero()
