#!/usr/bin/python3
'''filters tables'''
import MySQLdb
import sys


def query_states():
    '''Queries a database and returns records that match the arguments'''
    args = sys.argv
    username, password, db_name, state_name_searched = args[1],
    args[2], args[3], args[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s;"
    cursor.execute(query, [state_name_searched])
    result = cursor.fetchall()

    i = 0
    while (i < len(result)):
        print(result[i])
        i += 1


if __name__ == "__main__":
    query_states()
