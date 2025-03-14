import mysql.connector
from config import database as db

class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self):
        self.host=db["host"]
        self.user=db["user"]
        self.password=db["password"]
        self.database=db["database"]

    def getCursor(self):
        self.connection = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.closeAll()
        return results

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self, values):
        cursor = self.getCursor()
        sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        rows_updated = cursor.rowcount
        self.closeAll()
        return rows_updated

    def delete(self, id):
        cursor = self.getCursor()
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        self.connection.commit()
        rows_deleted = cursor.rowcount
        self.closeAll()
        return rows_deleted

studentDAO = StudentDAO()