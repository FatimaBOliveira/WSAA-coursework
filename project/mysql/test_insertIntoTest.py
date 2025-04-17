import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clinic"
)

cursor = db.cursor()

# Insert into patient table.
#sql="insert into patient (id, name, age, type_of_treatment) values (%s,%s,%s, %s)"
#values = (1,"John", 77,"HDF")

# Insert into treatment table.
sql="INSERT INTO treatment (patient_id, date_time, bp_systolic, bp_diastolic, heart_rate, notes) VALUES (%s, %s, %s, %s, %s, %s)"
values = (2,"2025-04-15 10:30", 155, 75, 65, "Patient is stable")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

cursor.close()
db.close()