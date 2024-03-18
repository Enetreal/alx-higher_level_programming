#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) == 4:
        user = sys.argv[1]
        passW = sys.argv[2]
        dataB = sys.argv[3]

        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
                user, passW, dataB
                )

        engine = create_engine(DATABASE_URL)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        """Query State object with id = 2"""
        update = session.query(State).filter(State.id == 2).first()

        """Update the name of the state"""
        if update:
            update.name = "New Mexico"
            session.commit()

        session.close()
