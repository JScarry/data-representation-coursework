
import requests
import json
from statistics import mean

url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    allbooks = response.json()
    return allbooks
    #print (response.text)




def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()
    #print (response.text)


if __name__ == "__main__":
    book= {                 #book to create
        'Author':"testaa",
        'Title':"testaatitle",
        "Price": 123
    }
    bookdiff= {               #differences to update
        'Author':"testaa",
        'Title':"testaatitle",
        "Price": 4321
    }
    #print(getAllBooks())

    getAllBooks()
    with open("lines.allbooks") as lines:   #https://stackoverflow.com/questions/66572010/how-to-find-average-of-values-in-file-with-json-like-format
        d = [json.loads(line) for line in lines.readlines()]
        print(f"Average for {len(d)} requests: {sum(i['Price'] for i in d) / len(d)}")
