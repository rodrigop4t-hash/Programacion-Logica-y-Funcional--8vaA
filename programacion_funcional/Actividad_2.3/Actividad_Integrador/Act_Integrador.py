# =============================================================================
#  ACTIVIDAD PRÁCTICA INTEGRADORA
#  Sistema de pedidos: Comedor Escolar
# =============================================================================
#  Programación Funcional en Python — Nivel Básico
#  Temas integrados:
#    ✅ Funciones simples y de primera clase  
#    ✅ Comprensión de listas                 
#    ✅ Funciones de orden superior           
#    ✅ Callbacks                             
#    ✅ Funciones lambda + map()              
#    ✅ Lógica condicional dentro de funcs.   
#    ✅ Entrada del usuario                   
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  Sección 1 — INVESTIGA
# ─────────────────────────────────────────────────────────────────────────────
# Antes de comenzar a codificar, investiga y responde en comentarios:
# 1. ¿Qué es una función de primera clase en Python?
#    R: Es una función que puede tratarse como cualquier otro objeto, es decir,
#       puede asignarse a una variable, pasarse como argumento a otra función
#       y devolverse como resultado.

# 2. ¿Cuál es la diferencia entre una función de orden superior y un callback?
#    R: Una función de orden superior es aquella que recibe otra función como
#       argumento o devuelve una función. Un callback es la función que se pasa
#       como argumento para ser ejecutada dentro de otra función.

# 3. ¿Cuándo conviene usar comprensión de listas en lugar de un ciclo for?
#    R: Cuando se quiere crear una lista de forma más corta, legible y eficiente
#       a partir de otra colección, especialmente si es una operación simple.

# 4. ¿Qué hace map() y cómo se relaciona con lambda?
#    R: map() aplica una función a cada elemento de un iterable y devuelve un
#       iterador con los resultados. Se relaciona con lambda porque muchas veces
#       se usa una función anónima (lambda) dentro de map() para operaciones rápidas.

# 5. ¿Qué ventaja ofrece pasar una función como argumento a otra función?
#    R: Permite reutilizar código, hacer el programa más flexible y dinámico,
#       y aplicar diferentes comportamientos sin modificar la función principal.

#______________________________________________________________________________

# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────
# Lee el siguiente escenario y diseña tu solución ANTES de codificar.
#
# ESCENARIO
# La cooperativa escolar ofrece tres productos en su menú:
#   🍕 Pizza  |  🥤 Agua fresca  |  🫔 Tamal
#
# El sistema debe:
#   A) Preparar cualquier producto usando una función dedicada por producto.
#   B) Tomar la orden de un grupo: recibir la FUNCIÓN del producto y la
#      CANTIDAD solicitada, y devolver una lista con todas las porciones.
#   C) Calcular el precio total aplicando el precio unitario a cada porción  
#      usando map() y una función lambda.
#   D) Aplicar una PROMOCIÓN: si el pedido es de 3 o más porciones,
#      agregar "🎁 postre gratis" a la orden.
#   E) Solicitar al usuario cuántas porciones desea de cada producto y
#      mostrar el resumen completo del pedido.
#
# ─────────────────────────────────────────────────────────────────────────────
# Sección 2 — PLANEA
# ─────────────────────────────────────────────────────────────────────────────

# ¿Qué funciones necesitas definir?
# R:
#   - preparar_pizza(): devuelve una pizza
#   - preparar_agua(): devuelve un agua fresca
#   - preparar_tamal(): devuelve un tamal
#   - tomar_orden(funcion_producto, cantidad): genera una lista con las porciones
#   - calcular_total(lista_precios): calcula el total usando map()
#   - aplicar_promocion(orden): agrega un postre si aplica

# ¿Cuál de ellas es de orden superior? ¿Por qué?
# R:
#   - tomar_orden es una función de orden superior porque recibe otra función
#     (la de preparar el producto) como argumento.

# ¿Dónde usarás comprensión de listas?
# R:
#   - En tomar_orden(), para generar la lista de productos:
#     [funcion_producto() for _ in range(cantidad)]

# ¿Dónde usarás lambda + map()?
# R:
#   - En calcular_total(), para multiplicar cada precio por la cantidad o
#     transformar los elementos de la lista en sus precios:
#     map(lambda x: precio_unitario, lista_productos)

# ─────────────────────────────────────────────────────────────────────────────


# ─────────────────────────────────────────────────────────────────────────────
# Sección 3 — CODIFICA
# ─────────────────────────────────────────────────────────────────────────────
# Completa cada paso en el orden indicado.
# Puedes apoyarte en los archivos del carpeta para recordar la sintaxis.


# ── PASO 1 ──────────────────────────────────────────────────────────────────
# Define tres funciones simples, sin parámetros, que devuelvan el nombre
# (y emoji) del producto correspondiente. Son funciones de primera clase.
#
# Referencia: ejercicio1_cafe.py → preparar_cafe()
#             desafio2_alimentos.py → preparar_pizza(), preparar_hamburguesa()

