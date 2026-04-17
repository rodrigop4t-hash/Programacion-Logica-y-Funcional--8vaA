###
# EJERCICIOS (for)
###
from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.

for num in range(2, 21, 2):
    print(num)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.

numeros = [10, 20, 30, 40, 50]

suma = 0
for num in numeros:
    suma += num

media = suma / len(numeros)
print("Media:", media)

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.

numeros = [15, 5, 25, 10, 20]

maximo = numeros[0]

for num in numeros:
    if num > maximo:
        maximo = num

print("Máximo:", maximo)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

# Con for
resultado = []
for palabra in palabras:
    if len(palabra) > 5:
        resultado.append(palabra)

print(resultado)

# Con list comprehension
resultado2 = [p for p in palabras if len(p) > 5]
print(resultado2)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]

letra = input("Introduce una letra: ").lower()

contador = 0
for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1

print("Cantidad:", contador)