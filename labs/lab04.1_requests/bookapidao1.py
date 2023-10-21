
import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()
    #print (response.text)

def getBookById(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()
    #print (response.text)

def updateBook(id, bookdiff):  # update book (id and difference specified in main))
    updateurl =  url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

def createBook(book):
    response = requests.post(url, json=book)
    #headers ={ "Content-type": "application/json"}
    #response = requests.post(url, data=json.dumps(book), headers=headers)
    return response.json()

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
    print(getAllBooks())
    #print(getBookById(303))
    #print(deleteBook(317))
    #print (createBook(book))
    #print(updateBook(316, bookdiff))  # update book id xxx with bookdiff
