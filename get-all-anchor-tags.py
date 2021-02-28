#GET ALL ANCHOR TAGS
import requests
from bs4 import BeautifulSoup

url = input('ENTER YOUR TARGET URL HERE')

response=requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
