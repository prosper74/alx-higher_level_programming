#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
safe from MySQL injections
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(host="localhost", user=argv[1],
                              passwd=argv[2], db=argv[3], port=3306)
    cur = db_conn.cursor()
    MATCH = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (MATCH, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
