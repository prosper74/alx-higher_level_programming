#!/usr/bin/python3
"""script that lists all states from the database `hbtn_0e_0_usa`"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    dn_conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = dn_conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dn_conn.close()