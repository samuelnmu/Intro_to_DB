import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',               
            password='password'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting or creating database: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
