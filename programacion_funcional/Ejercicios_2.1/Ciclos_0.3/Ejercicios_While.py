###
# EJERCICIOS (while)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

num = 10

while num >= 1:
    print(num)
    num -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

num = 1
suma = 0

while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1

print("Suma:", suma)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

n = int(input("Introduce un número: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print("Factorial:", factorial)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

password = ""

while len(password) < 8:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")

print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

num = int(input("Introduce un número: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

n = int(input("Introduce un número: "))
num = 2

while num <= n:
    es_primo = True
    i = 2

    while i < num:
        if num % i == 0:
            es_primo = False
            break
        i += 1

    if es_primo:
        print(num)

    num += 1
    