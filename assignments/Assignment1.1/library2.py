from xml.dom.minidom import parse

filename = "library.xml"

doc = parse(filename)
#with open(filename) as fp:
    #doc = parse(fp)
#root = doc.getroot()
#print(root)
BookNodeList = doc.getElementsByTagName("Book")
print(len(BookNodeList))
BooksNodeList = doc.getElementsByTagName("Books")
print(len(BooksNodeList))
#categoryNode = BooksNodeList.getElementsByName("category").item(0)
#print(categoryNode)

for booksNode in BooksNodeList:
    print("->")
    booksNode = booksNode.getAttribute("category")
    print ("Category: ", booksNode)
    for bookNode in BookNodeList:
            titleNode = bookNode.getElementsByTagName("title").item(0)
            title = titleNode.firstChild.nodeValue.strip()
            print ("Title: ", title)
            authorNode = bookNode.getElementsByTagName("author").item(0)
            author = authorNode.firstChild.nodeValue.strip()
            print ("Author: ", author)
print("->")           
