### mostrar tablas de multiplicar ###
import os



while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 numero = int(input("MOSTRAR LA TABLA DEL NUMERO = "))
 print("")
 for i in range(1, 11):
  calcular = numero * i
  print(f"{numero} X {i} = {calcular}")
 input("\nPresione ENTER para continuar...")
