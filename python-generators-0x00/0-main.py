#!/usr/bin/python3

from seed import connect_db, create_database, connect_to_prodev, create_table, insert_data, stream_user_data

# Step 1: Connect to MySQL server
connection = connect_db()
if connection:
    # Step 2: Create database
    create_database(connection)
    connection.close()
    print("Connection successful and database ensured.")

# Step 3: Connect to ALX_prodev
connection = connect_to_prodev()
if connection:
    # Step 4: Create table
    create_table(connection)
    # Step 5: Insert CSV data
    insert_data(connection, 'user_data.csv')
    
    # Step 6: Stream first 5 rows using generator
    print("\nFirst 5 rows from user_data:")
    count = 0
    for row in stream_user_data(connection):
        print(row)
        count += 1
        if count >= 5:
            break

    connection.close()
