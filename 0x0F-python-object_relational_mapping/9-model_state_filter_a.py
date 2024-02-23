#!/usr/bin/python3
'''lists all state objects that contain the letter a'''
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f'''mysql+mysqldb://{username}:
                           {password}@localhost/{db_name}''',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like('%a%')).all()
    for state in result:
        print(f'{state.id}: {state.name}')
