import mysql.connector

def stream_users():
    """Yield one row at a time from user_data as a dictionary"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="925259@Nangami",       
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data;")

    # single loop to yield rows
    for row in cursor:
        yield row

    # close resources after iteration
    cursor.close()
    connection.close()