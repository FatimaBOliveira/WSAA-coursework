import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="wsaa"
)
mycursor = connection.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

mycursor.execute(sql)
mycursor.close()
connection.close()