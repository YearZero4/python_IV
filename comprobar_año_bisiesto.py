
import os
while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 def es_bisiesto(año):
  if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
   return True
  else:
   return False
 year = int(input("Año a comprobar si es bisiesto = "))
 if es_bisiesto(year):
  print(f"{year} este año es bisiesto.")
 else:
  print(f"{year} este año no es bisiesto")
 input("\nPresione Enter Para Continuar...")
