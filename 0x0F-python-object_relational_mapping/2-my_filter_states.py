#!/usr/bin/python3
'''filters tables'''
import MySQLdb
import sys


def query_states():
    '''Queries a database and returns records that match the arguments'''
    args = sys.argv
    username, password = args[1], args[2]
    db_name, state_name_searched = args[3], args[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)
    db.query("""SELECT *
             FROM states WHERE name LIKE '{}';""".format(state_name_searched))
    r = db.store_result()
    result = r.fetch_row(0)

    i = 0

    while (i < len(result)):
        print(result[i])
        i += 1
    return


if __name__ == "__main__":
    query_states()
