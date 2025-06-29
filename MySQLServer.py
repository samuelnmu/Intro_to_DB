import pymysql

def create_database():
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = pymysql.connect(
            host='localhost',
            user='root',          
            password='assword',  
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            # Create database if not exists 
            sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(sql)

        connection.commit()
        print("Database 'alx_book_store' created successfully!")

    except pymysql.MySQLError as e:
        print(f"Error while connecting or creating database: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
