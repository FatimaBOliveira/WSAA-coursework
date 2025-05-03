# flask server that links to a DAO
# author: Fatima Oliveira

from flask import Flask, request, jsonify, abort
from datetime import datetime, timedelta
#from treatmentDAOskeleton import treatmentDAO
from TreatmentDAO import treatmentDAO
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
#CORS(app)   # Enable CORS globally for the API
#CORS(app, supports_credentials=True)  # Enable CORS with credentials
#CORS(app, resources={r"/treatment/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
        return "Hello world!"

# getall
# curl http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['GET'])
def getall():
        return jsonify(treatmentDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/treatment/1
@app.route('/treatment/<int:patient_id>', methods=['GET'])
def findbyid(patient_id):
    treatment = treatmentDAO.findByID(patient_id)  # Query the DAO
    if not treatment:  # Check if the patient exists
        abort(404, description="Patient not found")
    return jsonify(treatment)

#create
# curl -H "Content-Type: application/json" -X POST -d "{\"patient_id\":2,\"date_time\":\"2025-04-17 10:10\", \"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"Patient is feeling well.\"}" http://127.0.0.1:5000/treatment
@app.route('/treatment', methods=['POST'])
def create():
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


        #### CREATE ERROR IN CASE THAT PATIENT_ID DOESNT EXIST. this will be included in final rest-py
        #existing_patient = patientDAO.findByID(id)
        #if not existing_patient:
        #    return jsonify({"error": f"Patient with ID {id} not found."}), 404
        
        return jsonify(treatmentDAO.create(treatment))

# update
# curl -H "Content-Type:application/json" -X PUT -d "{\"bp_systolic\":100, \"bp_diastolic\":65, \"heart_rate\":69, \"notes\":\"BP dropping, UF suspended.\"}" "http://127.0.0.1:5000/treatment/2/2025-04-17%2010:10"
@app.route('/treatment/<int:patient_id>/<string:date_time>', methods=['PUT'])
def update(patient_id, date_time):
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
def delete(patient_id, date_time):
    result = treatmentDAO.findByID(patient_id)  # Check if patient exists
    if not result:
        abort(404, description="Patient not found")

    treatment = treatmentDAO.delete(patient_id, date_time)
    if not treatment:
        abort(404, description="Treatment record not found or already deleted.")

    return jsonify({"message": f"Treatment for the patient {patient_id} at {date_time} deleted successfully"})

if __name__ == "__main__":
    app.run(debug = True)