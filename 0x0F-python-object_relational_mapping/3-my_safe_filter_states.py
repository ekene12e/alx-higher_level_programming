#!/usr/bin/python3
"""List all states where 'name' matches the argument
But this time, one safe from MySQL injection.
Username, password, database name, and state name given as user args
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
    cur.execute("""SELECT id,
                    name FROM states
                    ORDER BY id ASC""")
    selected_states = cur.fetchall()
    for state in selected_states:
        if (state[1] == search_name):
            print(state)

    cur.close()
    db.close()
