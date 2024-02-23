#!/usr/bin/python3
'''lists all objects in DB'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def query_db():
    '''Queries the db for all records'''
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db = create_engine(
        f'''mysql+mysqldb://{username}:{password}@localhost/{db_name}''',
        pool_pre_ping=True)
    Session = sessionmaker(bind=db)
    session = Session()

    result = session.query(State).all()
    for state in result:
        print(f'{state.id}: {state.name}')
    return


if __name__ == "__main__":
    query_db()
