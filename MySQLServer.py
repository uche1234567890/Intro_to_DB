import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
