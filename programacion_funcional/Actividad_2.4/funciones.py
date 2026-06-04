# EJEMPLO CALLBACK

def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a, b):
    return a + b

def resta(a, b):  # Función de primer orden
    return a - b

resultado = operar(5, 3, suma)  # La función suma actúa como callback al ejecutarse en operar
print(resultado)

'''
Un callback es una función que se pasa a otra función como argumento y se espera
que sea llamada dentro de esa función.

Las funciones de primer orden son aquellas que no toman otras funciones como
argumentos ni devuelven funciones.
'''

# EJEMPLO FUNCIÓN PRIMERA CLASE

def saludo():
    return "¡Hola!"

mi_variable = saludo()  # Ejecutamos la función y la asignamos a una variable
print(mi_variable)

def saludo2():
    return "¡Que tal!"

mi_variable2 = saludo2  # Asignamos la función sin paréntesis a una variable
print(mi_variable2())

'''
Una función de primera clase puede asignarse a variables,
pasarse como argumento y devolverse desde otras funciones.
'''

# EJEMPLO FUNCIÓN DE ORDEN SUPERIOR

def elegir_operacion(operacion):  # función de orden superior

    def multiplicar(x):
        return x * 2

    def dividir(x):
        return x / 2

    if operacion == "multiplicar":
        return multiplicar  # Retornamos la función sin ejecutarla
    else:
        return dividir

doble = elegir_operacion("multiplicar")
print(doble(10))

divide2 = elegir_operacion("dividir")
print(divide2(10))

'''
Una función de orden superior es aquella que puede recibir otras funciones
como argumentos o devolver una función como resultado.
'''

# EJEMPLO FUNCIÓN ANÓNIMA = LAMBDA

doble = lambda x: x * 2
print(doble(5))

cuadrado = lambda x: x ** 2
print(cuadrado(4))

def cuadrado(x):
    return x ** 2

print(cuadrado(4))

# función de orden superior que recibe una función como argumento
def aplicar_funcion(funcion, valor):
    return funcion(valor)

resultado = aplicar_funcion(lambda x: x ** 3, 3)
print(resultado)  # Imprime 27

numeros = [1, 2, 3, 4]

dobles = list(map(lambda x: x * 2, numeros))

alumnos = ['Alejandro', 'Miguel', 'Vinicio', 'Rodney', 'Marcial']

saludar_alumnos = list(
    map(lambda nombre: 'Hola ' + nombre, alumnos)
)

print(saludar_alumnos)

# sin lambda

def saludar(nombre):
    return 'Hola ' + nombre

lista_saludos = list(map(saludar, alumnos))
# print(lista_saludos)

'''
Una función anónima, también conocida como función lambda,
es una función sin nombre que se define utilizando la palabra clave lambda.

Pueden pasarse como argumentos sin necesidad de definirlas antes.

Se utilizan cuando la función es simple y solo se necesita en un lugar.
'''