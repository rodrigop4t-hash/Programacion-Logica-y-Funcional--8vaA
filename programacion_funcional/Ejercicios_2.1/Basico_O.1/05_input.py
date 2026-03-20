from os import system
if system ("clear") !=0: system("cls")

nombre = input("Hola como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuantos años tienes?\n")
age = int(age)
print(f"Tienes {age}, años")

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")