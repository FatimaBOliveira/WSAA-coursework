import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password=""
)
mycursor = connection.cursor()
mycursor.execute("CREATE database wsaa")

mycursor.close()
connection.close()