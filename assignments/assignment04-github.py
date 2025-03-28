# Program that reads a file from a repository and replace the text "Andrew" with my name.
# The program will then commit those changes and push it back to the repository.
# Author: Fatima Oliveira

# Import libraries
from github import Github
import requests
import json
from config import apikeys as cfg

# GitHub raw URL of the JSON file
url = "https://raw.githubusercontent.com/andrewbeattycourseware/WSAA-Courseware/main/code/Topic-01-introduction%20-%20Copy/book.json"

# Fetch the file
response = requests.get(url)
contentOfFile = response.text
#print (contentOfFile)

# Load JSON
data = json.loads(contentOfFile)

# Function that replaces data in the json file
def replace_in_json(data, old_data, new_data):
    return json.loads(json.dumps(data).replace(old_data, new_data))
                                               
# Replace name
replace_data = replace_in_json(data, "Andrew Beatty", "Fatima Oliveira")

# Convert back to JSON
updated_content = json.dumps(replace_data, indent=4)
#print(updated_content)

# Api key
apikey = cfg["apikeywsaa"]
g = Github(apikey)

# Get repo
# https://pygithub.readthedocs.io/en/latest/examples/Repository.html
repo = g.get_repo("FatimaBOliveira/WSAA-coursework")
#print(repo)

# A function that creates or reads the modified file in my repository.
# https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html#github.Repository.Repository.create_file
def create_or_read():

    # Check if the file exists in the repository.
    try:
        fileInfo = repo.get_contents(path="assignments/json/assignment4_book.json")
        urlFile = fileInfo.download_url
        # Print the contents of the file
        response = requests.get(urlFile)
        contentFile = response.text
        print (contentFile)
    
    # Create a file if it doesn't exist. It will be automatically committed and pushed to the repository.
    except: 
        create_file = repo.create_file(path ="assignments/json/assignment4_book.json", 
                                       message = "Create new file: assignment4_book.json", content = updated_content)

# Run function
if __name__ == "__main__":
    create_or_read()