#!/usr/bin/python3

import mysql.connector

class Mysql():

    def __init__(self, **mysql_user):
        self.mysql_user = mysql_user
        

    def connect(self):
        self.connection = mysql.connector.connect(**self.mysql_user)
        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            print("Connected to MySQL database")
        else:
            print("Connection failed.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.errors.ProgrammingError:
            raise ValueError("You have an error in your SQL syntax")
        except mysql.connector.errors.DatabaseError:
            print('\t[INFO]: Database db_shop is exist.')
        try:
            self.connection.commit()
        except Exception:
            return self.cursor.fetchall()