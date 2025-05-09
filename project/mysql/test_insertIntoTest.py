import mysql.connector

from dbconfig import database as db

db = mysql.connector.connect(
  host= db['host'],
  user= db['user'],
  password= db['password'],
  database= db['database']
)

cursor = db.cursor()

# Insert into patient table.
sql="insert into patient (id, name, age, type_of_treatment) values (%s,%s,%s, %s)"
values = (1,"John", 77,"HDF")

# Insert into treatment table.
sql_2="INSERT INTO treatment (patient_id, date_time, bp_systolic, bp_diastolic, heart_rate, notes) VALUES (%s, %s, %s, %s, %s, %s)"
values_2 = (1,"2025-04-15 10:30", 155, 75, 65, "Patient is stable")

cursor.execute(sql, values)
cursor.execute(sql_2, values_2)

db.commit()
print("Record inserted")

cursor.close()
db.close()