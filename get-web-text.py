#get website text
import requests
from bs4 import BeautifulSoup

url = input("ENTER YOUR TARGET URL HERE - ") # --enter url

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

print(soup.get_text())

