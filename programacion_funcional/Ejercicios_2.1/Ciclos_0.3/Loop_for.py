###
#1 - Bucle (while)
# Permite ejecutar un bloque de codigo repentinamente mientrras se cunpla una condicion

from os import system
if system("clean") !=0: system("cls")

print("\n Bucle for:")

#Iterar una lista
frutas = ["manzana", "Pera", "Mandarina"]
for fruta in frutas:
    print(fruta)

#Iterar sobre cualquier cosa que sea iterable
cadena = "estudiante"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "Pera", "Mandarina"]
for idx, Value in enumerate(frutas):
    print(f"El indice es {idx} y la fruta es {Value}")

#bucle anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
      print(f"^{letra}{numero}")

#break
print("\n break:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
      print(f"El loro esta escondido en el indice {idx}")
      break

#continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro": continue

    print(animal)

#Conpresionsion de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

#Muestra los numeros Pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 ==0]
print(pares)
     
###
# EJERCICIOS
