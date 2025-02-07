import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="mydb"
)

mycursor = mydb.cursor()
try:
    mycursor.execute("""
        CREATE DATABASE IF NOT EXISTS alx_book_store;
    """
    )
    print("Table created successfully!")
except mysql.connector.Error:
    print("Error")
mycursor.close()
mydb.close()