# Patient DAO 
# Author: Fatima Oliveira

import mysql.connector
from dbconfig import database as db

class PatientDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       db['host']
        self.user=       db['user']
        self.password=   db['password']
        self.database=   db['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def getAll(self):
        cursor = self.getcursor()
        sql="SELECT * from patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

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
    
    def create(self, patient):
        cursor = self.getcursor()
        sql = "INSERT INTO patient (id, name, age, type_of_treatment) VALUES (%s, %s, %s, %s)"
        values = (patient.get("id"), patient.get("name"), patient.get("age"), patient.get("type_of_treatment"))
        cursor.execute(sql, values)

        self.connection.commit()
        #newid = cursor.lastrowid
        #patient["id"] = newid
        self.closeAll()
        return patient


    def update(self, id, patient):
        cursor = self.getcursor()
        sql = "UPDATE patient SET name= %s, age=%s, type_of_treatment=%s WHERE id=%s"
        print(f"Update patient {patient}")
        values = (patient.get("name"), patient.get("age"), patient.get("type_of_treatment"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM patient WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)

        if cursor.rowcount == 0:  # Check if no rows were affected
            return None
        
        self.connection.commit()
        self.closeAll()

        print("Delete done")
        return True


    def convertToDictionary(self, resultLine):
        attkeys = ["id", "name", "age", "type_of_treatment"]
        patient = {}
        currentkey = 0
        for attrib in resultLine:
            patient[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return patient

        
patientDAO = PatientDAO()