# Patient DAO
# This file is responsible for all direct executions on the MySQL "patient" table.
# Author: Fatima Oliveira

# Import library
import mysql.connector

# Import configuration file with the keys
from dbconfig import database as db

# Object constructor for handling all MySQL interactions
class PatientDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    # Database configuration, using the config file. This function is always executed when the class is called.
    def __init__(self):
        self.host=       db['host']
        self.user=       db['user']
        self.password=   db['password']
        self.database=   db['database']

    # Function that connects to MySQL and returns a cursor
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

    # Get all patients from the table   
    def getAll(self):
        cursor = self.getcursor()
        sql="SELECT * from patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    # Returns a specific patient by ID
    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM patient WHERE id = %s"
        values = (id,)
    
        cursor.execute(sql, values)
        result = cursor.fetchone()
    
        if result is None:
            return None
    
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    # Create a new patient
    def create(self, patient):
        cursor = self.getcursor()
        sql = "INSERT INTO patient (id, name, age, type_of_treatment) VALUES (%s, %s, %s, %s)"
        values = (patient.get("id"), patient.get("name"), patient.get("age"), patient.get("type_of_treatment"))
        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        return patient

    # Update patient
    def update(self, id, patient):
        cursor = self.getcursor()
        sql = "UPDATE patient SET name= %s, age=%s, type_of_treatment=%s WHERE id=%s"
        print(f"Update patient {patient}")
        values = (patient.get("name"), patient.get("age"), patient.get("type_of_treatment"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    # Delete patient by ID
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM patient WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)

        if cursor.rowcount == 0:  # Check if no rows were affected
            print("No patient found to delete.")
            self.closeAll()
            return None
        
        self.connection.commit()
        self.closeAll()

        print("Delete done")
        return True

    # Converts a tuple result into a dictionary with patient attributes
    def convertToDictionary(self, resultLine):
        attkeys = ["id", "name", "age", "type_of_treatment"]
        patient = {}
        currentkey = 0
        for attrib in resultLine:
            patient[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return patient

# Create a patientDAO object to be used in other files
patientDAO = PatientDAO()