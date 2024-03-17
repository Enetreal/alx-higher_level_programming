#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb as db
from sys import argv

def list_all_cities(username, password, database):
    try:
        # Connect to the database
        db_connect = db.connect(host="localhost", port=3306,
                user=username, passwd=password, db=database)

        with db_connect.cursor() as db_cursor:
            # Execute SQL query
            db_cursor.execute("SELECT cities.id, cities.name,
            states.name \
                    FROM cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC")
            rows_selected = db_cursor.fetchall()

        # Display the results
        if rows_selected:
            for row in rows_selected:
                print(row)
        else:
            print("No cities found in the database.")

    except db.Error as e:
        print(f"Database error: {e}")
    finally:
        # Close the database connection
        if 'db_connect' in locals():
            db_connect.close()

if __name__ == '__main__':
    # Check if correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: ./list_cities.py <username> <password>
                <database>")
        exit(1)

    list_all_cities(argv[1], argv[2], argv[3])
