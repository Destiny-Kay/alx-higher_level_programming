#!/usr/bin/python3
'''prints first object of the query'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'''mysql+mysqldb://{username}:{password}@localhost/{db_name}''',
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).first()
    if result:
        print(f'{result.id}: {result.name}')
