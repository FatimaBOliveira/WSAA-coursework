# Author: Fatima Oliveira

# Import library
import mysql.connector

# Import configuration file with the keys
from dbconfig import database as db

# Connect to mysql
connection = mysql.connector.connect(
 host= db['host'],
 user= db['user'],
 password= db['password'],
)

# Create a cursor and execute MySQL command to create a database
mycursor = connection.cursor()
mycursor.execute("CREATE database clinic")

# Close cursor and connection
mycursor.close()
connection.close()