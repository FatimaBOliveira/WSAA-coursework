# This program that checks my existing repositories and the contents of mywork folder in WSAA-coursework repository.
# Author: Fatima Oliveira

import requests
import json

#filename = "repos-public.json"
#URL = 'https://api.github.com/users/FatimaBOliveira/repos'

filename = "wsaa-mywork.json"
URL = "https://api.github.com/repos/FatimaBOliveira/WSAA-coursework/contents/mywork/"


response = requests.get(URL)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)