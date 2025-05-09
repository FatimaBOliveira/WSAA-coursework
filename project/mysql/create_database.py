import mysql.connector
from dbconfig import database as db

connection = mysql.connector.connect(
 host= db['host'],
 user= db['user'],
 password= db['password'],
)
mycursor = connection.cursor()
mycursor.execute("CREATE database clinic")

mycursor.close()
connection.close()