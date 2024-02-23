#!/usr/bin/python3
'''reurns a filtered list of results from the states field in  DB'''
import MySQLdb
import sys


def query_states_filter():
    '''REturns a list of records from the states field'''
    args = sys.argv
    username, password, db_name = args[1], args[2], args[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)
    db.query("""SELECT * FROM states WHERE name LIKE 'N%';""")
    r = db.store_result()
    result = r.fetch_row(0)

    i = 0
    while (i < len(result)):
        print(result[i])
        i += 1
    return


if __name__ == "__main__":
    query_states_filter()
