#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db_conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
