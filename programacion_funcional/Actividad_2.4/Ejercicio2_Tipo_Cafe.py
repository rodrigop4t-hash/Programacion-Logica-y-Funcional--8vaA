# Ejercicio 2: Ordenar tipo de café
# Objetivo: Ordenar distintos tipos de café

'''

Los grupos de VIII de ISC tienen cambios de humor y ahora cada grupo quiere un tipo de café:

-- café americano y
-- café de olla.

****Dato curioso: Los cambios de humor de mis alumnos son bastante frecuentes.

Con esta información, tendremos que revisar la función ordenar café del ejercicio anterior para
agregar la variedad de café.

Debemos modificar ordenar_cafe para que acepte una función como parámetro y así poder cambiar el tipo
de café que se va a preparar.

Esto hace que obtener_cafe sea más flexible y ofrece al programador mayor control cuando cambian las
solicitudes del cliente.

1.- Crea una función preparar_cafe que no recibe parámetros y devuelve una cadena que representa una
taza de café americano.

2.- Crea otra esta función devuelve una cadena que representa una taza de café de olla.

3.- Crea otra función ordenar_cafe que acepta dos parámetros:
    - una función que prepara café y
    - número de tazas.

4.- Dentro de la función ordenar:
    - Crea una lista que guarde las tazas de café.
    - Dentro de la función ordenar, aplica la iteración a través de una lista por comprensión para
      llamar a la función preparar según el número de tazas proporcionado.
    - Finalmente la función ordenar devuelve la lista tazas_cafe.

5.- Crear una variable cafe para el grupo A que recibe el número de tazas que prefieren el sabor
americano.

6.- Crear una variable cafe para el grupo B que recibe el número de tazas que prefieren el sabor de
olla.

7.- Imprimir en una sola línea ambas órdenes.
'''

def prepara_cafe ():
    return "café_americano"

def prepara_cafe ():
    return "café_olla"

def ordenar_cafe (preparar_cafe, numero_tazas):
    tazas_cafe = (prepara_cafe() for _ in range(numero_tazas))
    return tazas_cafe


#solo modificar el codigo a partir de aqui
cafe_grupo_a = ordenar_cafe(preparar_cafe_americano, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_olla, 12)
#solo modificar el codigo hasta aqui

print(cafe_grupo_a, cafe_grupo_b)