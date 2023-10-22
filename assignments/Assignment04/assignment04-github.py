
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)
#for repo in g.get_user().get_repos():
 #print(repo.name)

repo = g.get_repo("JScarry/aPrivateRepository")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
newContents = contentOfFile.replace("Andrew", "Jarlath")
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)

