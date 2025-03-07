# Author: Fatima Oliveira

from flask import Flask, request
import bookdao

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"

# getall
# curl http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def getall():
    return "get all"

# find by id
# curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

#create
# curl -H "Content-Type:application/json" -X POST -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
# read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

#delete
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)