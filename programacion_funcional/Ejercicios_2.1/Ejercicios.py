from os import system
if system ("clear") !=0: system("cls")

print("\nEjercicio 1: Imprimir mensaje")
print("Escribe un programa que inprima tu nombre y tu ciudad en lineas separadas.")


### Completa aqui 

print(" Me llamo Julio Rodrigo Pat Balam y vivo en Felipe Cariilo Puerto")


print("\nEjercicio 2: Muestra los tipos de datos de las siguientes Variables:")
print("Usa el comando 'type()'para determinar el tipo de datos de cada Variable.")
a = 15
b = "Hola Mundo"
c = True
d = None

### Completa aqui 

## De entero
print(type(15))
## Imprimir un texto
print(type("Hola Mundo"))
## Tipo Boolena
print(type(True))
## Tipo dato especial
print(type(None))


print("\nEjercicio 3: Casting de Tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Que ocurre?")

### Completa aqui 

##1ero convertir de a entero y despues a float
print(int(float("12345")))
##2do Convertir float a entero
print(int(3.99))


print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para inprimir una presentacion.")

#!Hola¡ Me llamo tu_nombre y tengo tu_edad años, mido tu_altura metros

### Completa aqui 
my_name = "Julio"
my_edad = 21
my_height = 1.71

print(f"!Hola¡ Me llamo {my_name}, y tengo {my_edad}años, mido {my_height} metros")


print("\nEjercicio 5: Numeros")
print("1. Crear una variable con el numero PI (sin asignar una variable)")
print("2. Rendondea el numero con round()")
print("3. Haz la division entera entre el numero que te salio y el numero 2")
print("4. El resultado deberia ser 1")

## Pasos en uno
print( round(3.1416) // 2 )
