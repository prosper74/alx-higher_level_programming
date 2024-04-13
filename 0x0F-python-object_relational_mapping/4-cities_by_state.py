#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db_conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db_conn.close()
