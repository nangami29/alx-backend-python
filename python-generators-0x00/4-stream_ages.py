#Compute average age of users using a generator

import mysql.connector

def stream_user_ages():
    """Generator that yields user ages one by one"""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       
        password="925259@Nangami",      
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data;")

    for (age,) in cursor:  
        yield age

    cursor.close()
    connection.close()


def compute_average_age():
    # the average age using the generator
    total_age = 0
    count = 0

    for age in stream_user_ages():  # second loop
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
        return

    average = total_age / count
    print(f"Average age of users: {average}")


if __name__ == "__main__":
    compute_average_age()
