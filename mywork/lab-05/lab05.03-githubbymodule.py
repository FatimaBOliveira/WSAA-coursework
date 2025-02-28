from github import Github
from config import apikeys as cfg

apikey = cfg["apikeywsaa"]
# use your own key
g = Github(apikey)
for repo in g.get_user().get_repos():
 print(repo.name)


#######################################################
import requests

# URL of the private account
privatekey= cfg["apikey"]
private = Github(privatekey)
private_repo = private.get_repo("FatimaBOliveira/aprivateone")
#print(private_repo.clone_url)

# Link to the raw contents of the file.
fileInfo = private_repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Print the contents of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

# Add new line to the txt file
newContents = contentOfFile + "\nI'm good =)"
#print (newContents)

# Commit new changes
gitHubResponse=private_repo.update_file(fileInfo.path,"\nupdated", newContents,fileInfo.sha)
print (gitHubResponse)