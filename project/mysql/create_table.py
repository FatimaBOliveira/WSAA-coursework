# Author: Fatima Oliveira

# Import library
import mysql.connector

# Import configuration file with the keys
from dbconfig import database as db

# Connect to mysql and create a cursor
connection = mysql.connector.connect(
 host= db['host'],
 user= db['user'],
 password= db['password'],
 database= db['database']
)
mycursor = connection.cursor()

# Create table patient
sql="CREATE TABLE patient ( id INT PRIMARY KEY, name VARCHAR(200), age INT, type_of_treatment ENUM('HD', 'HDF')) ENGINE=InnoDB"

# Create table treatment
sql_2="CREATE TABLE treatment (patient_id INT, date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, bp_systolic INT, bp_diastolic INT, heart_rate INT, notes VARCHAR(500), CONSTRAINT fk_treatment FOREIGN KEY (patient_id) REFERENCES patient(id) ON DELETE CASCADE) ENGINE=InnoDB"

# Execute and close connection
mycursor.execute(sql)
mycursor.execute(sql_2)
mycursor.close()
connection.close()