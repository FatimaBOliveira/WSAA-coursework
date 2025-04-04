# flask server that links to a DAO
# author: Fatima Oliveira

from flask import Flask, request, jsonify, abort
#from PatientDAOskeleton import patientDAO
from PatientDAO import patientDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world!"

# getall
# curl http://127.0.0.1:5000/patient
@app.route('/patient', methods=['GET'])
def getall():
        return jsonify(patientDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/patient/1
@app.route('/patient/<int:id>', methods=['GET'])
def findbyid(id):
    patient = patientDAO.findByID(id)  # Query the DAO
    if not patient:  # Check if the patient exists
        abort(404, description="Patient not found")
    return jsonify(patient)


#create
# curl -H "Content-Type: application/json" -X POST -d "{\"name\":\"Mary\", \"age\":66, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient
@app.route('/patient', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        patient = {}

        if "name" not in jsonstring:
                abort(403)
        patient["name"] = jsonstring["name"]
        if "age" not in jsonstring:
                abort(403)
        patient["age"] = jsonstring["age"]
        if "type_of_treatment" not in jsonstring:
                abort(403)
        patient["type_of_treatment"] = jsonstring["type_of_treatment"]
        
        return jsonify(patientDAO.create(patient))

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Mary\", \"age\":67, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient/2

@app.route('/patient/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        patient = {}

        if "name" in jsonstring:
                patient["name"] = jsonstring["name"]
        if "age" in jsonstring:
                patient["age"] = jsonstring["age"]
        if "type_of_treatment" in jsonstring:
                patient["type_of_treatment"] = jsonstring["type_of_treatment"]
        
        return jsonify(patientDAO.update(id, patient))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/patient/1

@app.route('/patient/<int:id>', methods=['DELETE'])
def delete(id):
    result = patientDAO.findByID(id)  # Check if patient exists
    if not result:
        abort(404, description="Patient not found")
    
    # Delete the patient and return success message
    patientDAO.delete(id)
    return jsonify({"message": f"Patient with ID {id} deleted successfully"})

if __name__ == "__main__":
    app.run(debug = True)