import statistics #proporciona funciones para realizar calculos estadisticos como, media, mediana,varianza.
from tabulate import tabulate # libreria para formatear datos en tablas, facilita la visualizacion de los datos.

# Calcula la media aritmética de una lista de números.
def calcular_media(lista):
    return round(statistics.mean(lista), 4) # mean del modulo statistics para calcualr la media de la lista de numeros.
                                        # redonde el resultado a 4 decimales, esta funcion devuelve la media arimetrica    
# Calcula la moda y su frecuencia en una lista de números.
def calcular_moda(lista):
    frecuencias = {} #se crea diccionario fecuencias la misma  de cada numero de la lista
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1 # incrementa el conteo para cada numero de la lista
    
    moda_frecuencia_maxima = max(frecuencias.values())#frecuncia maxima entre los valores del diccionario
    moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]#lista de numeros de fecuencia maxima

    if len(set(frecuencias.values())) == 1: # verifica si todas las freciencias son iguales
        return None, None # si todas las feciencias son iguales devuleve  " none none "
    else:
        return moda, moda_frecuencia_maxima # de lo contario delvuelve la lista de moda y su  frecuncia maxima 

# Calcula la mediana de una lista de números.
def calcular_mediana(lista):
    lista_ordenada = sorted(lista) #ordena la lista de numeros en ascendente
    return round(statistics.median(lista_ordenada), 4) # calcula la mediana y redonde a 4 decimales 

# Calcula la desviación estándar de una lista de números.
def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista) # calcula la desviacion de la lista de numeros 
    return round(desviacion_estandar, 4) # redondea a 4 decimales 

# Calcula la varianza de una lista de números.
def calcular_varianza(lista):
    varianza = statistics.variance(lista) # calcular la varianza de la lista de numeros
    return round(varianza, 4) # redonde a 4 decimales 

# Calcula la frecuencia absoluta de cada elemento en una lista de números.
def frecuencia_absoluta(lista):
    frecuencias = {} # se crea diccionario para contar cuantas veces aparece cada numero de la lista
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1 # incrementa el conteo para cada numero de la lista
    return frecuencias
    #devuelve el diccionario de frecuencias absolutas

# Calcula la frecuencia relativa de cada elemento en una lista de números.
def frecuencia_relativa(lista):
    total = len(lista) # calcula el numero total de elemtos de la lista
    frec_abs = frecuencia_absoluta(lista) # calcula las frecuencias absolutas usando la funcion "ferecuencia absoluta"
    frec_relativa = {clave: round(valor / total, 4) for clave, valor in frec_abs.items()}
    return frec_relativa #! calcula la freciencia relativa, didvidindo cada fecuencia absoluta por el total y
                        #! redondeado a 4 decimales, devuelve el diccionario de frecuencias relativas
# Calcula la frecuencia porcentual de cada elemento en una lista de números.
def frecuencia_porcentual(lista):
    frec_rel = frecuencia_relativa(lista) # calcula las frecuencias relativas usando la funcion "fecuencia_relativa"
    frec_porcentual = {clave: round(valor * 100, 4) for clave, valor in frec_rel.items()}
    return frec_porcentual #! calcula las fecuencias relativa por 100 y redondeado a 4 decimales 
#esta funcion devuelve el diccionario de frecuencias porcentuales
# Calcula la frecuencia absoluta acumulada de una lista de números.
def frecuencia_absoluta_acumulada(lista):
    frec_abs = frecuencia_absoluta(lista)
    acumulado = 0
    frec_abs_acum = {}
    for clave, valor in sorted(frec_abs.items()):
        acumulado += valor
        frec_abs_acum[clave] = acumulado
    return frec_abs_acum

# Calcula la frecuencia relativa acumulada de una lista de números.
def frecuencia_relativa_acumulada(lista):
    total = len(lista)
    frec_rel = frecuencia_relativa(lista)
    acumulado = 0
    frec_rel_acum = {}
    for clave, valor in sorted(frec_rel.items()):
        acumulado += valor
        frec_rel_acum[clave] = round(acumulado, 4)
    return frec_rel_acum

# Calcula la frecuencia porcentual acumulada de una lista de números.
def frecuencia_porcentual_acumulada(lista):
    frec_porcent = frecuencia_porcentual(lista)
    acumulado = 0
    frec_porcent_acum = {}
    for clave, valor in sorted(frec_porcent.items()):
        acumulado += valor
        frec_porcent_acum[clave] = f"{round(acumulado, 4)}%"
    return frec_porcent_acum

# Muestra un menú de opciones para el usuario.
def menu():
    opcion = None
    try:
        print("\n")
        print("0. Para cerrar el menú.")
        print("1. Visualizar la MEDIA.")
        print("2. Visualizar la MODA.")
        print("3. Visualizar la MEDIANA.")
        print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
        print("5. Visualizar la VARIANZA.")
        print("6. Visualizar FRECUENCIA ABSOLUTA.")
        print("7. Visualizar FRECUENCIA RELATIVA.")
        print("8. Visualizar FRECUENCIA PORCENTUAL.")
        print("9. Visualizar FRECUENCIA ABSOLUTA ACUMULADA.")
        print("10. Visualizar FRECUENCIA RELATIVA ACUMULADA.")
        print("11. Visualizar FRECUENCIA PORCENTUAL ACUMULADA.\n")
        opcion = int(input("Ingrese el número de la opción que desea visualizar: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
    return opcion

# Solicita al usuario ingresar una lista de datos.
def ingresar_datos():
    cantidad = 0
    numeros = []
    print('Ingrese los datos uno por uno (ENTER), luego para ir al menú ingrese "n" \n')
    while True:
        numero = input(f"Ingrese el dato número {cantidad + 1}: ")
        if numero.lower() == "n":
            break
        else:
            try:
                numero = float(numero)
                cantidad += 1
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'n' para terminar.")
    return numeros

# Función principal que ejecuta el programa.
def main():
    numeros = ingresar_datos()
    opcion = menu()

    while opcion != 0:
        if opcion == 1:
            print(tabulate([["MEDIA", calcular_media(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 2:
            moda, frecuencia = calcular_moda(numeros)
            if moda is None:
                print("No hay moda en los datos.")
            else:
                print(tabulate([["MODA", f"{moda} (Frecuencia: {frecuencia})"]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 3:
            print(tabulate([["MEDIANA", calcular_mediana(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 4:
            print(tabulate([["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 5:
            print(tabulate([["VARIANZA", calcular_varianza(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 6:
            print(tabulate([["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 7:
            print(tabulate([["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 8:
            print(tabulate([["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)]], headers=["Operación", "Resultado en porcentajes (%)"], tablefmt="grid"))
        elif opcion == 9:
            print(tabulate([["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 10:
            print(tabulate([["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        elif opcion == 11:
            print(tabulate([["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
        else:
            print("Opción no válida.")
        
        opcion = menu()

if __name__ == "__main__":
    main()