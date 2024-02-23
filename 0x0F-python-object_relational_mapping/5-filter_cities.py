#!/usr/bin/python3
'''lists all cities of a particular state provided as an arg'''
import sys
import MySQLdb


if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    db_name, state_name = sys.argv[3], sys.argv[4]

    db = MySQLdb.Connect(host="localhost", port=3306,
                         user=username, password=password, database=db_name)

    cursor = db.cursor()
    query = f"""SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = '{state_name}'"""

    cursor.execute(query)
    result = cursor.fetchall()

    num = len(result)
    i = 0
    for city in result:
        city_name = city[0]
        if (i == num - 1):
            print(city_name)
            break
        print(city_name, end=', ')
        i += 1
