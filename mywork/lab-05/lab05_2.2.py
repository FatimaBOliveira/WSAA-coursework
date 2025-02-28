# Program that checks a private repository
# Author: Fatima Oliveira

import requests
import json
from config import apikeys as cfg

url = 'https://api.github.com/repos/FatimaBOliveira/aprivateone'

apikey = cfg["apikey"]
filename = "repos-private.json"

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()
print (response.json())

with open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
