import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa"
)
mycursor = connection.cursor()

sql="select * from student where id = %s"
values = (1,)

mycursor.execute(sql, values)
result = mycursor.fetchall()

for x in result:
    print(x)

mycursor.close()
connection.close()