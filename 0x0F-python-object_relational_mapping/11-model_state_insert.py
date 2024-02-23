#!/usr/bin/python3
'''adds a State object to the db'''
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

    new_record = State(name="Louisiana")
    session.add(new_record)
    session.commit()
    print(new_record.id)
