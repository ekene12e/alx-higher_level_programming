#!/usr/bin/python3
""" a script that lists all states from the
database hbtn_0e_0_usa"""
import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]
db = MySQLdb.connect(host='localhost', user=user, passwd=password, db=db_name)
cur = db.cursor()
cur.execute("SELECT name FROM states ORDER BY states.id")
