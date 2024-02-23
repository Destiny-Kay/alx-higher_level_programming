#!/usr/bin/python3
'''lists all cities in a db'''
import MySQLdb
import sys


def query_cities_by_state():
    args = sys.argv
    username, password, db_name = args[1], args[2], args[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)
    cursor = db.cursor()
    query = """SELECT cities.id,cities.name,states.name
                FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;"""
    cursor.execute(query)
    result = cursor.fetchall()

    i = 0
    while (i < len(result)):
        print(result[i])
        i += 1

    return


if __name__ == "__main__":
    query_cities_by_state()
