import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="clinic"
)

cursor = db.cursor()
sql="insert into patient (id, name, age, type_of_treatment) values (%s,%s,%s, %s)"
values = (1,"John", 77,"HDF")

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

cursor.close()
db.close()