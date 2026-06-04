# Objetivo: Mostrar el uso de comprensión de listas en Python

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doble = []  # lista vacía

for n in numeros:
    doble.append(n * 2)

print(doble)

# Genera otra lista de los cuadrados de los números en la lista numeros
cuadrados = [num ** 2 for num in numeros]

lista_cuadruple = list(map(lambda x: x * 4, numeros))
print(lista_cuadruple)

# Genera otra lista con el cubo de cada uno de los números de la lista
cubo = [elemento ** 3 for elemento in numeros]

cadena = ["hola " + "que hace" for _ in range(3)]

# Genera una lista de cadenas para cada elemento del rango de 5
saludos = ["hola" for _ in range(5)]
saludos2 = ["que hace" for _ in range(3)]




# Elabora una serie de ejercicios usando comprensión de listas

# Ejercicio 1: Generar una lista de los números pares del 1 al 20
pares = [n for n in range(1, 21) if n % 2 == 0]

# Ejercicio 2: Generar una lista de las primeras 10 potencias de 2
potencias_dos = [2 ** n for n in range(10)]

# Ejercicio 3: Generar una lista de las palabras en una frase dada
frase = "La programación funcional es divertida"
palabras = [palabra for palabra in frase.split()]