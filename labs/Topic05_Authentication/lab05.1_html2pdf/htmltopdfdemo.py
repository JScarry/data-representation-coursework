import requests
import urllib.parse
from config1 import config1 as cfg

targetUrl = "https://en.wikipedia.org/wiki/API_key"

apiKey = cfg["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("document.pdf", "wb") as handler:
    handler.write(result)