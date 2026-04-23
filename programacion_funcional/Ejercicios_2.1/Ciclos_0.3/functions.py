###
# 04 - Funciones
# Bloques de codigo reutilizables para hacer tareas especificas 
###

from os import system
if system("clean") !=0: system("cls")

#"""" Definicion de una funcion

# def nombre _de_la_funcion(parametro1, parametro2, ...)
#  #docstring
# cuerpo de la funcion
# return valor_valor_de_retorno # opcional

#""""

# #Ejemplo de una funcion para imprimir algo en consola
# def saludar():
# print(f"¡Hola!")

# #Ejemplo de una funcion con parametro
# def saludar_a(nombre):
# print(f""¡Hola {nombre}!")

# saludar_al(Estudiante")
# saludar_al("jefa")
# saludar_al("profesor")
# saludar_al("directora")
# saludar_al("prefecto")

## Funciones con mas parametros
#def sumar(a, b):
# suma = a + b
# return suma

# ## Funciones con más parámetros
# def sumar(a, b):
#     suma = a + b
#     return suma

# result = sumar(2, 3)
# print(result)


# ## Documentar las funciones con docstring
# def restar(a, b):
#     """Resta dos números y devuelve el resultado"""
#     return a - b


# parámetros por defecto
# def multiplicar(a, b = 2):
#     return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))


# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")


# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("carlos", 25, "pajaro")
describir_persona("persona", "ingeniero", 39)


# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="perro", nombre="Reyes", edad=25)
describir_persona(sexo="mujer", nombre="Alejandra", edad=21)


# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_informacion_de(nombre="Carlos", edad=25, sexo="ave")
print("\n")
mostrar_informacion_de(name="Sofia", edad=21, coutry="Mexico")
print("\n")
mostrar_informacion_de(nick="Socio", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="La que barre", es_nodo=True, gato=40)

####