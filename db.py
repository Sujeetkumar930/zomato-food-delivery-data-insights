import mysql.connector

class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zomato_project"
        )

        self.cursor = self.conn.cursor()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        
    
