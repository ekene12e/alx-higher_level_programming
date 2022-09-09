#!/usr/bin/python3
""" a script that lists all states from the
database hbtn_0e_0_usa"""
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
                    WHERE name LIKE BINARY '{}'
                    ORDER BY id ASC""".format(search_name))
    selected_states = cur.fetchall()
    for state in selected_states:
        print(state)

    cur.close()
    db.close()
