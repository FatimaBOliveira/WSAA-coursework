# Treatment DAO 
# Author: Fatima Oliveira

import mysql.connector
from dbconfig import database as db

class TreatmentDAO:
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
        sql="SELECT * from treatment ORDER BY patient_id, date_time DESC"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            #print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, patient_id):
        cursor = self.getcursor()
        sql = "SELECT * FROM treatment WHERE patient_id = %s ORDER BY date_time"
        values = (patient_id,)
    
        cursor.execute(sql, values)
        result = cursor.fetchall()
    
        if result is None:
            return None
    
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def create(self, treatment):
        cursor = self.getcursor()
        sql = "INSERT INTO treatment (patient_id, date_time, bp_systolic, bp_diastolic, heart_rate, notes) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (treatment.get("patient_id"), treatment.get("date_time"), treatment.get("bp_systolic"), treatment.get("bp_diastolic"), treatment.get("heart_rate"), treatment.get("notes"))
        cursor.execute(sql, values)

        self.connection.commit()
        #newid = cursor.lastrowid
        #treatment["patient_id"] = newid
        self.closeAll()
        return treatment


    def update(self, patient_id, date_time, treatment):
        cursor = self.getcursor()
        sql = "update treatment set bp_systolic= %s, bp_diastolic=%s, heart_rate=%s, notes=%s where patient_id = %s AND DATE_FORMAT(date_time, '%Y-%m-%d %H:%i') = %s"
        print(f"Update treatment {treatment}")
        values = (treatment.get("bp_systolic"), treatment.get("bp_diastolic"), treatment.get("heart_rate"), treatment.get("notes"), patient_id, date_time)
        cursor.execute(sql, values)
        rows_updated = cursor.rowcount
        self.connection.commit()
        self.closeAll()
        return {"updated": rows_updated}
        
    def delete(self, patient_id, date_time):
        cursor = self.getcursor()
        sql = "delete from treatment where patient_id = %s AND DATE_FORMAT(date_time, '%Y-%m-%d %H:%i') = %s"
        values = (patient_id, date_time)
        cursor.execute(sql, values)

        if cursor.rowcount == 0:  # Check if no rows were affected
            return None
        
        self.connection.commit()
        self.closeAll()

        print("Delete done")
        return True


    def convertToDictionary(self, resultLine):
        attkeys = ["patient_id", "date_time", "bp_systolic", "bp_diastolic", "heart_rate", "notes"]
        treatment = {}
        currentkey = 0
        for attrib in resultLine:
            treatment[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return treatment
            
treatmentDAO = TreatmentDAO()