#!/usr/bin/python3
'''updates records in db'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'''mysql+mysqldb://{username}:
                           {password}@localhost/{db_name}''',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()