def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"
# ── PASO 2 ──────────────────────────────────────────────────────────────────
# Define la función calcular_promocion(cantidad).
# Si cantidad >= 3, devuelve el string "🎁 postre gratis".
# En caso contrario, devuelve un string vacío "".
#
# Referencia: desafio2_alimentos.py → calcular_bonus()

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3 ──────────────────────────────────────────────────────────────────
# Define la función tomar_orden(preparar_alimento, cantidad, precio_unitario).
#
# Esta función es de ORDEN SUPERIOR porque recibe otra función como argumento.
# preparar_alimento → función que se usará como callback (pizza, agua o tamal)
# cantidad          → número de porciones
# precio_unitario   → costo por porción (número)
#
# Dentro de la función debes:
#   a) Usar COMPRENSIÓN DE LISTAS para generar la lista de porciones,
#      llamando a preparar_alimento() en cada iteración.
#   b) Usar map() con una función LAMBDA para calcular el precio de cada
#      porción: cada elemento de la lista recibe el precio_unitario.
#      Convierte el resultado en lista con list().
#   c) Llamar a calcular_promocion(cantidad) y guardar el resultado.
#   d) Devolver una tupla: (porciones, precios, promocion)
#
# Referencia: ejercicio2_tipoCafe.py → ordenar_cafe()
#             desafio2_alimentos.py  → ordenar_alimento()
#             compresionListas.py    → map + lambda
#             funciones.py           → callbacks y orden superior

    # ── PASO 3 ──────────────────────────────────────────────────────────────────

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas
    porciones = [preparar_alimento() for _ in range(cantidad)]

    # b) map() + lambda para precios
    precios = list(map(lambda x: precio_unitario, porciones))

    # c) Promoción
    promocion = calcular_promocion(cantidad)

    # d) Devuelve los tres valores
    return porciones, precios, promocion


# ── PASO 4 ──────────────────────────────────────────────────────────────────
# Solicita al usuario la cantidad de cada producto y toma las órdenes.
# Almacena cada resultado en una variable distinta.
#
# Referencia: desafio1_hotcake.py → input() + int()

# ── PASO 4 ──────────────────────────────────────────────────────────────────

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

# Llama a tomar_orden para cada producto.
# Precios sugeridos: pizza=25, agua=10, tamal=15
orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)

# ── PASO 5 ──────────────────────────────────────────────────────────────────
# Muestra el resumen del pedido.
# Para cada orden imprime: porciones, precios y promoción (si aplica).
#
# Ejemplo de salida esperada:
#   🍕 PIZZAS   → ['🍕 pizza', '🍕 pizza', '🍕 pizza']
#   💲 Precios  → [25, 25, 25]
#   🎁 Promo    → 🎁 postre gratis
#
# Referencia: solucionAlimentos.py → print de tupla

# ── PASO 5 ──────────────────────────────────────────────────────────────────

print("\n========== RESUMEN DEL PEDIDO ==========")

# Desempaqueta cada tupla en sus tres partes
porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")

# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────
# Ejecuta el programa con los siguientes casos y verifica los resultados.
#
# ─────────────────────────────────────────────────────────────────────────────
# Sección 4 — PRUEBA
# ─────────────────────────────────────────────────────────────────────────────

# CASO 1 — Sin promoción
# Entrada:
#   Pizzas: 2  | Aguas: 1  | Tamales: 2
# Resultado esperado: sin promoción en todas
# Resultado obtenido: ✅ Coincide
# Observación:
#   Ninguna orden mostró "🎁 postre gratis", correcto.

# CASO 2 — Con promoción en todas
# Entrada:
#   Pizzas: 3  | Aguas: 5  | Tamales: 4
# Resultado esperado: todas con promoción
# Resultado obtenido: ✅ Coincide
# Observación:
#   Todas las órdenes mostraron "🎁 postre gratis", correcto.

# CASO 3 — Promoción mixta
# Entrada:
#   Pizzas: 1  | Aguas: 3  | Tamales: 2
# Resultado esperado: solo aguas con promoción
# Resultado obtenido: ✅ Coincide
# Observación:
#   Solo la orden de aguas mostró promoción, correcto.

# CASO 4 — Verificación de precios
# Entrada:
#   3 pizzas → [25, 25, 25]
#   4 tamales → [15, 15, 15, 15]
# Resultado obtenido: ✅ Coincide
# Observación:
#   map() + lambda generó correctamente las listas de precios.

# Conclusión general:
#   - ¿El resultado coincide con lo esperado? ✅
#   - ¿Errores detectados? Ninguno
#   - ¿Qué cambiarías? Nada, el programa funciona correctamente.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Desafío extra (opcional)
# ─────────────────────────────────────────────────────────────────────────────
# Si terminaste antes y quieres ir más allá:
#
# 1. Usa sum() y map() + lambda para calcular el TOTAL a pagar de cada orden.

def calcular_total(precios):
    return sum(map(lambda x: x, precios))

# 2. Crea una función elegir_producto(nombre) que sea de ORDEN SUPERIOR:
#    recibe un string ("pizza", "agua" o "tamal") y DEVUELVE la función
#    de preparación correspondiente (sin ejecutarla).
#    Referencia: funciones.py → elegir_operacion()

def elegir_producto(nombre):
    if nombre == "pizza":
        return preparar_pizza
    elif nombre == "agua":
        return preparar_agua
    elif nombre == "tamal":
        return preparar_tamal
    else:
        return None
    
# 3. Usa la función del punto 2 para reemplazar los argumentos directos en
#    las llamadas a tomar_orden().

orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
# ─────────────────────────────────────────────────────────────────────────────