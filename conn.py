import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establish a connection to the MySQL database and print the status."""
    try:
        
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",       
            password="",  
            database="findmyboarding"  
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Successfully connected to MySQL Server version", db_info)
            return connection
        else:
            print("Connection failed.")
            return None
    except Error as e:
        print("Error while connecting to MySQL:", e)
        return None

