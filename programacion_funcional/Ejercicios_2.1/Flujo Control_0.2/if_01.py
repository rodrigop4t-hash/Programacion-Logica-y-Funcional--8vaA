##
# 01 - Sentencia condicional (if,elif, else)
#Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\n Sentencia simple condicional")
# Podemos usar la palabra clave "if" para ejecutar un bloque de código
# solo si se cumple una condición.
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Si no se cumple la condición, no se ejecuta el bloque de código
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

# Podemos usar el comando "else" para ejecutar un bloque de código
# si no se cumple la condición anterior del if
print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencia condicional con elif")
# Además de usar "if" y "else", podemos usar "elif" para determinar
# múltiples condiciones, ten en cuenta que sólo se ejecutará el primer bloque
# de código que cumpla la condición (o la del else, si está presente)
nota = 5
if nota >= 9:
    print("¡Sobresaliente!")
elif nota >= 7:
    print("Notable!")
elif nota >= 5:
    print("¡Aprobado!")
else:
    print("¡No está calificado!")

print("\n Condiciones múltiples")
edad = 16
tiene_carnet = True

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript:
# && sería and
# || sería or

# En el caso que seas mayor de edad y tengas carnet...
# entonces podrás conducir
if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("POLICIA 🚓!!!!!!")

# En un pueblo de Isla Holbox son más relajados y
# te dejan conducir si eres mayor de edad o tienes carnet
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox 🚗")
else:
    print("Paga al policía y te dejará conducir!!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
# JavaScript -> !
if not es_fin_de_semana:
    print("¡¡SC, anda que hay que ir al Tec!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

# Más fácil sería:
# if edad < 18:
#     print("No puedes entrar a la disco")
# elif tiene_dinero:
#     print("Puedes ir a la discoteca")
# else:
#     print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
    print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
    print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
    print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
    print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condición] else [código si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)