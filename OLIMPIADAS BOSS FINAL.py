import math
from collections import defaultdict

# FUNCIONES BÁSICAS

def agregar_elementos_input():
    lista = []
    numero_muestra = 0
    print("Ingrese los datos uno por uno, y presione enter para continuar. Ingrese 'FIN' para finalizar.")
    while True:
        valor = input(f"Ingrese dato número {numero_muestra + 1}: ")
        if valor.replace('.', '', 1).isdigit():
            lista.append(float(valor))
            numero_muestra += 1
        elif valor.upper() == "FIN":
            print("Fin de la muestra")
            break
        else:
            print("Comando no válido, intente de nuevo.")
    
    lista = sorted(lista)
    return lista

def media(lista):
    return round(sum(lista) / len(lista), 4)

def mediana(lista):
    n = len(lista)
    lista_ordenada = sorted(lista)
    if n % 2 == 0:
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return round(mediana, 4)

def moda(lista):
    frecuencias = defaultdict(int)
    for valor in lista:
        frecuencias[valor] += 1
    max_frecuencia = max(frecuencias.values())
    modas = [valor for valor, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
    return modas

def rango(lista):
    return round(max(lista) - min(lista), 4)

def varianza(lista):
    media_valor = media(lista)
    return round(sum((x - media_valor) ** 2 for x in lista) / len(lista), 4)

def desviacion_estandar(lista):
    return round(math.sqrt(varianza(lista)), 4)

def curtosis(lista):
    media_valor = media(lista)
    n = len(lista)
    s = desviacion_estandar(lista)
    suma = sum((x - media_valor) ** 4 for x in lista)
    g = ((1/n) * suma) / (s ** 4) - 3
    return round(g, 4)

def interpretar_curtosis(g):
    if g < 0:
        return "Platicúrtica"
    elif g == 0:
        return "Mesocúrtica"
    else:
        return "Leptocúrtica"

def frecuencias(lista):
    frecuencias = defaultdict(int)
    for valor in lista:
        frecuencias[valor] += 1
    for valor, frecuencia in frecuencias.items():
        print(f"Valor: {valor}, Frecuencia: {frecuencia}")

# FUNCIONES DE PROBABILIDAD

def distribucion_binomial(n, p, k):
    coef_binomial = math.comb(n, k)
    probabilidad = coef_binomial * (p ** k) * ((1 - p) ** (n - k))
    return round(probabilidad, 4)

def distribucion_poisson(lmbda, k):
    probabilidad = (math.exp(-lmbda) * (lmbda ** k)) / math.factorial(k)
    return round(probabilidad, 4)

# MENÚ PRINCIPAL

def menu_estadistica_descriptiva(lista):
    while True:
        opcion = int(input("1 = MEDIDAS DE POSICIÓN\n2 = MEDIDAS DE DISPERSIÓN\n3 = FRECUENCIAS\n4 = COEFICIENTE DE CURTOSIS\n5 = VOLVER\n ==> "))
        if opcion == 1:
            print(f"Media: {media(lista)}")
            print(f"Mediana: {mediana(lista)}")
            modas = moda(lista)
            print(f"Moda: {', '.join(map(str, modas))}")
        elif opcion == 2:
            print(f"Rango: {rango(lista)}")
            print(f"Varianza: {varianza(lista)}")
            print(f"Desviación Estándar: {desviacion_estandar(lista)}")
        elif opcion == 3:
            frecuencias(lista)
        elif opcion == 4:
            g = curtosis(lista)
            interpretacion = interpretar_curtosis(g)
            print(f"Coeficiente de Curtosis: {g} ({interpretacion})")
        elif opcion == 5:
            break
        else:
            print("Comando incorrecto, intente de nuevo.")

def menu_probabilidad_y_estadistica():
    while True:
        opcion = int(input("1 = DISTRIBUCIÓN BINOMIAL\n2 = DISTRIBUCIÓN DE POISSON\n3 = VOLVER\n ==> "))
        if opcion == 1:
            n = int(input("Ingrese el número de ensayos (n): "))
            p = float(input("Ingrese la probabilidad de éxito (p): "))
            k = int(input("Ingrese el número de éxitos deseados (k): "))
            resultado = distribucion_binomial(n, p, k)
            print(f"La probabilidad binomial de obtener {k} éxitos en {n} ensayos es: {resultado}")
        elif opcion == 2:
            lmbda = float(input("Ingrese el valor esperado de la distribución de Poisson (λ): "))
            k = int(input("Ingrese el número de éxitos deseados (k): "))
            resultado = distribucion_poisson(lmbda, k)
            print(f"La probabilidad de Poisson de obtener {k} éxitos es: {resultado}")
        elif opcion == 3:
            break
        else:
            print("Comando incorrecto, intente de nuevo.")

def menu_principal():
    lista = []
    print("Bienvenido al módulo de Estadística Descriptiva y Probabilidad.")
    while True:
        opcion = int(input("1 = INGRESAR DATOS\n2 = ESTADÍSTICA DESCRIPTIVA\n3 = PROBABILIDAD Y ESTADÍSTICA\n4 = SALIR\n ==> "))
        if opcion == 1:
            lista = agregar_elementos_input()
        elif opcion == 2:
            if lista:
                menu_estadistica_descriptiva(lista)
            else:
                print("No hay datos disponibles. Ingrese los datos primero.")
        elif opcion == 3:
            menu_probabilidad_y_estadistica()
        elif opcion == 4:
            print("Fin!")
            break
        else:
            print("Comando incorrecto, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
