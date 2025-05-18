# Server
# Flask server that connects the DAOs to the web application
# This is the main file for linking the backend data access to the frontend
# author: Fatima Oliveira

# Import libraries
from flask import Flask, request, jsonify, abort, send_from_directory
from flask_cors import CORS
from datetime import datetime

# Import the DAOs
from PatientDAO import patientDAO
from TreatmentDAO import treatmentDAO

# Initialize Flask app
app = Flask(__name__, static_url_path='', static_folder='interface') # The "interface" folder is set as the static folder to serve HTML pages
# https://flask.palletsprojects.com/en/stable/api/

# Enable CORS to allow requests
CORS(app)

# Root route
# curl http://127.0.0.1:5000/
@app.route('/')
def index():
        return "Hello world!"

####################################################################################################################
# Patients

# Get all patients
# curl http://127.0.0.1:5000/patient
@app.route('/patient', methods=['GET'])
def getall():
        return jsonify(patientDAO.getAll())

# Find patient by id
# curl http://127.0.0.1:5000/patient/1
@app.route('/patient/<int:id>', methods=['GET'])
def findbyid(id):
    patient = patientDAO.findByID(id)  # Query the DAO
    if not patient:  # Check if the patient exists
        abort(404, description="Patient not found")
    return jsonify(patient)

# Create patient
# curl -H "Content-Type: application/json" -X POST -d "{\"id\":1,\"name\":\"Mary\", \"age\":66, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient
@app.route('/patient', methods=['POST'])
def create():
        # Read JSON data from the request body
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

# Update a patient by id
# curl -H "Content-Type:application/json" -X PUT -d "{\"name\":\"Mary\", \"age\":67, \"type_of_treatment\":\"HD\"}" http://127.0.0.1:5000/patient/1
@app.route('/patient/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        patient = {}

        existing_patient = patientDAO.findByID(id)
        if not existing_patient:
            return jsonify({"error": f"Patient with ID {id} not found."}), 404
        
        if "name" in jsonstring:
                patient["name"] = jsonstring["name"]
        if "age" in jsonstring:
                patient["age"] = jsonstring["age"]
        if "type_of_treatment" in jsonstring:
                patient["type_of_treatment"] = jsonstring["type_of_treatment"]
        
        return jsonify(patientDAO.update(id, patient))

# Delete a patient by id
# curl -X DELETE  http://127.0.0.1:5000/patient/1
@app.route('/patient/<int:id>', methods=['DELETE'])
def delete(id):
    result = patientDAO.findByID(id)
    if not result:
        abort(404, description="Patient not found")
    
    # Delete the patient and return success message
    patientDAO.delete(id)
    return jsonify({"message": f"Patient with ID {id} deleted successfully"})

####################################################################################################################
# Treatments

# Get all Treatments
# curl http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['GET'])
def getall_tx():
        return jsonify(treatmentDAO.getAll())

# Find treatment by patient id
# curl http://127.0.0.1:5000/treatment/1
@app.route('/treatment/<int:patient_id>', methods=['GET'])
def findbyid_tx(patient_id):
    treatment = treatmentDAO.findByID(patient_id)  # Query the DAO
    if not treatment:  # Check if the patient exists
        abort(404, description="Patient not found")
    return jsonify(treatment)

# Create a treatment
# curl -H "Content-Type: application/json" -X POST -d "{\"patient_id\":1,\"date_time\":\"2025-04-17 10:10\", \"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"Patient is feeling well.\"}" http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['POST'])
def create_tx():
        # Read JSON data from the request body
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

# Update a treatment by patient id, date and time
# curl -H "Content-Type:application/json" -X PUT -d "{\"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"BP dropping, UF suspended.\"}" "http://127.0.0.1:5000/treatment/1/2025-04-17%2010:10"
@app.route('/treatment/<int:patient_id>/<string:date_time>', methods=['PUT'])
def update_tx(patient_id, date_time):
        jsonstring = request.json
        treatment = {}

        existing_patient = treatmentDAO.findByID(patient_id)
        if not existing_patient:
            return jsonify({"error": f"Patient with ID {patient_id} not found."}), 404
        
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
        
        try:
                # Parse date_time from URL (expected format: 'YYYY-MM-DD HH:MM')
                # Convert the date_time string into a datetime object to match MySQL timestamp format
                parsed_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M') # https://www.geeksforgeeks.org/python-datetime-strptime-function/
                # Format to include seconds for MySQL query
                date_time_str = parsed_time.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
              return jsonify({"error": "Invalid date_time format. Use 'YYYY-MM-DD HH:MM'"}), 400
        
        try:
                updated = treatmentDAO.update(patient_id, date_time_str, treatment)
        except Exception as e:
            # Optional: log the error e
            return jsonify({"error": "Internal server error during update"}), 500
        return jsonify(updated)
        #return jsonify(treatmentDAO.update(patient_id, date_time_str, treatment))

# Delete a treatment
# curl -X DELETE  "http://127.0.0.1:5000/treatment/1/2025-04-17%2010:10"

@app.route('/treatment/<int:patient_id>/<string:date_time>', methods=['DELETE'])
def delete_tx(patient_id, date_time):
    result = treatmentDAO.findByID(patient_id)  # Check if patient exists
    if not result:
        abort(404, description="Patient not found")

    treatment = treatmentDAO.delete(patient_id, date_time)
    if not treatment:
        abort(404, description="Treatment record not found or already deleted.")

    return jsonify({"message": f"Treatment for the patient {patient_id} at {date_time} deleted successfully"})

####################################################################################################################
# HTML pages

# Access treatment.html from the "interface" folder
# Open in the web browser: http://127.0.0.1:5000/treatment_i
@app.route('/treatment_i')
def treatment_ui():
    # send_from_directory uses the treatment.html file from the "interface" static folder defined above in the app
    return send_from_directory('interface', 'treatment.html')  # https://programtalk.com/python/flask-send_from_directory-function-serve-files/

# Access patient.html from the "interface" folder
# Open in the web browser: http://127.0.0.1:5000/patient_i
@app.route('/patient_i')
def patient_ui():
    return send_from_directory('interface', 'patient.html')

# Initialise the app
if __name__ == "__main__":
    app.run(debug = True)