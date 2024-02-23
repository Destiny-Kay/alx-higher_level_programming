#!/usr/bin/python3
'''queries data based on provided variable'''
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base


if __name__ == "__main__":
    username, password, db_name, state_name_search = sys.argv[1],
    sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine(f'''mysql+mysqldb://{username}:
                           {password}@localhost/{db_name}''',
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(
        State.name.like(state_name_search)).first()
    if result is None:
        print("Not found")
    else:
        print(result.id)
