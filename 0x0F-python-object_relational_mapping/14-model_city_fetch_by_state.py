#!/usr/bin/python3
"""
Start database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    lists all State objects from the database hbtn_0e_6_usa
    """
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for c, s in session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
