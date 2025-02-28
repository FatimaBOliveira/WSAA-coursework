# Program that reads a web page and converts it into pdf file.
# Author: Fatima Oliveira

import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://en.wikipedia.org/wiki/Atlantic_Technological_University"

apiKey = cfg["htmlpdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)