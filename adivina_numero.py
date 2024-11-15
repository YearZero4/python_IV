### ADIVINAR NUMERI DEL 0 -9 ###

import random

numero_aleatorio = random.randint(0,9)
while True:
 numero_usuario = int(input("Introduce Numero [0,9] = "))
 if numero_usuario == numero_aleatorio:
  print("Adivinastes el numero")
 else:
  print("Te equivocastes jaja que pendejo")
 print("")
