from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
        return "Hello"
#get all
@app.route('/books')
def getAll():
        return "served by get All()"
#find by id
@app.route('/books/<int:id>')
def findByID(id):
        return "served by find by id with id "+str(id)
#create
@app.route('/books', methods=['POST'])
def create():
        return "served by create"
#update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        return "served by update with id "+str(id)
#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return "served by delete with id "+str(id)

if __name__ == "__main__":
        app.run(debug = True)