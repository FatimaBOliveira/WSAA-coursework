import mysql.connector

from dbconfig import database as db

db = mysql.connector.connect(
  host= db['host'],
  user= db['user'],
  password= db['password'],
  database= db['database']
)

cursor = db.cursor()

# Delete patient.
sql="delete from patient where id = %s"
values = (1,)

# Delete a row in treatment.
sql_2="delete from treatment where patient_id = %s AND date_time = %s"
values_2 = (1,"2025-04-15 10:30")

cursor.execute(sql, values)
cursor.execute(sql_2, values_2)

db.commit()
print("delete done")

cursor.close()
db.close()