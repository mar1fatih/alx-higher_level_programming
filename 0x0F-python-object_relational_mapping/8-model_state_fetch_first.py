#!/usr/bin/python3
"""prints the first State object from the database"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).first()
    if not ins:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
