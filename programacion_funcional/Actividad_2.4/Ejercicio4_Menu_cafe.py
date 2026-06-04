# Ejercicio 4: Mostrar el menú de la cafetería
# Objetivo: Usar comprensión de listas para formatear y mostrar el menú de una cafetería con los precios de cada bebida.

'''
1.- Crea una función llamada ver_menu que recibe un diccionario llamado menu.
2.- Dentro de la función, usa comprensión de listas para recorrer menu.items().
    Cada elemento del diccionario tiene dos partes: la clave (nombre de la bebida) y el valor (precio).
    Estructura: para nombre, precio en menu.items()
3.- Para cada par clave-valor, genera una cadena con el formato: "Americano: $25.50"
Es decir: f"{nombre.capitalize()}: ${precio:.2f}"
4.- La función debe devolver la lista generada por la comprensión.
5.- Crea el menú variable con el diccionario de precios mostrado arriba.
6.- Llama a ver_menu con el diccionario menu y guarda el resultado en una variable llamada menu_formateado.
7.- Imprima cada elemento de menu_formateado en una línea separada usando un ciclo for.
Salida esperada (los precios pueden variar según el diccionario):
    Americano: $25.50
    Café de olla: $22.00
    Capuchino: $35.75
    Coca: $40.00
    Agua: $18.50
'''

# Ejercicio 4: Mostrar el menú de la cafetería

def ver_menu(menu):
    return [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]

# Diccionario del menú
menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50
}

# Llamar a la función
menu_formateado = ver_menu(menu)

# Imprimir cada elemento en una línea separada
for bebida in menu_formateado:
    print(bebida)