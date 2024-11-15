### CONTADOR DE VOCALES


vocales = ['a', 'e', 'i', 'o', 'u']
texto = 'hola como estas'

for i in vocales:
 conteo = texto.count(i)
 if conteo != 0:
  print(f"Vocal -> [{i}] {conteo}")
