import mysql.connector

from dbconfig import database as db

db = mysql.connector.connect(
  host= db['host'],
  user= db['user'],
  password= db['password'],
 database= db['database']
)

cursor = db.cursor()

# Update patient table.
sql="update patient set name= %s, age=%s, type_of_treatment=%s  where id = %s"
values = ("John Dean",78, "HDF", 1)

# Update tretament table.
sql_2="update treatment set bp_systolic= %s, bp_diastolic=%s, heart_rate=%s, notes=%s where patient_id = %s AND date_time = %s"
values_2 = (100,60,50, "BP stable", 1, "2025-04-15 10:30")

cursor.execute(sql, values)
cursor.execute(sql_2, values_2)

db.commit()
print("update done")

cursor.close()
db.close()