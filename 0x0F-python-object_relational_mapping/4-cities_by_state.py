#!/usr/bin/python3
"""List all cities from the db
Username, password, and database name given as user args
Can only use execute() once
Sort ascending order by cities.id
"""
import MySQLdb
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=password,
                         db=db_name,
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    selected_cities = cur.fetchall()
    for city in selected_cities:
        print(city)

    cur.close()
    db.close()

