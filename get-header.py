#get headers of requested site
import requests 

response = requests.get(input('ENTER YOUR TARGET URL ' )) 
  
print(response.headers) 
