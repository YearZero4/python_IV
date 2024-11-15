### LISTA DE DNS ###
from bs4 import BeautifulSoup as b
import requests
url='https://www.mundodeportivo.com/urbantecno/tecnologia/20-dns-mas-rapidas-seguras-2022'
peticion = requests.get(url)
soup = b(peticion.content, 'html.parser')
buscar = soup.find_all('td')

for i in buscar:
 resultados=i.text
 comprobar = resultados.find('.')
 if comprobar == -1:
  print('\n' + resultados)
 else:
  print(resultados)

input()
