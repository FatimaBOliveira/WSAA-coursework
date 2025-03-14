import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa"
)
mycursor = connection.cursor()

sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)

mycursor.execute(sql, values)
connection.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.close()
connection.close()