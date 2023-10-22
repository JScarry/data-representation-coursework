
from github import Github
import requests
from config import config as cfg  #find the prog config.py and import config as cgf (this holds the api key as githubkey) 

apikey = cfg["githubkey"] 
g = Github(apikey)
#for repo in g.get_user().get_repos():
 #print(repo.name)

repo = g.get_repo("JScarry/aPrivateRepository") #this uses Pygithub to get the repo
#print(repo.clone_url)                          #prints out the repo url

fileInfo = repo.get_contents("test.txt")     #gets the file test.txt from the repo
urlOfFile = fileInfo.download_url            #gets the url of the file
#print (urlOfFile)

response = requests.get(urlOfFile)       
contentOfFile = response.text               #gets contents of the file
newContents = contentOfFile.replace("Andrew", "Jarlath")    #replaces the words in the string
print (newContents)                         #print out the new contents, to confirm words are replaced

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)    #pushes file by commit with comment "updated by prog"
print (gitHubResponse)   #print confirmation response from github

