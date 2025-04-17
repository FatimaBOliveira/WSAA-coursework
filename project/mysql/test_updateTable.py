import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="clinic"
)

cursor = db.cursor()

# Update patient table.
#sql="update patient set name= %s, age=%s, type_of_treatment=%s  where id = %s"
#values = ("John Dean",78, "HDF", 1)

# Update tretament table.
sql="update treatment set bp_systolic= %s, bp_diastolic=%s, heart_rate=%s, notes=%s where patient_id = %s AND date_time = %s"
values = (100,60,50, "BP stable", 1, "2025-04-15 10:30")

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()