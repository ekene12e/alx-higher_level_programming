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
    db = MySQLdb.connect(host='localhost',
                         user=user,
                         passwd=password,
                         db=db_name,
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    print(", ".join([city[2]
                     for city in cur.fetchall()
                     if city[4] == sys.argv[4]]))
    cur.close()
    db.close()
