import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("host"),
            user=os.getenv("user"),
            password= os.getenv("password"),
            database=os.getenv("students")
        )

        self.mycursor = self.db.cursor(dictionary=True)
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS students")
        self.mycursor.execute("USE students")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY,"
                         "name VARCHAR(255) NOT NULL,"
                         "student_id VARCHAR(255) NOT NULL,"
                         "email VARCHAR(255) NOT NULL,"
                         "phone VARCHAR(20) NOT NULL,"
                         "gender VARCHAR(255))"
        )

        self.mycursor.execute("USE students")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS account(id INT AUTO_INCREMENT PRIMARY KEY,"
                              "email VARCHAR(255) NOT NULL,"
                              "password TEXT NOT NULL)")

    def execute_query(self, query, values=None):
        if values:
            self.mycursor.execute(query, values)
        else:
            self.mycursor.execute(query)
        self.db.commit()

    def fetch_all(self, query, values=None):
        if values:
            self.mycursor.execute(query, values)
        else:
            self.mycursor.execute(query)
        return self.mycursor.fetchall()




