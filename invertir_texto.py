### INVERTIR CADENA DE TEXTO ###

texto = 'hola mundo'

split=texto.split()
cadena_invertida=[]
for i in split:
 cadena_invertida.append(i[::-1])

invertido=' '.join(cadena_invertida)
print(invertido)
