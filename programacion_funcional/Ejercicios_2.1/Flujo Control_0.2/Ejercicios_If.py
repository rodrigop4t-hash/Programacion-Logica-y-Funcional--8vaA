###
# EJERCICIOS
###
from os import system
if system("clear") != 0: system("cls")

#Ejercicio 1: Determinar el mayor de dos números
#Pide al usuario que introduzca dos números y muestra un mensaje
#indicando cuál es mayor o si son iguales

print("Ejercicio 1")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El mayor es:", num1)
elif num2 > num1:
    print("El mayor es:", num2)
else:
    print("Ambos números son iguales")

#Ejercicio 2: Calculadora simple
#Pide al usuario dos números y una operación (+, -, *, /)
#Realiza la operación y muestra el resultado (maneja la división entre zero)

print("Ejercicio 2")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
operacion = (input("Ingresa una Operacion de tipo (+, -, *, /): "))

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")

#Ejercicio 3: Año bisiesto
#Pide al usuario que introduzca un año y determina si es bisiesto.
#Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 рего no por 400.

print("Ejercicio 3")

anio = int(input("Ingresa un Año: "))


if (anio / 4 == 0 and anio / 100  != 0) or (anio / 400 == 0):
    print("El año si es bisiesto")
else:
    print("El año no es bisiesto")


#Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# Bebé (0-2 años)
#Niño (3-12 años)
#Adolescente (13-17 años)
# Adulto (18-64 años)
# Adulto mayor (65 años o más)

print ("Ejercicio 4")

edad = int(input("Ingresa tu edad: "))

if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad >= 3 and edad <= 12:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
elif edad >= 65:
    print("Adulto mayor")
else:
    print("Edad no válida")
