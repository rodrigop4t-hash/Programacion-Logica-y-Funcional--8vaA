###
#1 - Bucle (while)
# Permite ejecutar un bloque de codigo repentinamente mientrras se cunpla una condicion

from os import system
if system("clean") !=0: system("cls")

print("\n Bucle while:")

#Bucle con una simple condicion
contador = 0

while contador <= 5:
    print(contador)
    contador += 1 # es super inportante para evitar bucle infinitos

#Utilizando la palabra break, para ronper el bucle
print("\n Bucle while con break:")
contador = 0
           
while True:
  print(contador)
  contador +=1
  if contador ==5:
     break #Sale del bucle
  
#continue, que lo hace es saltar esa iteracion en concreto
# y continuar con el bucle
print("\n Bucle con continuar")
contador = 0
while contador < 10:
   contador += 1

   if contador % 2 == 0:
      continue
   
   print(contador)

#else, esta condicion cuando se ejcuta ?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
   print(contador)
else:
   print("El bucle a terminado")

#Pedirle al usuario un numero que tiene
#que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
   numero = int(input("Escribe un numero positivo: "))
if numero < 0:
   print("El numero debe ser positivo. Intenta Otra vez")

print(f"El numero que has introducido es {numero}")

numero = -1
while numero <0:
   try:
      numero = int(input("Escribe un numero positivo: "))
      if numero < 0:
         print("El numero debe ser positivo. Intenta Otra vez")
   except:
      print("Lo que introduces debe ser un numero!")

print(f"El numero que has introducido es {numero}")

###
#EJERCICIOS 