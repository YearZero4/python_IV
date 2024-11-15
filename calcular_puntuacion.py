### CALCULAR PROMEDIO DE CALIFICACION DE UN ESTUDIANTE ##
import os

while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 calificacion = int(input('Cual es tu calificacion = '))
 porcentaje=int(input("Porcentaje = "))
 print("")
 calcular = calificacion * porcentaje / 100
 print(f"{calificacion} puntos equivale a {calcular} del {porcentaje}%")
 input("\nPresione ENTER para continuar...")
