#!/usr/bin.python3
'''model definition'''
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


sql_engine = create_engine("""mysql+mysqldb://localhost:3306""",
                           pool_pre_ping=True)

# Base.metadata.create_all(sql_engine)
