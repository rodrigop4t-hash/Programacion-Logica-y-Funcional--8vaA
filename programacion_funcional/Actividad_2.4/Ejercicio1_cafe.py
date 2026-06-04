#Ejercicio 1: Ordenar cafe para el grupo ISC
#

'''
1.- Crear una función que no tome ningún argumento y devuelva la cadena de texto "café".
para simular la preparación de una taza de café ☕.

2.- Crear función para tomar la orden del café que toma un argumento numero_tazas, que indica cuántas
tazas de café se desean.

    Dentro de la función:
    --Almacena los resultados en una lista llamada tazas_cafe.
    --Utiliza una lista por comprensión para llamar a la función preparar_cafe según el numero_tazas
      proporcionado. Ir archivo compresionListas.py
    --Finalmente devuelve la lista tazas_cafe.

3.- Llama a la 2da función con el numero de tazas que requiere y almacenar en una variable
cafe_para_grupo.

4.- Imprimir el contenido de la variable cafe_para_grupo, es decir, la lista de la cadena "café".

'''

# Ejercicio 1: Ordenar café para el grupo ISC

def preparar_cafe():
    return "café"

def tomar_orden(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(numero_tazas)]
    return tazas_cafe

cafe_para_grupo = tomar_orden(5)

print(cafe_para_grupo)
