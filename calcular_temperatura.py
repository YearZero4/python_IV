### INVERTIR CADENA DE TEXTO ###

def celsius_a_fahrenheit(temperatura):
 return temperatura * 1.8 + 32
def fahrenheit_a_celsius(temperatura):
 return (temperatura - 32) / 1.8

temperatura_f = celsius_a_fahrenheit(17)
print(f'La temperatura en fahrenheit es: {temperatura_f}')


temperatura_c = fahrenheit_a_celsius(17)
print(f'La temperatura en Celsius es: {temperatura_c}')
