#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument."""


import MySQLdb
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>
                <state_name>".format(sys.argv[0]))
        sys.exit(1)

    try:
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )

        cur = conn.cursor()

        # Use parameterized query to prevent SQL injection
        cur.execute(
                'SELECT * FROM states WHERE name LIKE BINARY %s 
                ORDER BY id ASC;',
                (sys.argv[4],)
                )

        rows = cur.fetchall()

        for res in rows:
            print(res)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and connection regardless of any exceptions
        if cur:
            cur.close()
        if conn:
            conn.close()

