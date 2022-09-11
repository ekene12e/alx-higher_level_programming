#!/usr/bin/python3
"""Gets all City objects from database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True
                                                    )

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(City).join(State).order_by(State.id):
        print("{:d}: {}".format(instance.id, instance.name))
