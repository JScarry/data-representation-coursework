from ast import Pass
import requests
import json

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en" #url split so we can insert target dataset

def getAllAsFile(dataset):     #get all files function to get all files from the url
    with open("cso.json", "wt") as fp:     #save the file as cso.json 
        print(json.dumps(getAll(dataset)), file=fp)  #print out the dataset. In this case it is dataset FIQ02 - specified in main function call
def getAll(dataset):     #function that gets all datasets from specified url
    url = urlBegining + dataset + urlEnd  
    response = requests.get(url)
    return response.json()  #returns a response in json         

if __name__ == "__main__":
    getAllAsFile("FIQ02")  #Function call speciffying target data = Exchequer Account (Historical Series) = FIQ02
    