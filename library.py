from xml.dom.minidom import parse

filename = "library.xml"

doc = parse(filename)
#with open(filename) as fp:
#    doc = parse(fp)

BookNodeList = doc.getElementsByTagName("Book")
print(len(BookNodeList))
for bookNode in BookNodeList:
    print("->")
    titleNode = bookNode.getElementsByTagName("title").item(0)
    title = titleNode.firstChild.nodeValue.strip()
    print (title)
