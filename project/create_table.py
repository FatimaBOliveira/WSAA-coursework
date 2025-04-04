import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="clinic"
)
mycursor = connection.cursor()
sql="CREATE TABLE patient ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200), age INT, type_of_treatment ENUM('HD', 'HDF')) ENGINE=InnoDB"
sql_2="CREATE TABLE treatment (data_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, id INT, bp_systolic INT, bp_dialystolic INT, heart_rate INT, notes VARCHAR(500), PRIMARY KEY (data_time, id), CONSTRAINT fk_treatment FOREIGN KEY (id) REFERENCES patient(id) ON DELETE CASCADE) ENGINE=InnoDB"

mycursor.execute(sql)
mycursor.close()
connection.close()