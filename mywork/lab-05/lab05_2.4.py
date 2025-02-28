# Program that makes a change in my repository. It will create a new file and commit it in Github.
# Author: Fatima Oliveira 

# Libraries
import json
import requests
import base64
from config import apikeys as cfg

# Replace with your GitHub personal access token
token = cfg["apikeywsaa"]
filename = "lab-04.json" 
commit_message = "New json file with contents of lab-04 folder"

# API URL to create a new file
url = "https://api.github.com/repos/FatimaBOliveira/WSAA-coursework/contents/mywork/lab-04"

response = requests.get(url)
#print (response.status_code)
repoJSON = response.json()
#print (response.json())

# Create new JSON file
#with  open(filename, "w") as fp:      # Once created, it is unnecessary to run it again as it will do a new file every time.
#    json.dump(repoJSON, fp, indent=4)

# API URL to create a new file
url_path = "https://api.github.com/repos/FatimaBOliveira/WSAA-coursework/contents/mywork/lab-04/lab-04.json"

# Read the JSON file content
with open(filename, "r") as file:
    file_content = file.read()

# Encode the file content to base64
content_base64 = base64.b64encode(file_content.encode()).decode()

# Access Github.
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Check if the file already exists
response = requests.get(url_path, headers=headers)

if response.status_code == 200:
    # File exists, retrieve the sha
    file_info = response.json()
    sha = file_info["sha"]

    # Update the existing file
    data = {
        'message': commit_message,
        'content': content_base64,
        'sha': sha
    }

    response = requests.put(url_path, headers=headers, json=data)

else:
    # File does not exist, create a new file
    data = {
        'message': commit_message,
        'content': content_base64
    }

    response = requests.put(url_path, headers=headers, json=data)

if response.status_code in (200, 201):
    print("File created and committed successfully.")
else:
    print("Failed to create and commit file:", response.json())

# https://stackoverflow.com/questions/75327473/how-do-you-push-files-to-a-github-repo-in-python