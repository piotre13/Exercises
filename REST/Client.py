import requests
import json


res = requests.post('http://127.0.0.1:8080/', json={"name": "Pippo", "surname": "Pluto", "email": "pippo@"})

print(res)