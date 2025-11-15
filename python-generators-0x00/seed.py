import mysql.connector
from mysql.connector import errorcode
import uuid
import csv
 

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="925259@Nangami"
        )
        return connection
    except mysql.connector.Error as err:
        print (f"Error: {err}")
        return None
    
def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        cursor.close()

def connect_to_prodev():
    #connect to the ALX_prodev database
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="925259@Nangami",
            database = "ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
#create the user_data table
def create_table(connection):
    cursor = connection.cursor()
    create_table_query ="""CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX(user_id)
    );"""
    try:
        cursor.execute(create_table_query)
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    finally:
        cursor.close()
#insert csv data 
def insert_data(connection, user_data):
    cursor =connection.cursor()
    with open(user_data, newline='') as f:
        reader=csv.DictReader(f)
        for row in reader:
            user_id = str(uuid.uuid4())
            try:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) "
                    "VALUES (%s, %s, %s, %s)",
                    (user_id, row['name'], row['email'], int(row['age']))
                )
            except mysql.connector.Error as err:
                print(f"Failed to insert row {row}: {err}")
    connection.commit()
    cursor.close()
    print("CSV data inserted successfully")

    #a generator to stream rows
def stream_user_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    row = cursor.fetchone()
    while row:
        yield row
        row = cursor.fetchone()
        
