import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clinic"
)

cursor = db.cursor()

# Select from patient table.
#sql="select * from patient where id = %s"
#values = (1,)

# Select from treatment table.
sql="select * from treatment where patient_id = %s AND date_time LIKE %s"
values = (1, "2025-04-15%")

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

cursor.close()
db.close()