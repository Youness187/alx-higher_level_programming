#!/usr/bin/python3
"""
Start database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    lists all State objects from the database hbtn_0e_6_usa
    """
    link = "mysql+mysqldb://{}:{}@localhost/{}"
    engine = create_engine(
        link.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
