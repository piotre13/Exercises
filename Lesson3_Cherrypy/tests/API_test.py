import requests
import json

url = 'https://api.teleport.org/api/cities/'
res = requests.get(url)
data = json.loads(res.text)
print(res)

res2 = requests.get('https://api.teleport.org/api/countries/iso_alpha2:CN/salaries')
print(res2)