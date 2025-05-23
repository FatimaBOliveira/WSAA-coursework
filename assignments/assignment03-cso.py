# CSO
# This program loads the dataset for the "Exchequer Account (Historical Series)" from a RESTFul API of CSO. 
# It also stores the data into a file called "cso.json".
# "Exchequer Account (Historical Series)" dataset can be found here: https://data.cso.ie/table/FIQ02
# For a detailed walkthrough, please check this section in the README file: https://github.com/FatimaBOliveira/WSAA-coursework/tree/main/assignments#the-cso-assignment03-csopy
# Author: Fatima Oliveira

# Import libraries.
import requests
import json 

# URL to get the data.
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

# Load the data and convert it into json.
def getInfo():   
    response = requests.get(url)
    return response.json()

# Create a json file with the data.
def getAsFile():
    with open("./json/cso.json", "wt") as fp:
        print(json.dumps(getInfo()), file=fp)

# Run script.
if __name__ == "__main__":
    getAsFile()