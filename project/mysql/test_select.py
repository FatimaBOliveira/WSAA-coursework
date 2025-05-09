import mysql.connector

from dbconfig import database as db

db = mysql.connector.connect(
  host= db['host'],
  user= db['user'],
  password= db['password'],
  database= db['database']
)

cursor = db.cursor()

# Select from patient table.
sql="select * from patient where id = %s"
values = (1,)

# Select from treatment table.
sql_2="select * from treatment where patient_id = %s AND date_time LIKE %s"
values_2 = (1, "2025-04-15%")

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

cursor.execute(sql_2, values_2)
result_2 = cursor.fetchall()
for x_2 in result_2:
  print(x_2)

cursor.close()
db.close()