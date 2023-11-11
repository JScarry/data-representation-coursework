
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
# use your own key

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
#print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
#print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)

