### WEBSCRAPING A UN SITIO WEB ###

from bs4 import BeautifulSoup as b
import requests
url = 'https://www.wizcase.com/blog/best-free-public-dns-servers/'
peticion = requests.get(url)
soup = b(peticion.content, 'html.parser')
buscar_etiqueta = soup.find_all('strong')
for i in buscar_etiqueta:
	print(i)