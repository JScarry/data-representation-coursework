import requests
import json

filename = "repos-public-andrew-aprivateone.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
#url = 'https://api.github.com/users/andrewbeattycourseware/followers'
url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'  #api

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
