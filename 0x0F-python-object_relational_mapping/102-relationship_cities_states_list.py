#!/usr/bin/python3
"""Prints the State object with the name
passed as an argument from the database"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    try:
        # Establish connection to the database
        engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:
                {sys.argv[2]}@localhost:3306/{sys.argv[3]}')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the database for State objects and print associated cities
        for instance in session.query(State).order_by(State.id):
            for city_ins in instance.cities:
                print(city_ins.id, city_ins.name, sep=": ", end="")
                print(" -> " + instance.name)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        if session is not None:
            session.close()
