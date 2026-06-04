
print ("Evaluacion 2.2")

### EJERCICIO 1: PRESENTACIÓN PERSONAL
##Descripción
##Crea un programa simple que muestre información sobre una persona.

# Ejercicio 1: Presentación personal

# Mis Datos
nombre = "Julio"
edad = 25
ciudad = "Felipe Carrillo Puerto"
estudiante = True

# Mostrar la información
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Vivo en:", ciudad)
print("¿Soy estudiante?:", estudiante)


##EJERCICIO 2: CASA DE CAMBIO
## Situación
## Convierte dinero de una moneda a otra usando una tasa de cambio.

# Ejercicio 2: Casa de Canbio

# Definir la tasa de cambio
tasa_cambio = 19.00  # 1 USD = 19.00 MXN

# Pedir al usuario la cantidad en USA
usd = float(input("¿Cuántos USD tienes?: "))

# Calcular la conversión
mxn = usd * tasa_cambio

# Mostrar el resultado
print(f"{usd:.2f} USD = {mxn:.2f} MXN")


##EJERCICIO 3: ¿QUIEN ES MAYOR DE EDAD?
##Descripción
##Comparas las edades de dos personas para determinar quién es mayor

#Ejercicio 3:¿Quien es mayor de edad?

# Pedir datos de la primera persona
nombre1 = input("Nombre de la primera persona: ")
edad1 = int(input(f"Edad de {nombre1}: "))

# Pedir datos de la segunda persona
nombre2 = input("Nombre de la segunda persona: ")
edad2 = int(input(f"Edad de {nombre2}: "))

# Comparar edades
if edad1 > edad2:
    diferencia = edad1 - edad2
    print(f"{nombre1} es mayor que {nombre2} por {diferencia} años.")
elif edad2 > edad1:
    diferencia = edad2 - edad1
    print(f"{nombre2} es mayor que {nombre1} por {diferencia} años.")
else:
    print(f"{nombre1} y {nombre2} tienen la misma edad.")

##EJERCICIO 4: BOLETA DE CALIFICACIONES
##Descripción
##Eres docente y necesitas calcular la nota final de un estudiante.



##EJERCICIO 6: TABLA DE MULTIPLICAR
##Descripción
##Necesitas imprimir la tabla de multiplicar de un número ingresado por el usuario.

# EJERCICIO 6: Tabla de multiplicar

# Pedir número al usuario
num = int(input("¿Tabla de qué número? (1-12): "))

if num < 1 or num > 12:
    print("Número fuera de rango. Debe ser entre 1 al 12")
else:
    print(f"Tabla del {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


##EJERCICIO 7: NÚMEROS PARES E IMPARES
##Descripción
##Necesita imprimir números pares e impares en un rango especificado por el usuario