# flask server that links to a DAO
# author: Fatima Oliveira

#from flask import Flask, request, jsonify, abort
from flask import Flask, request, jsonify, abort, send_from_directory
from datetime import datetime, timedelta
from PatientDAO import patientDAO
from TreatmentDAO import treatmentDAO
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)   # Enable CORS globally for the API
#CORS(app, supports_credentials=True)  # Enable CORS with credentials
#CORS(app, resources={r"/treatment/*": {"origins": "*"}})
#CORS(app, resources={r"/*": {"origins": "*"}})

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
# curl -H "Content-Type: application/json" -X POST -d "{\"id\":1,\"name\":\"Mary\", \"age\":66, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient
@app.route('/patient', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        patient = {}

        if "id" not in jsonstring:
               abort(400)
        patient["id"] = jsonstring["id"]
        if "name" not in jsonstring:
                abort(400)
        patient["name"] = jsonstring["name"]
        if "age" not in jsonstring:
                abort(400)
        patient["age"] = jsonstring["age"]
        if "type_of_treatment" not in jsonstring:
                abort(400)
        patient["type_of_treatment"] = jsonstring["type_of_treatment"]

        existing_patient = patientDAO.findByID(patient["id"])
        if existing_patient:
                abort(409, description="Patient with this ID already exists.")
        
        return jsonify(patientDAO.create(patient))

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Mary\", \"age\":67, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient/2

@app.route('/patient/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        patient = {}

        existing_patient = patientDAO.findByID(id)
        if not existing_patient:
            return jsonify({"error": f"Patient with ID {id} not found."}), 404
        
        #if "id" in jsonstring: # NOT NEEDED IN UPDATE
        #        patient["id"] = jsonstring["id"]
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

#######################################################################################################################
# getall
# curl http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['GET'])
def getall_tx():
        return jsonify(treatmentDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/treatment/1
@app.route('/treatment/<int:patient_id>', methods=['GET'])
def findbyid_tx(patient_id):
    treatment = treatmentDAO.findByID(patient_id)  # Query the DAO
    if not treatment:  # Check if the patient exists
        abort(404, description="Patient not found")
    return jsonify(treatment)

#create
# curl -H "Content-Type: application/json" -X POST -d "{\"patient_id\":2,\"date_time\":\"2025-04-17 10:10\", \"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"Patient is feeling well.\"}" http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['POST'])
def create_tx():
        # read json from the body
        jsonstring = request.json
        treatment = {}

        if "patient_id" not in jsonstring:
               abort(400) 
        treatment["patient_id"] = jsonstring["patient_id"]
        if "date_time" not in jsonstring:
                abort(400)
        treatment["date_time"] = jsonstring["date_time"]
        if "bp_systolic" not in jsonstring:
                abort(400)
        treatment["bp_systolic"] = jsonstring["bp_systolic"]
        if "bp_diastolic" not in jsonstring:
                abort(400)
        treatment["bp_diastolic"] = jsonstring["bp_diastolic"]
        if "heart_rate" not in jsonstring:
                abort(400)
        treatment["heart_rate"] = jsonstring["heart_rate"]
        if "notes" not in jsonstring:
                abort(400)
        treatment["notes"] = jsonstring["notes"]

        # Check if patient exists
        patient_id = treatment["patient_id"]
        existing_patient = patientDAO.findByID(patient_id)
        if not existing_patient:
            return jsonify({"error": f"Patient with ID {patient_id} not found."}), 404
        
        return jsonify(treatmentDAO.create(treatment))

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"BP dropping, UF suspended.\"}" "http://127.0.0.1:5000/treatment/2/2025-04-17%2010:10"
@app.route('/treatment/<int:patient_id>/<string:date_time>', methods=['PUT'])
def update_tx(patient_id, date_time):
        jsonstring = request.json
        treatment = {}

        existing_patient = treatmentDAO.findByID(patient_id)
        if not existing_patient:
            return jsonify({"error": f"Patient with ID {patient_id} not found."}), 404
        
        try:
        # Handle URL-decoded time
                parsed_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
                adjusted_time = parsed_time - timedelta(hours=0)  # Adjust for timezone difference
                date_time_str = adjusted_time.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
              return jsonify({"error": "Invalid date_time format. Use 'YYYY-MM-DD HH:MM'"}), 400
        
        if "bp_systolic" not in jsonstring:
                abort(400)
        treatment["bp_systolic"] = jsonstring["bp_systolic"]
        if "bp_diastolic" not in jsonstring:
                abort(400)
        treatment["bp_diastolic"] = jsonstring["bp_diastolic"]
        if "heart_rate" not in jsonstring:
                abort(400)
        treatment["heart_rate"] = jsonstring["heart_rate"]
        if "notes" not in jsonstring:
                abort(400)
        treatment["notes"] = jsonstring["notes"]
       
        return jsonify(treatmentDAO.update(patient_id, date_time_str, treatment))

# Delete
# curl -X DELETE  "http://127.0.0.1:5000/treatment/2/2025-04-17%2010:10"

@app.route('/treatment/<int:patient_id>/<string:date_time>', methods=['DELETE'])
def delete_tx(patient_id, date_time):
    result = treatmentDAO.findByID(patient_id)  # Check if patient exists
    if not result:
        abort(404, description="Patient not found")

    treatment = treatmentDAO.delete(patient_id, date_time)
    if not treatment:
        abort(404, description="Treatment record not found or already deleted.")

    return jsonify({"message": f"Treatment for the patient {patient_id} at {date_time} deleted successfully"})



################################################################
# To access both pages 
# Serve treatment.html from treatment_interface
# http://127.0.0.1:5000/treatment_ui
@app.route('/treatment_ui')
def treatment_ui():
    return send_from_directory('interface', 'treatment.html')

# Serve patient.html from patient_interface
# http://127.0.0.1:5000/patient_ui
@app.route('/patient_ui')
def patient_ui():
    return send_from_directory('interface', 'patient.html')



if __name__ == "__main__":
    app.run(debug = True)