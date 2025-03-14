import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa"
)
mycursor = connection.cursor()

sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)

mycursor.execute(sql, values)
connection.commit()
print("update done")

mycursor.close()
connection.close()