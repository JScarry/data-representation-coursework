from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

cars=[{"id":1,"Make":"Ford","Model":"Fiesta","Price":1000},
      {"id":2,"Make":"Ford","Model":"Focus","Price":1002},
      {"id":3,"Make":"Toyota","Model":"Corolla","Price":1022},
      {"id":4,"Make":"VW","Model":"Polo","Price":1333},
      {"id":5,"Make":"VW","Model":"Golf","Price":1033},
      {"id":6,"Make":"Ford","Model":"Fiesta","Price":2100},
      {"id":7,"Make":"Volvo","Model":"c30","Price":100},
      {"id":8,"Make":"Audi","Model":"a1","Price":10000},
      ]
nextId=9

@app.route('/')
def index():
        return "Hello"
#get all
@app.route('/cars')
def getAll():
        return jsonify(cars)
#find by id
@app.route('/cars/<int:id>')
def findByID(id):
        foundCars = list(filter (lambda t : t["id"]== id, cars))
        #print(foundCars)
        if len(foundCars) == 0:
                return jsonify({}), 204
        return jsonify(foundCars[0])  #if 2 cars have the same id this will return only the first one
        return "served by find by id with id "+str(id)
#create
#curl -X "POST" -H "content-type:application/json" -d "{\"Make\":\"test\",\"Model\":\"testb\",\"Price\":1111}" http://127.0.0.1:5000/cars
@app.route('/cars', methods=['POST'])
def create():
    global nextId
    if not request.json: #if there is no json request then return 400
        abort(400)

    car = {
        "id" : nextId,
        "Make": request.json["Make"],
        "Model": request.json["Model"],
        "Price": request.json["Price"]
    }
    cars.append(car)    
    nextId+= 1
    return jsonify(car)


#update
# curl -X PUT -d "{\"Make\":\"Frd\",\"Model\":\"Mondeo\",\"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/cars/1
@app.route('/cars/<int:id>', methods=['PUT'])
def update(id):
        foundCars = list(filter (lambda t : t["id"]== id, cars))
        if len(foundCars) == 0:
                return jsonify({}), 404
        currentCar = foundCars[0]
        if 'Make' in request.json:
               currentCar['Make'] = request.json['Make']
        if 'Model' in request.json:
               currentCar['Model'] = request.json['Model']
        if 'Price' in request.json:
               currentCar['Price'] = request.json['Price']

        return jsonify(currentCar)
#delete

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
        foundCars = list(filter (lambda t : t["id"]== id, cars))
        if len(foundCars) == 0:
                return jsonify({}), 404
        cars.remove(foundCars[0])

        return jsonify({"done":True})

if __name__ == "__main__":
        app.run(debug = True)