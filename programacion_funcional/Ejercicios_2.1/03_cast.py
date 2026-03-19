from os import system
if system ("clear") !=0: system("cls")

print("Conversion Tipos")
#Convierte una cadena
print(2 + int("100"))
#Convierte entero a cadena
print("100" + str(2))
#Convierte una cadena a un numero decimal
print(type(float("3.1416")))
#Convertir un numero decimal a entero
print(int(3.1416))

#Evaluar Valores Numericos
print(bool(3))
print(bool(0))
print(bool(-1))

#Evaluar Cadenas como booleana
print(bool(""))
print(bool(" "))
print(bool("False"))

#Rendodear un numero decimal
print(round(2.51))


