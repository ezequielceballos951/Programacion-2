#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva un diccionario donde las claves son las 
#letras iniciales de las palabras y los valores son listas de palabras que comienzan con esa letra.

def letras_inicial(lista):
    nuevo_dicc = {}
    frecuencia = 1
    palabra = ''.join(lista).split()
    for palabra in lista:
        inicial = palabra[0].lower()
        if inicial not in nuevo_dicc:
            nuevo_dicc[inicial] = [frecuencia]
        else:
            frecuencia += 1
            nuevo_dicc[inicial] = [frecuencia]
    return nuevo_dicc

lista_palabras = ["Milanesa", "Fideos", "Crema", "Mondongo", "Mango"]
resultado = letras_inicial(lista_palabras)
print(f"{resultado}")