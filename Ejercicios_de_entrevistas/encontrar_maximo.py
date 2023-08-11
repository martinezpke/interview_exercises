""" 
    Pregunta 1: Resolución de Problemas y Algoritmos. 
    
    Escribe un programa en el lenguaje de tu elección 
    que resuelva el problema de encontrar el número 
    más grande en una lista de números enteros.

"""

def encontrar_maximo(lista):
    maximo = 0
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

numeros = [5, 10, 38, 8, 15]
resultado = encontrar_maximo(numeros)
print("El número más grande es:", resultado)