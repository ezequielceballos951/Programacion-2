import math
from scipy.stats import kurtosis
import scipy.stats as stats

# MEDIDAS DE POSICIÓN

def MEDIA(lista):
    media = sum(lista)/len(lista)
    return media 

def CALCULAR_MODA(lista):
    Max_Contador = 0
    Modas = []
    
    for Numero in lista:
        Cont = 0
        for Elem in lista:
            if Elem == Numero:
                Cont += 1
        if Cont > Max_Contador:
            Max_Contador = Cont
            Modas = [Numero]
        elif Cont == Max_Contador and Numero not in Modas:
            Modas.append(Numero)

    if len(Modas) == len(set(lista)): # set elimina automáticamente los elementos duplicados y conserva solo uno de cada elemento
        return "No hay moda"
    else:
        return Modas

def CALCULAR_MEDIANA(lista):
    listaOrdenada=sorted(lista) # Ordena la lista de mayor a menor para luego poder obtener el valor del medio
    longitudLista=len(listaOrdenada) # Almacena la longitud de la lista (ya ordenada)
    
    if longitudLista % 2 == 0: # Verifica si la longitud de la lista ordenada es par
        medioIzq = listaOrdenada[longitudLista // 2 - 1 ] # Define el indice del medio izquierdo de la lista dividiendo por dos (division entera) y restando 1 para posicionarse a la izquierda
        medioDer = listaOrdenada[longitudLista // 2 ] # Define el indice del medio derecho de la lista 
        mediana = (medioIzq + medioDer) / 2 # Suma las variables del medio y las divide por dos respetando la formula para calcular la mediana en listas con una longitud par
        return mediana
    else:
        mediana = listaOrdenada [longitudLista // 2] # En caso de ser impar se obtiene el indice central 
        return mediana

# Calcular promedio (sumatoria de todos los datos / cantidad de datos)
def CALCULAR_PROMEDIO(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def CALCULAR_CUARTILES(lista):
    Longitud_Lista = len(lista)
    mediana = CALCULAR_MEDIANA(lista)   # se define la mediana para ser utilizada como q2

    if Longitud_Lista % 2 == 0:
        mitad_inferior = lista[:Longitud_Lista//2] # obtiene la mitad inferior de la lista utilizando el slicing (comienza al principio de la lista y finaliza en la mitad Longitud_lista//2)
        mitad_superior = lista[Longitud_Lista//2:] # obtiene la mitad superior de la lista utilizando el slicing (comienza en la mitad Longitud_lista//2 finaliza en el ultimo indice de la lista)
    else:
        mitad_inferior = lista[:Longitud_Lista//2] # obtiene la mitad inferior de la lista utilizando el slicing (comienza al principio de la lista y finaliza en la mitad Longitud_lista//2)
        mitad_superior = lista[Longitud_Lista//2 + 1:] # obtiene la mitad superior de la lista utilizando el slicing (comienza en la mitad Longitud_lista//2 finaliza en el ultimo indice de la lista)

    q1 = CALCULAR_MEDIANA(mitad_inferior) # se calcula la mediana de la mitad inferior
    q2 = mediana # se define a q2 como la mediana
    q3 = CALCULAR_MEDIANA(mitad_superior) # se calcula la mediana de la mitad superior
    
    return q1 ,q2, q3

# Calcular desviación estándar: raíz cuadrada ((suma((elemento - media)**2))/cantidad de datos - 1)
def DESVIACION_ESTANDAR(lista):
    n = len(lista)
    if n <= 1:
        return 0
    promedio = MEDIA(lista)
    # Calcula la suma de los cuadrados de las diferencias entre cada elemento y el promedio
    suma_resta_cuadrado = sum((x - promedio) ** 2 for x in lista)
    # Calcula la desviación estandar dividiendo la suma de las diferencias cuadradas entre n-1
    # y tomando la raíz cuadrada del resultado
    desviacion = (suma_resta_cuadrado / (n - 1)) ** 0.5
    return round(desviacion, 4)

def RANGO(lista):
    # En la función rango, se resta el menor valor de las muestras al mayor valor de la muestra
    valor_rango = lista[-1] - lista[0]
    return valor_rango

# FRECUENCIAS

def CALCULAR_FRECUENCIA_ABSOLUTA(lista):
    # Creamos un diccionario para almacenar las frecuencias.
    # Las claves serán los números de muestra y los valores serán la cantidad de veces que se repiten los números.
    frecuencias = {} 
    for elemento in lista: # Iteramos sobre cada elemento en la lista
        if elemento in frecuencias: # Verificamos si el elemento ya está en el diccionario
            frecuencias[elemento] += 1  # Si el elemento ya está en el diccionario, incrementamos su contador de frecuencia en 1.
        else:
            frecuencias[elemento] = 1  # Si el elemento no está en el diccionario, lo agregamos al diccionario con una frecuencia de 1.
    return frecuencias

def CALCULAR_FRECUENCIA_ABSOLUTA_ACUMULADA(lista):
    Frecuencias_Absolutas = CALCULAR_FRECUENCIA_ABSOLUTA(lista) # Se obtienen las frecuencias absolutas con la función ya creada
    Frecuencia_Absoluta_Acumulada = {} # Diccionario para almacenar la frecuencia absoluta acumulada de cada elemento
    Acumulador = 0 # Variable acumuladora para almacenar la frecuencia acumulada actual
    for elemento, frecuencia in Frecuencias_Absolutas.items(): # Recorrer las frecuencias absolutas y calcular la frecuencia absoluta acumulada
        Acumulador += frecuencia # Incrementar el acumulador con la frecuencia actual
        Frecuencia_Absoluta_Acumulada[elemento] = Acumulador # Asignar la frecuencia absoluta acumulada al elemento
    return Frecuencia_Absoluta_Acumulada

def SOLO_UN_ELEMENTO(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# En esta función se ingresa una lista, y se devuelve otra lista con las frecuencias relativas de cada elemento de la lista (elementos no repetidos)
# Frecuencia absoluta / cantidad de datos
def CALCULAR_FRECUENCIA_RELATIVA(lista):
    # 1. lista para utilizar al final. 2. Una lista con los elementos sin repetir. 3. El diccionario con las frecuencias absolutas de la lista
    frecuencia_relativa = []
    frecuencia_absoluta = CALCULAR_FRECUENCIA_ABSOLUTA(lista)
    lista_simple = SOLO_UN_ELEMENTO(lista)
    # Se evaluan los elementos que estan en la lista, y utilizando el elemento como key, se busca el valor absoluto del elemento
    # Al tener la frecuencia absoluta, se la divide por la cantidad de elementos en la lista original. Se agrega SOLO el valor relativo a la lista
    # en la posición del elemento 
    for elemento in lista_simple:
        absoluta = frecuencia_absoluta[(elemento)]
        frecuencia = absoluta / len(lista)
        frecuencia_relativa.append(round(frecuencia, 4)) # ver si hay que redondearlo o no
    # Devuelve una LISTA
    return frecuencia_relativa

# La frecuencia relativa de x, sumado a las frecuencias relativas de todos los datos anteriores
def CALCULAR_FRECUENCIA_RELATIVA_ACUMULADA(lista):
    # Se crea una lista nueva, vacía, que es donde se van a guardar los datos de la acumulada
    frecuencia_relativa_acumulada = []
    # Se crea una variable tipo lista que almacena las frecuencias relativas de los elementos de la lista
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    total = 0

    # Se pasa por cada elemento de la lista, y se lo suma al total, el cual va acumulando todos los valores
    for i in range (len(frecuencia_relativa)):
        total += frecuencia_relativa[i]
        frecuencia_relativa_acumulada.append(round(total, 2))
    # La función devuelve una LISTA con todos los valores de la acumulada, en la posición de los elementos de la lista, ya ordenados de mayor a menor.
    return frecuencia_relativa_acumulada

# En esta función se calcula la frecuencia porcentual de cada elemento en la lista
def CALCULAR_FRECUENCIA_PORCENTUAL(lista):
    # Se llama a la función CALCULAR_FRECUENCIA_RELATIVA para obtener la frecuencia relativa
    frecuencia_relativa = CALCULAR_FRECUENCIA_RELATIVA(lista)
    # La expresión "elemento * 100" multiplica cada valor de la lista por 100 para calcular su porcentaje
    frecuencia_porcentual = [round(elemento * 100, 2) for elemento in frecuencia_relativa]
    return frecuencia_porcentual

def CALCULAR_FRECUENCIA_PORCENTUAL_ACUMULADA(lista):
    # Obtiene la frecuencia porcentual utilizando la función CALCULAR_FRECUENCIA_PORCENTUAL
    frecuencia_porcentual = CALCULAR_FRECUENCIA_PORCENTUAL(lista)
    frecuencia_porcentual_acumulada = []
    total = 0
    # Recorre los elementos de la frecuencia porcentual, sumándolos y añadiéndolos a la lista de la frecuencia porcentual acumulada
    for i in range(len(frecuencia_porcentual)):
        total += frecuencia_porcentual[i]
        frecuencia_porcentual_acumulada.append(round(total, 2))
    return frecuencia_porcentual_acumulada

# Para calcular la curtosis, se utiliza la función kurtosis de scipy.stats
def CALCULAR_CURTOSIS(lista):
    return kurtosis(lista, fisher=True)

# DISTRIBUCIONES

# Función para calcular la probabilidad usando la distribución binomial
def DISTRIBUCION_BINOMIAL(n, p, k):
    coef_binomial = math.comb(n, k)
    probabilidad = coef_binomial * (p ** k) * ((1 - p) ** (n - k))
    return probabilidad

# Función para calcular la probabilidad usando la distribución de Poisson
def DISTRIBUCION_POISSON(lmbda, k):
    return (lmbda ** k) * (math.exp(-lmbda)) / math.factorial(k)
