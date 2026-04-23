###
# 03 - Ranger ()
# Permiso crear una secuencia de numeros. Puede ser utilzado for pero no solo para esp
###

from os import system
if system("clean") !=0: system("cls")

print("\nRanger:")

#Generado una secuenca de Numero del 0 al 9
for num in range(10):
 print(num)
 
#ranger(inicio, fin)
for num in range(5, 10):
 print(num)

#ranger(inicio, fin paso)
for num in range(0, 1000, 5):
 print(num)

for num in range(-5, 0):
 print(num)

 for num in range(10, 0, -1):
  print(num)

 for num in range(0, 444):
  print(num)

 nums = range(10)
 list_of_nums = list(nums)
 print(list_of_nums)

# seria para hacerlo cinco veces
for _ in range(5):
 print("Hacer coinco veces algo")

 ###