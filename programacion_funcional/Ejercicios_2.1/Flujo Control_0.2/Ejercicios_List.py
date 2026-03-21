###
# EJERCICIOS

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("Ejercicio 1 El mensaje Secreto")

mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = mensaje[7:]

print(secreto)

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("Ejercicio 2 Intercanbio de posiciones")

numeros = [10, 20, 30, 40, 50]

numeros[0], numeros[-1] = numeros[-1], numeros[0]

print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes
# y el pan de abajo, en ese orden.

print("Ejercicio 3 El sándwich de listas")

pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo

print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("Ejercicio 4  Duplicado la lista")

lista = [10, 20, 30, 40, 50]

centro = lista[len(lista)//2]

print("El centro es:", centro)

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se
# encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("Ejercicio 5 Extrayendo el centro")

lista = [10, 20, 30, 40, 50]

centro = lista[len(lista)//2]

print("El centro es:", centro)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

print("Ejercicio 6 Reversa parcial")

lista = [1, 2, 3, 4, 5, 6]

mitad = len(lista) // 2

resultado = lista[:mitad][::-1] + lista[mitad:]

print(resultado)