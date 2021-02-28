#here code for get html in preetified form
import requests
from bs4 import BeautifulSoup

url = input("ENTER YOUR TARGET URL HERE : ")  # -- enter url here

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)




