#!/usr/bin/python3
"""Prints the State object with the given name"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """
    Main function to query the database for the State object
    with the given name and print its ID if found.
    """
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
            username, password, database
        )

        engine = create_engine(DATABASE_URL)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query db for state
        state = session.query(State).filter(State.name == state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")
    else:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

if __name__ == '__main__':
    main()
