import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clinic"
)

cursor = db.cursor()

# Delete patient.
#sql="delete from patient where id = %s"
#values = (1,)

# Delete a row in treatment.
sql="delete from treatment where patient_id = %s AND date_time = %s"
values = (1,"2025-04-15 10:30")

cursor.execute(sql, values)

db.commit()
print("delete done")

cursor.close()
db.close()