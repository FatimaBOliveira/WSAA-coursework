# Treatment DAO
# This file is responsible for all direct executions on the MySQL "treatment" table.
# Author: Fatima Oliveira

# Import library
import mysql.connector

# Import configuration file with the keys
from dbconfig import database as db

# Object constructor for handling all MySQL interactions
class TreatmentDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    # Database configuration, using the config file.
    def __init__(self):
        self.host=       db['host']
        self.user=       db['user']
        self.password=   db['password']
        self.database=   db['database']

    # Connects to MySQL and returns a cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    # Close the MySQL connection and cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
     
    # Get all treatments from the table, ordered by most recent date and time
    def getAll(self):
        cursor = self.getcursor()
        sql="SELECT * from treatment ORDER BY date_time DESC"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []

        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # Returns a specific treatment by patient ID, ordered by most recent date and time
    def findByID(self, patient_id):
        cursor = self.getcursor()
        sql = "SELECT * FROM treatment WHERE patient_id = %s ORDER BY date_time DESC"
        values = (patient_id,)
        cursor.execute(sql, values)
        rows = cursor.fetchall()

        if not rows:
            self.closeAll()
            return None

        treatments = []
        for row in rows:
            treatment = self.convertToDictionary(row)
            treatments.append(treatment)

        self.closeAll()
        return treatments

     # Create a new treatment
    def create(self, treatment):
        cursor = self.getcursor()
        sql = "INSERT INTO treatment (patient_id, date_time, bp_systolic, bp_diastolic, heart_rate, notes) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (treatment.get("patient_id"), treatment.get("date_time"), treatment.get("bp_systolic"), treatment.get("bp_diastolic"), treatment.get("heart_rate"), treatment.get("notes"))
        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        return treatment

    # Update a treatment by patient ID and specific date and time
    def update(self, patient_id, date_time, treatment):
        cursor = self.getcursor()
        sql = ("""
            UPDATE treatment
            SET bp_systolic = %s, bp_diastolic = %s, heart_rate = %s, notes = %s
            WHERE patient_id = %s AND date_time LIKE %s;
            """)

        print(f"Update treatment {treatment}")

        values = (treatment.get("bp_systolic"), treatment.get("bp_diastolic"), treatment.get("heart_rate"), treatment.get("notes"), patient_id, date_time)
        cursor.execute(sql, values)
        rows_updated = cursor.rowcount
        self.connection.commit()
        self.closeAll()
        return {"updated": rows_updated}

    # Delete a treatment by patient ID and specific date and time     
    def delete(self, patient_id, date_time):
        cursor = self.getcursor()
        sql = "delete from treatment where patient_id = %s AND date_time LIKE %s;"
        values = (patient_id, f"{date_time}%")  # Add % to match seconds if not included in input
        cursor.execute(sql, values)

        if cursor.rowcount == 0:  # Check if no rows were affected
            print("No treatment found to delete.")
            self.closeAll()
            return None
        
        self.connection.commit()
        self.closeAll()

        print("Delete done")
        return True

    # Converts a tuple result into a dictionary with treatment attributes
    def convertToDictionary(self, resultLine):
        attkeys = ["patient_id", "date_time", "bp_systolic", "bp_diastolic", "heart_rate", "notes"]
        treatment = {}
        currentkey = 0
        for attrib in resultLine:
            treatment[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return treatment

# Create a treatmentDAO object to be used in other files          
treatmentDAO = TreatmentDAO()