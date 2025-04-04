import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="clinic"
)

cursor = db.cursor()
sql="update patient set name= %s, age=%s, type_of_treatment=%s  where id = %s"
values = ("John Dean",78, "HDF", 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()