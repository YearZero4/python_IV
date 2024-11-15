### COMPROBAR SI UNA CLAVE ES SEGURA ###
from colorama import init, Fore, Style
import re

init(autoreset=True)
GREEN = f'{Fore.GREEN}{Style.BRIGHT}'
RED = f'{Fore.RED}{Style.BRIGHT}'
WHITE = f'{Fore.WHITE}{Style.BRIGHT}'

claves_array = ['password1234', 'Killer12.$', 'python_&&5K', 'admin66']

for clave in claves_array:
 patron = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,}$'
 comprobar = re.search(patron, clave)
 if comprobar != None:
  print(f"{GREEN}Clave Segura => {WHITE}{clave}\n")
 else:
  print(f"{RED}Error [CLAVE NO SEGURA] =>{WHITE} {clave}\nPor F\
avor Verifique que su clave contenga:\n\n-Almenos\
1 Caracter en mayuscula\n-Caracteres en minuscula\n\
-Caracteres Alfanumericos\n-Caracteres Especiales\n\
-Que contega como minimo 8 caracteres\n")
input("")
