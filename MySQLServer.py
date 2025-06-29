import mysql.connector

def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',               # Change if needed
            password='your_root_password'  # Change to your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Exception as e:
        print(f"Error while connecting or creating database: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
