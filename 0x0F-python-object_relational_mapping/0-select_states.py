#!/usr/bin/python3
"""Lists all states in a DB"""
import sys
from MySQLdb import _mysql
import MySQLdb


def quey_states():
    '''Queries all statese in the database'''
    args = sys.argv
    username, password, db_name = args[1], args[2], args[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)

    db.query("""SELECT * FROM states ORDER BY id ASC;""")

    r = db.store_result()
    result = r.fetch_row(0)

    i = 0
    while (i < len(result)):
        print(result[i])
        i += 1

    return


if __name__ == "__main__":
    quey_states()
